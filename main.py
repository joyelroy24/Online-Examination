from flask import *
from public import public
from examiner import examiner
from parent import parent
from student import student
from admin	import admin

app=Flask(__name__)
app.secret_key="abcd"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(examiner,url_prefix='/examiner')
app.register_blueprint(parent,url_prefix='/parent')
app.register_blueprint(student,url_prefix='/student')
app.run(debug=True,port="5050")