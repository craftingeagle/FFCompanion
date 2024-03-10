from commands import handle_command

def main():
    print("Welcome to FFCompanion!")
    while True:
        command = input("Enter command: ")
        if command.lower() == 'exit':
            print("Exiting FFCompanion.")
            break
        else:
            handle_command(command)

if __name__ == "__main__":
    main()
