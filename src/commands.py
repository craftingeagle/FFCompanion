from database import PlayerDB

db = PlayerDB()

def handle_command(command):
    if command.lower() == 'help':
        print("Available commands: help, list_players, add_player, delete_player, update_player, create_team, exit")
    elif command.lower() == 'list_players':
        players = db.get_players()
        print("Player List:")
        for player in players:
            print(player)
    elif command.lower() == 'add_player':
        username = input("Enter player username: ")
        level = int(input("Enter player level: "))
        kills = int(input("Enter player kills: "))
        deaths = int(input("Enter player deaths: "))
        assists = int(input("Enter player assists: "))
        db.add_player(username, level, kills, deaths, assists)
        print("Player added successfully.")
    elif command.lower() == 'delete_player':
        player_id = int(input("Enter player ID to delete: "))
        db.delete_player(player_id)
        print("Player deleted successfully.")
    elif command.lower() == 'update_player':
        player_id = int(input("Enter player ID to update: "))
        field = input("Enter field to update (username/level/kills/deaths/assists): ")
        value = input(f"Enter new value for {field}: ")
        db.update_player(player_id, field, value)
        print("Player updated successfully.")
    elif command.lower() == 'create_team':
        team_name = input("Enter team name: ")
        leader_id = int(input("Enter leader ID: "))
        db.create_team(team_name, leader_id)
        print("Team created successfully.")
    elif command.lower() == 'exit':
        print("Exiting FFCompanion.")
    else:
        print("Invalid command. Type 'help' for available commands.")

