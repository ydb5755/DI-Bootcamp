from portfolio import portfolio, app
from flask import render_template, redirect, url_for, flash
from portfolio.forms import BlogSignUpForm, MessageForm
from portfolio.models import User, Message, Blog

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blogs')
def blogs():
    blog_form = BlogSignUpForm()
    blog = Blog.query.filter_by(name=blog_form.blog.data).first()
    user = User.query.filter_by(email=blog_form.email.data).first()
    if blog_form.validate_on_submit():
        if user:
            user.blogs.append(blog)
            portfolio.session.commit()
        else:
            user = User(name=blog_form.name.data, email=blog_form.email.data)
            user.blogs.append(blog)
            user.save_user()
        flash(f"You've been signed up for the {blog.name} blog!")
        redirect(url_for('landing_page'))
    return render_template('blogs.html', blog_form=blog_form)

@app.route('/blog/<int:blog_id>')
def ind_blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    return render_template('ind_blog.html', blog=blog)


@app.route('/contact')
def contact():
    message_form = MessageForm()
    if message_form.validate_on_submit():
        user = User.query.filter_by(email=message_form.email).first()
        if user:
            message_to_send = Message(text=message_form.message.data, user=user)
            message_to_send.save_message()
        else:
            user = User(name=message_form.name.data, email=message_form.email.data)
            user.save_user()
            message_to_send = Message(text=message_form.message.data, user=user)
            message_to_send.save_message()
        return redirect(url_for('contact_confirmation'))
    return render_template('contact.html', message_form=message_form)

