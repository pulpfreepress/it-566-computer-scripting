# Home Inventory Application Framework

Implements a reference application you can use for inspiration. 

The application displays a sample menu from which users make a selection. The application processes user's menu choice and calls a corresponding method, which is stubbed out, or exits the application when the user enters 7 by setting the `self.keep_going` to `False`.

## General Instructions
Clone the containing repo into a local folder of your choice on your machine:

`git@github.com:pulpfreepress/it-566-computer-scripting.git`

Run `./build.sh` to check for required tools and display a list of commands.

Run `./build.sh --install` to install Pipfile packages.

**NOTE:** If you're running Windows, you'll need to edit the `build.sh` script, locate the `runmain()` method and change `python3` to `python`.

Run `./build.sh --runmain` to run the Home Inventory Application. 

Feel free to use this as the basis of your application if you're having trouble getting started. 


