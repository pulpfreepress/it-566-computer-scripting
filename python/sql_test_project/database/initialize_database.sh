#!/bin/bash

# create logs directory if not there
echo 'Creating logs directory if it does not already exist...'
mkdir -p logs

echo 'Dropping database...'
mysql < db_version_1/drop_database.sql 2>&1 > logs/drop_database.log
echo 'Dropping user...'
mysql < db_version_1/drop_user.sql 2>&1 > logs/drop_user.log
echo 'Creating database...'
mysql < db_version_1/create_database.sql 2>&1 > logs/create_database.log
echo 'Creating user...'
mysql < db_version_1/create_user.sql 2>&1 > logs/create_user.log
echo 'Creating tables...'
mysql < db_version_1/create_tables.sql 2>&1 > logs/create_tables.log
echo 'Inserting test data...'
mysql < db_version_1/insert_test_data.sql 2>&1 > logs/insert_test_data.log


