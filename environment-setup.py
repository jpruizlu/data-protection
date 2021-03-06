#######################################
#     Initial environment setup       #
#######################################

import sys 
import os 
import subprocess
import time

try:
    print subprocess.check_output(['pip','install','--user','--upgrade','pip'])
    cmd='yes|sudo pip uninstall pip'
    print subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    time.sleep(1)
    print subprocess.check_output(['pip','install','--user','boto3'])
    print subprocess.check_output(['pip','install','--user','aws-encryption-sdk'])
    print subprocess.check_output(['pip','install','--user','ikpdb'])
    print subprocess.check_output(['pip','install','--user','pathlib'])
    print subprocess.check_output(['pip','install','--user','flask'])
    print subprocess.check_output(['pip','install','--user','pyopenssl'])
    print "\n"
    print "Workshop environment setup was successful"
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
else:
    exit(0)