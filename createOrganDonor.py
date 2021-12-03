import psycopg2


def insertOrganDonor(donorid,bloodtype,age,chronicaldiseases,drugusage,tattoodate,medhistory,lastdonation,phonenumber,region,oname):
    """ Connect to the PostgreSQL database server """
    conn = None
    sql = """
        INSERT INTO organdonor(donorid,bloodtype,age,chronicaldiseases,drugusage,tattoodate,medhistory,lastdonation,phonenumber,region,oname)
        VALUES(%s)"""
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
        
        cur.execute(sql, (donorid,bloodtype,age,chronicaldiseases,drugusage,tattoodate,medhistory,lastdonation,phonenumber,region,oname))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("ERROR:")
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def main():
    insertOrganDonor(1,'A-',32,'None','None','NULL','NONE','NULL',7732023030,'chicago','lung')
    insertOrganDonor(2,"AB-",23,"None","Alcohol","NULL","NONE","NULL",7732023030,"chicago","lung")
    insertOrganDonor(3,"O+",55,"None","Smoked","NULL","NONE","NULL",7732023010,"chicago","lung")

if __name__ == '__main__':
    main()


