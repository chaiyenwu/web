#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: justinwu
"""
fp=open('file.txt','w')
if fp !=None:
    print('檔案開啟成功')
fp.close()
fp=open('file.txt','w')
if fp!=None:
    fp.write('小白')
fp.close()
fp=open('file.txt','r')
if fp!=None:
    str=fp.read()
    print(str)
fp.close()

fp=open('file.txt','w')
if fp!=None:
    fp.write('宇哲') 
    fp.write('大宇哲')  
fp.close()
