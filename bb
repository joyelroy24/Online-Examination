<!DOCTYPE html>

<html> 
	<head> 
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Learn &mdash; Free Website Template, Free HTML5 Template by freehtml5.co</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Free HTML5 Website Template by freehtml5.co" />
	<meta name="keywords" content="free website templates, free html5, free template, free bootstrap, free website template, html5, css3, mobile first, responsive" />
	<meta name="author" content="freehtml5.co" />

	<!-- 
	//////////////////////////////////////////////////////

	FREE HTML5 TEMPLATE 
	DESIGNED & DEVELOPED by FreeHTML5.co
		
	Website: 		http://freehtml5.co/
	Email: 			info@freehtml5.co
	Twitter: 		http://twitter.com/fh5co
	Facebook: 		https://www.facebook.com/fh5co

	//////////////////////////////////////////////////////
	 -->

  	<!-- Facebook and Twitter integration -->
	<meta property="og:title" content=""/>
	<meta property="og:image" content=""/>
	<meta property="og:url" content=""/>
	<meta property="og:site_name" content=""/>
	<meta property="og:description" content=""/>
	<meta name="twitter:title" content="" />
	<meta name="twitter:image" content="" />
	<meta name="twitter:url" content="" />
	<meta name="twitter:card" content="" />

	<link href="https://fonts.googleapis.com/css?family=Work+Sans:300,400,500,700,800" rel="stylesheet">
	
	<!-- Animate.css -->
	<link rel="stylesheet" href="/static/css/animate.css">
	<!-- Icomoon Icon Fonts-->
	<link rel="stylesheet" href="/static/css/icomoon.css">
	<!-- Bootstrap  -->
	<link rel="stylesheet" href="/static/css/bootstrap.css">

	<!-- Magnific Popup -->
	<link rel="stylesheet" href="/static/css/magnific-popup.css">

	<!-- Owl Carousel  -->
	<link rel="stylesheet" href="/static/css/owl.carousel.min.css">
	<link rel="stylesheet" href="/static/css/owl.theme.default.min.css">

	<!-- Theme style  -->
	<link rel="stylesheet" href="/static/css/style.css">

	<!-- Modernizr JS -->
	<script src="/static/js/modernizr-2.6.2.min.js"></script>
	<!-- FOR IE9 below -->
	<!--[if lt IE 9]>
	<script src="js/respond.min.js"></script>
	<![endif]-->
	<script type="text/javascript">
		$(document).ready(function(){
		$('submit').click(function(event){
			event.preventDefault();
			var	sec = $('sec').val();
			var	min = $('min').val();
			$.ajax({
			    type: "POST",
			    url: "student_participateexam",
			    data: { min:min, sec:sec},		    
			    dataType: "json",
			    success: function(result){
			        			    }
			});
		});
	});

	</script>


	 <script language ="javascript" >
	 	$(function() {
        $("input[name='min']").on('input', function(e) {
            alert("Haiiii");

        });
    		}
	 	
        var tim;
        alert("Fgh");
        var min = document.getElementById("min").value;
        alert(min);
        var sec = document.getElementById("sec").value;

        var f = new Date();
        function f1() {
            f2();
            document.getElementById("starttime").innerHTML = "Your started your Exam at " + f.getHours() + ":" + f.getMinutes();
             
          
        }
        function f2() {
            if (parseInt(sec) > 0) {
                sec = parseInt(sec) - 1;
                document.getElementById("showtime").innerHTML = "Your Left Time  is :"+min+" Minutes ," + sec+" Seconds";
                document.getElementById("mins").value = min;
                document.getElementById("secs").value=sec;
                tim = setTimeout("f2()", 1000);

            }
            else {
                if (parseInt(sec) == 0) {
                    min = parseInt(min) - 1;
                    if (parseInt(min) == -1) {
                        clearTimeout(tim);
                        location.href = "student_viewexamshedules";
                    }
                    else {
                        sec = 60;
                        document.getElementById("showtime").innerHTML = "Your Left Time  is :" + min + " Minutes ," + sec + " Seconds";
                        document.getElementById("mins").value= min;
                        document.getElementById("secs").value=sec;
                        tim = setTimeout("f2()", 1000);
                    }
                }
               
            }
        }
    </script>
  

	</head>



<body >
	<div class="fh5co-loader"></div>
	
	<div id="page">
	<nav class="fh5co-nav" role="navigation">
		<div class="top">
			<div class="container">
				<div class="row">
					<div class="col-xs-12 text-right">
						<p class="num">Call: +01 123 456 7890</p>
						<ul class="fh5co-social">
							<li><a href="#"><i class="icon-twitter"></i></a></li>
							<li><a href="#"><i class="icon-dribbble"></i></a></li>
							<li><a href="#"><i class="icon-github"></i></a></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<div class="top-menu">
			<div class="container">
				<div class="row">
					<div class="col-xs-1">
						<div id="fh5co-logo"><a href="index.html">Learn<span>.</span></a></div>
					</div>
					<div class="col-xs-11 text-right menu-1">
						<ul>
							<li class="active"><a href="student_home">HOME</a></li>
							<li><a href="student_viewexamshedules">VIEW EXAMS TO ATTEND</a></li>
							<li><a href="student_viewresults">VIEW RESULTS</a></li>
							<!-- <li><a href="admin_manage_exam">MANGE EXAMS</a></li>
							<li><a href="admin_viewreults">VIEW REULTS</a></li> -->
							<!-- <li class="has-dropdown">
								<a href="blog.html">Blog</a>
								<ul class="dropdown">
									<li><a href="#">Web Design</a></li>
									<li><a href="#">eCommerce</a></li>
									<li><a href="#">Branding</a></li>
									<li><a href="#">API</a></li>
								</ul>
							</li> -->
							<!-- <li><a href="contact.html">Contact</a></li> -->
							<li class="btn-cta"><a href="/"><span>LOGOUT</span></a></li>
							<!-- <li class="btn-cta"><a href="#"><span>Create a Course</span></a></li> -->
						</ul>
					</div>
				</div>

			</div>
		</div>
	</nav>

	<header id="fh5co-header" class="fh5co-cover" role="banner" style="background-image:url(/static/exam2.png); background-attachment: fixed;height: auto" data-stellar-background-ratio="0.5">
		<div class="overlay"></div>
		<div class="container-fluid">
			<div class="row">
				<div class="col-md-12  text-center">
					<div class="display-t">
						<div class="display-tc animate-box" data-animate-effect="fadeIn">
<center>


    <form runat="server" method="post">
    <div>
      <table width="100%" align="center">
        <tr>
        	<td><input type="text" name="mini" value="1" id="mini"></td>
          <td>
            <div id="starttime"></div>
 
            <div id="endtime"></div>
 			
            <div class="d1" id="showtime" style="color: red;font-size: 20px;font-family: verdana;"></div>
          </td>
        </tr>
        <tr>
          <td>
          	<input type="text" name="min" oninput="f1()" id="min" value="{{data['m']}}">
          	<input type="text" name="sec" id="sec" value="{{data['s']}}">

          	<input type="text" name="mins"  id="mins">
          	<input type="text" name="secs" id="secs">
          </td>
        </tr>
      </table>
    </div>


<script type="text/javascript">
	var currentValue = 0;
function handleClick(myRadio) {
    currentValue = myRadio.value;
    // alert(currentValue)
    document.getElementById("anss").value =  currentValue;
}

	</script>

	{% if data['next'] %}
	<h1>{{data['qno']}}. {{data['next'][0]['question']}}</h1>
	<table class="table" style="width: 700px">
		<input type="text" name="anss" hidden id="anss">

		{% for row in data['next'] %}
		<tr>
			<td>{{loop.index}}.</td>
			{% if data['added'] %}
				{% if data['added'][0]['qstansr_id'] |int==row['qstansr_id'] |int %}
				<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}" checked>
				{{row['option']}}</td>	
				{% else %}
				<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}">
				{{row['option']}}</td>
				{% endif %}
			{% else %}
			<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}">
			{{row['option']}}</td>
			{% endif %}
			
		</tr>
		{% endfor %}
		<tr>
			<td colspan="3" align="center"><input type="submit" name="nxtsubmit" value="SUBMIT" class="btn btn-primary"></td>
		</tr>
		<tr>
			<br>
			<td colspan="3" align="left"><a href="?action2=pre&pid={{data['next'][0]['question_id']-1}}&examid={{examid}}&qno={{data['qno']}}" class="btn btn-warning">PREVIOUS</a></td>
			{% if data['last']==data['next'][0]['question_id'] %}
			<tr>
				<td colspan="3" align="center"><input type="submit" name="complete" value="CLICK HERE TO EXIT FROM EXAM" class="btn btn-danger"></td>
			</tr>
			
			{% else %}
			<td colspan="3" align="right"><a href="?action=next&nid={{data['next'][0]['question_id']+1}}&examid={{examid}}&qno={{data['qno']}}" class="btn btn-danger">NEXT</a></td>
			{% endif %}
	</table>	
	{% elif data['pre'] %}	
	<table class="table" style="width: 700px">
		<input type="text" name="anss" hidden id="anss">
		<h1>{{data['qno']}}. {{data['pre'][0]['question']}}</h1>
		{% for row in data['pre'] %}
		<tr>
			<td>{{loop.index}}.</td>
			{% if data['added'] %}
				{% if data['added'][0]['qstansr_id'] |int==row['qstansr_id'] |int %}
				<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}" checked>
				{{row['option']}}</td>	
				{% else %}
				<td><input type="radio" name="ans" onclick="handleClick(this)"  value="{{row['qstansr_id']}}">
				{{row['option']}}</td>
				{% endif %}
			{% else %}
			<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}">
			{{row['option']}}</td>
			{% endif %}
		
		</tr>
		{% endfor %}
		<tr>
			<td colspan="3" align="center"><input type="submit" name="presubmit" value="SUBMIT" class="btn btn-primary"></td>
		</tr>
		<tr><br>
			<td colspan="3" align="left">
			{% if data['qone']==data['pre'][0]['question_id'] %}
			{{pass}}

			{% else %}<a href="?action2=pre&pid={{data['pre'][0]['question_id']-1}}&examid={{examid}}&qno={{data['qno']}}" class="btn btn-warning">PREVIOUS</a></td>
			{% endif %}
			<td colspan="3" align="right"><a href="?action=next&nid={{data['pre'][0]['question_id']+1}}&examid={{examid}}&qno={{data['qno']}}" class="btn btn-danger">NEXT</a></td>
			
	</table>	

	{% else %}

	{% if data['1q'] %}
	<h1>{{data['qno']}}. {{data['1q'][0]['question']}}</h1>
	<table class="table" style="width: 700px">
		<input type="text" name="anss" hidden id="anss" >
		{% for row in data['1q'] %}
		<tr>
			<td>{{loop.index}}.</td>
				{% if data['added'] %}
					{% if data['added'][0]['qstansr_id'] |int==row['qstansr_id'] |int %}
						<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}" checked>
						{{row['option']}}</td>	
					{% else %}
						<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}">
						{{row['option']}}</td>
					{% endif %}
				{% else %}
					<td><input type="radio" onclick="handleClick(this)" name="ans" value="{{row['qstansr_id']}}">
					{{row['option']}}</td>
				{% endif %}
		</tr>
		{% endfor %}

		<tr>

			<td colspan="3" align="center"><input type="submit" name="submit" value="SUBMIT" class="btn btn-primary"></td>
		</tr>
		<tr>
			
			<td colspan="3" align="right"><a href="?action=next&nid={{data['1q'][0]['question_id']+1}}&examid={{examid}}&qno={{data['qno']}}" class="btn btn-danger">NEXT</a></td>
		</tr>
	</table>		
	{% endif %}	

	{% endif %}	
