import random
import math

name_file = open('name List','r')
contents = name_file.readlines()
name_list = []
for line in contents:
    name_list.append(line.replace('\n',''))

people_file = open('People', 'w')
people_file.write('PersonID,Name,Age,Personality_Rating\n')
for x in range(100):
    random_Name = name_list[random.randint(1,len(name_list)-1)]
    random_age = random.randint(20,75)
    random_personality = round(random.randint(1,100))
    people_file.write('{},{},{}\n'.format(random_Name,random_age,random_personality))