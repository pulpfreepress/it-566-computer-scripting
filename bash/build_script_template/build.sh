#!/bin/bash

#: Title        : build.sh
#: Date         : 10 September 2022
#: Author       : Rick Miller
#: Version      : 1.0
#: Description  : Build script template
#: Options      : None

# Global Constants
declare -r TOOLS="aws git python pipenv sometoolnotinstalled"

# Global Variables 
declare _confirm=1


check_tools() { 	## Check if required tools are installed
	echo "Checking for required tools..."
	for tool in $TOOLS
	do
		type $tool &> /dev/null && ([ $_confirm -eq 1 ] && echo "$tool: OK" || true) || (echo "$tool: MISSING"; exit 1);
	done
}


display_usage() {
	echo
	echo "-----------------------------------------"
	echo " Usage: ./`basename $0` [ -help | message | no argument ] "
	echo 
	echo " Examples: ./`basename $0` -help.         # Show this usage mesage "
	echo "           ./`basename $0` -checktools    # Check for required tools "
	echo "           ./`basename $0`                # Execute default action "
}

default_action() {
 	printf "%s " $@
}


process_arguments() {
	case $1 in
		-help) # If first argument is '-help' call display_usage
			display_usage 
			;;

		-checktools) # Verify required development tools are installed
			check_tools
			;;

		*) 	# Otherwise, call default_action with all arguments	
			default_action $@
	esac
}


main(){
	process_arguments "$@"
	exit 1
}


# Call main() with all command-line arguments
main "$@"

