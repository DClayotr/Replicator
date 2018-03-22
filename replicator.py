import os
from sys import argv

script = argv
name = str(script[0])

cmd = 'start payload.txt'
cmd2 = 'copy replicator.py clone'
os.system(cmd)
os.mkdir('clone')
os.system(r'copy payload.txt clone')
os.system(cmd2)

input("press enter to close")