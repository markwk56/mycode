#!/usr/bin/env python3

numb_of_stars = int(input("enter number of stars for gretaest ppoint "))


for star in range(1, numb_of_stars+1):
    for num in range(star):
        print(" * ", end = "")
    print("\n")
count2 = int(numb_of_stars)

for num in range(count2-1,0,-1):
    print(" * "*num)
#    print("\n")    



print("\n")








