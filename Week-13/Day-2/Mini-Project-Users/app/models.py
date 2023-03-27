from app import robots

class User(robots.Model):
    id       = robots.Column(robots.Integer, primary_key=True)
    name     = robots.Column(robots.String(64))
    street   = robots.Column(robots.String(64))
    city     = robots.Column(robots.String(64))
    zipcode  = robots.Column(robots.String(64))