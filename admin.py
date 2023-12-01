from flask import *
from database import *

admin=Blueprint('admin',__name__)
 
@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')

@admin.route('/admin_manage_course',methods=['get','post'])
def admin_manage_course():
	data={}
	q="select* from courses"
	res=select(q)
	if res:
		data['courses']=res
	if 'submit' in request.form:
		course=request.form['course']
		q="select * from courses where course_name='%s'"%(course)
		res=select(q)
		if res:
			flash(course+'  is'+'  already added')
			return redirect(url_for('admin.admin_manage_course'))
		else:
			q="insert into courses values(NULL,'%s')"%(course)
			insert(q)
			return redirect(url_for('admin.admin_manage_course'))
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from courses where course_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_course'))
	if action=='update':
		q="select * from courses where course_id='%s'"%(id)
		res=select(q)
		data['updater']=res
	if 'update' in request.form:
		upcourse=request.form['upcourse']
		q="update courses set course_name='%s' where course_id='%s'"%(upcourse,id)
		update(q)
		return redirect(url_for('admin.admin_manage_course'))
	return render_template('admin_manage_course.html',data=data)

@admin.route('/admin_manage_subjects',methods=['get','post'])
def admin_manage_subjects():
	data={}
	cname=request.args['cname']
	data['cname']=cname
	cid=request.args['cid']
	data['cid']=cid
	q="select * from subjects where course_id='%s'"%(cid)
	res=select(q)
	if res:
		data['subjects']=res
	if 'submit' in request.form:
		subject=request.form['subject']
		q="select * from subjects where course_id='%s' and subject_name='%s'"%(cid,subject)
		res=select(q)
		if res:
			flash(subject+" is already added")
		else:
			q="insert into subjects values(NULL,'%s','%s')"%(cid,subject)
			insert(q)
			return redirect(url_for('admin.admin_manage_subjects',cid=cid,cname=cname))
	if 'action' in request.args:
		action=request.args['action']
		sid=request.args['sid']
		sname=request.args['sname']
		data['sname']=sname
	else:
		action=None
	if action=='delete':
		q="delete from subjects where subject_id='%s'"%(sid)
		delete(q)
		return redirect(url_for('admin.admin_manage_subjects',cname=cname,cid=cid))
	if action=='update':
		q="select * from subjects where subject_id='%s'"%(sid)
		res=select(q)
		data['updater']=res
	if 'update' in request.form:
		upsubject=request.form['upsubject']
		q="update subjects set subject_name='%s' where subject_id='%s'"%(upsubject,sid)
		update(q)
		return redirect(url_for('admin.admin_manage_subjects',cname=cname,cid=cid))
	return render_template('admin_manage_subjects.html',data=data)

@admin.route('/admin_manage_examiner',methods=['get','post'])
def admin_manage_examiner():
	data={}
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		qua=request.form['qua']
		ph=request.form['ph']
		email=request.form['email']
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where user_name='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			flash("user name and password already taken by another user")
			return redirect(url_for('admin.admin_manage_examiner'))
		else:
			q="insert into login values(NULL,'%s','%s','examiner')"%(uname,password)
			res=insert(q)
			q="insert into examiner values(NULL,'%s','%s','%s','%s','%s','%s')"%(res,fname,lname,qua,ph,email)
			insert(q)
	q="select * from examiner inner join login using(login_id)"
	res=select(q)
	data['examiner']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete login,examiner from examiner inner join login on login.login_id=examiner.login_id where login.login_id='%s' "%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_examiner'))
	if action=='update':
		q="select * from examiner where login_id='%s'"%(id)
		res=select(q)
		data['updater']=res
	if 'update' in request.form:
		fname=request.form['upfname']
		lname=request.form['uplname']
		qua=request.form['upqua']
		ph=request.form['upph']
		email=request.form['upemail']
		q="update examiner set first_name='%s',last_name='%s',qualification='%s',phone='%s',email='%s' where login_id='%s'"%(fname,lname,qua,ph,email,id)
		print(q)
		update(q)
		return redirect(url_for('admin.admin_manage_examiner'))
	return render_template('admin_manage_examiner.html',data=data)

@admin.route('/admin_manage_exam',methods=['get','post'])
def admin_manage_exam():
	data={}
	q="select * from subjects"
	res=select(q)
	data['subject']=res
	q="select * from examiner"
	res=select(q)
	data['examiner']=res
	if 'submit' in request.form:
		title=request.form['title']
		details=request.form['details']
		subid=request.form['subject']
		examiner_id=request.form['examiner']
		examdate=request.form['date']
		examfee=request.form['examfee']
		q="insert into exams values(NULL,'%s','%s','%s','%s','%s','%s','Announced')"%(title,details,subid,examiner_id,examdate,examfee)
		insert(q)
	q="SELECT * FROM exams INNER JOIN subjects USING(subject_id) INNER JOIN examiner USING(examiner_id) INNER JOIN courses USING(course_id)"
	res=select(q)
	data['exams']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from exams where exam_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_exam'))
	if action=='update':
		q="select * from exams inner join subjects using(subject_id) where exam_id='%s'"%(id)
		res=select(q)
		data['updater']=res		
	if 'update' in request.form:
		detail=request.form['updetails']
		examiner=request.form['upexaminer']
		date=request.form['update']
		status=request.form['upstatus']
		q="update exams set exam_details='%s',examiner_id='%s',exam_date='%s',exam_status='%s' where exam_id='%s'"%(detail,examiner,date,status,id)
		update(q)
		return redirect(url_for('admin.admin_manage_exam'))
	if 'action2' in request.args:
		action2=request.args['action2']
		id=request.args['id']
		data['title']=request.args['examtitle']
		q="SELECT * FROM payment INNER JOIN `students` USING(student_id) WHERE exam_id='%s'"%(id)
		data['students']=select(q)
	return render_template('admin_manage_exam.html',data=data)

@admin.route('/admin_viewreults',methods=['get','post'])
def admin_viewreults():
	data={}
	q="SELECT * FROM exams INNER JOIN subjects USING(subject_id) INNER JOIN examiner USING(examiner_id) INNER JOIN courses USING(course_id) WHERE exams.`exam_status`='result published'"
	res=select(q)
	data['exams']=res
	if 'action' in request.args:
		action=request.args['action']
		examid=request.args['id']
		title=request.args['examtitle']
		data['title']=title
	else:
		action=None
	if action=='viewstu':
		q="SELECT * FROM result INNER JOIN `exams` USING(`exam_id`) INNER JOIN students USING(student_id)  WHERE exam_id='%s' ORDER BY total_mark DESC"%(examid)
		data['viewstu']=select(q)
		q="select sum(maximum_mark) from questions where exam_id='%s'"%(examid)
		max=select(q)
		data['max']=max[0]['sum(maximum_mark)']
	return render_template('admin_viewreults.html',data=data)