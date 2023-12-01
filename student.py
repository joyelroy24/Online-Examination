from flask import *
from database import *
student=Blueprint('student',__name__)

@student.route('/student_home',methods=['get','post'])
def student_home(): 
	sid=session['sid']
	sname=session['sname']
	return render_template('student_home.html',sname=sname)

@student.route('/student_viewexamshedules',methods=['get','post'])
def student_viewexamshedules():
	data={}
	sid=session['sid']
	q="SELECT *,examiner.`first_name` AS examinerfname FROM exams INNER JOIN examiner USING(examiner_id) INNER JOIN subjects USING(subject_id) INNER JOIN courses USING(course_id) INNER JOIN payment USING(exam_id) WHERE payment.`student_id`='%s' and exams.exam_status='Announced'"%(sid)
	res=select(q)
	if res:
		data['exam']=res
	if 'action' in request.args:
		examid=request.args['examid']
		q="select * from participation where student_id='%s' and exam_id='%s' "%(sid,examid)
		res=select(q)
		if res:
			flash('YOU ALREADY ATTENDED THIS EXAM')
		else:	
			return redirect(url_for('student.student_participateexam',examid=examid))
	return render_template('student_viewexamshedules.html',data=data)

@student.route('/student_participateexam',methods=['get','post'])
def student_participateexam():
	data={}
	data['sec']=10
	data['min']=0
	sid=session['sid']
	examid=request.args['examid']

	def pre(preid,qone):
		global pid
		pid=preid
		qone=qone
		print("juygjug")
		q="select `question_id` from questions where question_id='%s' and exam_id='%s'"%(pid,examid)
		res=select(q)
		if res:
			q="select * from answers where student_id='%s' and qstansr_id in(select qstansr_id from questionanswer where question_id='%s')"%(sid,pid)
			added=select(q)	
			print(added)		
			data['added']=added
			q="SELECT * FROM `questionanswer` inner join questions using(question_id) WHERE `questionanswer`.`question_id`='%s'"%(res[0]['question_id'])
			print(q)
			res=select(q)
			print(res)
			data['pre']=res
		else:
			pid=int(pid)-1
			if pid<int(qone):
				pass
			else:
				pre(pid,qone)

	def next(nextid,last):
		global nid
		nid=nextid
		last=last
		q="select * from questions where question_id='%s' and exam_id='%s'"%(nid,examid)
		res=select(q)
		if res:
			q="select * from answers where student_id='%s' and qstansr_id in(select qstansr_id from questionanswer where question_id='%s')"%(sid,nid)
			added=select(q)	
			print("addednnnnnnnnnnnnnnnnnnnnnnnnnn",added)		
			data['added']=added
			q="SELECT * FROM `questionanswer` INNER JOIN `questions` USING(`question_id`) WHERE `questionanswer`.`question_id`='%s'"%(res[0]['question_id'])
			res=select(q)
			data['next']=res
		else:
			nid=int(nid)+1
			if nid>int(last):
				pass
			else:
				next(nid,last)
	# q="SELECT * FROM questions INNER JOIN `questionanswer` USING(`question_id`) WHERE `questions`.`exam_id`='%s'"%(exam_id)
	q="SELECT `question_id` FROM `questions` INNER JOIN exams USING (exam_id) WHERE `exams`.`exam_id`='%s' order by question_id"%(examid)	
	
	qid=select(q)	

	if qid:
		data['m']='5'
		data['s']='30'
		qone=qid[0]['question_id']
		print(qone)
		data['qone']=qone
		last=qid[-1]['question_id']
		data['last']=last
		q="SELECT * FROM `questionanswer` INNER JOIN `questions` USING(`question_id`) WHERE `questionanswer`.`question_id`='%s'"%(qone)
		data['qno']=1
		data['1q']=select(q)
		q="select * from answers where student_id='%s' and qstansr_id in(select qstansr_id from questionanswer where question_id='%s')"%(sid,qone)
		added=select(q)	
		print(added)		
		data['added']=added

		
	if 'action' in request.args:
		data['qno']=request.args['qno']
		data['qno']=int(data['qno'])+1
		action=request.args['action']
		nextid=request.args['nid']
		next(nextid,last)
	else:
		action=None
	if 'action2' in request.args:
		data['qno']=request.args['qno']
		data['qno']=int(data['qno'])-1
		action=request.args['action2']
		preid=request.args['pid']
		pre(preid,qone)
		print("gyh")
	else:
		action=None
	if 'submit' in request.form:
		anss=request.form['anss']

		print("...................."+anss)
		if anss:
			ans=request.form['ans']
			q="SELECT * FROM questionanswer INNER JOIN  questions USING(`question_id`) WHERE questions.question_id='%s' AND `questionanswer`.`qstansr_id`='%s'"%(qone,ans)		
			res=select(q)
			if res:
				if res[0]['status']=='true':
					q="select * from answers where student_id='%s' and qstansr_id in(select qstansr_id from questionanswer where question_id='%s')"%(sid,qone)
					res1=select(q)
					
					print(q)
					if res1:
						curans_id=res1[0]['qstansr_id']
						q="update answers set mark_awarded='%s',qstansr_id='%s' where qstansr_id='%s' and student_id='%s'"%(res[0]['maximum_mark'],ans,curans_id,sid)
						print(q)
						update(q)
						return redirect(url_for('student.student_participateexam',examid=examid))
					else:

						q="insert into answers values(NULL,'%s','%s','%s')"%(ans,sid,res[0]['maximum_mark'])
						insert(q)
						return redirect(url_for('student.student_participateexam',examid=examid))

				else:
					q="select * from answers where student_id='%s' and qstansr_id in(select qstansr_id from questionanswer where question_id='%s')"%(sid,qone)
					res1=select(q)
					
					print(q)
					if res1:
						curans_id=res1[0]['qstansr_id']
						q="update answers set mark_awarded=0,qstansr_id='%s' where qstansr_id='%s' and student_id='%s'"%(ans,curans_id,sid)
						update(q)
						return redirect(url_for('student.student_participateexam',examid=examid))
					else:
						q="insert into answers values(NULL,'%s','%s',0)"%(ans,sid)
						insert(q)
						return redirect(url_for('student.student_participateexam',examid=examid))
	if 'nxtsubmit' in request.form:
		anss=request.form['anss']

		print("...................."+anss)
		if anss:
			ans=request.form['ans']
		
			print(ans)
			q="SELECT * FROM questionanswer INNER JOIN  questions USING(`question_id`) WHERE questions.question_id='%s' AND `questionanswer`.`qstansr_id`='%s'"%(nid,ans)
			print(q)
			res=select(q)
			print(res)
			if res:
				if res[0]['status']=='true':
					print(res,"77777777777")
					q="select * from answers where student_id='%s' and qstansr_id in(select qstansr_id from questionanswer where question_id='%s')"%(sid,nid)
					print(q)
					res1=select(q)
					# print(res1)
					if res1:
						curans_id=res1[0]['qstansr_id']
						print(q)
						q="update answers set mark_awarded='%s',qstansr_id='%s' where qstansr_id='%s' and student_id='%s'"%(res[0]['maximum_mark'],ans,curans_id,sid)
						update(q)
						return redirect(url_for('student.student_participateexam',action='next',nid=nid,examid=examid,qno=data['qno']-1))
					else:
						q="insert into answers values(NULL,'%s','%s','%s')"%(ans,sid,res[0]['maximum_mark'])
						insert(q)
						return redirect(url_for('student.student_participateexam',action='next',nid=nid,examid=examid,qno=data['qno']-1))

				else:
					q="select * from answers where student_id='%s' and qstansr_id in(select qstansr_id from questionanswer where question_id='%s')"%(sid,nid)
					print(q)
					res1=select(q)
					print(res1)	
					if res1:
						curans_id=res1[0]['qstansr_id']
						print(curans_id)
						q="update answers set mark_awarded=0,qstansr_id='%s' where qstansr_id='%s' and student_id='%s'"%(ans,curans_id,sid)
						res=update(q)
						print(res)
						return redirect(url_for('student.student_participateexam',action='next',nid=nid,examid=examid,qno=data['qno']-1))
					else:
						q="insert into answers values(NULL,'%s','%s',0)"%(ans,sid)
						insert(q)
						return redirect(url_for('student.student_participateexam',action='next',nid=nid,examid=examid,qno=data['qno']-1))
	if 'presubmit' in request.form:
		anss=request.form['anss']

		print("...................."+anss)
		if anss:
			ans=request.form['ans']
			ans=request.form['ans']
			q="SELECT * FROM questionanswer INNER JOIN  questions USING(`question_id`) WHERE questions.question_id='%s' AND `questionanswer`.`qstansr_id`='%s'"%(pid,ans)
		
			res=select(q)
			if res:
				if res[0]['status']=='true':
					q="select * from answers where student_id='%s' and qstansr_id in(select qstansr_id from questionanswer where question_id='%s')"%(sid,pid)
					res1=select(q)
					
					if res1:
						curans_id=res1[0]['qstansr_id']
						q="update answers set mark_awarded='%s',qstansr_id='%s' where qstansr_id='%s' and student_id='%s'"%(res[0]['maximum_mark'],ans,curans_id,sid)
						update(q)
						return redirect(url_for('student.student_participateexam',action2='pre',pid=pid,examid=examid,qno=data['qno']+1))

					else:
						q="insert into answers values(NULL,'%s','%s','%s')"%(ans,sid,res[0]['maximum_mark'])
						insert(q)
						return redirect(url_for('student.student_participateexam',action2='pre',pid=pid,examid=examid,qno=data['qno']+1))
				else:

					q="select * from answers where student_id='%s' and qstansr_id in(select qstansr_id from questionanswer where question_id='%s')"%(sid,pid)
					
					res1=select(q)
					
					if res1:
						curans_id=res1[0]['qstansr_id']
						q="update answers set mark_awarded=0,qstansr_id='%s' where qstansr_id='%s' and student_id='%s'"%(ans,curans_id,sid)
						update(q)
						return redirect(url_for('student.student_participateexam',action2='pre',pid=pid,examid=examid,qno=data['qno']+1))
					else:
						q="insert into answers values(NULL,'%s','%s',0)"%(ans,sid)
						insert(q)
						return redirect(url_for('student.student_participateexam',action2='pre',pid=pid,examid=examid,qno=data['qno']+1))
	if 'complete' in request.form:
		q="SELECT SUM(mark_awarded) FROM answers WHERE student_id='%s' AND qstansr_id IN(SELECT qstansr_id FROM questionanswer WHERE question_id IN (SELECT question_id FROM questions WHERE exam_id='%s'))"%(sid,examid)
		res=select(q)
		print(res)
		if res:
			result=res[0]['SUM(mark_awarded)']
			q="insert into result values(NULL,'%s','%s','%s')"%(examid,sid,result)
			insert(q)
			q="insert into participation values(NULL,'%s','%s')"%(examid,sid)
			insert(q)
		return redirect(url_for('student.student_viewexamshedules'))
	return render_template('student_participateexam.html',data=data,examid=examid)

@student.route('student_viewresults',methods=['get','post'])
def student_viewresults():
	data={}
	sid=session['sid']
	q="SELECT *,examiner.`first_name` AS examinerfname FROM exams INNER JOIN examiner USING(examiner_id) INNER JOIN subjects USING(subject_id) INNER JOIN courses USING(course_id) INNER JOIN participation USING(exam_id) WHERE participation.student_id='%s' AND exams.exam_status NOT IN('Announced')"%(sid)
	print(q)
	res=select(q)
	data['exams']=res
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['examid']
		name=request.args['examname']
		data['name']=name
	else:
		action=None
	if action=='result':
		q="SELECT *,SUM(`maximum_mark`) FROM `questions` WHERE exam_id='%s'"%(id)
		res=select(q)
		data['total']=res[0]['SUM(`maximum_mark`)']
		q="select * from result where exam_id='%s' and student_id='%s'"%(id,sid)
		data['result']=select(q)
	return render_template('student_viewresults.html',data=data)