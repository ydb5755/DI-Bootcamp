from portfolio import portfolio

user_blogs = portfolio.Table('user_blogs',
                              portfolio.Column('user_id', portfolio.Integer, portfolio.ForeignKey('user.id')),
                              portfolio.Column('blog_id', portfolio.Integer, portfolio.ForeignKey('blog.id'))
                              )

class User(portfolio.Model):
    id       = portfolio.Column(portfolio.Integer, primary_key=True)
    name     = portfolio.Column(portfolio.String(64), nullable=False)
    email    = portfolio.Column(portfolio.String(64), nullable=False, unique=True)
    messages = portfolio.relationship('Message', backref='user', lazy='dynamic')
    blogs    = portfolio.relationship('Blog', secondary=user_blogs, backref='followers')

    def save_user(self):
        portfolio.session.add(self)
        portfolio.session.commit()

class Message(portfolio.Model):
    id      = portfolio.Column(portfolio.Integer, primary_key=True)
    text    = portfolio.Column(portfolio.String(64), nullable=False)
    sent_by = portfolio.Column(portfolio.Integer, portfolio.ForeignKey('user.id'))

    def save_message(self):
        portfolio.session.add(self)
        portfolio.session.commit()

class Blog(portfolio.Model):
    id          = portfolio.Column(portfolio.Integer, primary_key=True)
    name        = portfolio.Column(portfolio.String(64), nullable=False)
    description = portfolio.Column(portfolio.String(200), nullable=False)
    img         = portfolio.Column(portfolio.String(200), default='static/default_pic.jpg')

    def save_blog(self):
        portfolio.session.add(self)
        portfolio.session.commit()

class Projects(portfolio.Model):
    id          = portfolio.Column(portfolio.Integer, primary_key=True)
    name        = portfolio.Column(portfolio.String(64), nullable=False)
    description = portfolio.Column(portfolio.String(200), nullable=False)
    url         = portfolio.Column(portfolio.String(64), nullable=False)

    def save_project(self):
        portfolio.session.add(self)
        portfolio.session.commit()