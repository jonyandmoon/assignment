import mysql.connector
import os
import json
from typing import Dict, Tuple
class DB:
    db_conn :str
    db_name :str
    def __init__(self):
        # get database server credentials
        file=open("./config_db.json", "r" )
        json_config = file.read()
        config=json.loads(json_config)
        self.db_name=config['db_name']
        self.db_conn = mysql.connector.connect(
        host=config["db_host"],
        user=config["db_user"],
        password=config["db_password"]
        )
        mycursor = self.db_conn.cursor()
        # check whether db exists
        mycursor.execute("select schema_name from information_schema.schemata where schema_name = '"+self.db_name+"';")
        myresult = mycursor.fetchone()
        if(myresult):
            mycursor.execute("USE "+self.db_name);
            mycursor.close();
        else:
            self.setupDB()
        
    def setupDB(self):
        mycursor = self.db_conn.cursor(dictionary=True)
        # create DB
        mycursor.execute("CREATE DATABASE "+self.db_name)
        mycursor.execute("USE "+self.db_name)
        with open(
            "./setup.sql", "r"
        ) as file:
            script = file.read()
            mycursor.execute(script)
        mycursor.close()
        self.db_conn.close()

    
    #blue print of execute commands
    def call_from_db(self,query):
        cursor = self.db_conn.cursor()
        cursor.execute(query)
        data=cursor.fetchall()
        cursor.close()
        return data
    
    def conn_close(self):
        self.db_conn.close()

    def commit_db(self):
        self.db_conn.commit()

    def  __del__(self):
        self.conn_close()
    