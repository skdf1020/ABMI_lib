import pyodbc
import pandas as pd


class DBcon:
    # get connection with server
    def __init__(self, ip_ad, db_name, uid, pwd, tsc=False):
        self.db_name = db_name
        if tsc is True:
            self.con = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};\
                                        SERVER=" + ip_ad + ";\
                                        DATABASE=" + db_name + ";\
                                        Trusted_connection=yes")
        else:
            self.con = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};\
                                        SERVER=" + ip_ad + ";\
                                        DATABASE=" + db_name + ";\
                                        uid=" + uid + ";\
                                        pwd=" + pwd)

    # get table schema
    def schema_tables(self):
        query = "select * from " + self.db_name + ".INFORMATION_SCHEMA.TABLES"
        return pd.read_sql_query(query, self.con)

    # get column schema
    def schema_columns(self):
        query = "select TABLE_NAME, COLUMN_NAME, DATA_TYPE from " + self.db_name + ".INFORMATION_SCHEMA.COLUMNS"
        return pd.read_sql_query(query, self.con)

    # execute query
    def _query(self, query):
        return pd.read_sql_query(query, self.con)    

#class datafrm:
#    def __init__(self, query, con):
#        self.result = pd.read_sql_query(query, con)

#    def get_table(self):
#        return self.result

#    def iloc(self, row, end, col):
#        return self.result.iloc[row:end, col]

#    def values(self):
