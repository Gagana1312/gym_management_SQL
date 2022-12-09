import mysql.connector as mysql 
import pymysql;
import maskpass
import re
from colored import fg, bg, attr
from tabulate import tabulate
from pyfiglet import Figlet
print(f"{fg(148)}Enter Username: " )
username = input()
# print( f"{fg(148)}Enter Password: " )   
password = maskpass.askpass(mask="*") 

try:
    conn = pymysql.connect( host='localhost',
                        user=username,
                        password=password,
                        db='marino' )
    
except Exception as e:
    print(f"{fg(1)} Invalid Credentials, Try again",e)
    print("")
    print("")


    
command_handler = conn.cursor()

# db = mysql.connect(host ="localhost",user = lines[0], password=lines[1],database="marino")
# command_handler = db.cursor(buffered=True)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
Pattern = re.compile(r"(?:\+\d{3})?\d{3}\D?\d{4}")
   
#Admin Session 
def admin_session():
    # print("Login successfully, Welcome Admin!")
 while 1:
        print("")
        print(f"{fg(23)}Welcome to Admin Panel")
        print("")
        print(f"{fg(209)}1.Staff Panel")
        print(f"{fg(209)}2.Student Panel")
        print(f"{fg(209)}3.Back")
        print("")

        user_option = input(str(f"{fg(99)}Option : "))
        if user_option == "1":
            while 1:
                print("")
                print(f"{fg(111)}Staff Panel")
                print("")
                print(f"{fg(209)}1. Register new staff")
                print(f"{fg(209)}2. Delete existing staff")
                print(f"{fg(209)}3. Read existing staff")
                print(f"{fg(209)}4. Update existing staff")
                print("5. Back")
                admin_user_option = input(str(f"{fg(99)}Option : "))

                if admin_user_option == "1":
                    print("")
                    print(f"{fg(111)}Register New Staff")
                    print("")
                     # idstaff = input(str("ID: "))
                    emailid = input(str(f"{fg(148)}Staff emailid: "))
                    if(re.fullmatch(regex, emailid)):
                        password = input(str(f"{fg(148)}Staff password: "))
                        staff_name = input(str(f"{fg(148)}Staff Name: "))
                        staff_age = input(str(f"{fg(148)}Staff Age: "))
                        phone_number = input(str(f"{fg(148)}Staff Phone Number: "))
                        
                        if Pattern.match(phone_number):
                                #  print("Valid")
                                 query_vals = (staff_name,staff_age,phone_number,emailid,password)
                                 command_handler.execute("call staff_reg(%s,%s,%s,%s,%s)",query_vals)
                                 conn.commit()
                                 print(emailid + f"{fg(2)} has been registered as a staff")
                                 print("")
                                 print(f"{fg(148)}Updated Staff Details")
                                 print("")
                                 # emailid = input(str("Email ID: "))
                                 # query_vals = (emailid)
                                 print(f"{fg(229)}")
                                 command_handler.execute("Select * from staff")
                                 # fetch all the matching rows 
                                 result = command_handler.fetchall()
                                 columns = ['Staff ID', 'Staff name', 'Staff Age', 'Phone Number', "Email ID","Password"]
                                 print(tabulate(result,headers=columns,tablefmt="grid"))
             
                        else:
                                print(f"{fg(1)}Invalid Phone Number, Try again!")
                                break
                            

                        
                        # command_handler.execute("INSERT INTO marino.staff (staff_name,staff_age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s)",query_vals)
                        
                    else:
                        print(f"{fg(1)}Invalid Email format, Try again")
                        break

                elif admin_user_option == "2":
                    print("")
                    print(f"{fg(111)}Delete Existing Staff Account")
                    print("")
                    print("")
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    print(f"{fg(229)}")
                    command_handler.execute("Select * from staff")
                    # fetch all the matching rows 
                    result = command_handler.fetchall()
                    columns = ['Staff ID', 'Staff name', 'Staff Age', 'Phone Number', "Email ID","Password"]
                    print(tabulate(result,headers=columns,tablefmt="grid"))
                    emailid = input(str(f"{fg(148)}Email ID: "))
                    password = input(str(f"{fg(148)}Password: "))
                    query_vals = (emailid,password)
                    # command_handler.execute("DELETE FROM staff WHERE emailid = %s AND password = %s",query_vals)
                    command_handler.execute("call staff_del(%s,%s)",query_vals)
                    conn.commit()
                    if command_handler.rowcount < 1: 
                        print("Staff not found")
                    else:
                        print("")
                        print(emailid + f"{fg(1)} has been deleted!")
                        print("")
                        print(f"{fg(111)}Updated Staff Details")
                        print("")
                        # emailid = input(str("Email ID: "))
                        # query_vals = (emailid)
                        print(f"{fg(229)}")
                        command_handler.execute("Select * from staff")
                        # fetch all the matching rows 
                        result = command_handler.fetchall()
                        columns = ['Staff ID', 'Staff name', 'Staff Age', 'Phone Number', "Email ID","Password"]
                        print(tabulate(result,headers=columns,tablefmt="grid"))

                elif admin_user_option == "3":
                    print("")
                    print(f"{fg(111)}All Existing Staff Details")
                    print("")
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    print(f"{fg(229)}")
                    command_handler.execute("Select * from staff")
                    # fetch all the matching rows 
                    result = command_handler.fetchall()
                    columns = ['Staff ID', 'Staff name', 'Staff Age', 'Phone Number', "Email ID","Password"]
                    print(tabulate(result,headers=columns,tablefmt="grid"))
    
                    # loop through the rows
                    # for row in result:
                    #     print(f"{fg(5)}")
                    #     print(row)
                    #     print("\n")
                    conn.commit()
                    if command_handler.rowcount < 1: 
                        print("")
                        print(f"{fg(1)}No Staff found")

                elif admin_user_option == "4":
                    print("")
                    print(f"{fg(111)}Update Existing Staff Details")
                    print("")
                    print(f"{fg(229)}")
                    command_handler.execute("Select * from staff")
                    # fetch all the matching rows 
                    result = command_handler.fetchall()
                    columns = ['Staff ID', 'Staff name', 'Staff Age', 'Phone Number', "Email ID","Password"]
                    print(tabulate(result,headers=columns,tablefmt="grid"))
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    update_idstaff = input(str(f"{fg(148)}Staff ID to be updated: "))
                    staff_name = input(str(f"{fg(148)}Staff Name: "))
                    staff_age = input(str(f"{fg(148)}Staff Age: "))
                    phone_number = input(str(f"{fg(148)}Staff Phone Number: "))
            
                    query_vals = (staff_name,staff_age,phone_number,update_idstaff)
                    command_handler.execute("Update staff SET staff_name = %s,staff_age=%s,phone_number=%s where idstaff=%s",query_vals)
            
                    conn.commit()
                    print(f"{fg(2)}Updated Successfully!")
                    print("")
                    print(f"{fg(111)}Updated Staff Details")
                    print("")
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    print(f"{fg(229)}")
                    command_handler.execute("Select * from staff")
                    # fetch all the matching rows 
                    result = command_handler.fetchall()
                    columns = ['Staff ID', 'Staff name', 'Staff Age', 'Phone Number', "Email ID","Password"]
                    print(tabulate(result,headers=columns,tablefmt="grid"))
                    if command_handler.rowcount < 1: 
                        print("")
                        print(f"{fg(1)}No Staff found")
             
                

                elif admin_user_option == "5":
                 break
                else:
                    print("")
                    print(f"{fg(1)}Invalid option!")

        if user_option == "2":
            while 1:
                print("")
                print(f"{fg(203)}User Panel")
                print("")
                print(f"{fg(209)}1. Register new user")

                print(f"{fg(209)}2. Delete existing user")

                print(f"{fg(209)}3. Read existing user")

                print(f"{fg(209)}4. Update existing user")

                print("5. Back")
        
                client_user_option = input(str(f"{fg(99)}Option : "))

                if client_user_option == "1":
                    print("")
                    print(f"{fg(111)}Register New User")
                    print("")
                    # idstaff = input(str("ID: "))
                    emailid = input(str(f"{fg(148)}user emailid: "))
                    if(re.fullmatch(regex, emailid)):
                        password = input(str(f"{fg(148)}user password: "))
                        first_name = input(str(f"{fg(148)}First Name: "))
                        last_name = input(str(f"{fg(148)}Last Name: "))
                        age = input(str(f"{fg(148)}user Age: "))
                        phone_number = input(str(f"{fg(148)}user Phone Number: "))
                        query_vals = (first_name,last_name,age,phone_number,emailid,password)
                        # command_handler.execute("INSERT INTO marino.user(first_name,last_name,age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
                        command_handler.execute("call user_reg(%s,%s,%s,%s,%s,%s)",query_vals)
                        conn.commit()
                        print(first_name + f"{fg(2)} has been registered as a User")
                        print("")
                        print(f"{fg(148)}Updated User Details")
                        print("")
                        # emailid = input(str("Email ID: "))
                        # query_vals = (emailid)
                        print(f"{fg(229)}")
                        command_handler.execute("Select * from user")
                        # fetch all the matching rows 
                        result = command_handler.fetchall()
                        columns = ['User ID', 'First Name','Last Name', 'User Age', 'Phone Number', "Email ID","Password"]
                        print(f"{fg(109)}")
                        print(tabulate(result,headers=columns,tablefmt="grid"))

                    else:
                        print(f"{fg(148)}Invalid Email format, Try again")
                        break
        
        
        
                elif client_user_option == "2":
                    print("")
                    print(f"{fg(111)}Delete Existing User Account")
                    print("")
                    emailid = input(str(f"{fg(148)}Email ID: "))
                    password = input(str(f"{fg(148)}Password: "))
                    query_vals = (emailid,password)
                    # command_handler.execute("DELETE FROM user WHERE emailid = %s AND password = %s",query_vals)
                    command_handler.execute("call user_del(%s,%s)",query_vals)
                    conn.commit()
                    if command_handler.rowcount < 1: 
                        print("")
                        print(f"{fg(1)}User not found")
                    else:
                        print(emailid + f"{fg(1)} has been deleted!")
                        print("")
                        print(f"{fg(148)}Updated User Details")
                        print("")
                        # emailid = input(str("Email ID: "))
                        # query_vals = (emailid)
                        print(f"{fg(229)}")
                        command_handler.execute("Select * from user")
                        # fetch all the matching rows 
                        result = command_handler.fetchall()
                        columns = ['User ID', 'First Name','Last Name', 'User Age', 'Phone Number', "Email ID","Password"]
                        print(f"{fg(109)}")
                        print(tabulate(result,headers=columns,tablefmt="grid"))

       

                elif client_user_option == "3":
                    print("")
                    print(f"{fg(111)}All Existing User Details")
                    print("")
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    print(f"{fg(229)}")
                    command_handler.execute("Select * from user")
                    # fetch all the matching rows 
                    result = command_handler.fetchall()
                    columns = ['User ID', 'First Name','Last Name', 'User Age', 'Phone Number', "Email ID","Password"]
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))

                    # loop through the rows
                    # for row in result:
                    #     print(f"{fg(5)}")
                    #     print(row)
                    #     print("\n")
                    conn.commit()
                    if command_handler.rowcount < 1: 
                        print("")
                        print("No User found")

                elif client_user_option == "4":
                    print("")
                    print(f"{fg(111)}Update Existing User Details")
                    print("")
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    print(f"{fg(229)}")
                    command_handler.execute("Select * from user")
                    # fetch all the matching rows 
                    result = command_handler.fetchall()
                    columns = ['User ID', 'First Name','Last Name', 'User Age', 'Phone Number', "Email ID","Password"]
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))

                    update_iduser = input(str(f"{fg(148)}User ID to be updated: "))
                    first_name = input(str(f"{fg(148)}User First Name: "))
                    last_name = input(str(f"{fg(148)}User Last Name: "))
                    user_age = input(str(f"{fg(148)}User Age: "))
                    phone_number = input(str(f"{fg(148)}Staff Phone Number: "))
                    query_vals = (first_name,last_name,user_age,phone_number,update_iduser)
                    command_handler.execute("Update user SET first_name = %s,last_name=%s,age=%s,phone_number=%s where userid=%s",query_vals)
            
                    conn.commit()
                    print(f"{fg(2)}")
                    print(first_name + " Updated Successfully!")
                    print("")
                    print(f"{fg(20)}Updated User Details")
                    print("")
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    print(f"{fg(229)}")
                    command_handler.execute("Select * from user")
                    # fetch all the matching rows 
                    result = command_handler.fetchall()
                    columns = ['User ID', 'First Name','Last Name', 'User Age', 'Phone Number', "Email ID","Password"]
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))
                    if command_handler.rowcount < 1: 
                        print("")
                        print("No User found")

                elif client_user_option == "5":
                    break
                else:
                    print("")
                    print(f"{fg(1)}Invalid Option!")
            
        elif user_option == "3":
            break
       
