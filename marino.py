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
#Admin Session 
def admin_session():
    # print("Login successfully, Welcome Admin!")
 while 1:
        print("")
        print(f"{fg(23)}Welcome to Admin Panel")
        print("")
        print(f"{fg(148)}1.Staff Panel")
        print(f"{fg(148)}2.Student Panel")
        print(f"{fg(148)}3.Back")
        print("")

        user_option = input(str(f"{fg(99)}Option : "))
        if user_option == "1":
            while 1:
                print("")
                print("Staff Panel")
                print("")
                print(f"{fg(148)}1. Register new staff")
                print(f"{fg(148)}2. Delete existing staff")
                print(f"{fg(148)}3. Read existing staff")
                print(f"{fg(148)}4. Update existing staff")
                print("5. Back")
                admin_user_option = input(str(f"{fg(99)}Option : "))

                if admin_user_option == "1":
                    print("")
                    print(f"{fg(73)}Register New Staff")
                    print("")
                     # idstaff = input(str("ID: "))
                    emailid = input(str("Staff emailid: "))
                    if(re.fullmatch(regex, emailid)):
                        password = input(str("Staff password: "))
                        staff_name = input(str("Staff Name: "))
                        staff_age = input(str("Staff Age: "))
                        phone_number = input(str("Staff Phone Number: "))
                        query_vals = (staff_name,staff_age,phone_number,emailid,password)
                        # command_handler.execute("INSERT INTO marino.staff (staff_name,staff_age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s)",query_vals)
                        command_handler.execute("call staff_reg(%s,%s,%s,%s,%s)",query_vals)
                        conn.commit()
                        print(emailid + f"{fg(2)} has been registered as a staff")
                    else:
                        print("Invalid Email format, Try again")
                        break

                elif admin_user_option == "2":
                    print("")
                    print(f"{fg(148)}Delete Existing Staff Account")
                    print("")
                    emailid = input(str("Email ID: "))
                    password = input(str("Password: "))
                    query_vals = (emailid,password)
                    # command_handler.execute("DELETE FROM staff WHERE emailid = %s AND password = %s",query_vals)
                    command_handler.execute("call staff_del(%s,%s)",query_vals)
                    conn.commit()
                    if command_handler.rowcount < 1: 
                        print("Staff not found")
                    else:
                        print("")
                        print(emailid + f"{fg(1)} has been deleted!")

                elif admin_user_option == "3":
                    print("")
                    print(f"{fg(148)}All Existing Staff Details")
                    print("")
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
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
                        print("No Staff found")

                elif admin_user_option == "4":
                    print("")
                    print(f"{fg(148)}Update Existing Staff Details")
                    print("")
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    update_idstaff = input(str("Staff ID to be updated: "))
                    staff_name = input(str("Staff Name: "))
                    staff_age = input(str("Staff Age: "))
                    phone_number = input(str("Staff Phone Number: "))
                    query_vals = (staff_name,staff_age,phone_number,update_idstaff)
                    command_handler.execute("Update staff SET staff_name = %s,staff_age=%s,phone_number=%s where idstaff=%s",query_vals)
            
                    conn.commit()
                    print("Updated Successfully!")
                    if command_handler.rowcount < 1: 
                        print("")
                        print("No Staff found")
             
                

                elif admin_user_option == "5":
                 break
                else:
                    print("")
                    print("Invalid option!")

        if user_option == "2":
            while 1:
                print("")
                print(f"{fg(148)}User Panel")
                print("")
                print(f"{fg(148)}1. Register new user")

                print(f"{fg(148)}2. Delete existing user")

                print(f"{fg(148)}3. Read existing user")

                print(f"{fg(148)}4. Update existing user")

                print("5. Back")
        
                client_user_option = input(str(f"{fg(99)}Option : "))

                if client_user_option == "1":
                    print("")
                    print(f"{fg(148)}Register New User")
                    print("")
                    # idstaff = input(str("ID: "))
                    emailid = input(str("user emailid: "))
                    if(re.fullmatch(regex, emailid)):
                        password = input(str("user password: "))
                        first_name = input(str("First Name: "))
                        last_name = input(str("Last Name: "))
                        age = input(str("user Age: "))
                        phone_number = input(str("user Phone Number: "))
                        query_vals = (first_name,last_name,age,phone_number,emailid,password)
                        # command_handler.execute("INSERT INTO marino.user(first_name,last_name,age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
                        command_handler.execute("call user_reg(%s,%s,%s,%s,%s,%s)",query_vals)
                        conn.commit()
                        print(first_name + f"{fg(2)} has been registered as a User")
                    else:
                        print("Invalid Email format, Try again")
                        break
        
        
        
                elif client_user_option == "2":
                    print("")
                    print(f"{fg(148)}Delete Existing User Account")
                    print("")
                    emailid = input(str("Email ID: "))
                    password = input(str("Password: "))
                    query_vals = (emailid,password)
                    # command_handler.execute("DELETE FROM user WHERE emailid = %s AND password = %s",query_vals)
                    command_handler.execute("call user_del(%s,%s)",query_vals)
                    conn.commit()
                    if command_handler.rowcount < 1: 
                        print("")
                        print("User not found")
                    else:
                        print(emailid + f"{fg(1)} has been deleted!")

       

                elif client_user_option == "3":
                    print("")
                    print(f"{fg(148)}All Existing User Details")
                    print("")
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
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
                    print(f"{fg(148)}Update Existing User Details")
                    print("")
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    update_iduser = input(str("User ID to be updated: "))
                    first_name = input(str("User First Name: "))
                    last_name = input(str("User Last Name: "))
                    user_age = input(str("User Age: "))
                    phone_number = input(str("Staff Phone Number: "))
                    query_vals = (first_name,last_name,user_age,phone_number,update_iduser)
                    command_handler.execute("Update user SET first_name = %s,last_name=%s,age=%s,phone_number=%s where userid=%s",query_vals)
            
                    conn.commit()
                    print(f"{fg(2)}")
                    print(first_name + " Updated Successfully!")
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
        print(f"{fg(148)}Welcome to Staff Panel")
        print("")
        print("1.User Panel")
        print("2.Locker Panel")
        print("3.Equipment Panel")
        print("4.Activity Panel")
        print("5.Back")

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
                elif u_option == "5":
                   break

                else: 
                    print("")
                    print(f"{fg(1)}Invaliid Selection!")
            
            
        
        

        elif user_option == "2":
         while 1:
            print(" ")
            print(f"{fg(73)}Welcome to Locker Panel")
            print("1. Create new locker")
            print("2. Delete locker")
            print("3. Assign a locker")
            print("4. View all lockers")
            print("5. Back")
            l_option = input(str(f"{fg(99)}Option :"))
            if l_option == "1":
                print("")
                print(f"{fg(73)}Create a new locker")

    
                type_of_locker = input(str("Enter the type of Locker (Personal/Standard): "))
                idstaff = id
                # userid = input(str("Enter the user ID : "))
                query_vals = (type_of_locker,idstaff)
                # command_handler.execute("Insert into marino.locker(type_of_locker,idstaff,userid) values(%s,%s,0)",query_vals)
                command_handler.execute("call locker_reg(%s,%s,0)",query_vals)
                conn.commit()
                print("New locker has been created!")

            elif l_option == "2":
                print("")
                print(f"{fg(73)}Delete a locker")
                command_handler.execute ("Select idlocker,type_of_locker from locker")
                result = command_handler.fetchall()
                columns = ['Locker ID', 'Type of Locker']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))

                idlocker = input(str("Enter the locker ID : "))
                query_vals = (idlocker,)
                # command_handler.execute("Delete from locker where idlocker = %s",query_vals)
                command_handler.execute("call locker_del(%s)",query_vals)
                conn.commit()
                if command_handler.rowcount < 1:
                    print("Locker Not found")
                else:
                    print(idlocker + " locker has been deleted successfully")

            elif l_option == "3":
                    print("")
                    print(f"{fg(148)}Assign locker to a User")
                    print("")
                    print("Available Lockers")
                    command_handler.execute ("Select idlocker,type_of_locker,userid from locker where userid=0 ")
                    result = command_handler.fetchall()
                    columns = ['Locker ID', 'Type of Locker','user_id']
                    print(f"{fg(109)}")
                    print(tabulate(result,headers=columns,tablefmt="grid"))
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    update_iduser = input(str("User ID to be updated: "))
                    idlocker = input(str("Enter Locker ID : "))
                    query_vals = (update_iduser,idlocker)
                    command_handler.execute("Update locker SET userid=%s where idlocker=%s",query_vals)
            
                    conn.commit()
                    print(idlocker + " Updated Successfully!")

                    # todo add condition to handle incorrect value
                    # if command_handler.rowcount < 1: 
                    #     print("")
                    #     print("No User found")
                    # else:
                    #       print(f"{fg(2)}")
                    #       print(idlocker + " Updated Successfully!")

            elif l_option == "4":
                print("")
                print(f"{fg(73)}Viewing a Locker")
                command_handler.execute ("Select idlocker, type_of_locker,userid from locker")
                result = command_handler.fetchall()
                columns = ['Locker ID', 'Type of Locker', 'User ID']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))
                # for row in result: 
                #     print(row)
                #     print("\n")
                conn.commit()

                if command_handler.rowcount < 1:
                    print("Lockers not found!")
                else:
                        print("Invalid option!")
                
            
            elif l_option == "5":
                break
            else:
                print(f"{fg(1)}Invaliid Selection!")

        elif user_option == "3":
         while 1:
            print(" ")
            print(f"{fg(73)}Welcome to Equipment Panel")
            print("1. Add an equipment")
            print("2. Delete an equipment")
            print("3. View all equipments")
            print("4. Assign an equipment")
            print("5. Back")

            e_option = input(str(f"{fg(99)}Option : "))
            if e_option == "1":
                print("")
                print(f"{fg(73)}Add a new Equipment")
    
                name = input(str("Name of the equipment: "))
                idstaff = id
                idactivity = 0
                query_vals = (name,idstaff,idactivity)
                # command_handler.execute("Insert into marino.equipment(name,idstaff,idactivity) values(%s,%s,%s)",query_vals)
                command_handler.execute("call equipment_reg(%s,%s,%s)",query_vals)
                conn.commit()
                print("New equipment has been added!")

            elif e_option == "2":
                print("")
                print(f"{fg(73)}Remove an equipment")
                command_handler.execute ("Select idequipment,name from equipment")
                result = command_handler.fetchall()
                columns = ['Equipment ID', 'Name of Equipment']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))

                idequipment = input(str("Enter the Equipment ID : "))
                query_vals = (idequipment,)
                # command_handler.execute("Delete from equipment where idequipment = %s",query_vals)
                command_handler.execute("call equipment_del(%s)",query_vals)
                conn.commit()
                if command_handler.rowcount < 1:
                    print("Equipment Not found")
                else:
                    print(idequipment + " equipment has been deleted successfully")


            elif e_option == "3":
                print("")
                print(f"{fg(73)}Viewing all Equipments")

                command_handler.execute ("Select idequipment,name,idactivity from equipment")
                result = command_handler.fetchall()
                columns = ['Equipment ID', 'Name of Equipment', 'Activity ID']
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))

                # for row in result: 
                #     print(row)
                #     print("\n")
                conn.commit()

                if command_handler.rowcount < 1:
                    print("Equipments not found!")

            elif e_option == "4":
                    print("")
                    print(f"{fg(148)}Assign Equipment to a Activity")
                    print("")
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
                    idactivity = input(str("Activity ID: "))
                    idequipment = input(str("Enter Equipment ID : "))
                    query_vals = (idactivity,idequipment)
                    command_handler.execute("Update equipment SET idactivity=%s where idequipment=%s",query_vals)
            
                    conn.commit()
                    print(idequipment + " Updated Successfully!")
                    
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
            print(f"{fg(73)}Welcome to Activity Panel")
            print("1. Create an activity")
            print("2. Delete an activity")
            print("3. View all activity")
            print("4. Update an activity")
            print("5. Back")

            a_option = input(str(f"{fg(99)}Option : "))
            if a_option == "1":
                print("")
                print(f"{fg(73)}Create an activity")

                name = input(str("Enter the name of the activity: "))
                room_no = input(str("Enter the room number for the activity: "))
                price = input(str('Enter activity rate: '))

                query_vals = (name,room_no)
                # command_handler.execute("Insert into marino.activity (name,room_no) values (%s,%s)",query_vals)
                command_handler.execute("call activity_reg(%s,%s,%s)",query_vals)
                conn.commit()

                print("New Activity has been created!")
            elif a_option == "2":
                print("")
                print(f"{fg(55)}Delete an activity")
                command_handler.execute ("Select * from activity")
                result_act = command_handler.fetchall()
                columns = ['Activity ID', 'Name of Activity','Alloted Room','Rate']
                print(f"{fg(109)}")
                print(tabulate(result_act,headers=columns,tablefmt="grid"))

                idactivity = input(str("Enter the acitvity ID: "))
                query_vals = (idactivity,)
                # command_handler.execute("Delete from activity where idactivity = %s", query_vals)
                command_handler.execute("call activity_del(%s)",query_vals)
                conn.commit()

                if command_handler.rowcount < 1:
                    print("Activity doesn't exist")
                else:
                    print("Activity has been deleted successfully!")

            elif a_option == "3":
                print("")
                print(f"{fg(73)}View all activity")

                command_handler.execute("SELECT * from activity")
                # command_handler.execute("SELECT a.idactivity,a.name,a.room_no,e.idequipment,e.name from activity as a JOIN equipment as e ON a.idactivity=e.idactivity;")
                # query_vals = ()
                # command_handler.execute("call activity_Equip_table()",query_vals)
                result = command_handler.fetchall()
                columns = ['Activity ID', 'Activity Name','Room Number',"Rate"]
                print(f"{fg(109)}")
                print(tabulate(result,headers=columns,tablefmt="grid"))


                # for row in result:
                #     print (row)
                conn.commit()

                if command_handler.rowcount <1:
                    print("No details found")

            elif a_option == "4":
                    print("")
                    print(f"{fg(148)}Assign Activity to a User")
                    print("")
                    command_handler.execute ("Select * from activity")
                    result_act = command_handler.fetchall()
                    columns = ['Activity ID', 'Name of Activity','Alloted Room',"Rate"]
                    print(f"{fg(109)}")
                    print(tabulate(result_act,headers=columns,tablefmt="grid"))
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    idactivity = input(str("Activity ID: "))
                    name = input(str("activity Name: "))
                    room_no = input(str("Enter Room ID : "))
                    query_vals = (room_no,name,idactivity)
                    command_handler.execute("Update activity SET room_no=%s,name=%s where idactivity=%s",query_vals)
            
                    conn.commit()
                    print(name + " Updated Successfully!")
                    
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
            break
        
        else:
            print(f"{fg(1)}Invaliid Selection!")
       

