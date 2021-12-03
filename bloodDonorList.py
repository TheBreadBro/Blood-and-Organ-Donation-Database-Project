import psycopg2
from tabulate import tabulate

def bloodDonorList(region, bloodtype, minage, maxage,conn):
    """ Connect to the PostgreSQL database server """
    try:
		
        # create a cursor
        cur = conn.cursor()
        
        exec = """
            SELECT donorID, bloodType, age, drugUsage 
            FROM donor
            WHERE region = '{region}' and bloodtype = '{bloodtype}' and age between {min} and {max} and lastDonation >= CURRENT_DATE - INTERVAL '6 months'
            ORDER BY donorID ASC;
                            """.format(region = region,bloodtype=bloodtype,min=minage,max=maxage)

	# execute a statement
        print('List of Available Donors: ')
        cur.execute(exec)
        row = cur.fetchone()
        donors = []
        headers = ['ID','bloodType','Age','Drug Usage']
        while row is not None:
            currrow = []
            for i in range(0,4):
                currrow.append(row[i])
            donors.append(currrow)
            row = cur.fetchone()
        print(tabulate(donors,headers,tablefmt="pipe"),'\n')
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)