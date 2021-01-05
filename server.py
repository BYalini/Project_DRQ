from flask import Flask, url_for, request, redirect, abort, jsonify, session
from CarDao import carDao
from PersonDao import personDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')
app.secret_key = 'someSecrtetasdrgsadfgsdfg3ko'

@app.route('/')
def home():
    if not 'username' in session:
        return redirect(url_for('login'))
    
    # return 'welcome ' + session['username'] +\
       #  '<br><a href="'+url_for('logout')+'">logout</a>'
    return redirect('http://127.0.0.1:5000/index.html') 
    #+ session['username']
    #'<br><a href="'+url_for('logout')+'">logout</a>'

@app.route('/login')
def login():
    return '<h1> Click to login</h1> <br/>'+\
        '<button>'+\
            '<a href="'+url_for('proccess_login')+'">' +\
                'login' +\
            '</a>' +\
        '</button>'

@app.route('/processlogin')
def proccess_login():
    #check credentials
    #if bad redirect to login page again

    #else
    session['username']="I dunno"
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))


@app.route('/data')
def getData():
    if not 'username' in session:
        abort(401)
    return '{"data":"all here"}'
    

#get all
#curl http://127.0.0.1:5000/car

@app.route('/car')
def getAll():
    return jsonify(carDao.getAll())
    
@app.route('/person')
def getAllP():
    return jsonify(personDao.getAllP())

# find By id
#curl http://127.0.0.1:5000/car/171-MO-12533

@app.route('/car/<registration>')
def findById(registration):
    return jsonify(carDao.findById(registration))

@app.route('/person/<int:personID>')
def findByIdP(personID):
    return jsonify(personDao.findByIdP(personID))

# create
# curl -X POST -d "{\"registration\":\"171-G-395\", \"make\":\"Ford\", \"model\":\"Ka\", \"colour\":\"Silver\", \"mileage\":125882, \"engineSize\":1.0}" -H Content-Type:application/json http://127.0.0.1:5000/car
@app.route('/car', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)

    car = {
        "registration": request.json["registration"],
        "make": request.json["make"],
        "model": request.json["model"],
        "colour": request.json["colour"],
        "mileage": request.json["mileage"],
        "engineSize": request.json["engineSize"]

    }
    return jsonify(carDao.create(car))
    #return "served by Create "

#create person
@app.route('/person', methods=['POST'])
def createP():
   
    if not request.json:
        abort(400)

    person = {
        "personID": request.json["personID"],
        "name": request.json["name"],
        "age": request.json["age"],
        "sex": request.json["sex"],
        "cregistration": request.json["cregistration"],
        "isStudent": request.json["isStudent"]

    }
    return jsonify(personDao.createP(person))

#
#update
# curl -X PUT -d "{\"make\":\"test\", \"model\":\"Ka\", \"colour\":\"Black\"}" -H Content-Type:application/json http://127.0.0.1:5000/car/05-MO-17931


@app.route('/car/<registration>', methods=['PUT'])
def update(registration):
    foundCar=carDao.findById(registration)
    print (foundCar)
    if foundCar == {}:
        return jsonify({}), 404
    currentCar = foundCar
    if 'make' in request.json:
        currentCar['make'] = request.json['make']
    if 'model' in request.json:
        currentCar['model'] = request.json['model']
    if 'colour' in request.json:
        currentCar['colour'] = request.json['colour']
    if 'mileage' in request.json:
        currentCar['mileage'] = request.json['mileage']
    if 'engineSize' in request.json:
        currentCar['engineSize'] = request.json['engineSize']
    carDao.update(currentCar)

    return jsonify(currentCar)

#update person
@app.route('/person/<int:personID>', methods=['PUT'])
def updateP(personID):
    foundPerson=personDao.findByIdP(personID)
    print (foundPerson)
    if foundPerson == {}:
        return jsonify({}), 404
    currentPerson = foundPerson
    if 'name' in request.json:
        currentPerson['name'] = request.json['name']
    if 'age' in request.json:
        currentPerson['age'] = request.json['age']
    if 'sex' in request.json:
        currentPerson['sex'] = request.json['sex']
    if 'cregistration' in request.json:
        currentPerson['cregistration'] = request.json['cregistration']
    if 'isStudent' in request.json:
        currentPerson['isStudent'] = request.json['isStudent']
    personDao.updateP(currentPerson)

    return jsonify(currentPerson)
#
#delete
# curl -X DELETE http://127.0.0.1:5000/car/171-MO-12533


@app.route('/car/<registration>', methods=['DELETE'])
def delete(registration):
    carDao.delete(registration)

    return jsonify({"done": True})

#delete person
@app.route('/person/<int:personID>', methods=['DELETE'])
def deleteP(personID):
    personDao.deleteP(personID)

    return jsonify({"done": True})

if __name__ == "__main__":
    app.run(debug=True)
