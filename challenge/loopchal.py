#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for item in farms:
    print(item)

# level 1
# change 0 to look at other entries in the list


for x in farms[2]["agriculture"]:
    print(x)


print(farms[0])

print(farms[0]["agriculture"])

print(farms[0]["name"])


print(farms[2]["agriculture"][0])












