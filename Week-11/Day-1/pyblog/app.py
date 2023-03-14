import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/<username>')
def index_with_user(username):
    html = f'''
        <html>
            <head>
                <title>Home Page - Microblog</title>
            </head>
            <body>
                <h1>Hello, {username}!</h1>
            </body>
        </html>'''
    return html

@app.route('/blog')
def blog():
    return 'Welcome to my blog!'

articles = ['article1', 'article2', 'article3']

@app.route('/blog/articles')
def blog_articles():
    article_string = '''
    {{ content }}
    Hello There!
    '''
    return flask.render_template_string(article_string, content=articles)

@app.route('/login')
def login():
    return 'loginPage'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(flask.escape(username))

@app.route('/home/<username>')
def template(username):
    template_string =  '''
        <html>
            <head>
                <title>Home Page - Microblog</title>
            </head>
            <body>
                <h1>Hello, {{ name }}! How are you ?</h1>
                <a href={{url_for('blog_articles')}}> Blog Articles </a>
            </body>
        </html>
    '''
    html = flask.render_template_string(template_string, name=username)
    return html

with app.test_request_context():
    print(flask.url_for('index'))
    print(flask.url_for('login'))
    print(flask.url_for('login', next='/'))
    print(flask.url_for('profile', username='John Doe'))


# if __name__ == "__main__":
#     app.run(debug=True,port=5000)