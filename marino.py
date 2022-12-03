import mysql.connector as mysql 
from colored import fg, bg, attr

db = mysql.connect(host ="localhost",user = "root", password="arps@1899",database="marino")
command_handler = db.cursor(buffered=True)

def admin_session():
    # print("Login successfully, Welcome Admin!")
 while 1:
        print("Welcome to Admin Panel")
        print(" ")
        print("1. Register new staff")
        print("2. Register new user")
        print("3. Delete existing staff")
        print("4. Delete existing user")
        print("5. Read existing staff")
        print("6. Read existing user")
        print("7. Update existing staff")
        print("8. Update existing user")
        print("9. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Register New Staff")
            # idstaff = input(str("ID: "))
            emailid = input(str("Staff emailid: "))
            password = input(str("Staff password: "))
            staff_name = input(str("Staff Name: "))
            staff_age = input(str("Staff Age: "))
            phone_number = input(str("Staff Phone Number: "))
            query_vals = (staff_name,staff_age,phone_number,emailid,password)
            command_handler.execute("INSERT INTO marino.staff (staff_name,staff_age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s)",query_vals)
            db.commit()
            print(emailid + " has been registered as a staff")

        elif user_option == "2":
            print("")
            print("Register New User")
            # idstaff = input(str("ID: "))
            emailid = input(str("user emailid: "))
            password = input(str("user password: "))
            first_name = input(str("First Name: "))
            last_name = input(str("Last Name: "))
            age = input(str("user Age: "))
            phone_number = input(str("user Phone Number: "))
            query_vals = (first_name,last_name,age,phone_number,emailid,password)
            command_handler.execute("INSERT INTO marino.user(first_name,last_name,age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
            db.commit()
            print(first_name + " has been registered as a User")
        
        elif user_option == "3":
            print("")
            print("Delete Existing Staff Account")
            emailid = input(str("Email ID: "))
            password = input(str("Password: "))
            query_vals = (emailid,password)
            command_handler.execute("DELETE FROM staff WHERE emailid = %s AND password = %s",query_vals)
            db.commit()
            if command_handler.rowcount < 1: 
                print("Staff not found")
            else:
                print(emailid + " has been deleted!")
        
        elif user_option == "4":
            print("")
            print("Delete Existing User Account")
            emailid = input(str("Email ID: "))
            password = input(str("Password: "))
            query_vals = (emailid,password)
            command_handler.execute("DELETE FROM user WHERE emailid = %s AND password = %s",query_vals)
            db.commit()
            if command_handler.rowcount < 1: 
                print("User not found")
            else:
                print(emailid + " has been deleted!")

        elif user_option == "5":
            print("")
            print("All Existing Staff Details")
            # emailid = input(str("Email ID: "))
            # query_vals = (emailid)
            command_handler.execute("Select * from staff")
            # fetch all the matching rows 
            result = command_handler.fetchall()
  
            # loop through the rows
            for row in result:
                print(row)
                print("\n")
            db.commit()
            if command_handler.rowcount < 1: 
                print("No Staff found")

        elif user_option == "6":
            print("")
            print("All Existing User Details")
            # emailid = input(str("Email ID: "))
            # query_vals = (emailid)
            command_handler.execute("Select * from user")
            # fetch all the matching rows 
            result = command_handler.fetchall()
  
            # loop through the rows
            for row in result:
                print(row)
                print("\n")
            db.commit()
            if command_handler.rowcount < 1: 
                print("No User found")

        # if user_option == "7":
        #     print("")
        #     print("Update exisitng Staff")
        #     # idstaff = input(str("ID: "))
        #     emailid = input(str("Staff emailid: "))
        #     password = input(str("Staff password: "))
        #     staff_name = input(str("Staff Name: "))
        #     staff_age = input(str("Staff Age: "))
        #     phone_number = input(str("Staff Phone Number: "))
        #     query_vals = (staff_name,staff_age,phone_number,emailid,password)
        #     command_handler.execute("Update INTO marino.staff (staff_name,staff_age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s)",query_vals)
        #     db.commit()
        #     print(emailid + " has been updated in staff")
        
        elif user_option == "9":
            break
        else:
            print("Invalid option Selected!")
    
def staff_session():
    while 1:
        print(" ")
        print("Welcome to Staff Panel")
        print(" ")
        print("1. Register new user")     
        print("2. Delete existing user")
        print("3. Read existing user")
        print("4. Update existing user")
        print("5. Create new locker")
        print("6. Delete locker")
        print("7. Assign a locker")
        print("8. View all lockers")
        print("9. Add an equipment")
        print("10. Delete an equipment")
        print("11. View all equipments")
        print("12. Assign an equipment")
        print("13. Create an activity")
        print("14. Delete an activity")
        print("15. View all activity")
        print("16. Update an activity")
        print("17. Logout")

        user_option = input(str("Option : "))
       
        if user_option == "1":
            print("")
            print("Register New User")
            # idstaff = input(str("ID: "))
            emailid = input(str("user emailid: "))
            password = input(str("user password: "))
            first_name = input(str("First Name: "))
            last_name = input(str("Last Name: "))
            age = input(str("user Age: "))
            phone_number = input(str("user Phone Number: "))
            query_vals = (first_name,last_name,age,phone_number,emailid,password)
            command_handler.execute("INSERT INTO marino.user(first_name,last_name,age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
            db.commit()
            print(first_name + " has been registered as a User")
        
       
        
        elif user_option == "2":
            print("")
            print("Delete Existing User Account")
            emailid = input(str("Email ID: "))
            password = input(str("Password: "))
            query_vals = (emailid,password)
            command_handler.execute("DELETE FROM user WHERE emailid = %s AND password = %s",query_vals)
            db.commit()
            if command_handler.rowcount < 1: 
                print("User not found")
            else:
                print(emailid + " has been deleted!")

        elif user_option == "3":
            print("")
            print("All Existing User Details")

            command_handler.execute("Select * from user")

            # fetch all the matching rows 
            result = command_handler.fetchall()
  
            # loop through the rows
            for row in result:
                print(row)
                print("\n")
            db.commit()
            if command_handler.rowcount < 1: 
                print("No User found")
        
        elif user_option == "5":
            print("")
            print("Create a new locker")

            type_of_locker = input(str("Enter the type of Locker (Personal/Standard): "))
            idstaff = input(str("Enter the staff ID : "))
            userid = input(str("Enter the user ID : "))
            query_vals = (type_of_locker,idstaff,userid)
            command_handler.execute("Insert into marino.locker(type_of_locker,idstaff,userid) values(%s,%s,%s)",query_vals)
            db.commit()
            print("New locker has been created!")

        elif user_option == "6":
            print("")
            print("Delete a new locker")

            idlocker = input(str("Enter the locker ID : "))
            query_vals = (idlocker,)
            command_handler.execute("Delete from locker where idlocker = %s",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Locker Not found")
            else:
                print(idlocker + " locker has been deleted successfully")

        # elif user_option == "7":
        elif user_option == "8":
            print("")
            print("Viewing a Locker")
                
            command_handler.execute ("Select * from locker")
            result = command_handler.fetchall()

            for row in result: 
                print(row)
                print("\n")
            db.commit()

            if command_handler.rowcount < 1:
                print("Lockers not found!")

        elif user_option == "9":
            print("")
            print("Add a new Equipment")

            name = input(str("Name of the equipment: "))
            idstaff = input(str("Enter the staff ID : "))
            idactivity = input(str("Enter the activity ID : "))
            query_vals = (name,idstaff,idactivity)
            command_handler.execute("Insert into marino.equipment(name,idstaff,idactivity) values(%s,%s,%s)",query_vals)
            db.commit()
            print("New equipment has been added!")

        elif user_option == "10":
            print("")
            print("Remove an equipment")

            idequipment = input(str("Enter the Equipment ID : "))
            query_vals = (idequipment,)
            command_handler.execute("Delete from equipment where idequipment = %s",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Equipment Not found")
            else:
                print(idequipment + " equipment has been deleted successfully")

        # elif user_option == "11":
        elif user_option == "12":
            print("")
            print("Viewing all Equipments")
                
            command_handler.execute ("Select * from equipment")
            result = command_handler.fetchall()

            for row in result: 
                print(row)
                print("\n")
            db.commit()

            if command_handler.rowcount < 1:
                print("Equipments not found!")
        
        elif user_option == "13":
            print("")
            print("Create an activity")

            name = input(str("Enter the name of the activity: "))
            room_no = input(str("Enter the room number for the activity: "))
            
            query_vals = (name,room_no)
            command_handler.execute("Insert into marino.activity (name,room_no) values (%s,%s)",query_vals)
            db.commit()

            print("New Activity has been created!")

        elif user_option == "14":
            print("")
            print("Delete an activity")

            idactivity = input(str("Enter the acitvity ID: "))
            query_vals = (idactivity,)
            command_handler.execute("Delete from activity where idactivity = %s", query_vals)
            db.commit()

            if command_handler.rowcount < 1:
                print("Activity doesn't exist")
            else:
                print("Activity has been deleted successfully!")

        elif user_option == "15":
            print("")
            print("View all activity")

            command_handler.execute("SELECT a.idactivity,a.name,a.room_no,e.idequipment,e.name from activity as a JOIN equipment as e ON a.idactivity=e.idactivity;")
            result = command_handler.fetchall()

            for row in result:
                print (row)
            db.commit()

            if command_handler.rowcount <1:
                print("No details found")


        elif user_option == "17":
            break
        else:
            print("Invaliid Selection!")


   
def user_session():
    while 1:
        print(" ")
        print("Welcome to User Panel")
        print(" ")
        print("1. Register new Activity")     
        print("2. Delete existing activity")
        print("3. View your locker")
        print("4. View Bill")
        print("5. Update User details")
        print("9. Logout")

        user_option = input(str("Option : "))
       
        if user_option == "1":
            print("")
            print("Register New Activity")
            # idstaff = input(str("ID: "))
            emailid = input(str("user emailid: "))
            password = input(str("user password: "))
            first_name = input(str("First Name: "))
            last_name = input(str("Last Name: "))
            age = input(str("user Age: "))
            phone_number = input(str("user Phone Number: "))
            query_vals = (first_name,last_name,age,phone_number,emailid,password)
            command_handler.execute("INSERT INTO marino.user(first_name,last_name,age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
            db.commit()
            print(first_name + " has been registered as a User")
        
       
        
        elif user_option == "2":
            print("")
            print("Delete existing activity")
            emailid = input(str("Email ID: "))
            password = input(str("Password: "))
            query_vals = (emailid,password)
            command_handler.execute("DELETE FROM user WHERE emailid = %s AND password = %s",query_vals)
            db.commit()
            if command_handler.rowcount < 1: 
                print("User not found")
            else:
                print(emailid + " has been deleted!")

        elif user_option == "3":
            print("")
            print("View your locker")
            # emailid = input(str("Email ID: "))
            # query_vals = (emailid)
            userid = input(str("Enter user ID: "))
            query_vals = (userid,)
            command_handler.execute("Select * from locker where userid = %s",query_vals)
            # fetch all the matching rows 
            result = command_handler.fetchall()
  
            # loop through the rows
            for row in result:
                print(row)
                # print("\n")
            db.commit()
            if command_handler.rowcount < 1: 
                print("No Locker found")

                
        elif user_option == "4":
            print("")
            print("Viewing Bill")
                
        elif user_option == "9":
            break
        else:
            print("Invaliid Selection!")



#Admin Authorization
def auth_admin():
    print("")
    print("Admin Login")
    print("")
    emailid = input(str("Email ID: "))
    password = input(str("Password: "))
    query_vals = (emailid,password)
    command_handler.execute("Select * from marino.admin where emailid = %s AND password = %s",query_vals)

    if command_handler.rowcount<=0:
        print ("Login not recognized")
    else:
        print("Welcome " + emailid)
        admin_session()

#Staff Authorization
def auth_staff():
    print("")
    print("Staff Login")
    print("")
    emailid = input(str("Email ID: "))
    password = input(str("Password: "))
    query_vals = (emailid,password)
    command_handler.execute("Select * from marino.staff where emailid = %s AND password = %s",query_vals)

    if command_handler.rowcount<=0:
        print ("Login not recognized")
    else:
        print("Welcome " + emailid)
        staff_session()

#User Authorization
def auth_user():
    print("")
    print("User Login")
    print("")
    emailid = input(str("Email ID: "))
    password = input(str("Password: "))
    query_vals = (emailid,password)
    command_handler.execute("Select * from marino.user where emailid = %s AND password = %s",query_vals)

    if command_handler.rowcount<=0:
        print ("Login not recognized")
    else:
        print("Welcome " + emailid)
        user_session()
#New User Authorization
def auth_new_user():
    print("")
    print("New User Registration")
    print("")
    emailid = input(str("user emailid: "))
    password = input(str("user password: "))
    first_name = input(str("First Name: "))
    last_name = input(str("Last Name: "))
    age = input(str("user Age: "))
    phone_number = input(str("user Phone Number: "))
    query_vals = (first_name,last_name,age,phone_number,emailid,password)
    command_handler.execute("INSERT INTO marino.user(first_name,last_name,age,phone_number,emailid,password) VALUES (%s,%s,%s,%s,%s,%s)",query_vals)
    db.commit()
    print(first_name + " has been registered as a User")
    
    print("")
    
   



def main():
    while 1:
        print(f"{fg(73)}Welcome to Marino Center Database Sytsem")
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
            break
        else:
            print("No valid options")

main()