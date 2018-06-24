#!/bin/bash

if [ -z "$1" ]
then
    echo "No database name supplied, using default (stx)"
    DB_NAME=stx
else
    DB_NAME=$1
fi

echo 'Remove the database, if present'
dropdb ${DB_NAME}
echo 'Create a new database'
createdb ${DB_NAME}
echo 'Using Flask SQLAlchemy to create main database tables'
cd app
rm -rf migrations
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
echo 'adding function that duplicates a table, including indexes & foreign keys'
cd ..
psql ${DB_NAME} < create_table_like.sql
echo 'All done'
