import psycopg2
from tabulate import tabulate

def operationsReport(region,conn):
    """ Connect to the PostgreSQL database server """
    try:
        # create a cursor
        cur = conn.cursor()
        
        exec = """
            SELECT d.dName, d.completedOperations
            FROM doctor d
            INNER JOIN hospital h on h.hospitalid = d.hospitalid
            WHERE h.region = '{region}'
            ORDER BY completedOperations DESC, d.doctorID ASC;
        """.format(region = region)
	# execute a statement
        print('Operations Report: ')
        cur.execute(exec)
        row = cur.fetchone()
        donors = []
        headers = ['Name','Completed Operations']
        while row is not None:
            currrow = []
            for i in range(0,2):
                currrow.append(row[i])
            donors.append(currrow)
            row = cur.fetchone()
        print(tabulate(donors,headers,tablefmt="pipe"),'\n')
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)