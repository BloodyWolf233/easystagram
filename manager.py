# -*- encoding=UTF-8 -*-

from easystagram import app, db
from flask_script import Manager
from easystagram.models import User
from random import random

manager = Manager(app)


def get_image_url():
    return 'https://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'

@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0, 10):
        db.session.add(User('User' + str(i), 'a' + str(i)))
        for j in range(0,3):

    db.session.commit()


if __name__ == '__main__':
    manager.run()
