#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import os

app = Flask(__name__)

import the_finder.config
import the_finder.routes

#
#if __name__ == '__main__':
    #app.run(debug=True,host='0.0.0.0')#,