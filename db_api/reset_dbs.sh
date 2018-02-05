#!/bin/bash
echo 'Removing the existing databases'
dropdb stx
dropdb stx_test
echo 'Creating the main and test databases'
createdb stx
createdb stx_test
echo 'Using Flask SQLAlchemy to create main database tables'
cd app
rm -rf migrations
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
echo 'Dumping the main database schema,and copying into the test database'
pg_dump --schema-only -f /tmp/stx.sql stx
psql stx_test < /tmp/stx.sql
cd ..
echo 'All done'
