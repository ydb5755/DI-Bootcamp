
# 🌟 Exercise 1
# Instructions
# Use pip to install the flask module.
# Run the command import flask in a python shell.
# Run the command dir(flask) to see the different methods that come along with flask.
import flask
# print(dir(flask))


# 🌟 Exercise 2
# Instructions
# Using Flask, create a template for your CV.
# Your CV should contain:
# Your name
# A picture
# Your hobbies
# Your skills
# Your strengths
# Your weaknesses
# Bonus: Add some CSS
# Hint : To add some CSS take a look at the video called Static Files in the Online Learning section.

app = flask.Flask(__name__)
@app.route('/')
def cv_page():
    return flask.render_template('cv.html')

app.run(debug=True)