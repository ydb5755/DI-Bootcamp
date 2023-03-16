import flask
import markdown

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.redirect(flask.url_for('lesson'))

@app.route('/lesson1')
def lesson():
    with open('Week-11\Day-2\Daily-Challenge\lesson1\md-files\in-this-chapter.md') as f:
        md = f.read()
    html = markdown.markdown(md) # there is no need for a new variable you can just do return markdown.markdown(md)
    return html

@app.route('/exercise')
def exercise():
    with open('Week-11\Day-2\Daily-Challenge\lesson1\md-files\exercises.md') as f:
        md = f.read()
    html = markdown.markdown(md)
    return html

if __name__ == '__main__':
    app.run(debug=True)
