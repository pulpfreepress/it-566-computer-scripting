#!/bin/bash

# create logs directory if not there
echo 'Creating logs directory if it does not already exist...'
mkdir -p logs
echo 'Deleting old log files if they exist...'
rm -f logs/*

d=$(date)
echo $d
echo  $d': Dropping database...' | tee -a logs/drop_database.log
mysql < db_version_1/drop_database.sql 2>&1 | tee -a logs/drop_database.log
echo $d': Dropping user...' | tee -a logs/drop_user.log
mysql < db_version_1/drop_user.sql 2>&1 | tee -a logs/drop_user.log
echo $d': Creating database...' | tee -a logs/create_database.log
mysql < db_version_1/create_database.sql 2>&1 | tee -a logs/create_database.log
echo $d': Creating user...' | tee -a logs/create_user.log
mysql < db_version_1/create_user.sql 2>&1 | tee -a logs/create_user.log
echo $d': Creating tables...' | tee -a logs/create_tables.log
mysql < db_version_1/create_tables.sql 2>&1 | tee -a logs/create_tables.log
echo $d': Inserting test data...' | tee -a logs/insert_test_data.log
mysql < db_version_1/insert_test_data.sql 2>&1 | tee -a logs/insert_test_data.log

