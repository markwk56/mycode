#!/usr/bin/env python3

numb_of_stars = int(input("enter number of stars for gretaest ppoint "))


for star in range(1, numb_of_stars+1):
    for num in range(star):
        print(" * ", end = "")
    print("\n")
count2 = int(numb_of_stars)

count= range(count2-1)

for star in range(count2-1):
    for num in count:
        count -= 1
        print(" * ")
    print("\n")    



print("\n")








