import psycopg2
from tabulate import tabulate

def organDonorList(region, organ):
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
            SELECT donorid, age, chronicalDiseases, drugUsage from organdonor
            WHERE oname = '{organname}' and region = '{region}';
                """.format(organname = organ,region = region)

	# execute a statement
        print('List of Available Donors: ')
        cur.execute(exec)
        row = cur.fetchone()
        donors = []
        headers = ['ID','Age','Chronical Diseases','Drug Usage']
        while row is not None:
            currrow = []
            for i in range(0,4):
                currrow.append(row[i])
            donors.append(currrow)
            row = cur.fetchone()
        print(tabulate(donors,headers,tablefmt="pipe"),'\n')
        input("Click enter to view a list of specialized doctors")
        print("List of Available doctors: ")
        exec = """
            SELECT doctorid, dname, fee, hname from doctor
            NATURAL JOIN hospital
            WHERE specialization = '{organname}' and region = '{region}';
                """.format(organname = organ,region = region)
        cur.execute(exec)
        row = cur.fetchone()
        headers = ['ID','Name','Fee','Hospital']
        doctors = []
        while row is not None:
            currrow = []
            for i in range(0,4):
                currrow.append(row[i])
            doctors.append(currrow)
            row = cur.fetchone()
        print(tabulate(doctors,headers,tablefmt="pipe"),'\n')
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def main():
    organDonorList("chicago","lung")


if __name__ == '__main__':
    main()


