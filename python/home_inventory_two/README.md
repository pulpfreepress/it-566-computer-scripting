# Project Template
Provides a suggested multifile project organization suitable for IT 566 and a wide range of professional python projects. 

## Assumptions
- Python 3.10.6+ is installed
- Python source code is stored in src directory
- Tests are stored in tests directory.
- Pipenv is used to create virtual environment
- Pytest used for testing

## How To Run

- Run `./build.sh --checktools` to ensure required tools are installed

```
Sat Sep 17 15:21:21 EDT 2022
~/dev/dev.classes/it-566-computer-scripting/python/project_template (main)
[545:48] swodog@RicksMacPro $ ./build.sh --checktools
Checking for required tools...
aws: OK
git: OK
python3: OK
pipenv: OK
sometoolnotinstalled: MISSING
```
- Currently checks for: aws, git, python3, pipenv, and sometoolnotinstalled just to show you how a missing tool report would look like...aws refers to the aws cli.
- Edit TOOLS list in `.build.sh` to add or remove tools as you see fit
- `./build.sh --runmain` executes `pipenv run python3 src/main.py`
- `./build.sh --help` displays usage explained here
```
Sat Sep 17 15:26:36 EDT 2022
~/dev/dev.classes/it-566-computer-scripting/python/project_template (main)
[546:49] swodog@RicksMacPro $ ./build.sh --help

-----------------------------------------
 Usage: ./build.sh [ --help | --checktools | no argument | --install | --runmain | --runtests ]

 Examples: ./build.sh --checktools   # Show this usage message
           ./build.sh --help         # Check for required tools
           ./build.sh                # Default: -checktools and -help
           ./build.sh --install      # pipenv install
           ./build.sh --runmain      # pipenv run python3 src/main.py
           ./build.sh --runtests     # pipevn run pytest
```

**NOTE:** May need to change python3 to python on Windows
