#!/bin/bash

mysql -u root -proot test_database < "/docker-entrypoint-initdb.d/01_create_tables.sql"