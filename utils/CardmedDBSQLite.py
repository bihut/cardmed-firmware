import os
import sqlite3
from models_cardmed import *
from models_cardmed import CardmedDB
from models_cardmed.MonitorDataDB import MonitorDataDB
from utils.Utils import Utils


class CardmedDBSQLite:
    TABLE_CARDMED="cardmed"
    TABLE_CONFIGURATIONS="configurations"
    TABLE_MONITORDATA="monitordata"
    def __init__(self, db_file,clean=False):
        self.db_file = db_file
        self.conn = None
        if clean:
            self.deleteDB()
        self.create_connection()
        self.create_tables()

    def deleteDB(self):
        if os.path.exists(self.db_file):
            print(f"Eliminando base de datos '{self.db_file}'...")
            os.remove(self.db_file)
    def create_connection(self):
        try:
            if not os.path.exists(self.db_file):
                print(f"Creando base de datos '{self.db_file}'...")
                open(self.db_file, 'a').close()  # Crear el archivo
            self.conn = sqlite3.connect(self.db_file)
            print(f"Conexión a la base de datos '{self.db_file}' establecida correctamente")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos '{self.db_file}': {e}")

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Conexión a la base de datos cerrada")

    def create_tables(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS cardmed (
                                deviceid TEXT PRIMARY KEY,
                                customid TEXT NOT NULL default '',
                                address TEXT,
                                country TEXT,
                                entity TEXT,
                                owner TEXT,
                                owneremail TEXT,
                                ownerphone TEXT,
                                deployed timestamp default (strftime('%s', 'now'))
                            )
                        """)


            cursor.execute("""
                CREATE TABLE IF NOT EXISTS configurations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company TEXT,
                    device TEXT,
                    models TEXT,
                    path TEXT,
                    lastupdate timestamp default (strftime('%s', 'now'))
                )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS monitordata (
                created timestamp default (strftime('%s', 'now')),
                configuration_id INTEGER NOT NULL,
                att TEXT NOT NULL,
                val FLOAT,
                PRIMARY KEY(configuration_id,created,att),
                FOREIGN KEY (configuration_id) REFERENCES configurations (id)
            )
            """)
            self.conn.commit()
            print("Tablas  creada exitosamente")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla 'users': {e}")

    def execute_query(self, query, parameters=()):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, parameters)
            self.conn.commit()
            print("Consulta ejecutada exitosamente")
            return cursor
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

    def insert_configuration(self, configuration):
        query = "INSERT INTO "+CardmedDBSQLite.TABLE_CONFIGURATIONS+" (company, device,models,path) VALUES (?, ?, ?,?)"
        self.execute_query(query, (configuration.company, configuration.device, configuration.model,configuration.path))

    def insert_cardmed(self, cardmed):
        query = "INSERT INTO "+CardmedDBSQLite.TABLE_CARDMED+" (deviceid, customid,address,country,entity,owner,owneremail,ownerphone) VALUES (?, ?, ?,?,?,?, ?, ?)"
        self.execute_query(query, (cardmed.deviceid, cardmed.customid, cardmed.address,cardmed.country,cardmed.entity,cardmed.owner,cardmed.owneremail,cardmed.ownerphone))

    def update_cardmedByID(self, deviceid, cardmed):
        query = "UPDATE "+CardmedDBSQLite.TABLE_CARDMED+" SET customid = ?, address = ?, country = ?, entity = ?, owner = ?, owneremail = ?, ownerphone = ? WHERE deviceid = ?"
        self.execute_query(query, (cardmed.customid, cardmed.address, cardmed.country, cardmed.entity, cardmed.owner, cardmed.owneremail, cardmed.ownerphone, deviceid))

    def update_configuration(self, configuration_id, configuration):
        query = "UPDATE "+CardmedDBSQLite.TABLE_CONFIGURATIONS+" SET company = ?, device = ?, models = ?, path = ? WHERE id = ?"
        self.execute_query(query, (configuration.company, configuration.device, configuration.model, configuration.path, configuration_id))

    def delete_configuration(self, configuration_id):
        query = "DELETE FROM "+CardmedDBSQLite.TABLE_CONFIGURATIONS+" WHERE id = ?"
        self.execute_query(query, (configuration_id,))

    def deleteAllConfigurations(self):
        query = "DELETE FROM "+CardmedDBSQLite.TABLE_CONFIGURATIONS
        self.execute_query(query)

    def insertMonitorData(self, monitorData):
        query = "INSERT INTO "+CardmedDBSQLite.TABLE_MONITORDATA+" (created, configuration_id, att, val) VALUES (?, ?, ?, ?)"
        self.execute_query(query, (monitorData.created, monitorData.configuration_id, monitorData.att, monitorData.val))

    def getAllMonitorDataByConfigurationID(self, configuration_id):
        query = "SELECT * FROM "+CardmedDBSQLite.TABLE_MONITORDATA+" WHERE configuration_id = ?"
        cursor = self.execute_query(query, (configuration_id,))
        return cursor.fetchall()
# Ejemplo de uso:
if __name__ == "__main__":
    debug = True
    db_file = "db/cardmed_database_borrar.db"
    db = CardmedDBSQLite(db_file,clean=(not debug))
    #config = ConfigurationDB.ConfigurationDB(1, "company1", "device1", "model1", "path1", "2021-10-01")
    #db.insert_configuration(config)
    for i in range(0,10):
        monitordata=MonitorDataDB(Utils.getCurrentTimeStamp(),1,"att"+str(i),i)
        db.insertMonitorData(monitordata)
    # Insertar un usuario
    ##db.insert_user("user1", "user1@example.com", "password1")

    # Actualizar la contraseña de un usuario
    #db.update_user_password(1, "new_password")

    # Eliminar un usuario
    #db.delete_user(1)

    # Recuperar un usuario por su ID
    #user = db.get_user_by_id(1)
    #if user:
    #    print("Usuario encontrado:", user)
    #else:
    #    print("Usuario no encontrado")

    # Recuperar todos los usuarios
    #users = db.get_all_users()
    #print("Todos los usuarios:", users)

    db.close_connection()