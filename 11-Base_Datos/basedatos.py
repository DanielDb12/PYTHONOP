import sqlite3
import getpass

def main():
    crear_usuario(5,"juan","superclave")

def main2():
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(username,password):
        print("login correcto")

    else:
        print('Login incorrecto')


def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    print("Query a ejecutar: ", query)

    rows = cursor.execute(query)
    data = rows.fetchone()
    print("data es",type(data))




    cursor.close()
    conn.close()
   
'''if data == None:
    return False

return True
'''



def crear_usuario(identificador,usuario,clave):
    '''insolation_Level NOne nos sirve para enviar automaticamente al servidor '''
    conn = sqlite3.connect('miaplicacion.db', isolation_level=None)
    cursor = conn.cursor()

    query = f"INSERT INTO users(id,username,password) VALUES(?,?,?)"

    rows = cursor.execute(query, (identificador, usuario, clave))
    print(type(rows))

    '''el commit hay que colocarse para enviarle al servidor'''
    conn.commit()
    cursor.close()
    conn.close()

     

if __name__ == '__main__':
    main()
