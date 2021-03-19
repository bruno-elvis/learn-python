from os import read
import pandas as pd
import pyodbc
"""
server = 'tcp:myserver.database.windows.net'
database = 'Empresario' 
username = 'sa' 
password = 'SA_0bjetiva' 
cnx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
"""
#def retorna_conexao_sql():        
server = "SERVIDOR\OBJETIVA"
database = "Empresario"
username = "sa"
password = "SA_0bjetiva"
    
cnx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    
#return cnx.cursor()

qryUSE = 'USE Empresario GO'
qry = 'SELECT * FROM CAIXA'


pd.read_sql('USE Empresario GO', cnx)
consulta = pd.read_sql(qry, cnx)

print(pd.head())

cnx.close()

# MANIPULAÇÃO DE ARQUIVOS #
data = open("CONTAS.TXT", 'r+')

arquivo = pd.read_csv("CONTAS.TXT",  encoding = 'utf-8')

print(arquivo)
print(data.read())