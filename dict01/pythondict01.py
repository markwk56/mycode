#!/usr/bin/env python3

## create a dictionary
switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

## display parts of the dictionary
print( switch["hostname"] )
print( switch["ip"] )

## request a 'fake' key
print( switch["hostname"] )  


list1 = [{'id': '642459', 'name': 'Mark Keys', 'url': 'https://n218.meraki.com/o/YO9F3c/manage/organization/overview'}]

print(list1[0]["name"])




