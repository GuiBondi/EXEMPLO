from classes import pyodbc

class ColaboradorConnector:

    def obterConnectionString(self):
        servername='localhost'
        database='Loja'
        username='LojaUser'
        password='Pa$$w0rd'

        server="DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};PORT={};DATABASE={};UID={};PWD={};".format(servername,1433,database,username,password)

        return server

    def login(self,username,password):

        conn=pyodbc.connect(self.obterConnectionString())

        cursor=conn.cursor()

        sqlquery="EXEC dbo.SP_Login ?,?"
        
        values=(username, password)

        cursor.execute(sqlquery,values)

        result=cursor.fetchall()

        conn.close()

        return result

    def logout(self,username):

        conn=pyodbc.connect(self.obterConnectionString())

        cursor=conn.cursor()

        sqlquery="EXEC dbo.SP_Logout ?"

        values=(username)

        cursor.execute(sqlquery,values)

        result=cursor.fetchall()

        conn.close()

        return result

    def registarColaborador(self,username,nome,usernamenovo,password,telefone,email):

        conn=pyodbc.connect(self.obterConnectionString())

        cursor=conn.cursor()

        sqlquery="EXEC dbo.SP_RegistarColaborador ?,?,?,?,?,?"
        
        values=(username,nome,usernamenovo,password,telefone,email)

        cursor.execute(sqlquery,values)

        result=cursor.fetchall()

        conn.commit()

        conn.close()

        return result

    def recuperarPassword(self,email):

        conn=pyodbc.connect(self.obterConnectionString())

        cursor=conn.cursor()

        sqlquery="EXEC dbo.SP_RecuperarPassword ?"
        
        values=(email)

        cursor.execute(sqlquery,values)

        result=cursor.fetchall()

        conn.close()

        return result

    def novaPassword(self,username, password1, password2):

        conn=pyodbc.connect(self.obterConnectionString())

        cursor=conn.cursor()

        sqlquery="EXEC dbo.SP_NovaPassword ?,?,?"
        
        values=(username, password1, password2)

        cursor.execute(sqlquery,values)

        result=cursor.fetchall()

        conn.commit()

        conn.close()

        return result