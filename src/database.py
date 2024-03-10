import sqlite3

class PlayerDB:
    def __init__(self):
        self.conn = sqlite3.connect('ffcompanion.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Players (
                                id INTEGER PRIMARY KEY,
                                username TEXT,
                                level INTEGER,
                                kills INTEGER,
                                deaths INTEGER,
                                assists INTEGER
                            )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Teams (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                leader_id INTEGER,
                                FOREIGN KEY(leader_id) REFERENCES Players(id)
                            )''')
        self.conn.commit()

    def add_player(self, username, level, kills, deaths, assists):
        self.cursor.execute('''INSERT INTO Players (username, level, kills, deaths, assists)
                            VALUES (?, ?, ?, ?, ?)''', (username, level, kills, deaths, assists))
        self.conn.commit()

    def delete_player(self, player_id):
        self.cursor.execute("DELETE FROM Players WHERE id = ?", (player_id,))
        self.conn.commit()

    def update_player(self, player_id, field, value):
        self.cursor.execute(f"UPDATE Players SET {field} = ? WHERE id = ?", (value, player_id))
        self.conn.commit()

    def get_players(self):
        self.cursor.execute("SELECT * FROM Players")
        return self.cursor.fetchall()

    def create_team(self, name, leader_id):
        self.cursor.execute('''INSERT INTO Teams (name, leader_id)
                            VALUES (?, ?)''', (name, leader_id))
        self.conn.commit()