#Staff Session
def staff_session(id):
    while 1:
        print("")
        print(f"{fg(111)}Welcome to Staff Panel")
        print("")
        print(f"{fg(209)}1.User Panel")
        print(f"{fg(209)}2.Locker Panel")
        print(f"{fg(209)}3.Equipment Panel")
        print(f"{fg(209)}4.Activity Panel")
        print(f"{fg(209)}5.Trainer Panel")
        print(f"{fg(209)}6.Back")

        user_option = input(str(f"{fg(99)}Option : "))

        if user_option == "1":
            while 1:
                print(" ")
                print(f"{fg(73)}Welcome to User Panel")
                print(" ")
                print("1. Register new user")     
                print("2. Delete existing user")
                print("3. Read existing user")
                print("4. Update existing user")
                print("5. Back")
                u_option = input(str(f"{fg(99)} Option :"))
                if u_option == "1":
                    print("")
                    print(f"{fg(73)}Register New User")
                    # idstaff = input(str("ID: "))
                    emailid = input(str("user emailid: "))
                    if(re.fullmatch(regex, emailid)):
                        password = input(str("user password: "))
                        first_name = input(str("First Name: "))
                        last_name = input(str("Last Name: "))
                        age = input(str("user Age: "))
                        phone_number = input(str("user Phone Number: "))
                        query_vals = (first_name,last_name,age,phone_number,emailid,password)
                        command_handler.execute("INSERT INTO marino.user(first_name,last_name,age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
                        conn.commit()
                        print(first_name + " has been registered as a User")
                    else:
                         print("Invalid Email format, Try again")
                         break
            
       
        
                elif u_option == "2":
                    print("")
                    print(f"{fg(73)}Delete Existing User Account")
                    print("")
                    print(f"{fg(73)}All Existing User Details")

                    command_handler.execute("Select * from user")
                    columns = ['User ID', 'First Name','Last Name', 'User Age', 'Phone Number', "Email ID","Password"]
                    # fetch all the matching rows 
                    result = command_handler.fetchall()
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))

                    command_handler.execute ("Select userid, first_name,last_name,age,phone_number from user")
                    result = command_handler.fetchall()
                    columns = ['USER ID', 'First Name', 'Last Name','Age','Phone Number']
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))
                    userid = input(str("User ID: "))
                    query_vals = (userid,)
                    command_handler.execute("DELETE FROM user WHERE userid = %s",query_vals)
                    conn.commit()
                    if command_handler.rowcount < 1: 
                        print("User not found")
                    else:
                     print(emailid + " has been deleted!")
                    print(f"{fg(73)}Updated User Details")

                    command_handler.execute("Select * from user")
                    columns = ['User ID', 'First Name','Last Name', 'User Age', 'Phone Number', "Email ID","Password"]
                    # fetch all the matching rows 
                    result = command_handler.fetchall()
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))

                elif u_option == "3":
                    print("")
                    print(f"{fg(73)}All Existing User Details")

                    command_handler.execute("Select * from user")
                    columns = ['User ID', 'First Name','Last Name', 'User Age', 'Phone Number', "Email ID","Password"]
                    # fetch all the matching rows 
                    result = command_handler.fetchall()
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))
        
                    conn.commit()
                    if command_handler.rowcount < 1: 
                        print("No User found")

                elif u_option == "4":
                    print("")
                    print(f"{fg(148)}Update Existing User Details")
                    print("")
                    command_handler.execute ("Select userid, first_name,last_name,age,phone_number from user")
                    result = command_handler.fetchall()
                    columns = ['User ID', 'First Name', 'Last Name','Age','Phone Number']
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    update_iduser = input(str("User ID to be updated: "))
                    first_name = input(str("User First Name: "))
                    last_name = input(str("User Last Name: "))
                    user_age = input(str("User Age: "))
                    phone_number = input(str("User Phone Number: "))
                    query_vals = (first_name,last_name,user_age,phone_number,update_iduser)
                    command_handler.execute("Update user SET first_name = %s,last_name=%s,age=%s,phone_number=%s where userid=%s",query_vals)
            
                    conn.commit()
                
                    if command_handler.rowcount < 1: 
                        print("")
                        print("No User found")
                    else:
                          print(f"{fg(2)}")
                          print(first_name + " Updated Successfully!")
                          print(f"{fg(73)}All Existing User Details")

                          command_handler.execute("Select * from user")
                          columns = ['User ID', 'First Name','Last Name', 'User Age', 'Phone Number', "Email ID","Password"]
                          # fetch all the matching rows 
                          result = command_handler.fetchall()
                          print(f"{fg(109)}")
                          print(tabulate(result,headers=columns,tablefmt="grid"))

                elif u_option == "5":
                   break

                else: 
                    print("")
                    print(f"{fg(1)}Invaliid Selection!")
            

        elif user_option == "2":
         while 1:
            print(" ")
            print(f"{fg(111)}Welcome to Locker Panel")
            print(f"{fg(209)}1. Create new locker")
            print(f"{fg(209)}2. Delete locker")
            print(f"{fg(209)}3. Assign a locker")
            print(f"{fg(209)}4. View all lockers")
            print(f"{fg(209)}5. Back")
            l_option = input(str(f"{fg(99)}Option :"))
            if l_option == "1":
                print("")
                print(f"{fg(73)}Create a new locker")

                print(f"{fg(111)}Viewing a Locker")
                print(f"{fg(229)}")
                command_handler.execute ("Select idlocker, type_of_locker,userid from locker")
                result = command_handler.fetchall()
                columns = ['Locker ID', 'Type of Locker', 'User ID']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))
    
                type_of_locker = input(str(f"{fg(148)}Enter the type of Locker (Personal/Standard): "))
                idstaff = id
                # userid = input(str("Enter the user ID : "))
                query_vals = (type_of_locker,idstaff)
                # command_handler.execute("Insert into marino.locker(type_of_locker,idstaff,userid) values(%s,%s,0)",query_vals)
                command_handler.execute("call locker_reg(%s,%s,0)",query_vals)
                conn.commit()
                print("New locker has been created!")
                print(f"{fg(73)}Updated Locker")
                print(f"{fg(229)}")
                command_handler.execute ("Select idlocker, type_of_locker,userid from locker")
                result = command_handler.fetchall()
                columns = ['Locker ID', 'Type of Locker', 'User ID']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))

            elif l_option == "2":
                print("")
                print(f"{fg(111)}Delete a locker")
                print(f"{fg(229)}")
                command_handler.execute ("Select idlocker,type_of_locker from locker")
                result = command_handler.fetchall()
                columns = ['Locker ID', 'Type of Locker']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))

                idlocker = input(str(f"{fg(148)}Enter the locker ID : "))
                query_vals = (idlocker,)
                # command_handler.execute("Delete from locker where idlocker = %s",query_vals)
                command_handler.execute("call locker_del(%s)",query_vals)
                conn.commit()
                if command_handler.rowcount < 1:
                    print("Locker Not found")
                else:
                    print(idlocker + " locker has been deleted successfully")
                    print(f"{fg(2)}Viewing a Locker")
                    print(f"{fg(229)}")
                    command_handler.execute ("Select idlocker, type_of_locker,userid from locker")
                    result = command_handler.fetchall()
                    columns = ['Locker ID', 'Type of Locker', 'User ID']
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))

            elif l_option == "3":
                    print("")
                    print(f"{fg(111)}Assign locker to a User")
                    print("")
                    print(f"{fg(78)}Available Lockers")
                    print(f"{fg(229)}")
                    command_handler.execute ("Select idlocker,type_of_locker,userid from locker where userid=0 ")
                    result = command_handler.fetchall()
                    columns = ['Locker ID', 'Type of Locker','user_id']
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    update_iduser = input(str(f"{fg(148)}User ID to be updated: "))
                    idlocker = input(str(f"{fg(148)}Enter Locker ID : "))
                    query_vals = (update_iduser,idlocker)
                    command_handler.execute("Update locker SET userid=%s where idlocker=%s",query_vals)
            
                    conn.commit()
                    print(idlocker + " Updated Successfully!")
                    print(f"{fg(111)}Viewing a Locker")
                    print(f"{fg(229)}")
                    command_handler.execute ("Select idlocker, type_of_locker,userid from locker")
                    result = command_handler.fetchall()
                    columns = ['Locker ID', 'Type of Locker', 'User ID']
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))

                    # todo add condition to handle incorrect value
                    # if command_handler.rowcount < 1: 
                    #     print("")
                    #     print("No User found")
                    # else:
                    #       print(f"{fg(2)}")
                    #       print(idlocker + " Updated Successfully!")

            elif l_option == "4":
                print("")
                print(f"{fg(111)}Viewing a Locker")
                print(f"{fg(229)}")
                command_handler.execute ("Select idlocker, type_of_locker,userid from locker")
                result = command_handler.fetchall()
                columns = ['Locker ID', 'Type of Locker', 'User ID']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))
                print(f"{fg(111)}Viewing Locker without users")
                print(f"{fg(229)}")
                command_handler.execute("select locker_without_users() from activity LIMIT 1")
                result = command_handler.fetchall()
                columns = ['Locker without users']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))
                # for row in result: 
                #     print(row)
                #     print("\n")
                conn.commit()

                if command_handler.rowcount < 1:
                    print("Lockers not found!")
                
                
            
            elif l_option == "5":
                break
            else:
                print(f"{fg(1)}Invaliid Selection!")

        elif user_option == "3":
         while 1:
            print(" ")
            print(f"{fg(111)}Welcome to Equipment Panel")
            print(f"{fg(209)}1. Add an equipment")
            print(f"{fg(209)}2. Delete an equipment")
            print(f"{fg(209)}3. View all equipments")
            print(f"{fg(209)}4. Assign an equipment")
            print(f"{fg(209)}5. Back")

            e_option = input(str(f"{fg(99)}Option : "))
            if e_option == "1":
                print("")
                print(f"{fg(111)}Add a new Equipment")
    
                name = input(str(f"{fg(148)}Name of the equipment: "))
                idstaff = id
                idactivity = 0
                query_vals = (name,idstaff,idactivity)
                print(f"{fg(229)}")
                # command_handler.execute("Insert into marino.equipment(name,idstaff,idactivity) values(%s,%s,%s)",query_vals)
                command_handler.execute("call equipment_reg(%s,%s,%s)",query_vals)
                conn.commit()
                print(f"{fg(2)}New equipment has been added!")
                print("")
                print(f"{fg(111)}Viewing all Equipments")
                print(f"{fg(229)}")
                command_handler.execute ("Select idequipment,name,idactivity from equipment")
                result = command_handler.fetchall()
                columns = ['Equipment ID', 'Name of Equipment', 'Activity ID']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))

            elif e_option == "2":
                print("")
                print(f"{fg(111)}Remove an equipment")
                print(f"{fg(229)}")
                command_handler.execute ("Select idequipment,name from equipment")
                result = command_handler.fetchall()
                columns = ['Equipment ID', 'Name of Equipment']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))
                idequipment = input(str(f"{fg(148)}Enter the Equipment ID : "))
                query_vals = (idequipment,)
                # command_handler.execute("Delete from equipment where idequipment = %s",query_vals)
                print(f"{fg(229)}")
                command_handler.execute("call equipment_del(%s)",query_vals)
                conn.commit()
                if command_handler.rowcount < 1:
                    print(f"{fg(1)}Equipment Not found")
                else:
                    print(idequipment + " equipment has been deleted successfully")
                    print(f"{fg(73)}Updated all Equipments")
                    print(f"{fg(229)}")
                    command_handler.execute ("Select idequipment,name,idactivity from equipment")
                    result = command_handler.fetchall()
                    columns = ['Equipment ID', 'Name of Equipment', 'Activity ID']
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))


            elif e_option == "3":
                print("")
                print(f"{fg(111)}Viewing all Equipments")
                print(f"{fg(229)}")
                command_handler.execute ("Select idequipment,name,idactivity from equipment")
                result = command_handler.fetchall()
                columns = ['Equipment ID', 'Name of Equipment', 'Activity ID']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))
                print(f"{fg(73)}Viewing Equipment without Activity")
                print(f"{fg(229)}")
                command_handler.execute("select equipment_without_activity() from activity LIMIT 1")
                result = command_handler.fetchall()
                columns = ['Equipment without Activity']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))

                # for row in result: 
                #     print(row)
                #     print("\n")
                conn.commit()

                if command_handler.rowcount < 1:
                    print(f"{fg(1)}Equipments not found!")

            elif e_option == "4":
                    print("")
                    print(f"{fg(111)}Assign Equipment to a Activity")
                    print("")
                    print(f"{fg(229)}")
                    command_handler.execute ("Select idequipment,name from equipment")
                    result_eqp = command_handler.fetchall()
                    columns = ['Equipment ID', 'Name of Equipment']
                    print(f"{fg(109)}")
                    print(tabulate(result_eqp,headers=columns,tablefmt="grid"))
                    command_handler.execute ("Select * from activity")
                    result_act = command_handler.fetchall()
                    columns = ['Activity ID', 'Name of Activity','Alloted Room']
                    print(f"{fg(109)}")
                    print(tabulate(result_act,headers=columns,tablefmt="grid"))
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    idactivity = input(str(f"{fg(148)}Activity ID: "))
                    idequipment = input(str(f"{fg(148)}Enter Equipment ID : "))
                    query_vals = (idactivity,idequipment)
                    command_handler.execute("Update equipment SET idactivity=%s where idequipment=%s",query_vals)
            
                    conn.commit()
                    print(idequipment + " Updated Successfully!")
                    print(f"{fg(111)}Viewing all Equipments")
                    print(f"{fg(229)}")
                    command_handler.execute ("Select idequipment,name,idactivity from equipment")
                    result = command_handler.fetchall()
                    columns = ['Equipment ID', 'Name of Equipment', 'Activity ID']
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))
                    
                    # todo add condition to handle incorrect value
                    # if command_handler.rowcount < 1: 
                    #     print("")
                    #     print("No User found")
                    # else:
                    #       print(f"{fg(2)}")
                    #       print(idlocker + " Updated Successfully!")
            elif e_option == "5":
                break
            else:
                print(f"{fg(1)}Invaliid Selection!")
        
       

        elif user_option == "4":
         while 1:
            print(" ")
            print(f"{fg(111)}Welcome to Activity Panel")
            print(f"{fg(209)}1. Create an activity")
            print(f"{fg(209)}2. Delete an activity")
            print(f"{fg(209)}3. View all activity")
            print(f"{fg(209)}4. Update an activity")
            print(f"{fg(209)}5. Back")

            a_option = input(str(f"{fg(99)}Option : "))
            if a_option == "1":
                print("")
                print(f"{fg(111)}Create an activity")

                name = input(str(f"{fg(148)}Enter the name of the activity: "))
                room_no = input(str(f"{fg(148)}Enter the room number for the activity: "))
                price = input(str(f"{fg(148)}Enter activity rate: "))

                query_vals = (name,room_no,price)
                # command_handler.execute("Insert into marino.activity (name,room_no) values (%s,%s)",query_vals)
                command_handler.execute("call activity_reg(%s,%s,%s)",query_vals)
                conn.commit()

                print(f"{fg(2)}New Activity has been created!")

                print(f"{fg(73)}Updated all activity")

                command_handler.execute("SELECT  idactivity,name,room_no,price from activity")
                # command_handler.execute("SELECT a.idactivity,a.name,a.room_no,e.idequipment,e.name from activity as a JOIN equipment as e ON a.idactivity=e.idactivity;")
                # query_vals = ()
                # command_handler.execute("call activity_Equip_table()",query_vals)
                result = command_handler.fetchall()
                columns = ['Activity ID', 'Activity Name','Room Number',"Rate"]
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))

            elif a_option == "2":
                print("")
                print(f"{fg(111)}Delete an activity")
                command_handler.execute ("Select idactivity,name,room_no,price from activity")
                result_act = command_handler.fetchall()
                columns = ['Activity ID', 'Name of Activity','Alloted Room','Rate']
                print(f"{fg(109)}")
                print(tabulate(result_act,headers=columns,tablefmt="grid"))
                idactivity = input(str(f"{fg(148)}Enter the acitvity ID: "))
                query_vals = (idactivity,)
                # command_handler.execute("Delete from activity where idactivity = %s", query_vals)
                command_handler.execute("call activity_del(%s)",query_vals)
                conn.commit()

                if command_handler.rowcount < 1:
                    print("Activity doesn't exist")
                else:
                    print("Activity has been deleted successfully!")
                    print(f"{fg(73)}Updated all activity")

                    command_handler.execute("SELECT  idactivity,name,room_no,price from activity")
                    # command_handler.execute("SELECT a.idactivity,a.name,a.room_no,e.idequipment,e.name from activity as a JOIN equipment as e ON a.idactivity=e.idactivity;")
                    # query_vals = ()
                    # command_handler.execute("call activity_Equip_table()",query_vals)
                    result = command_handler.fetchall()
                    columns = ['Activity ID', 'Activity Name','Room Number',"Rate"]
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))

            elif a_option == "3":
                print("")
                print(f"{fg(111)}View all activity")

                command_handler.execute("SELECT  idactivity,name,room_no,price from activity")
                # command_handler.execute("SELECT a.idactivity,a.name,a.room_no,e.idequipment,e.name from activity as a JOIN equipment as e ON a.idactivity=e.idactivity;")
                # query_vals = ()
                # command_handler.execute("call activity_Equip_table()",query_vals)
                result = command_handler.fetchall()
                columns = ['Activity ID', 'Activity Name','Room Number',"Rate"]
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))

                print(f"{fg(73)}Viewing Activity without Trainer")
                command_handler.execute("select Activity_without_trainers() from activity LIMIT 1")
                result = command_handler.fetchall()
                columns = ['Activity without Trainers']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))

                # for row in result:
                #     print (row)
                conn.commit()

                if command_handler.rowcount <1:
                    print("No details found")

            elif a_option == "4":
                    print("")
                    print(f"{fg(111)}Update Activity ")
                    print("")
                    command_handler.execute ("Select  idactivity,name,room_no,price,idtrainer from activity")
                    result_act = command_handler.fetchall()
                    columns = ['Activity ID', 'Name of Activity','Alloted Room',"Rate","Trainer ID"]
                    print(f"{fg(109)}")
                    print(tabulate(result_act,headers=columns,tablefmt="grid"))

                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    idactivity = input(str(f"{fg(148)}Activity ID: "))
                    name = input(str(f"{fg(148)}activity Name: "))
                    room_no = input(str(f"{fg(148)}Enter Room ID : "))
                    rate = input(str(f"{fg(148)}Enter the rate of the activity: "))
                    trainer_id = input(str(f"{fg(148)}Enter Trainer ID: "))
                    query_vals = (name,room_no,rate,trainer_id,idactivity)
                    command_handler.execute("Update activity SET name=%s,room_no=%s,price=%s,idtrainer=%s where idactivity=%s",query_vals)
                    conn.commit()

                    print(name + " Updated Successfully!")
                    print("")
                    print(f"{fg(73)}Updated all activity")

                    command_handler.execute("SELECT  idactivity,name,room_no,price,idtrainer from activity")
                    # command_handler.execute("SELECT a.idactivity,a.name,a.room_no,e.idequipment,e.name from activity as a JOIN equipment as e ON a.idactivity=e.idactivity;")
                    # query_vals = ()
                    # command_handler.execute("call activity_Equip_table()",query_vals)
                    result = command_handler.fetchall()
                    columns = ['Activity ID', 'Activity Name','Room Number',"Rate","Trainer ID"]
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))

                    # todo add condition to handle incorrect value
                    # if command_handler.rowcount < 1: 
                    #     print("")
                    #     print("No User found")
                    # else:
                    #       print(f"{fg(2)}")
                    #       print(idlocker + " Updated Successfully!")

            elif a_option == "5":
                 break
            else:
                print("")
                print(f"{fg(1)}Invaliid Selection!")
   
        elif user_option == "5":
            while 1:
                    print(" ")
                    print(f"{fg(111)}Welcome to Trainer Panel")
                    print(f"{fg(209)}1. Create new trainer")
                    print(f"{fg(209)}2. Remove trainer")
                    print(f"{fg(209)}3. Assign a trainer")
                    print(f"{fg(209)}4. View all trainers")
                    print(f"{fg(209)}5. Back")
                    l_option = input(str(f"{fg(99)}Option :"))
                    if l_option == "1":
                        print("")
                        print(f"{fg(111)}Create a new trainer")
                        trainer_name = input(str(f"{fg(148)}Enter Trainer name: "))
                        trainer_age = input(str(f"{fg(148)}Enter Trainer age: "))
                        trainer_phoneNumber = input(str(f"{fg(148)}Enter Trainer phone Number: "))
                        # userid = input(str("Enter the user ID : "))
                        query_vals = (trainer_name,trainer_age,trainer_phoneNumber)
                        # command_handler.execute("Insert into marino.locker(type_of_locker,idstaff,userid) values(%s,%s,0)",query_vals)
                        command_handler.execute("call trainer_reg(%s,%s,%s)",query_vals)
                        conn.commit()
                        print("New Trainer has been created!")

                    elif l_option == "2":
                        print("")
                        print(f"{fg(111)}Remove a Trainer")
                        print("")
                        print(f"{fg(73)}Viewing all Trainer")
                        command_handler.execute ("Select * from trainer")
                        result = command_handler.fetchall()
                        columns = ['Trainer ID', 'Trainer Name',"Trainer Age", 'Trainer Phone Number']
                        print(f"{fg(109)}")
                        print(tabulate(result,headers=columns,tablefmt="grid"))

                        trainer_id = input(str(f"{fg(148)}Enter the Trainer ID : "))
                        query_vals = (trainer_id,)
                        # command_handler.execute("Delete from locker where trainer_id = %s",query_vals)
                        command_handler.execute("Delete from trainer where idtrainer = %s;",query_vals)
                        conn.commit()
                        if command_handler.rowcount < 1:
                            print(f"{fg(1)}Trainer Not found")
                        else:
                            print(f"{fg(2)}"+ trainer_id + " trainer has been deleted successfully")
                            print("")
                        print(f"{fg(73)}Viewing all Trainer")
                        command_handler.execute ("Select * from trainer")
                        result = command_handler.fetchall()
                        columns = ['Trainer ID', 'Trainer Name',"Trainer Age", 'Trainer Phone Number']
                        print(f"{fg(109)}")
                        print(tabulate(result,headers=columns,tablefmt="grid"))

                    elif l_option == "3":
                        print("")
                        print(f"{fg(148)}Assign Trainer to a Activity")
                        print("")
                        print(f"{fg(111)}Available Trainers")
                        command_handler.execute ("Select * from trainer")
                        result = command_handler.fetchall()
                        columns = ['Trainer ID', 'Trainer Name',"Trainer Age", 'Trainer Phone Number']
                        print(f"{fg(109)}")
                        print(tabulate(result,headers=columns,tablefmt="grid"))


                        command_handler.execute ("Select * from activity where idtrainer=0")
                        result = command_handler.fetchall()
                        columns = ['Activity ID', 'Activity Name',"Room No.",'Rate', 'Trainer ID']
                        print(f"{fg(109)}")
                        print(tabulate(result,headers=columns,tablefmt="grid"))
                        # query_vals = (emailid)
                        # activity_id = input(str("Activity ID to be updated: "))
                        # trainer_id = input(str("Enter Trainer ID : "))
                        activity_id = input(f"{fg(148)}Activity ID to be updated: ")
                        trainer_id = input(f"{fg(148)}Enter Trainer ID : ")
                        query_vals = (trainer_id,activity_id)
                        command_handler.execute("Update activity SET idtrainer=%s where idactivity=%s",query_vals)

                        conn.commit()
                        print(f"{fg(2)}Updated Successfully!")
                        print("")
                        print(f"{fg(111)}Viewing Updated Trainer Data")
                        command_handler.execute ("Select * from activity")
                        result = command_handler.fetchall()
                        columns = ['Activity ID', 'Activity Name',"Room No.",'Rate', 'Trainer ID']
                        print(f"{fg(109)}")
                        print(tabulate(result,headers=columns,tablefmt="grid"))

                        # todo add condition to handle incorrect value
                        # if command_handler.rowcount < 1: 
                        #     print("")
                        #     print("No User found")
                        # else:
                        #       print(f"{fg(2)}")
                        #       print(idlocker + " Updated Successfully!")

                    elif l_option == "4":
                        print("")
                        print(f"{fg(111)}Viewing all Trainer")
                        command_handler.execute ("Select * from trainer")
                        result = command_handler.fetchall()
                        columns = ['Trainer ID', 'Trainer Name',"Trainer Age", 'Trainer Phone Number']
                        print(f"{fg(109)}")
                        print(tabulate(result,headers=columns,tablefmt="grid"))
                        conn.commit()
                        print("")
     


                        print(f"{fg(73)}Viewing Activity without Trainer")
                        command_handler.execute("select Activity_without_trainers() from activity LIMIT 1")
                        result = command_handler.fetchall()
                        columns = ['Activity without Trainers']
                        print(f"{fg(109)}")
                        print(tabulate(result,headers=columns,tablefmt="grid"))
        
                        if command_handler.rowcount < 1:
                            print(f"{fg(1)}Trainer not found!")
                       
                    elif l_option == "5":
                        break
                    else:
                         print(f"{fg(1)}Invalid Selection!")


        
        elif user_option == "6":
            break
        
        else:
            print(f"{fg(1)}Invalid Selection!")
       

