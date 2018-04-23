import resources
import datetime
import pymysql

conn = pymysql.connect(host='127.0.0.1',user='demoo',password='demo1234',db = 'taxidb')
a = conn.cursor()

class Session:
    def __init__(self,customer_name,Taxi_Number,Driver,Number_of_seats,location,mode):
        self.name = customer_name
        self.regno = Taxi_Number
        self.num = Number_of_seats
        self.location = location
        self.driver = Driver
        self.mode = mode

    def schedule(self):
        self.time = len(self.location)

        if(self.mode == "r"):
            print("You Driver is %s and you Taxi Number is %s"%(self.driver,self.regno))
            resources.Timer(self.time)

        timee=datetime.datetime.now().time()
        date=datetime.datetime.now().date()
        self.timestamp = "%s:%s|%s %s %s"%(timee.hour,timee.minute,date.day,date.month,date.year)

        sql = 'insert into log(timestamp,name,location,seats,taxino,driver,mode) values(%s,%s,%s,%s,%s,%s,%s)'

        a.execute(sql,(self.timestamp,self.name,self.location,self.num,self.regno,self.driver,self.mode))


        if(self.mode == "p"):
            sql = 'select `name` from log where `name` != %s and `location` = %s and `mode` =%s'
            countrow = a.execute(sql,(self.name,self.location,self.mode))
            if(countrow > 0):
                print("You'll be pooling with,")
                for i in range(countrow):
                    data = a.fetchone()
                    print(data[0])
                resources.Timer(self.time)
            else:
                print("You're riding solo, your Driver is %s and you Taxi Number is %s"%(self.driver,self.regno))
                resources.Timer(self.time)




        conn.commit()
        conn.close()





        # record = self.timestamp+"/"+self.name+"/"+self.location+"/"+str(self.num)+"/"+self.regno+"/"+self.driver
        #
        # file = open("log.txt","a")
        # file.write(record+"\n")
