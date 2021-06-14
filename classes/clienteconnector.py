from classes import pyodbc

class ClienteConnector:
 
    def obterConnectionString(self):
        servername='localhost'
        database='Loja'
        username='LojaUser'
        password='Pa$$w0rd'

        server="DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};PORT={};DATABASE={};UID={};PWD={};".format(servername,1433,database,username,password)

        return server

    def inserirCliente(self,username,tipoCliente,nome,nif,morada,codigoPostal,telefone,email):

        conn=pyodbc.connect(self.obterConnectionString())

        cursor=conn.cursor()

        sqlquery="EXEC dbo.SP_InserirCliente ?,?,?,?,?,?,?,?"

        values=(username,tipoCliente,nome,nif,morada,codigoPostal,telefone,email)

        cursor.execute(sqlquery,values)
        
        result=cursor.fetchall()
        
        conn.commit()

        conn.close()

        return result

    def consultarCliente(self,username,clienteID):

        conn=pyodbc.connect(self.obterConnectionString())

        cursor=conn.cursor()

        sqlquery="EXEC dbo.SP_ConsultarCliente ?,?"
        
        values=(username,clienteID)

        cursor.execute(sqlquery,values)

        result=cursor.fetchall()

        conn.close()

        return result

    def consultarTodosOsClientes(self,username):

        conn=pyodbc.connect(self.obterConnectionString())

        cursor=conn.cursor()

        sqlquery="EXEC dbo.SP_ConsultarTodosOsClientes ?"
        values=(username)
        
        cursor.execute(sqlquery,values)

        result=cursor.fetchall()

        conn.close()

        return result

    def atualizarCliente(self,username,clienteID,tipoCliente,nome,nif,morada,codigoPostal,telefone,email):

        conn=pyodbc.connect(self.obterConnectionString())

        cursor=conn.cursor()

        sqlquery="EXEC dbo.SP_atualizarCliente ?,?,?,?,?,?,?,?,?"

        values=(username,clienteID,tipoCliente,nome,nif,morada,codigoPostal,telefone,email)

        cursor.execute(sqlquery,values)

        result=cursor.fetchall()

        conn.commit()

        conn.close()

        return result

    def RemoverCliente(self,username,clienteID):

        conn=pyodbc.connect(self.obterConnectionString())

        cursor=conn.cursor()

        sqlquery="EXEC dbo.SP_RemoverCliente ?,?"

        values=(username,clienteID)

        cursor.execute(sqlquery,values)

        result=cursor.fetchall()

        conn.commit()

        conn.close()

        return result

    def Procurar(self,username,search):
        conn=pyodbc.connect(self.obterConnectionString())
        
        cursor=conn.cursor()

        sqlquery="EXEC dbo.SP_Search ?,?"

        values=(username,search)

        cursor.execute(sqlquery,values)

        result=cursor.fetchall()

        conn.close()

        return result 