#User session
def user_session(id):
    while 1:
        print(" ")
        print(f"{fg(111)}Welcome to User Panel")
        print(" ")
        print(f"{fg(209)}1. Register new Activity")     
        print(f"{fg(209)}2. Delete existing activity")
        print(f"{fg(209)}3. View your locker")
        print(f"{fg(209)}4. View Bill")
        print(f"{fg(209)}5. Update User details")
        print(f"{fg(209)}6. Logout")

        user_option = input(str(f"{fg(55)}Option : "))
       
        if user_option == "1":
            print("")
            print(f"{fg(111)}Register New Activity")
            # idstaff = input(str("ID: "))
            command_handler.execute ("Select * from activity")
            result_act = command_handler.fetchall()
            columns = ['Activity ID', 'Name of Activity','Alloted Room',"Rate"]
            print(f"{fg(109)}")
            print(tabulate(result_act,headers=columns,tablefmt="grid"))
            # activityId = 17006
            activityId = input(f"{fg(148)}Enter Activity ID: ")
            user_id = id
            query_vals = (activityId,user_id)
            command_handler.execute("call user_activity(%s,%s)",query_vals)
            conn.commit()
            print(activityId + " has been registered to you!")
        
       
        
        elif user_option == "2":
            print("")
            print(f"{fg(111)}Delete existing activity")
            # emailid = input(str("Email ID: "))
            # password = input(str("Password: "))
            user_id = id
            query_val = (user_id,)
            command_handler.execute ("select p.idpayment,a.price,a.idactivity,a.name from payment as p JOIN activity as a ON p.idactivity=a.idactivity JOIN user as u ON p.userid=u.userid where u.userid=%s GROUP BY p.idpayment",query_val)
            result_act = command_handler.fetchall()
            columns = ['Payment ID',"Rate", 'Activity ID','Activity Name','First Name',]
            print(f"{fg(109)}")
            print(tabulate(result_act,headers=columns,tablefmt="grid"))
            activityId = input(str(f"{fg(148)}Activity ID: "))
            query_vals = (activityId)
            command_handler.execute("call payment_del(%s)",query_vals)
            conn.commit()
            if command_handler.rowcount < 1: 
                print(f"{fg(2)}Activity not found")
            else:
                print(f"{fg(1)}"+activityId + " has been deleted!")

        elif user_option == "3":
            print("")
            print(f"{fg(111)}View your locker")
            # emailid = input(str("Email ID: "))
            # query_vals = (emailid)
            userid =  id
            query_vals = (userid,)
            command_handler.execute("Select * from locker where userid = %s",query_vals)
            # fetch all the matching rows 
            result = command_handler.fetchall()
            columns = ['Locker ID', 'Type of Locker','Staff ID', 'User ID']
            print(f"{fg(109)}")
            print(tabulate(result,headers=columns,tablefmt="grid"))
  
            # loop through the rows
            # for row in result:
            #     print(row)
                # print("\n")
            conn.commit()
            if command_handler.rowcount < 1: 
                print(f"{fg(1)} No Locker found")

                
        elif user_option == "4":
            print("")
            print(f"{fg(111)}Viewing Bill")
            user_id=id
            query_val = (id,)
            command_handler.execute ("select p.idpayment,a.price,a.idactivity,a.name from payment as p JOIN activity as a ON p.idactivity=a.idactivity JOIN user as u ON p.userid=u.userid where u.userid=%s GROUP BY p.idpayment",query_val)
            result_act = command_handler.fetchall()
            columns = ['Payment ID',"Rate", 'Activity ID','Activity Name','First Name',]
            print(f"{fg(109)}")
            print(tabulate(result_act,headers=columns,tablefmt="grid"))
            user_id = id
            query_val = (user_id,)
            command_handler.execute("select totalPayment(%s) from payment Limit 1",query_val)
            result = command_handler.fetchall()
            columns = ["Total Bill"]
            print(f"{fg(109)}")
            print(tabulate(result,headers=columns,tablefmt="grid"))
            conn.commit()

            if command_handler.rowcount < 1: 
                            print("")
                            print(f"{fg(1)}No Bill found")
            else:
                              print(f"{fg(2)}")
                              print(user_id + " Bill Amount!")


        elif user_option == "5":
                    print("")
                    print(f"{fg(111)}Update Existing User Details")
                    print("")
                    update_iduser = id
                    print(f"{fg(148)} User id : " + id)
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    emailid = input(str("Email ID: "))
                    if(re.fullmatch(regex, emailid)):
                        # update_iduser = input(str("User ID to be updated: "))
                        first_name = input(str(f"{fg(148)}User First Name: "))
                        last_name = input(str(f"{fg(148)}User Last Name: "))
                        user_age = input(str(f"{fg(148)}User Age: "))
                        phone_number = input(str(f"{fg(148)}Staff Phone Number: "))
                        password = input(str(f"{fg(148)}Password: "))
                        query_vals = (first_name,last_name,user_age,phone_number,emailid,password,update_iduser)
                        command_handler.execute("Update user SET first_name = %s,last_name=%s,age=%s,phone_number=%s,emailid=%s,password=%s where userid=%s",query_vals)

                        conn.commit()

                        if command_handler.rowcount < 1: 
                            print("")
                            print(f"{fg(1)}No User found")
                        else:
                              print("")
                              print(f"{fg(2)}"+first_name + " Updated Successfully!")
                    else:
                        print(f"{fg(1)}Invalid Email format, Try again")
                        break
                
        elif user_option == "6":
            break
        else:
            print(f"{fg(1)}Invaliid Selection!")



