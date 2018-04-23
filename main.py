from TaxiClass import Session
import Login
import os
import pymysql
import time

# DATABASE CONNECTION
conn = pymysql.connect(host='127.0.0.1',user='demoo',password='demo1234',db = 'taxidb')
a = conn.cursor()

customer = Login.Account()
os.system("cls")
print("Welcome %s, do you want to pool a taxi or ride solo?\n"%(customer))
choice = input("\n1.Ride solo\n2.Pool\n")

if(choice == "1"):
    print("You're riding solo")
    location = input("Where are you heading to?")

    # file = open("Staff.txt","r")
    # for line in file:
    #     index = line.find("*")
    #     if(line[index+1:].strip() == "0"):
    #         index1 = line.find("/")
    #         Taxi_Number = line[index1+1:index]
    #         Driver = line[:index1]

    sql = 'SELECT * from `staff` where `availability` = 0;'
    a.execute(sql)

    taxi_details = a.fetchone()
    Taxi_Number = taxi_details[1]
    Driver = taxi_details[0]

    transaction = Session(customer,Taxi_Number,Driver,1,location,"r")
    transaction.schedule()


elif(choice == "2"):
    print("You chose to pool")
    location = input("Where are you heading to?")

    sql1 = 'SELECT * from `staff` where `availability` = 0;'
    a.execute(sql1)

    taxi_details = a.fetchone()
    Taxi_Number = taxi_details[1]
    Driver = taxi_details[0]

    transaction = Session(customer,Taxi_Number,Driver,1,location,"p")
    transaction.schedule()
