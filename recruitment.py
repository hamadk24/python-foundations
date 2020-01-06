skills = ['Reading', 'Writing', 'Eating', 'Sleeping', 'Dancing', 'Playing']
cv = {}
Name = input('What is your name? ') 
cv['name'] = Name
Age = input('What is your age? ')
cv['age'] = Age
Experience = input('How many years of experience do you have? ')
cv['experience'] = Experience
cv['skills']=[]
print('''
	Skills:
	1. {}
	2. {}
	3. {}
	4. {}
	5. {}
	6. {}'''.format(skills[0], skills[1], skills[2], skills[3], skills[4], skills[5]))
skill1 = input('Choose a skill! ')
skill2 = input('Choose another skill! ')
cv['skills'].append(skills[int(skill1)-1])
cv['skills'].append(skills[int(skill2)-1])
if int(Age) > 21 and int(Experience) > 3 and (int(skill1) == 1 or int(skill2) == 1):
	print('Accepted!')
else:
	print('itla3 bara')
