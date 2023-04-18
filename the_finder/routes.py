#!/usr/bin/env python
# -*- coding: utf-8 -*-
from the_finder import app , redis_client
from flask import request

@app.route('/')
def get_main():
    redis_client.set('name', 'John')
    redis_client.set('k', '2')
    test = redis_client.get('name').decode()
    return "hi"+str(test)
    #return 'Hello, {}!'.format(redis_client.get('name').decode())
    

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
