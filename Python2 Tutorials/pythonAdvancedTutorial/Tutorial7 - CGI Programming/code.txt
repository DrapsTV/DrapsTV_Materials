
//code 0//
<Directory /var/www/>
	Options ExecCGI Indexes FollowSymLinks MultiViews
	AllowOverride None
	Order allow,deny
	allow from all
	AddHandler cgi-script .py
</Directory>

//code 1//

//Hello.py//

#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head><title>My First CGI Program</title></head>'
print '<body>'
print '<p> It works!!! </p>'
for i in range(5):
	print '<h1>Hello World! ' + i + '</h2>'
print '</body>'
print '</html>'


//code 2//

//hello.py//
#!/usr/bin/python
import cgi

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head><title>My First CGI Program</title></head>'
print '<body>'
print '<h1>Hello Program!</h1>'
form = cgi.FieldStorage()
if form.getvalue("name"):
	name = form.getvalue("name")
	print '<h1>Hello ' + name + '! Thanks for using my script!</h1><br />'
if form.getvalue("happy"):
	print "<p> Yay! I'm happy too! </p>"
if form.getvalue("sad"):
	print "<p> Oh no! Why are you sad? </p>"

print '<form method="post" action="hello.py">'
print '<p>Name: <input type="text" name="name"/></p>'
print '<input type="checkbox" name="happy" /> Happy'
print '<input type="checkbox" name="sad" /> Sad'
print '<input type="submit" value="Submit" />'
print '</form>'
print '</body>'
print '</html>'

