#!/usr/local/bin/python3
print("Content-type:text/html\n")

# CS131A:Spring 2015: wostner

import cgi

form = cgi.FieldStorage()

PAGE_TEMPLATE = """
<html>
    <head> {head:}</head>
    <body> 
    	{content:}
    	<hr />
    	{footer:}
    	</body>
</html>
"""

HEAD_TEMPLATE = """
    <title>{title:} </title>
    <link href="css/{css:}" rel="stylesheet" type="text/css" />
"""

FORM = """
    <form action='myfirstform.py' method='GET'>
        Your Nickname: 
        <input type='text' name='nickname' />
        <input type='submit' value='PUSH HERE' />
    </form>
"""


default = dict(
               head="HEAD HERE" , 
               content="CONTENT HERE" , 
               footer="FOOTER HERE",
               css="STYLESHEETFILE" , 
               title="TITLE HERE"
              )

page = dict()

page.update(
    default,
    css='stylish.css',
    title='my first python web form'
)


HEAD = HEAD_TEMPLATE.format(**page)

FOOTER = """<h3>Hello {}, nice nickname!</h3>""".format(form.getvalue('nickname', 'ANONYMOUS'))

page.update(
    head=HEAD,
    content=FORM,
    footer=FOOTER
)

PAGE = PAGE_TEMPLATE.format(**page)


print(PAGE)



