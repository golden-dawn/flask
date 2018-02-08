#!/bin/bash
echo 'Remove the database, if present'
dropdb stx
echo 'Create a new database'
createdb stx
echo 'Using Flask SQLAlchemy to create main database tables'
cd app
rm -rf migrations
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
echo 'adding function that duplicates a table, including indexes & foreign keys'
psql stx < create_table_like.sql
echo 'All done'
