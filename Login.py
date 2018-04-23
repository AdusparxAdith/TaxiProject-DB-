import os
import resources
import getpass
import time
import pymysql

conn = pymysql.connect(host='127.0.0.1',user='demoo',password='demo1234',db = 'taxidb')
a = conn.cursor()

tries = 0

def Register(username):
    password = getpass.getpass("Enter a password\n")
    Password(password)

    # file = open("users.txt","a")
    # file.write(username+"/"+password+"\n")

    sql = 'insert into users(username,password) values(%s,%s)'

    a.execute(sql,(username,password))
    conn.commit()
    conn.close()

    print("You've successfully registered")
    time.sleep(1)
    os.system("cls")
    return(username)

def Login(username):
    global tries
    password = getpass.getpass("Enter your password\n")

    sql = 'select `password` from users where username = %s'

    a.execute(sql, (username))
    dbpass = a.fetchone()

    if(password == dbpass[0]):
        os.system("cls")
        return(username)
    elif(password != dbpass[0]):
        print("Password mismatch, try again")
        tries +=1
        if(tries >= 3):
            print("Too many tries, wait for 5 seconds")
            time.sleep(5)
            tries = 0
        Login(username)
    return(username)

    # file = open("users.txt","r")
    # for line in file:
    #     index = line.find("/")
    #     if(line[:index].strip() == username and line[index+1:].strip() == password):
    #         os.system("cls")
    #         return(username)
    #     elif(line[:index].strip() == username and line[index+1:].strip() != password):
    #         print("Password mismatch try again")
    #         tries +=1
    #         if(tries>=3):
    #             print("Too many tries, wait for 5 seconds")
    #             time.sleep(5)
    #             tries = 0
    #         Login(username)
    # file.close()




def Password(password):
    if (any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and sum(c.isdigit() for c in password) >= 2):
        return()
    else:
        print("Enter a new password with a lower case letter, an uppercase letter and 2 numbers")
        password = input("Enter another password\n")
        Password(password)

def Account():
    choice = input("1.New user\n2.Registered user\n\n")

    if(choice == "1"):
        os.system("cls")
        resources.line()
        print("\nREGISTER\n")
        resources.line()

        exists = 0
        username = input("What is you name?\n")

        sql = 'select `username` from users where `username` = %s'
        entries = a.execute(sql,(username))
        if(entries > 0):
            print("User already exists")
            name = Login(username)
            return(name)
        name = Register(username)
        return(name)


        # file = open("users.txt","r")
        # for line in file:
        #     index = line.find("/")
        #     if(line[:index].strip() == username):
        #         print("User already exists")
        #         name = Login(username)
        #         return(name)
        # name = Register(username)
        # file.close()

    elif(choice == "2"):
        os.system("cls")
        resources.line()
        print("\nLOGIN\n")
        resources.line()

        username = input("Enter your username\n")
        sql = 'select `username` from users where `username` = %s'
        entries = a.execute(sql,(username))
        if(entries > 0):
            name = Login(username)
            return(name)

        # file = open("users.txt","r")
        # for line in file:
        #     index = line.find("/")
        #     if(line[:index].strip() == username):
        #         name = Login(username)
        #         return(name)

        else:
            print('User does not exist, Register account')
            time.sleep(1)
            os.system("cls")
            Account()



    else:
        print("Invalid option")
