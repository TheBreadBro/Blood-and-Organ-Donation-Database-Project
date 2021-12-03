import psycopg2
from tabulate import tabulate

def donorMatchList():
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
            SELECT h.hospitalID, h.hName, SUM((d.fee+h.hcost)*d.completedOperations) 
            FROM hospital h
            INNER JOIN doctor d
            on h.hospitalID = d.hospitalID
            GROUP BY h.hospitalID
            """
	# execute a statement
        print('Matched: ')
        cur.execute(exec)
        row = cur.fetchone()
        donors = []
        headers = ['Hospital ID','Hospital Name','Earnings']
        while row is not None:
            currrow = []
            for i in range(0,3):
                currrow.append(row[i])
            donors.append(currrow)
            row = cur.fetchone()
        print(tabulate(donors,headers,tablefmt="pipe"),'\n')
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def main():
    donorMatchList()


if __name__ == '__main__':
    main()


