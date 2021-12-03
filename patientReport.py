import psycopg2
from tabulate import tabulate

def patientReport(patientID,conn):
    """ Connect to the PostgreSQL database server """
    try:
        cur = conn.cursor()

        exec = exec = """
            SELECT *
            FROM patient
            WHERE patientID = '{pID}'; 
                            """.format(pID = patientID)
        print('Patient Information: ')
        cur.execute(exec)
        row = cur.fetchone()
        donors = []
        headers = ['Hospital ID','Hospital Name','Earnings']
        while row is not None:
            currrow = []
            for i in range(0,8):
                currrow.append(row[i])
            donors.append(currrow)
            row = cur.fetchone()
        print(tabulate(donors,headers,tablefmt="pipe"),'\n')
	# close the communication with the PostgreSQL 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


