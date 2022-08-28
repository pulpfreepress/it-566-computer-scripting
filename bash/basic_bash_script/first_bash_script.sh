#!/bin/bash

# This is a comment
# All characters to the right of the # are ignored
#: This is also a comment, but the colon helps if you need
#: to search for special types of comments. The character
#: you use is up to you...

#: Title        : first_bash_script
#: Date         : 28 August 2022
#: Author       : Rick Miller
#: Version      : 1.0
#: Description  : prints Hello, World!, or entered message
#: Options      : None

# Global Constants
declare -r DEFAULT_MESSAGE="Hello, World!"

# Global Variables 
declare _message=${DEFAULT_MESSAGE} # _message variable not used in script


display_usage() {
	echo
	echo "-----------------------------------------"
	echo " Usage: `basename $0` [ -help | message | no argument ] "
	echo 
	echo " Examples: ./first_bash_script.sh help     # Show this usage mesage "
	echo "           ./first_bash_script.sh message  # Print the message to the screen "
	echo "           ./first_bash_script.sh          # Print default message "
}

print_message() {
 	printf "%s " $@
}


process_arguments() {
	case $1 in
		-help) # If first argument is '-help' call display_usage
			display_usage 
			;;

		*) 	# Otherwise, call print_message with all arguments	
			print_message $@
	esac
}


main(){
	# If no arguments call print_message() with value of DEFAULT_MESSAGE
	if [ "$#" -lt 1 ]; 
	then
		print_message ${DEFAULT_MESSAGE}
	else
		# Else, call process_argument with all arguments
		process_arguments "$@"
	fi

	exit 1
}


# Call main() with all command-line arguments
main "$@"

