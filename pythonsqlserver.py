import pyodbc as pyo

server = 'LAPTOP-84NVN7AB\SQLEXPRESS' 
database = 'dbmvkcorner' 
username = 'mvkcorner' 
password = '12345678' 
cnxn = pyo.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print('1-CREA TABLA')
InstrucSQL = "USE dbmvkcorner; CREATE TABLE PERSONA (ID INTEGER PRIMARY KEY, Nombres VARCHAR(50) NOT NULL, Apellidos VARCHAR(50) NOT NULL,SEXO CHAR(1) NOT NULL,CREADO DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL);"
print ('Crea la tabla PERSONA')
with cursor.execute(InstrucSQL):
    print ('Tabla Creada!')
print('2-INSERTA 1 REGISTRO')
print ('Insertando')
InstrucSQL = "INSERT INTO [dbmvkcorner].[dbo].[PERSONA] ([ID],[Nombres],[Apellidos],[SEXO])  VALUES (?,?,?,?);"
with cursor.execute(InstrucSQL,1,'Mvk','Corner','M'):
    print ('Registro Insertado!')
print('3-INSERTA 2 REGISTRO')
print ('Insertando')
InstrucSQL = "INSERT INTO [dbmvkcorner].[dbo].[PERSONA] ([ID],[Nombres],[Apellidos],[SEXO])  VALUES (?,?,?,?);"
with cursor.execute(InstrucSQL,2,'Persona 2','Apellido 2','F'):
    print ('Registro Insertado!')
print('4-LEE LA TABLA')
print ('Leyendo tabla')
InstrucSQL = "SELECT TOP (10) [ID],[Nombres],[Apellidos],[SEXO] FROM [dbmvkcorner].[dbo].[PERSONA];"
with cursor.execute(InstrucSQL):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
        row = cursor.fetchone()
print('5-ACTUALIZA')
print ('Actualizar Datos')
InstrucSQL = "UPDATE [dbmvkcorner].[dbo].[PERSONA] SET [Apellidos] = ? WHERE [ID] = ?"
with cursor.execute(InstrucSQL,'Corners',1):
    print ('Actualizada!')
print('6-LECTURA ACTUALIZADO')
print ('Leyendo tabla')
InstrucSQL = "SELECT TOP (10) [ID],[Nombres],[Apellidos],[SEXO] FROM [dbmvkcorner].[dbo].[PERSONA];"
with cursor.execute(InstrucSQL):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
        row = cursor.fetchone()
print('7-BORRAR REGISTRO')
print ('Borrar')
InstrucSQL = "DELETE FROM [dbmvkcorner].[dbo].[PERSONA] WHERE ID = ?"
with cursor.execute(InstrucSQL,2):
    print ('Registro 2 Borrado!')
print('8-LECTURA')
print ('Leyendo tabla')
InstrucSQL = "SELECT TOP (10) [ID],[Nombres],[Apellidos],[SEXO] FROM [dbmvkcorner].[dbo].[PERSONA];"
with cursor.execute(InstrucSQL):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
        row = cursor.fetchone()
print('9-BORRA LA TABLA')
InstrucSQL = "DROP TABLE [dbmvkcorner].[dbo].[PERSONA];"
print ('Borra Tabla')
cursor.execute(InstrucSQL)
print ('Borrada')
print('FIN------------------')


