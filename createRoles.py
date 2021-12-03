import psycopg2



def createDoctor(username,password):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host = "localhost",
            dbname = "bloodDonation",
            user = "postgres",
            password = "password"
            )
		
        # create a cursor
        cur = conn.cursor()
        
        exec = """
            create role {username} WITH LOGIN PASSWORD '{password}';
            grant select on patient to {username};
            grant select on donor to {username};
            grant insert ON organ to {username};
        """.format(username = username,password = password)
        cur.execute(exec)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def createDoctor(username,password):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host = "localhost",
            dbname = "bloodDonation",
            user = "postgres",
            password = "password"
            )
		
        # create a cursor
        cur = conn.cursor()
        
        exec = """
            create role {username} WITH LOGIN PASSWORD '{password}';
            grant select on donor(donorID,bloodtype,chronicaldiseases,drugusage,medhistory)
        """.format(username = username,password = password)
        cur.execute(exec)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
