import psycopg2
from tabulate import tabulate

def donorMatchList(conn):
    """ Connect to the PostgreSQL database server """
    try:
        cur = conn.cursor()
        exec = """
            SELECT p.pname,p.patientid,d.donorID,p.bloodtype,d.bloodtype FROM donor d
            INNER JOIN patient p
            ON (d.bloodType = p.bloodType OR d.bloodType LIKE 'O_' OR p.bloodType LIKE 'AB_') AND d.region = p.region
            WHERE p.need = 'blood'
            ORDER BY
                p.patientid ASC,
                d.donorid ASC;
            """
	# execute a statement
        print('Matched Blood Donors: ')
        cur.execute(exec)
        row = cur.fetchone()
        donors = []
        headers = ['Patient Name','Patient ID','Donor ID','Patient Bloodtype','Donor Bloodtype']
        while row is not None:
            currrow = []
            for i in range(0,5):
                currrow.append(row[i])
            donors.append(currrow)
            row = cur.fetchone()
        print(tabulate(donors,headers,tablefmt="pipe"),'\n')
        exec = """
            SELECT p.pname,p.patientID,o.donorid,p.bloodtype,o.bloodtype,o.oname FROM organDonor o
            INNER JOIN patient p
            ON (o.bloodType = p.bloodType OR o.bloodType LIKE 'O_' OR p.bloodType = 'AB_') AND o.oName = p.need AND o.region = p.region
            WHERE p.need != 'blood';
            """
        print('Matched Organ Donors: ')
        cur.execute(exec)
        row = cur.fetchone()
        donors = []
        headers = ['Patient Name','Patient ID','Donor ID','Patient Bloodtype','Donor Bloodtype','Organ Donated']
        while row is not None:
            currrow = []
            for i in range(0,6):
                currrow.append(row[i])
            donors.append(currrow)
            row = cur.fetchone()
        print(tabulate(donors,headers,tablefmt="pipe"),'\n')
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)