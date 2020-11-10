#!/usr/bin/env python3
# import tools to manipulate files
import shutil

import os

# set workng directory

os.chdir('/home/student/mycode/')

# move file to new diretcory

shutil.move('raynor.obj', 'ceph_storage/')


xname = input('What is the new name for kerrigan.obj? ')

# move file and change its name

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