#Admin Authorization
def auth_admin():
    print("")
    print(f"{fg(111)}Admin Login")
    print("")
    emailid = input(str(f"{fg(148)}Email ID: "))
  
    if(re.fullmatch(regex, emailid)):
        # print("Valid Email")
        # password = input(str("Password: "))
        password = maskpass.askpass(mask="*")
        query_vals = (emailid,password)
        command_handler.execute("Select * from marino.admin where emailid = %s AND password = %s",query_vals)

        if command_handler.rowcount<=0:
            print (f"{fg(1)}Login not recognized")
        else:
            print("")
            print(f"{fg(2)}Welcome " + emailid)
            admin_session()
 
    else:
        print(f"{fg(1)}Invalid Email format, Try again")
        auth_admin()
        

    
    
    

    

#Staff Authorization
def auth_staff():
    print("")
    print(f"{fg(111)}Staff Login")
    print("")
    emailid = input(str(f"{fg(148)}Email ID: "))
    if(re.fullmatch(regex, emailid)):
        # print("Valid Email")
        # password = input(str("Password: "))
        password = maskpass.askpass(mask="*")
        query_vals = (emailid,password)
        command_handler.execute("Select * from marino.staff where emailid = %s AND password = %s",query_vals)
        result = command_handler.fetchall()
        columns = ['Staff_id ID']
        print(f"{fg(109)}")
        # print(tabulate(result,headers=columns,tablefmt="grid"))
        res=", ".join(map(str,result))
        id= res[1:-2]

        if command_handler.rowcount<=0:
         print (f"{fg(1)}Login not recognized")
        else:
            print("")
            print(f"{fg(2)}Welcome " + emailid + " " )
            staff_session(id)
    else:
        print("")
        print(f"{fg(1)}Invalid Email format, Try again")
        auth_staff()


