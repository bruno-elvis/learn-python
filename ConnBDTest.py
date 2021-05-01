'''
SQL SERVER
import pyodbc

#server = 'tcp:myserver.database.windows.net' 
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
     
server = "SERVIDOR\OBJETIVA"
database = "Empresario"
username = "sa"
password = "SA_0bjetiva"
    
cnx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)    

cursor = cnx.cursor()

qryUSE = 'USE Empresario'
qry = 'SELECT * FROM CADPRO'
'''

import fdb

con = fdb.connect(dsn='/var/database.fdb', user='SYSDBA', password='masterkey')
cursor = con.cursor()
cursor.executemany("SELECT * FROM DOC WHERE COD_MOD = '55'")
con.commit()
con.close()