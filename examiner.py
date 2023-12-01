from flask import * 
from database import *
  
examiner=Blueprint('examiner',__name__)

@examiner.route('/examiner_home',methods=['get','post'])
def examiner_home():
	name=session['ename']

	return render_template('examiner_home.html',name=name) 

@examiner.route('/examiner_viewexams',methods=['get','post'])
def examiner_viewexams():
	data={}
	myid=session['eid']
	name=session['ename']
	q="select * from exams inner join subjects using(subject_id) inner join courses using(course_id) where examiner_id='%s'"%(myid)
	res=select(q)
	data['exams']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='update':
		q="select * from exams where exam_id='%s'"%(id)
		data['upstatus']=select(q)
	if action=='conducted':
		q="update exams set exam_status='conducted' where exam_id='%s'"%(id)
		update(q)
		return redirect(url_for('examiner.examiner_viewexams'))

	if action=='published':
		q="update exams set exam_status='result published' where exam_id='%s'"%(id)
		update(q)
		return redirect(url_for('examiner.examiner_viewexams'))
	return render_template('examiner_viewexams.html',data=data)

@examiner.route('/examiner_managequest',methods=['get','post'])
def examiner_managequest():
	data={}
	id=request.args['id']
	name=request.args['name']
	if 'submit' in request.form:
		quest=request.form['quest']
		mark=request.form['mark']
		des=request.form['des']
		q="insert into questions values(NULL,'%s','%s','%s','%s')"%(id,quest,mark,des)
		insert(q)
		return redirect(url_for('examiner.examiner_managequest',id=id,name=name))
	q="select * from questions where exam_id='%s'"%(id)
	res=select(q)
	data['quest']=res
	if 'action' in request.args:
		action=request.args['action']
		qid=request.args['qid']
		quest=request.args['quest']
	else:
		action=None
	if action=='delete':
		q="delete from questions where question_id='%s'"%(qid)
		delete(q)
		q="delete from questionanswer where question_id='%s'"%(qid)
		delete(q)
		return redirect(url_for('examiner.examiner_managequest',id=id,name=name))
	return render_template('examiner_managequest.html',id=id,name=name,data=data)

@examiner.route('/examiner_addop',methods=['get','post'])
def examiner_addop():
	data={}
	id=request.args['id']
	name=request.args['name']
	quest=request.args['quest']
	qid=request.args['qid']
	if 'submit' in request.form:
		option=request.form['option']
		status=request.form['status'] 
		q="insert into questionanswer values(NULL,'%s','%s','%s')"%(qid,option,status)
		insert(q)
		return redirect(url_for('examiner.examiner_addop',quest=quest,qid=qid,name=name,id=id))
	q="select * from questionanswer where question_id='%s'"%(qid)
	res=select(q)
	data['option']=res
	if 'action' in request.args:
		oid=request.args['oid']
		q="delete from questionanswer where qstansr_id='%s'"%(oid)
		delete(q)
		return redirect(url_for('examiner.examiner_addop',quest=quest,qid=qid,name=name,id=id))
	return render_template('examiner_addop.html',quest=quest,qid=qid,name=name,id=id,data=data)

@examiner.route('/examiner_viewparticipants',methods=['get','post'])
def examiner_viewparticipants():
	data={}
	myid=session['eid']
	q="SELECT * FROM exams INNER JOIN `subjects` USING (subject_id) INNER JOIN `courses` USING(`course_id`) WHERE examiner_id='%s' AND exam_status NOT IN('Announced','Post Poned')"%(myid)
	data['exams']=select(q)
	print(q)
	print(data['exams'])
	if 'action' in request.args:
		action=request.args['action']
		examid=request.args['examid']
		title=request.args['examname']
		data['title']=title
	else:
		action=None
	if action=='viewstu':
		q="SELECT * FROM result INNER JOIN `exams` USING(`exam_id`) INNER JOIN students USING(student_id)  WHERE exam_id='%s' ORDER BY total_mark DESC"%(examid)
		data['viewstu']=select(q)
		q="select sum(maximum_mark) from questions where exam_id='%s'"%(examid)
		max=select(q)
		data['max']=max[0]['sum(maximum_mark)']
	return render_template('examiner_viewparticipants.html',data=data)