#User Authorization
def auth_user():
    print("")
    print(f"{fg(111)}User Login")
    print("")
    emailid = input(str("Email ID: "))
    if(re.fullmatch(regex, emailid)):
        # password = input(str("Password: "))
        password = maskpass.askpass(mask="*")
        query_vals = (emailid,password)
        command_handler.execute("Select userid from marino.user where emailid = %s AND password = %s",query_vals)
        result = command_handler.fetchall()
        columns = ['User ID']
        print(f"{fg(109)}")
        # print(tabulate(result,headers=columns,tablefmt="grid"))
        res=", ".join(map(str,result))
        id= res[1:-2]
        # print(id)

        if command_handler.rowcount<=0:
            print (f"{fg(1)}Login not recognized")
        else:
            print("")
            print(f"{fg(2)}Welcome " +emailid+ " ")
            user_session(id)
    else:
        print("")
        print(f"{fg(1)}Invalid Email format, Try again")
        auth_user()


#New User Authorization
def auth_new_user():
    print("")
    print(f"{fg(111)}New User Registration")
    print("")
    emailid = input(str(f"{fg(148)}user emailid: "))
    if(re.fullmatch(regex, emailid)):
        # print("Valid Email")
        password = input(str(f"{fg(148)}user password: "))
        first_name = input(str(f"{fg(148)}First Name: "))
        last_name = input(str(f"{fg(148)}Last Name: "))
        age = input(str(f"{fg(148)}user Age: "))
        phone_number = input(str(f"{fg(148)}user Phone Number: "))
        query_vals = (first_name,last_name,age,phone_number,emailid,password)
        command_handler.execute("INSERT INTO marino.user(first_name,last_name,age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
        conn.commit()
        print(first_name + " has been registered as a User")

        print("")
    else:
        print("")
        print(f"{fg(1)}Invalid Email format, Try again")
        auth_new_user()    
   


def main():
    while 1:
        print("")
        print(f"{fg(73)}Welcome to Marino Center Database System! ")
        print(" ")
        f = Figlet(font='slant')
        print (f.renderText('MARINO DBMS'))
        print(" ")
        print(f"{fg(209)}1. Login as admin")
        print(f"{fg(209)}2. Login as user")
        print(f"{fg(209)}3. Login as staff")
        print(f"{fg(209)}4. Register as user")
        print(f"{fg(209)}5. Quit")
        # print("2. Login as user")

        user_option = input(str(f"{fg(99)}Option : "))
        if user_option == "1":
            # print("Admin Login")
            auth_admin()
        elif user_option == "2":
            # print("User Login")
            auth_user()
        elif user_option == "3":
            # print("Staff Login")
            auth_staff()
        # elif user_option == "4":
        #     print("Trainer Login")
        elif user_option == "4":
            auth_new_user()
        elif user_option == "5":
            print(" ")
            f = Figlet(font='slant')
            print (f.renderText('THANK YOU'))
            break
        else:
            print(f"{fg(1)}Not a valid option!")
            

main()