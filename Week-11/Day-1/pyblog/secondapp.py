import flask
app = flask.Flask(__name__)

@app.route('/blog')
def blog_route():
    with open('homepage.html') as f:
        return flask.render_template_string(f.read())

articles = [
    {
        'name':'article1',
        'title':'article1 title'
    },
    {
        'name':'article2',
        'title':'article2 title'
    },
    {
        'name':'article3',
        'title':'article3 title'
    }
]

@app.route('/blog/articles')
def blog_articles():
    articles_titles = list(map(lambda article: article['title'], articles))
    with open('articles.html') as f:
        return flask.render_template_string(f.read(), articles=articles_titles)

@app.route('/profile')
def profile_redirect_to_blog():
    return flask.redirect(flask.url_for('blog_route'))

if __name__ == '__main__':
    app.run(debug=True)