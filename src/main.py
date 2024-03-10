from commands import handle_command
import sys
import os

# Set up colors for terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function to print welcome message
def print_welcome():
    print(bcolors.HEADER + "=========================================")
    print("          Welcome to FFCompanion")
    print("=========================================" + bcolors.ENDC)
    print(bcolors.OKGREEN + "Version: 1.0")
    print("Creator: CodeCraftingEagle")
    print("GitHub: https://github.com/craftingeagle")
    print("YouTube: https://www.youtube.com/@CodeCraftingEagle")
    print("Usage: Enter 'help' for available commands." + bcolors.ENDC)
    print(bcolors.HEADER + "=========================================")
    print("=========================================" + bcolors.ENDC)
def main():
    # Print welcome message
    print_welcome()

    while True:
        command = input("Enter command: ")
        if command.lower() == 'exit':
            print("Exiting FFCompanion.")
            break
        else:
            handle_command(command)

if __name__ == "__main__":
    main()
