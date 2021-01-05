import mysql.connector
import dbconfig as cfg
from mysql.connector import cursor

class PersonDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host =cfg.mysql['host'],
            user=cfg.mysql['username'],
            password =cfg.mysql['password'],
            database=cfg.mysql['database']
        )
        print ("connection made")

    def createP(self, person):
        cursor = self.db.cursor()
        print ("running insert")
        sql = "insert into person (personID, name, age, sex, cregistration, isStudent) values (%s,%s,%s,%s,%s,%s)"
        values = [
            person['personID'],
            person['name'],
            person['age'],
            person['sex'],
            person['cregistration'],
            person['isStudent']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAllP(self):
        cursor = self.db.cursor()
        sql = 'select * from person'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findByIdP(self, personID):
        cursor = self.db.cursor()
        sql = 'select * from person where personID = %s'
        values = [ personID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def updateP(self, person):
       cursor = self.db.cursor()
       sql = "update person set name = %s, age = %s, sex = %s, cregistration = %s, isStudent = %s where personID = %s"
       values = [
           person['name'],
           person['age'],
           person['sex'],
           person['cregistration'],
           person['isStudent'],
           person['personID']

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return person

    def deleteP(self, personID):
       cursor = self.db.cursor()
       sql = 'delete from person where personID = %s'
       values = [personID]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['personID','name', 'age', 'sex', 'cregistration', 'isStudent']
        person = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                person[colName] = value
        return person

personDao = PersonDao()
