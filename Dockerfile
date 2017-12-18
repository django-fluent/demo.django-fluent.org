# Build environment has gcc and develop header files. This is used to build all
# wheel files. They are installed in the smaller runtime container.
FROM python:2.7.14-stretch as build-image
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off

# Build wheel files for all dependencies
RUN mkdir -p /app/src/requirements /app/wheels
COPY src/requirements/*.txt /app/src/requirements/
ARG PIP_REQUIREMENTS=/app/src/requirements/docker.txt
RUN pip wheel --wheel-dir=/app/wheels/ -r $PIP_REQUIREMENTS

# Start runtime container
FROM python:2.7.14-slim-stretch
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    UWSGI_PROCESSES=1 \
    UWSGI_THREADS=10 \
    UWSGI_MODULE=fluentdemo.wsgi.production:application \
    DJANGO_SETTINGS_MODULE=fluentdemo.settings.docker

# Install runtime dependencies (can become separate base image)
# Also include gettext for now, so locale is still compiled here.
# It avoids busting the previous cache layers on code changes.
RUN apt-get update && \
    apt-get install --no-install-recommends -y libxml2 gettext && \
    rm -rf /var/lib/apt/lists/* /var/cache/debconf/*-old && \
    useradd --system --user-group app

# System config (done early, avoid running on every code change)
MAINTAINER vdboor@edoburu.nl
EXPOSE 8080 1717
VOLUME /app/web/media
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost:8080/api/ping/ || exit 1

# Install dependencies
RUN mkdir -p /app/src/requirements
COPY src/requirements/*.txt /app/src/requirements/
COPY --from=build-image /app/wheels/ /app/wheels/
ARG PIP_REQUIREMENTS=/app/src/requirements/docker.txt
RUN pip install --no-index --find-links /app/wheels/ -r $PIP_REQUIREMENTS

# Insert application code.
# - Prepare gzipped versions of static files for uWSGI to use
# - Create a default database inside the container (as demo),
#   when caller doesn't define DATABASE_URL
ENV DATABASE_URL sqlite:////tmp/demo.db
COPY web /app/web
COPY src /app/src
WORKDIR /app/src
RUN rm /app/src/*/settings/local.py* && \
    find . -name '*.pyc' -delete && \
    python -mcompileall -q */ && \
    /app/src/manage.py compilemessages && \
    /app/src/manage.py collectstatic --noinput --link && \
    /app/src/manage.py migrate && \
    /app/src/manage.py loaddata example_data.json && \
    gzip --keep --best --force --recursive /app/web/static/ && \
    mkdir -p /app/web/static/CACHE && \
    chown -R app:app /app/web/media/ /app/web/static/CACHE /tmp/demo.db

# Insert main code (still as root), then reduce permissions
COPY deployment/docker/uwsgi.ini /app/uwsgi.ini
CMD ["/usr/local/bin/uwsgi", "--ini", "/app/uwsgi.ini", "--procname-prefix-spaced", "uwsgi: $UWSGI_MODULE"]
USER app
