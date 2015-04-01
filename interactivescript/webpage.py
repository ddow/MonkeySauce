"""
simple web page template
"""


TEMPLATE = """
<html>
    <head>
        <title>
            {title:}
        </title>
    <body>
        <h1>{header:}</h1>
    {content:}
        <hr>
    </body>
</html>
"""

d = dict()
d['title'] = input('What is the title of your webpage? ')
d['header'] = input('What is the header of your webpage? ')
d['content'] = input('What content would you like to display? ')
d['content'] += input('Do you have anything else to say? ')

print(TEMPLATE.format(**d))
