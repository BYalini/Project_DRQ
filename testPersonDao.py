from PersonDao import personDao

person1 = {
    'personID': '1',
    'name': 'John',
    'age': '23',
    'sex': 'M',
    'cregistration': 'GH2000-01-01',
    'isStudent':1
}
person2 = {
    'personID': '2',
    'name': 'Tom',
    'age': '64',
    'sex': 'M',
    'cregistration': '2000-HG01-01',
    'isStudent':0
}

#returnValue = personDao.create(person)
returnValue = personDao.getAllP()
print(returnValue)
returnValue = personDao.findByIdP(person2['personID'])
print("find By Id")
print(returnValue)
returnValue = personDao.updateP(person2)
print(returnValue)
returnValue = personDao.findByIdP(person2['personID'])
print(returnValue)
returnValue = personDao.deleteP(person2['personID'])
print(returnValue)
returnValue = personDao.getAllP()
print(returnValue)
