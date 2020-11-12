#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel

column3 = input("Enter column3 header ")
column4 = input("Enter column4 header ")

# Request data from user
def get_ip_data(column3,column4):
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    column3_input = input("What is the data for column3 ")
    column4_input = input("What is the data for column4 ")
    d = {"IP": input_ip, "driver": input_driver, column3: column3_input, column4: column4_input}
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}] {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")


# Runtime
mylistdict = []  # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data(column3, column4))
    keep_going = input("\nWould you like to add another value? Enter to continue, or \
    enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print("The file " + filename + ".xls should be in your local directory")


