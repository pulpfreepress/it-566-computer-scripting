# Clean Architecture Example

This project demonstrates the following concepts:
- Separation of concerns
- Database design evolution

## Dependencies
- Python 3.10
- pipenv


## The Database
The database design has been altered from the simple one-table design shown in the sql_test_project. There are now two tables: inventories and items. There are two database script folders: **db_version_1** and **db_version_2**. The `initialize_database.sh` script does the following:
-  First, it creates version 1 of the database by calling all the scripts in the **db_version_1** directory. This results in a database named `home_inventory`, a user named `home_inventory_user`, and one table named `items`, which is populated with test data.
-  Next, it calls the scripts in the **db_version_2** directory in the following order:
    - *create_inventories_table.sql*: Create a new table called `inventories`
    - *insert_inventory_row.sql*: Inserts one row into the inventories table. This must be done so that a foreign key can be added to the items table
    - *alter_items_table.sql*: Creates a new column to hold a foreign key value, then establishes a foreign key constraint between the `items` table and the `inventories` table

  ## Application Architecture
  ![Clean Architecture](../../Images/CleanArchitecture.png)

Referring to the application architecture diagram shown above — A user launches the program by running main.py. 

## Running The Application
First, make sure you have MySQL running and you've confirmed the port number. You may need to edit the port number `mysql_persistence_wrapper.py`.

This project comes with a `build.sh` file which should be used because it assumes the use of a **pipenv virtual environment**. If the `.venv` directory is not present, which it will not be when you clone the repository, pipenv will install the packages listed in the `Pipfile.lock` file. 

To run the application type: `./build.sh --runmain` in a bash terminal. To get help simply type `./build.sh` with no arguments. The build script checks for a valid execution environment as shown in the output shown below.

```
Thu Nov 24 07:45:32 EST 2022
~/dev/dev.classes/it-566-computer-scripting/python/clean_architecture (main)
[517:17] swodog@RicksMacPro $ ./build.sh
Checking for required tools...
mysql: OK
git: OK
python3: OK
pipenv: OK

-----------------------------------------
 Usage: ./build.sh [ --help | --checktools | no argument | --install | --runmain | --runtests ]

 Examples: ./build.sh --checktools   		# Show this usage message
           ./build.sh --help         		# Check for required tools
           ./build.sh                		# Default: -checktools and -help
           ./build.sh --install      		# pipenv install
           ./build.sh --runmain      		# pipenv run python3 src/main.py
           ./build.sh --runtests     		# pipenv run pytest
           ./build.sh --checkdoccomments	# pipevn run pydocstyle src/
           ./build.sh --initialize_database	# source database/initialize_database.sh
```

## Where To Go From Here
Not all functionality is implemented. The menu indicates what works and what doesn't. I implemented several swaths through the architecture as a reference. 

## Screenshots
```
            Household Inventory Application

		1. New Inventory (Not Implemented)
		2. List Inventories
		3. Select Inventory
		4. List Inventory Items
		5. Add Items (Not Implemented)
		6. Exit

Please enter menu item number:
```

```
+----+----------------+-------------------------------+
| ID |      Name      |          Description          |
+----+----------------+-------------------------------+
| 1  | Home Inventory | List of all items in the home |
+----+----------------+-------------------------------+


Press any key to continue...
```

```
You entered: 3
select_inventory() method called.
+----+----------------+-------------------------------+
| ID |      Name      |          Description          |
+----+----------------+-------------------------------+
| 1  | Home Inventory | List of all items in the home |
+----+----------------+-------------------------------+


Select inventory id from list: 1
```

```
            Household Inventory Application

		1. New Inventory (Not Implemented)
		2. List Inventories
		3. Select Inventory
		4. List Inventory Items
		5. Add Items (Not Implemented)
		6. Exit

Please enter menu item number: 4
You entered: 4
list_inventory_items() method called...
+----+--------------+---------------+-------+
| ID | Inventory ID |      Item     | Count |
+----+--------------+---------------+-------+
| 1  |      1       |     Truck     |   1   |
| 2  |      1       |  MacBook Pro  |   1   |
| 3  |      1       |     Table     |   1   |
| 4  |      1       |      Car      |   1   |
| 5  |      1       |     Chair     |   1   |
| 6  |      1       | China Cabinet |   1   |
| 7  |      1       |      Sofa     |   1   |
+----+--------------+---------------+-------+


Press any key to continue...
```