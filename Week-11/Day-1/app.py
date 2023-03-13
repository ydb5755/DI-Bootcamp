import flask

app = flask.Flask(__name__)

@app.route('/blog')
def index():
    return 'Welcome to my blog!'

@app.route('/blog/articles')
def index1():
    html = '''
        <html>
            <head>
                <title>Home Page - Microblog</title>
            </head>
            <body>
                <h1>Hello!</h1>
            </body>
        </html>'''

    return html


if __name__ == "__main__":
    app.run(debug=True,port=5000)

