import psycopg2
from incomeReport import incomeReport
from organDonorList import organDonorList
from bloodDonorList import bloodDonorList
from donorMatchList import donorMatchList
from operationsReport import operationsReport
from createRoles import createDoctor,createPatient
from patientReport import patientReport
breakline = "-"*200

def main():
    host = input("\n Input in the host: ")
    database = input("\n Input in the Database Name:")
    user = input("\n Input in the username: ")
    password = input("\n Input in the password: ")
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host = host,
            dbname = database,
            user = user,
            password = password
            )
        while(True):
            print(  "\n 1:Organ Donor List \n",
                    "2:Blood Donor List \n",
                    "3:Donor Match List \n",
                    "4:Income Report \n",
                    "5:Operations Report \n",
                    "6:Create Doctor Role \n",
                    "7:Create Patient Role \n",
                    "Q:Quit")
            selected = input("Select an option: ")
            print(breakline)
            if selected == '1':
                region = input("\n Input in a region: ")
                organ = input("\n Input in an organ: ")
                print(breakline)
                organDonorList(region,organ,conn)
            elif selected == '2':
                region = input("\n Input in a region: ")
                bloodtype = input("\n Input in a bloodtype: ")
                minage = input("\n Input in a minimum age: ")
                maxage = input("\n Input in a maximum age: ")
                print(breakline)
                bloodDonorList(region,bloodtype,minage,maxage,conn)
            elif selected == '3':
                donorMatchList(conn)
            elif selected == '4':
                incomeReport(conn)
            elif selected == '5':
                region = input("\n Input in a region: ")
                print(breakline)
                operationsReport(region,conn)
            elif selected == '6':
                user = input("\n Input in a username: ")
                password = input("\n Input in a password: ")
                print(breakline)
                createDoctor(user,password,conn)
                print("Doctor Role Successfully made")
            elif selected == '7':
                user = input("\n Input in a username: ")
                password = input("\n Input in a password: ")
                print(breakline)
                createPatient(user,password,conn)
                print("Doctor Role Successfully made")
            elif selected == '8':
                id = input("\n Input a patient ID: ")
                print(breakline)
                
            elif selected == 'Q':
                break
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    
if __name__ == "__main__":
    main()