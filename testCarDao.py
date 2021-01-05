from CarDao import carDao

car1 = {
    'registration': '05-MO-17931',
    'make': 'Toyota',
    'model': 'Highlander',
    'colour': 'Green',
    'mileage': 253789,
    'engineSize': 1.6
}
car2 = {
    'registration': '10-G-2334',
    'make': 'Toyota',
    'model': 'Corolla',
    'colour': 'Green',
    'mileage': 123389,
    'engineSize': 1.3 

}

#returnValue = carDao.create(car)
returnValue = carDao.getAll()
print(returnValue)
returnValue = carDao.findById(car2['registration'])
print("find By Id")
print(returnValue)
returnValue = carDao.update(car2)
print(returnValue)
returnValue = carDao.findById(car2['registration'])
print(returnValue)
returnValue = carDao.delete(car2['registration'])
print(returnValue)
returnValue = carDao.getAll()
print(returnValue)
