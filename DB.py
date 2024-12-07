import pymysql

class Connection:
    def __init__(self):
        self.connection()
    
    def connection(self):
        try:
            connection_DB = pymysql.connect(
                host = "localhost",
                user = "root",
                password = "helloworld",
                database = "NewTaxi"
            )
            return connection_DB
        except Exception as e:
            print("Error:",e)