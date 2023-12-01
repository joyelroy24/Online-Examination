from flask import *
from database import *
parent=Blueprint('parent',__name__)

@parent.route('/phome',methods=['get','post'])
def phome():
	data={}
	pname=session['pname']
	data['pname']=pname
	pid=session['pid']
	data['pid']=pid
	return render_template('phome.html',data=data)

@parent.route('/pmanage_students',methods=['get','post'])
def pmanage_students():
	data={}
	pid=session['pid']
	q="select * from courses"
	res=select(q)
	data['course']=res
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		dob=request.form['dob']
		ph=request.form['ph']
		course=request.form['course']
		uname=request.form['uname']
		password=request.form['password']
		email=request.form['email']
		q="select * from login where user_name='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			flash("THIS USER NAME AND PASSWORD ARE ALREADY TAKEN BY OTHER USER")
		else:
			q="insert into login values(NULL,'%s','%s','student')"%(uname,password)
			res=insert(q)
			q="insert into students values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(pid,res,course,fname,lname,dob,ph,email)
			insert(q)
			return redirect(url_for('parent.pmanage_students'))
	q="select * from students inner join courses using(course_id) where parent_id='%s'"%(pid)
	res=select(q)
	data['student']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete login,students from students inner join login on students.login_id=login.login_id where students.student_id='%s'"%(id)
		delete(q)
		return redirect(url_for('parent.pmanage_students'))
	if action=='update':
		q="select * from students inner join courses using(course_id) where student_id='%s'"%(id)
		res=select(q)
		data['updater']=res
	if 'update' in request.form:
		fname=request.form['upfname']
		lname=request.form['uplname']
		ph=request.form['upph']
		email=request.form['upemail']
		course=request.form['course']
		dob=request.form['update']
		q="update students set first_name='%s',last_name='%s',phone='%s',email='%s',dob='%s',course_id='%s' where student_id='%s'"%(fname,lname,ph,email,dob,course,id)
		print(q)
		update(q)
		return redirect(url_for('parent.pmanage_students'))
	return render_template('pmanage_students.html',data=data)

@parent.route('/pview_examshedule',methods=['get','post'])
def pview_examshedule():
	data={}
	pid=session['pid']
	q="select * from students inner join courses using(course_id) where parent_id='%s'"%(pid)
	res=select(q)
	data['student']=res
	if 'action' in request.args:
		action=request.args['action']
		sid=request.args['sid']
		cid=request.args['cid']
	else:
		action=None	
	if action=='exam':
		q="SELECT *,examiner.`first_name` AS examinerfname FROM exams INNER JOIN examiner USING(examiner_id) INNER JOIN subjects USING(subject_id) INNER JOIN courses USING(course_id) INNER JOIN students USING(course_id) WHERE students.course_id='%s' and students.student_id='%s' and  exams.exam_status in('Announced','Post Poned')"%(cid,sid)
		res=select(q)
		data['exam']=res
	if 'action2' in request.args:
		action2=request.args['action2']
		examid=request.args['examid']
		sid=request.args['sid']
		fee=request.args['fee']
		cid=request.args['cid']
	else:
		action2=None
	if action2=='register':
		q="select * from payment where exam_id='%s' and student_id='%s'"%(examid,sid)
		res=select(q)
		if res:
			flash("YOU ALREADY REGISTERD")
			return redirect(url_for('parent.pview_examshedule',action='exam',sid=sid,cid=cid))
		else:
			data['pay']=fee
	if 'pay' in request.form:
		q="insert into payment values(NULL,'%s','%s','%s')"%(examid,sid,fee)
		insert(q)
		flash("sucessfully registered")
		return redirect(url_for('parent.pview_examshedule',action='exam',sid=sid,cid=cid))
	return render_template('pview_examshedule.html',data=data)

@parent.route('/pview_results',methods=['get','post'])
def pview_results():
	data={}
	pid=session['pid']
	q="select * from students inner join courses using(course_id) where parent_id='%s'"%(pid)
	res=select(q)
	data['student']=res
	if 'action' in request.args:
		sid=request.args['sid']
		data['sid']=sid
		name=request.args['name']
		data['name']=name
		q="select * from exams inner join examiner using(examiner_id) inner join subjects using(subject_id) inner join payment using(exam_id) where student_id='%s'"%(sid)
		res=select(q)
		print(res)
		if res:
			data['reg']=res
	if 'action2' in request.args:
		examid=request.args['examid']
		q="SELECT *,SUM(`maximum_mark`) FROM `questions` WHERE exam_id='%s'"%(examid)
		res=select(q)
		data['total']=res[0]['SUM(`maximum_mark`)']
		sid=request.args['sid']
		name=request.args['name']
		data['name']=name
		q="select * from result where exam_id='%s' and student_id='%s'"%(examid,sid)
		res=select(q)
		if res:
			data['result']=res
	return render_template('pview_results.html',data=data)