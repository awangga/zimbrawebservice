#!/usr/bin/env python
"""
insert.py -  Program to :
1. insert to outbox collection, 
2. check if main is running? if not run then run
"""
print "Content-Type: text-html"
print
import cgitb
cgitb.enable()
import cgi
import zws
import subprocess

form = cgi.FieldStorage()

rcpt = form["rcpt"].value
msg = form["msg"].value
subj = form["subj"].value


mail = zws.Zws()
mail.login('no-reply','asepdinamo')
mail.sendEmail(rcpt,msg,subj)


