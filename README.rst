Demo Project for django-fluent
==============================

This project shows various django-fluent modules,
and possible code layout for inspiration of your own projects.

Docker demo
-----------

To build the container and run it:

.. code-block:: bash

    docker-compose up

And open http://localhost:8000/
Any e-mail that is sent can be seen at: http://localhost:8025/

Production demo
~~~~~~~~~~~~~~~

Build the container. and run it:

.. code-block:: bash

    docker build -t fluentdemo .
    docker run --rm -p 8080:8080 fluentdemo

And open http://localhost:8080/

Local development
-----------------

Prerequisites
~~~~~~~~~~~~~

- Python >= 2.7
- pip
- virtualenv (virtualenvwrapper is recommended)

Development setup
~~~~~~~~~~~~~~~~~

To setup a local development environment:

.. code-block:: bash

    virtualenv env --prompt="(fluentdemo)"  # or mkvirtualenv fluentdemo
    source env/bin/activate

    cd src
    pip install -r requirements/dev.txt
    edit fluentdemo/settings/project.py    # Enter your DB credentials
    cp fluentdemo/settings/local.py.example fluentdemo/settings/local.py  # To enable debugging

    sudo su - postgres
    createuser fluentdemo  -P   # testtest is the default password
    createdb --template=template0 --encoding='UTF-8' --lc-collate='en_US.UTF-8' --lc-ctype='en_US.UTF-8' --owner=fluentdemo fluentdemo
    exit

    ./manage.py migrate
    ./manage.py runserver

Compiling SASS files
~~~~~~~~~~~~~~~~~~~~

Sass files are compiled to CSS during the development.
At the server, there is no need for installing development tools.

To setup your development system, install NodeJS from https://nodejs.org/.
On Mac OSX, you can also use ``brew install libsass node``.

Run the following command to compile SASS_ files::

    npm run gulp

This will compile the files, and watch for changes.
It also has LiveReload_ support.
Install a browser plugin from: http://livereload.com/extensions/
and toggle the "LiveReload" button in the browser to see CSS changes instantly.

License
-------

Feel free to use parts of this code in your projects.

.. image::  http://i.creativecommons.org/l/by/3.0/88x31.png
   :target: http://creativecommons.org/licenses/by/3.0/
   :alt: Creative Commons License

Except otherwise noted, this project is © 2016 Edoburu, under a `Creative Commons Attribution 3.0 Unported License <http://creativecommons.org/licenses/by/3.0/>`_.

The django-fluent modules are licensed under the Apache License Version 2.0.


.. Add links here:

.. _django-fluent: http://django-fluent.org/
.. _LiveReload: http://livereload.com/
.. _SASS: http://sass-lang.com/
