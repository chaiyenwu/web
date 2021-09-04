#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: justinwu
"""

from bottle import route, run

@route('/')
def home():
  return "林小寶的網頁,首頁"

run(host='localhost', port=9999)

