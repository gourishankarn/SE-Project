from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask import jsonify
from flask import request
from flask import make_response

from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'SE_DB'
app.config["MONGO_URI"] = "mongodb://localhost:27017/SE_DB"
mongo = PyMongo(app)


#not found handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'not found'}),404)


#student related apis

#Add student api
@app.route('/api/v1/student', methods=['POST'])
def add_student():
    _json=request.json
    print(_json)
    _name=_json['name']
    _usn=_json['usn']
    _password=_json['pwd']
    if _name and _usn and _password and request.method=='POST':
        _hashed_password=generate_password_hash(_password)
        print(_hashed_password  )
        id = mongo.db.student.insert({'name': _name, 'usn': _usn, 'pwd': _hashed_password})
        resp = jsonify('student added successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()


#list all student records
@app.route('/api/v1/student',methods=['GET'])
def list_students():
    students=mongo.db.student.find()
    resp=dumps(students)
    return resp


#list specific student
@app.route('/api/v1/student/<id>',methods=['GET'])
def student(id):
    student=mongo.db.student.find_one({'_id':ObjectId(id)})
    resp=dumps(student)
    return resp


#Delete specific Student
@app.route('/api/v1/student/<id>',methods=['DELETE'])
def delete_student(id):
    mongo.db.student.delete_one({'_id':ObjectId(id)})
    resp=jsonify('student deleted successfully')
    resp.status_code=200
    return resp

#Delete all Student
@app.route('/api/v1/student',methods=['DELETE'])
def delete_all_student():
    mongo.db.student.remove({})
    resp=jsonify('All student records are deleted');
    resp.status_code=200
    return resp


#Update Student
@app.route('/api/v1/student',methods=['PUT'])
def update_student():
    _json=request.json
    _id=_json['_id']
    _name = _json['name']
    _usn=_json['usn']
    _password = _json['pwd']
    if _name and _usn and _password and _id and request.method=='PUT':
        _hashed_password=generate_password_hash(_password)
        mongo.db.student.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},{'$set': {'name': _name, 'usn': _usn, 'pwd': _hashed_password}})
        resp = jsonify('User updated successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()



#courses releated apis

#Add course
@app.route('/api/v1/courses', methods=['POST'])
def add_course():
    _json=request.json
    print(_json)
    _cname=_json['coursename']
    _ccode=_json['coursecode']
    _credits=_json['credits']
    if _cname and _ccode and _credits and request.method=='POST':
        id = mongo.db.courses.insert({'coursename': _cname, 'coursecode': _ccode, 'credits': _credits})
        resp = jsonify('course added successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()

#Delete course
@app.route('/api/v1/courses/<id>',methods=['DELETE'])
def delete_course(id):
    mongo.db.courses.delete_one({'_id':ObjectId(id)})
    resp=jsonify('course deleted successfully')
    resp.status_code=200
    return resp


#Delete all courses
@app.route('/api/v1/courses',methods=['DELETE'])
def delete_all_courses():
    mongo.db.courses.remove({})
    resp=jsonify('All Courses are removed')
    resp.status_code=200
    return resp

#Update course
@app.route('/api/v1/courses',methods=['PUT'])
def udate_course():
    _json=request.json
    _id=_json['_id']
    _cname = _json['coursename']
    _ccode=_json['coursecode']
    _credits = _json['credits']
    if _cname and _cname and _credits and _id and request.method=='PUT':
        mongo.db.courses.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},{'$set': {'coursename': _cname, 'coursecode': _ccode, 'credits': _credits}})
        resp = jsonify('course updated successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()

#list all courses
@app.route('/api/v1/courses',methods=['GET'])
def list_course():
    courses=mongo.db.courses.find()
    resp=dumps(courses)
    return resp

#list perticular course
@app.route('/api/v1/courses/<id>',methods=['GET'])
def list_pert_course(id):
    course=mongo.db.courses.find_one({'_id':ObjectId(id)})
    resp=dumps(course)
    return resp




#Faculty apis
#Add Faculty
@app.route('/api/v1/faculty', methods=['POST'])
def add_faculty():
    _json=request.json
    print(_json)
    _name=_json['name']
    _fcode=_json['fcode']
    _email=_json['email']
    _dname=_json['Dname']
    _password=_json['pwd']
    if _name and _fcode and _email and _dname  and _password and request.method=='POST':
        _hashed_password=generate_password_hash(_password)
        print(_hashed_password )
        id = mongo.db.faculty.insert({'name': _name, 'fcode': _fcode,'email':_email,'Dname':_dname, 'pwd': _hashed_password})
        resp = jsonify('Faculty added successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()

#Delete Faculty
@app.route('/api/v1/faculty/<fcode>',methods=['DELETE'])
def delete_faculty(fcode):
    mongo.db.faculty.delete_one({'fcode':ObjectId(fcode)})
    resp=jsonify('faculty deleted successfully')
    resp.status_code=200
    return resp


#Update Faculty
@app.route('/api/v1/faculty',methods=['PUT'])
def update_faculty():
    _json=request.json
    _id=_json['_id']
    _name = _json['name']
    _email=_json['email']
    _dname=_json['Dname']
    _fcode=_json['fcode']
    _password = _json['pwd']
    if _name and _email and _fcode and _id and _password and _dname and request.method=='PUT':
        _hashed_password=generate_password_hash(_password)
        mongo.db.faculty.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},{'$set': {'name': _name, 'fcode': _fcode, 'Dname':_dname,'email':_email, 'pwd': _hashed_password}})
        resp = jsonify('Faculty updated successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()

#list all Faculties
@app.route('/api/v1/faculty',methods=['GET'])
def list_faculties():
    faculty=mongo.db.faculty.find()
    resp=dumps(faculty)
    return resp

#List any specific Faculty
@app.route('/api/v1/faculty/<id>',methods=['GET'])
def list_pert_faculty(id):
    faculty=mongo.db.faculty.find_one({'_id':ObjectId(id)})
    resp=dumps(faculty)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
