#!/usr/bin/env python
# -*- coding: utf-8 -*-
from the_finder import app
from flask import request

@app.route('/')
def get_main():
    return "Hello"

'''
OTHER PATH
'''
@app.route('/shutdown', methods=['GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'
