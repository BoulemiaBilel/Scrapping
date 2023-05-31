import sqlite3


class Database():

    def __init__(self):
        self.c = self.create_database()
        self.create_table()

    def create_database(self):

        try:
            conn = sqlite3.connect('projet_db.db')
            c = conn.cursor()
            return c
       
        except:
            pass

    def create_table(self):

        try:
            self.c.execute("""CREATE TABLE info (

                organisme VARCHAR(50),
                code_postal INT,
                adresse VARCHAR(200),
                telephone VARCHAR(15),
                courriel VARCHAR(30),
                site VARCHAR(50)
                )

                """)
        except:
            pass


    def add_data(self, data):

        self.c.execute("INSERT INTO info VALUES(:organisme, :code_postal, :adresse, :telephone, :courriel, :site)",
        {

        'organisme': data["organisme"],
        'code_postal': data["code_postal"],
        'adresse': data["adresse"],
        'telephone': data["telephone"],
        'courriel': data["courriel"],
        'site': data["site"],
        }
        )