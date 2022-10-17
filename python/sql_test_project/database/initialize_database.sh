#!/bin/bash

# create logs directory if not there
echo 'Creating logs directory if it does not already exist...'
mkdir -p logs

date
echo 'Dropping database...' | tee -a logs/drop_database.log
mysql < db_version_1/drop_database.sql | tee -a logs/drop_database.log
echo 'Dropping user...' 2>&1 >> logs/drop_user.log
mysql < db_version_1/drop_user.sql 2>&1 >> logs/drop_user.log
echo 'Creating database...' 2>&1 >> logs/create_database.log
mysql < db_version_1/create_database.sql 2>&1 > logs/create_database.log
echo 'Creating user...' 2>&1 >> logs/create_user.log
mysql < db_version_1/create_user.sql 2>&1 >> logs/create_user.log
echo 'Creating tables...' 2>&1 >> logs/create_tables.log
mysql < db_version_1/create_tables.sql 2>&1 >> logs/create_tables.log
echo 'Inserting test data...' 2>&1 >> logs/insert_test_data.log
mysql < db_version_1/insert_test_data.sql 2>&1 >> logs/insert_test_data.log


