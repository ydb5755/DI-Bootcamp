import flask

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template('homepage.html')

@app.route('/color/<background_color>')
def color(background_color):
    return flask.render_template('color.html', background_color=background_color)

app.run(debug=True)