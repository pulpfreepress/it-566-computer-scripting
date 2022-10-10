#!/bin/bash

mysql < db_version_1/drop_database.sql 2>&1 > logs/drop_database.log
mysql < db_version_1/create_database.sql 2>&1 > logs/create_database.log
mysql < db_version_1/create_tables.sql 2>&1 > logs/create_tables.log
mysql < db_version_1/insert_test_data.sql 2>&1 > logs/insert_test_data.log


