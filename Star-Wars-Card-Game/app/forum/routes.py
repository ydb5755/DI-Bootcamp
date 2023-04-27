from app.forum import forum
from flask import render_template, redirect, url_for, flash
from app.profiles.models import User, Card
from app.forum.forms import ThreadForm, CommentForm
from app.forum.models import Thread, Comment
from flask import current_app
from flask_login import current_user, login_required

def get_leaders():
    with current_app.app_context():
        all_users = User.query.all()
        # coin_leaders = User.query.all().order_by(User.coins)
        # point_leaders = User.query.all().order_by(sum(User.cards.point_value))
        coin_leader = all_users[0]
        point_leader = all_users[0]
        for user in all_users:
            if user.coins > coin_leader.coins:
                coin_leader = user

        for user in all_users:
            if user.get_card_points() > point_leader.get_card_points():
                point_leader = user
    return coin_leader, point_leader

@forum.route('/', methods=('GET', 'POST'))
@login_required
def forum_home():
    c, p = get_leaders()
    all_threads = Thread.query.all()
    thread_form = ThreadForm()
    if thread_form.validate_on_submit():
        thread = Thread(subject=thread_form.subject.data, user=current_user)
        thread.save_thread()
        return redirect(url_for('forum.forum_home'))
    return render_template('forum_home.html',
                           all_threads=all_threads,
                           thread_form=thread_form,
                           coin_leaders=c,
                           point_leaders=p)

@forum.route('/thread/<thread_id>', methods=('GET', 'POST'))
@login_required
def thread_page(thread_id):
    comment_form = CommentForm()
    thread = Thread.query.filter_by(id=thread_id).first()
    if comment_form.validate_on_submit():
        comment = Comment(content=comment_form.content.data,
                          thread=thread,
                          user=current_user)
        comment.save_comment()
        return redirect(url_for('forum.thread_page', thread_id=thread.id))
    return render_template('thread_page.html',
                           thread=thread,
                           comment_form=comment_form)