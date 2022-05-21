#!/bin/bash

docker-compose exec db bash -c "chmod 0775 docker-entrypoint-initdb.d/init_database.sh"
docker-compose exec db bash -c "./docker-entrypoint-initdb.d/init_database.sh"
python3 testdata.py
mysql -u root -h 127.0.0.1 --port 3306 -proot < testData.sql