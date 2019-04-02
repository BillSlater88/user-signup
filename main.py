from flask import Flask, request, redirect

import cgi

app = Flask(__name__)

app.config['DEBUG'] = True



page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Signup</title>
    </head>
    <body>
        <h1>Signup</h1>
"""

page_footer = """
    </body>
</html>
"""


username_form = """
    <form action="/username" method="post">
        <label>
            Username
            <input type="text" name="username"/>
        </label>
        <input type="submit" value="Submit Query"/>
    </form>
"""


@app.route("/")
def index():

    return page_header + username_form + page_footer



app.run()