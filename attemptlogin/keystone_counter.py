#!/usr/bin/env/python3 


loginfail = 0

keystone_file = open("/home/student/mycode1/attemptlogin/keystone.common.wsgi",'r')

keystone_file_lines=keystone_file.readlines()

for line in keystone_file_lines:
    if '-----] Authorization failed' in line:
        loginfail += 1 
print('the number of failed log in attempts is', loginfail)

keystone_file.close()


