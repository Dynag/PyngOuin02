import fichier.lib.connector as connector
import fichier.design as design
import fichier.param_db as param_db
import fichier.var as var



def create_server_connection():
    data = param_db.lire_param_db()
    host_name = data[0]
    database = data[1]
    user_name = data[2]
    user_password = data[3]

    connection = None
    try:
        connection = connector.connect(
            host=host_name,
            database=database,
            user=user_name,
            passwd=user_password
        )
    except Exception as inst:
        design.logs("MySql - create_server_connection - "+str(inst))

    return connection

def execute_query(query):
    try:
        connection = create_server_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
    except Exception as inst:
        design.logs("MySql - execute_query - "+str(inst))


def create_table(table):
    create_teacher_table = """
        CREATE TABLE IF NOT EXISTS """+str(var.nom_site)+"""(
          id INT PRIMARY KEY AUTO_INCREMENT,
          ip VARCHAR(40) NOT NULL,
          nom VARCHAR(40) NOT NULL,
          etat VARCHAR(3) NOT NULL,
          latence VARCHAR(40) NOT NULL
          );
         """
    try:
        execute_query(create_teacher_table)
    except Exception as inst:
        design.logs("MySql - create_table - "+str(inst))

def vider_table(table):
    delete = """
        TRUNCATE TABLE `""" + var.nom_site + """`"""
    try:
        execute_query(delete)
    except Exception as inst:
        design.logs("MySql - vider_table - "+str(inst))

def add_enre(ip, nom, etat, latence, table):

    add = """
    INSERT INTO `"""+var.nom_site+"""`(`ip`, `nom`, `etat`, `latence`) VALUES (
        '"""+ip+"""',
        '"""+nom+"""',
        '"""+etat+"""',
        '"""+latence+"""')
    """
    try:
        execute_query(add)
    except Exception as inst:
        design.logs("MySql - add_enre - "+str(inst))
