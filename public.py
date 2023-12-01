from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():
	return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where user_name='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['user_type']=='admin':
				return redirect(url_for('admin.adminhome'))
			if res[0]['user_type']=='parent':
				q="select * from parents inner join login using(login_id) where login_id='%s'"%(session['lid'])
				res=select(q)
				session['pid']=res[0]['parent_id']
				session['pname']=res[0]['first_name']
				return redirect(url_for('parent.phome'))
			if res[0]['user_type']=='examiner':
				q="select * from login inner join examiner using(login_id) where login_id='%s'"%(session['lid'])
				res=select(q)
				session['eid']=res[0]['examiner_id']
				session['ename']=res[0]['first_name']+" "+res[0]['last_name']
				return redirect(url_for('examiner.examiner_home'))
			if res[0]['user_type']=='student':
				q="select * from login inner join students using(login_id) where login_id='%s'"%(session['lid'])
				res=select(q)
				session['sid']=res[0]['student_id']
				session['sname']=res[0]['first_name']+" "+res[0]['last_name']
				return redirect(url_for('student.student_home'))
		else:
			flash("COMPLETE YOUR REGISTRATION BEFORE LOGIN")
	return render_template('login.html')

@public.route('/preg',methods=['get','post'])
def preg():
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		dob=request.form['dob']
		ph=request.form['ph']
		email=request.form['email']
		hname=request.form['hname']
		place=request.form['place']
		pin=request.form['pin']
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where user_name='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			flash("THIS USER NAME AND PASSWORD ARE ALREADY TAKEN BY OTHER USER")
			return redirect(url_for('public.preg'))
		else:
			q="insert into login values(NULL,'%s','%s','parent')"%(uname,password)
			res=insert(q)
			q="insert into parents values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(res,fname,lname,dob,ph,email,hname,place,pin)
			print(q)
			insert(q)
			return redirect(url_for('public.preg'))
	return render_template('preg.html')