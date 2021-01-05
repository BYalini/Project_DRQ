import mysql.connector
import dbconfig as cfg
from mysql.connector import cursor

class CarDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host =      cfg.mysql['host'],
            user=       cfg.mysql['username'],
            password=  cfg.mysql['password'],
            database=   cfg.mysql['database']
        )
        #print ("connection made")

    def create(self, car):
        cursor = self.db.cursor()
        print ("running insert")
        sql = "insert into car (registration, make, model, colour, mileage, engineSize ) values (%s,%s,%s,%s,%s,%s)"
        values = [
            car['registration'],
            car['make'],
            car['model'],
            car['colour'],
            car['mileage'],
            car['engineSize']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from car'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, registration):
        cursor = self.db.cursor()
        sql = 'select * from car where registration = %s'
        values = [ registration ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, car):
       cursor = self.db.cursor()
       sql = "update car set make = %s, model = %s, colour = %s, mileage = %s, engineSize = %s where registration = %s"
       values = [
           car['make'],
           car['model'],
           car['colour'],
           car['mileage'],
           car['engineSize'],
           car['registration']

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return car

    def delete(self, registration):
       cursor = self.db.cursor()
       sql = 'delete from car where registration = %s'
       values = [registration]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['registration','make', 'model', 'colour', 'mileage', 'engineSize']
        car = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                car[colName] = value
        return car

carDao = CarDao()
