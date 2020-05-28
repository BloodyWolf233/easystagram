# -*- encoding=UTF-8 -*-

from easystagram import app

@app.route('/')
def index():
    return 'Hello'