</form>
    

</center>

						</div>
					</div>
				</div>
			</div>
		</div>
	</header>


{% include 'footer.html' %}








<!-- <header id="fh5co-header" class="fh5co-cover" role="banner" style="background-image:url(/static/exam2.png); background-attachment: fixed;height: auto" data-stellar-background-ratio="0.5">
		<div class="overlay"></div>
		<div class="container-fluid">
			<div class="row">
				<div class="col-md-12  text-center">
					<div class="display-t">
						<div class="display-tc animate-box" data-animate-effect="fadeIn">
<center>
	<script type="text/javascript">
	var currentValue = 0;
function handleClick(myRadio) {
    currentValue = myRadio.value;
    // alert(currentValue)
    document.getElementById("anss").value =  currentValue;
}

	</script>
<form method="post">
	{% if data['next'] %}
	<h1>{{data['qno']}}. {{data['next'][0]['question']}}</h1>
	<table class="table" style="width: 700px">
		<input type="text" name="anss" hidden id="anss">

		{% for row in data['next'] %}
		<tr>
			<td>{{loop.index}}.</td>
			{% if data['added'] %}
				{% if data['added'][0]['qstansr_id'] |int==row['qstansr_id'] |int %}
				<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}" checked>
				{{row['option']}}</td>	
				{% else %}
				<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}">
				{{row['option']}}</td>
				{% endif %}
			{% else %}
			<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}">
			{{row['option']}}</td>
			{% endif %}
			
		</tr>
		{% endfor %}
		<tr>
			<td colspan="3" align="center"><input type="submit" name="nxtsubmit" value="SUBMIT" class="btn btn-primary"></td>
		</tr>
		<tr>
			<br>
			<td colspan="3" align="left"><a href="?action2=pre&pid={{data['next'][0]['question_id']-1}}&examid={{examid}}&qno={{data['qno']}}" class="btn btn-warning">PREVIOUS</a></td>
			{% if data['last']==data['next'][0]['question_id'] %}
			<tr>
				<td colspan="3" align="center"><input type="submit" name="complete" value="CLICK HERE TO EXIT FROM EXAM" class="btn btn-danger"></td>
			</tr>
			
			{% else %}
			<td colspan="3" align="right"><a href="?action=next&nid={{data['next'][0]['question_id']+1}}&examid={{examid}}&qno={{data['qno']}}" class="btn btn-danger">NEXT</a></td>
			{% endif %}
	</table>	
	{% elif data['pre'] %}	
	<table class="table" style="width: 700px">
		<input type="text" name="anss" hidden id="anss">
		<h1>{{data['qno']}}. {{data['pre'][0]['question']}}</h1>
		{% for row in data['pre'] %}
		<tr>
			<td>{{loop.index}}.</td>
			{% if data['added'] %}
				{% if data['added'][0]['qstansr_id'] |int==row['qstansr_id'] |int %}
				<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}" checked>
				{{row['option']}}</td>	
				{% else %}
				<td><input type="radio" name="ans" onclick="handleClick(this)"  value="{{row['qstansr_id']}}">
				{{row['option']}}</td>
				{% endif %}
			{% else %}
			<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}">
			{{row['option']}}</td>
			{% endif %}
		
		</tr>
		{% endfor %}
		<tr>
			<td colspan="3" align="center"><input type="submit" name="presubmit" value="SUBMIT" class="btn btn-primary"></td>
		</tr>
		<tr><br>
			<td colspan="3" align="left">
			{% if data['qone']==data['pre'][0]['question_id'] %}
			{{pass}}

			{% else %}<a href="?action2=pre&pid={{data['pre'][0]['question_id']-1}}&examid={{examid}}&qno={{data['qno']}}" class="btn btn-warning">PREVIOUS</a></td>
			{% endif %}
			<td colspan="3" align="right"><a href="?action=next&nid={{data['pre'][0]['question_id']+1}}&examid={{examid}}&qno={{data['qno']}}" class="btn btn-danger">NEXT</a></td>
			
	</table>	

	{% else %}

	{% if data['1q'] %}
	<h1>{{data['qno']}}. {{data['1q'][0]['question']}}</h1>
	<table class="table" style="width: 700px">
		<input type="text" name="anss" hidden id="anss" >
		{% for row in data['1q'] %}
		<tr>
			<td>{{loop.index}}.</td>
				{% if data['added'] %}
					{% if data['added'][0]['qstansr_id'] |int==row['qstansr_id'] |int %}
						<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}" checked>
						{{row['option']}}</td>	
					{% else %}
						<td><input type="radio" name="ans" onclick="handleClick(this)" value="{{row['qstansr_id']}}">
						{{row['option']}}</td>
					{% endif %}
				{% else %}
					<td><input type="radio" onclick="handleClick(this)" name="ans" value="{{row['qstansr_id']}}">
					{{row['option']}}</td>
				{% endif %}
		</tr>
		{% endfor %}

		<tr>

			<td colspan="3" align="center"><input type="submit" name="submit" value="SUBMIT" class="btn btn-primary"></td>
		</tr>
		<tr>
			
			<td colspan="3" align="right"><a href="?action=next&nid={{data['1q'][0]['question_id']+1}}&examid={{examid}}&qno={{data['qno']}}" class="btn btn-danger">NEXT</a></td>
		</tr>
	</table>		
	{% endif %}	

	{% endif %}	
</form>
</center>

						</div>
					</div>
				</div>
			</div>
		</div>
	</header>
</center>

{% include 'footer.html' %} -->