#!/bin/bash

#: Title        : build.sh
#: Date         : 10 September 2022
#: Author       : Rick Miller
#: Version      : 1.0
#: Description  : Build script template
#: Options      : None

# Global Constants
# TOOLS: A list of required tools. Edit as required. Sometoolnotinstalled to 
#        show what a missing tool message looks like. 
declare -r TOOLS="aws git python3 pipenv sometoolnotinstalled"

# Global Variables 
declare _confirm=1


check_tools() { 	## Check if required tools are installed
	echo "Checking for required tools..."
	for tool in $TOOLS
	do
		command -v $tool &> /dev/null && ([ $_confirm -eq 1 ] && echo "$tool: OK" || true) || (echo "$tool: MISSING"; exit 1);
	done
}


display_usage() {
	echo
	echo "-----------------------------------------"
	echo " Usage: ./`basename $0` [ -help | -checktools | no argument ] "
	echo 
	echo " Examples: ./`basename $0` -checktools    # Show this usage message "
	echo "           ./`basename $0` -help.         # Check for required tools "
	echo "           ./`basename $0`                # Default: -checktools and -help "
}

default_action() {
 	check_tools
 	display_usage
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

