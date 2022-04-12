.PHONY: install frontend messages env sync node_modules requirements upgrade

install: env node_modules frontend

requirements: requirements/base.in
	pip-compile -v --output-file requirements/base.txt requirements/base.in

env:
	pip install -r requirements/dev.txt

sync:
	pip-sync requirements/dev.txt requirements/base.txt

upgrade:
	pur --patch=Django,django-tinymce -r requirements/base.in
	pur --no-recursive -r requirements/docker.txt
	pur --no-recursive -r requirements/dev.txt
	pip-compile -v --upgrade --output-file requirements/base.txt requirements/base.in

node_modules:
	npm install

frontend:
	npm run gulp

images:
	npm run gulp imagemin

exampledata:
	./manage.py loaddata example_data.json

watch:
	npm run gulp watch

messages:
	django-admin.py compilemessages

clean:
	npm run gulp clean

test:
	py.test --reuse-db --nomigrations

retest:
	py.test --reuse-db --nomigrations --lf -vvs

coverage:
	py.test --reuse-db --nomigrations --cov --cov-report=term-missing

isort:
	isort -w1000 --recursive ./