#User session
def user_session(id):
    while 1:
        print(" ")
        print(f"{fg(73)}Welcome to User Panel")
        print(" ")
        print(f"{fg(208)}1. Register new Activity")     
        print(f"{fg(208)}2. Delete existing activity")
        print(f"{fg(208)}3. View your locker")
        print(f"{fg(208)}4. View Bill")
        print(f"{fg(208)}5. Update User details")
        print(f"{fg(208)}9. Logout")

        user_option = input(str("Option : "))
       
        if user_option == "1":
            print("")
            print(f"{fg(148)}Register New Activity")
            # idstaff = input(str("ID: "))
            command_handler.execute ("Select * from activity")
            result_act = command_handler.fetchall()
            columns = ['Activity ID', 'Name of Activity','Alloted Room',"Rate"]
            print(f"{fg(109)}")
            print(tabulate(result_act,headers=columns,tablefmt="grid"))
            # activityId = 17006
            activityId = input("Enter Activity ID: ")
            user_id = 10
            query_vals = (activityId,user_id)
            command_handler.execute("call user_activity(%s,%s)",query_vals)
            conn.commit()
            print(activityId + " has been registered to you!")
        
       
        
        elif user_option == "2":
            print("")
            print(f"{fg(148)}Delete existing activity")
            # emailid = input(str("Email ID: "))
            # password = input(str("Password: "))
            user_id = id
            query_val = (user_id,)
            command_handler.execute ("select p.idpayment,a.price,a.idactivity,a.name from payment as p JOIN activity as a ON p.idactivity=a.idactivity JOIN user as u ON p.userid=u.userid where u.userid= %s GROUP BY p.idpayment",query_val)
            result_act = command_handler.fetchall()
            columns = ['Payment ID',"Rate", 'Activity ID','Activity Name','First Name',]
            print(f"{fg(109)}")
            print(tabulate(result_act,headers=columns,tablefmt="grid"))
            activityId = input(str("Activity ID: "))
            query_vals = (activityId)
            command_handler.execute("call payment_del(%s)",query_vals)
            conn.commit()
            if command_handler.rowcount < 1: 
                print("Activity not found")
            else:
                print(activityId + " has been deleted!")

        elif user_option == "3":
            print("")
            print(f"{fg(148)}View your locker")
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
                print("No Locker found")

                
        elif user_option == "4":
            print("")
            print(f"{fg(148)}Viewing Bill")

        elif user_option == "5":
                    print("")
                    print(f"{fg(148)}Update Existing User Details")
                    print("")
                    update_iduser = id
                    print(" User id : " + id)
                    # emailid = input(str("Email ID: "))
                    # query_vals = (emailid)
                    emailid = input(str("Email ID: "))
                    if(re.fullmatch(regex, emailid)):
                        # update_iduser = input(str("User ID to be updated: "))
                        first_name = input(str("User First Name: "))
                        last_name = input(str("User Last Name: "))
                        user_age = input(str("User Age: "))
                        phone_number = input(str("Staff Phone Number: "))
                        password = input(str("Password: "))
                        query_vals = (first_name,last_name,user_age,phone_number,emailid,password,update_iduser)
                        command_handler.execute("Update user SET first_name = %s,last_name=%s,age=%s,phone_number=%s,emailid=%s,password=%s where userid=%s",query_vals)

                        conn.commit()

                        if command_handler.rowcount < 1: 
                            print("")
                            print("No User found")
                        else:
                              print(f"{fg(2)}")
                              print(first_name + " Updated Successfully!")
                    else:
                        print("Invalid Email format, Try again")
                        break
                
        elif user_option == "9":
            break
        else:
            print("Invaliid Selection!")



