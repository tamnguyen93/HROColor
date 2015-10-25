import os, subprocess
from subprocess import Popen, PIPE
cmd =["sudo" , "./pixy/build/hello_pixy/hello_pixy"]
process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
process.wait()
output = process.stdout.read()
outputSplit = output.split()
print outputSplit[1]
print 'hello this is pixy'
