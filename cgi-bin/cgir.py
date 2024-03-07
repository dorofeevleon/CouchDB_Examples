#! /usr/bin/python3
import sys
import cgi
import subprocess
#import cgitb
#cgitb.enable()

form = cgi.FieldStorage()

if "command" in form:
    cmd = ["cgir", "send", form["command"].value]
    print("Content-Type: text/html")
    print("")
    print(" ".join(cmd))
    subprocess.run(cmd)
else:
    print("Content-Type: text/html")
    print("")
    print("<p>bad request!</p>")