#Admin Authorization
def auth_admin():
    print("")
    print(f"{fg(148)}Admin Login")
    print("")
    emailid = input(str("Email ID: "))
  
    if(re.fullmatch(regex, emailid)):
        print("Valid Email")
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
        print("Invalid Email format, Try again")
        auth_admin()
        

    
    
    

    

#Staff Authorization
def auth_staff():
    print("")
    print(f"{fg(148)}Staff Login")
    print("")
    emailid = input(str("Email ID: "))
    if(re.fullmatch(regex, emailid)):
        print("Valid Email")
        # password = input(str("Password: "))
        password = maskpass.askpass(mask="*")
        query_vals = (emailid,password)
        command_handler.execute("Select * from marino.staff where emailid = %s AND password = %s",query_vals)
        result = command_handler.fetchall()
        columns = ['Staff_id ID']
        print(f"{fg(109)}")
        print(tabulate(result,headers=columns,tablefmt="grid"))
        res=", ".join(map(str,result))
        id= res[1:-2]

        if command_handler.rowcount<=0:
         print (f"{fg(1)}Login not recognized")
        else:
            print("")
            print(f"{fg(2)}Welcome " + emailid + " " +id)
            staff_session(id)
    else:
        print("Invalid Email format, Try again")
        auth_staff()


