import psycopg2



def createDoctor(username,password,conn):
    """ Connect to the PostgreSQL database server """
    try:
        # create a cursor
        cur = conn.cursor()
        
        exec = """
            create USER {username} WITH LOGIN PASSWORD '{password}';
            grant doctorrole on {username};
        """.format(username = username,password = password)
        cur.execute(exec)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def createPatient(username,password,conn):
    """ Connect to the PostgreSQL database server """
    try:

        cur = conn.cursor()
        
        exec = """
            create USER {username} WITH LOGIN PASSWORD '{password}';
            grant patientrole to {username};
        """.format(username = username,password = password)
        cur.execute(exec)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)