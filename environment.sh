#!/bin/bash

export FLASK_APP=wsgi.py
export FLASK_ENV='development'
export FLASK_DEBUG=1

export MYSQL_DB_USER='anonymous'
export MYSQL_DB_PASSWORD=''
export MYSQL_DB_DB='ensembl_website_97'
export MYSQL_DB_HOST='ensembldb.ensembl.org'
export MYSQL_DB_PORT='3306'

export SQLALCHEMY_DATABASE_URI="mysql+pymysql://MYSQL_DB_USER:MYSQL_DB_PASSWORD@MYSQL_DB_HOST:MYSQL_DB_PORT/MYSQL_DB_DB"
