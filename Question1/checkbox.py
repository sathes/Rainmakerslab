
"""
1. 
Question: 
You are given an HTML form, which contains the following entries:
<input type="checkbox" class="form" name="checkbox_2"/> 
<input type="checkbox" class="form" name="checkbox_1"/> 
<input type="checkbox" class="form" name="checkbox_3"/> 
... 
<input type="checkbox" class="form" name="checkbox_10"/> 
The above form has been submitted using the "POST" method.

Write code that will determine which checkboxes have been checked and print, in a space separated list, the checkbox numbers that were checked.

For example, if check-boxes 3, 5, and 10 are checked, you would print
3 5 10 

"""
from bottle import route, run, request

@route('/')
def hello():
    return '''<!doctype html>
    			<html>
					<title> Selct Check box </title>
						<body>
							<hi>Selct Check box</h1>
						    <form action="/get_check_box" method="post"> 
						    	<input type="checkbox" class="form" name="checkbox_1"/>
									1
								</br>
								<input type="checkbox" class="form" name="checkbox_2"/> 
									2
								</br>
								<input type="checkbox" class="form" name="checkbox_3"/> 
									3
								</br>
								<input type="checkbox" class="form" name="checkbox_4"/> 
									4
								</br>
								<input type="checkbox" class="form" name="checkbox_5"/> 
									5
								</br>
								<input type="checkbox" class="form" name="checkbox_6"/> 
									6
								</br>
								<input type="checkbox" class="form" name="checkbox_7"/> 
									7
								</br>
								<input type="checkbox" class="form" name="checkbox_8"/> 
									8
								</br>
								<input type="checkbox" class="form" name="checkbox_9"/> 
									9
								</br>
								<input type="checkbox" class="form" name="checkbox_10"/>
									10
								</br>
						    	<input value="select & submit" type="submit" /> 
						   	</form>
						</body>
					</html>'''


@route('/get_check_box', method='POST')
def do_get_check_box():
	x = [int(i.replace('checkbox_','')) for i in list(request.forms)]
	x = [str(i) for i in sorted(x)]
	x = ' '.join(x)
	return '<h2> Output:</h2> <br> <br> <p> %s </p>' %x

run(host='localhost', port=8080, debug=True)