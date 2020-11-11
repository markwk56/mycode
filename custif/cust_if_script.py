#!/usr/bin/env python3


print("This script will ask you to enter a number between 0 and 10 and then will give yo the title of the Star Wars movie")

while True:
    number = input("enter a number between 0 and 10. ").isnumeric()

    if number <=0 or number >=10:
        print("your entry was either not a number or a number beween 0 and 10. Please try again. ")
    else:
        break

if number == 1:
    print("The phantom menace")
elif number ==2:
    print("attack of the clones")
elif number == 3:
    print("revenge of the sith")
elif number == 4:
    print("a new hope")
elif number ==5:
    print("the empire strikes back")
elif number ==6:
    print("retunr of the jedi")
elif number ==7:
    print("the force awakens")
elif number ==8:
    print("the last jedi")
else:
    print("The rise of skywalker")



print("thanks for playing")






