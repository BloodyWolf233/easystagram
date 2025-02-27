# -*- encoding=UTF-8 -*-
import random
import unittest

from flask_script import Manager
from sqlalchemy import or_, and_

from easystagram import app, db
from easystagram.models import User, Image, Comment

manager = Manager(app)


def get_image_url():
    return 'https://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'


@manager.command
def init_database_test():
    db.drop_all()
    db.create_all()
    for i in range(0, 100):
        db.session.add(User('User' + str(i), 'a' + str(i)))
        for j in range(0, 5):
            db.session.add(Image(get_image_url(), i + 1))
            for k in range(0, 3):
                db.session.add(Comment('This is a comment' + str(k), 1 + 5 * i + j, i + 1))
    db.session.commit()


@manager.command
def retrieve_test():
    print 1, User.query.all()
    print 2, User.query.get(3)
    print 3, User.query.filter_by(id=5).first()
    print 4, User.query.order_by(User.id.desc()).offset(1).limit(2).all()
    print 5, User.query.filter(User.username.endswith('0')).limit(3).all()
    print 6, User.query.filter(or_(User.id == 2, User.id == 5)).all()
    print 7, User.query.filter(and_(User.id > 2, User.id < 5)).all()
    print 8, User.query.filter(and_(User.id > 2, User.id < 5)).first_or_404()
    print 9, User.query.paginate(page=1, per_page=10).items

    user = User.query.get(1)
    print 10, user.images

    image = Image.query.get(1)
    print 11, image, image.user


@manager.command
def update_test():
    for i in range(50, 100, 2):
        user = User.query.get(i)
        user.username = '[New1]' + user.username

    User.query.filter_by(id=51).update({'username': '[New2]'})
    db.session.commit()


@manager.command
def delete_test():
    for i in range(50, 100, 2):
        comment = Comment.query.get(i + 1)
        db.session.delete(comment)
    db.session.commit()


@manager.command
def run_test():
    tests = unittest.TestLoader().discover('./')
    unittest.TextTestRunner().run(tests)

if __name__ == '__main__':
    manager.run()