#User Authorization
def auth_user():
    print("")
    print(f"{fg(148)}User Login")
    print("")
    emailid = input(str("Email ID: "))
    if(re.fullmatch(regex, emailid)):
        # password = input(str("Password: "))
        password = maskpass.askpass(mask="*")
        query_vals = (emailid,password)
        command_handler.execute("Select * from marino.user where emailid = %s AND password = %s",query_vals)
        result = command_handler.fetchall()
        columns = ['User ID']
        print(f"{fg(109)}")
        print(tabulate(result,headers=columns,tablefmt="grid"))
        res=", ".join(map(str,result))
        id= res[1:-2]
        print(id)

        if command_handler.rowcount<=0:
            print (f"{fg(1)}Login not recognized")
        else:
            print("")
            print(f"{fg(2)}Welcome " + emailid+ " "+id)
            user_session(id)
    else:
        print("Invalid Email format, Try again")
        auth_user()


#New User Authorization
def auth_new_user():
    print("")
    print(f"{fg(148)}New User Registration")
    print("")
    emailid = input(str("user emailid: "))
    if(re.fullmatch(regex, emailid)):
        print("Valid Email")
        password = input(str("user password: "))
        first_name = input(str("First Name: "))
        last_name = input(str("Last Name: "))
        age = input(str("user Age: "))
        phone_number = input(str("user Phone Number: "))
        query_vals = (first_name,last_name,age,phone_number,emailid,password)
        command_handler.execute("INSERT INTO marino.user(first_name,last_name,age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
        conn.commit()
        print(first_name + " has been registered as a User")

        print("")
    else:
        print("Invalid Email format, Try again")
        auth_new_user()    
   


def main():
    while 1:
        print("")
        print(f"{fg(73)}Welcome to Marino Center Database System! ")
        print(" ")
        f = Figlet(font='slant')
        print (f.renderText('MARINO DBMS'))
        print(" ")
        print(f"{fg(148)}1. Login as admin")
        print(f"{fg(148)}2. Login as user")
        print(f"{fg(148)}3. Login as staff")
        print(f"{fg(148)}4. Register as user")
        print(f"{fg(148)}5. Quit")
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