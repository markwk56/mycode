#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginsuccess = 0 # counter for success
# open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

# loop over the file
for line in keystone_file:

    # if this 'fail pattern' appears in the line...
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
        print(line.split(" ")[-1])
    elif "-] Authorization failed" in line:
        loginsuccess += 1
print("The number of failed log in attempts is", loginfail)
print("The number of successful login atempts is", loginsuccess)
keystone_file.close() # close the open file


