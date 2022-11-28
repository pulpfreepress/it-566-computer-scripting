#!/bin/bash

# create logs directory if not there
echo 'Creating logs directory if it does not already exist...'
mkdir -p logs
echo 'Deleting old log files if they exist...'
rm -f logs/*

d=$(date)
echo $d

# Create Database Version 1
echo "Running DB Version 1 Scripts..."
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

# Refactor Database to Version 2
echo "-------------------------------------------------"
echo "Running DB Version 2 Scripts... "
echo  $d': Adding inventories table...' | tee -a logs/v2_create_inventories_table.log
mysql < db_version_2/create_inventories_table.sql 2>&1 | tee -a logs/v2_create_inventories_table.log
# Need to create a row in the inventories table before altering the items table
echo  $d': Inserting inventory row...' | tee -a logs/v2_insert_inventory_row.log
mysql < db_version_2/insert_inventory_row.sql 2>&1 | tee -a logs/v2_insert_inventory_row.log
echo  $d': Altering items table...' | tee -a logs/v2_alter_items_table.log
mysql < db_version_2/alter_items_table.sql 2>&1 | tee -a logs/v2_alter_items_table.log



