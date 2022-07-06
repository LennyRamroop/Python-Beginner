#Lenny Ramroop
#Gradebook mini project - completed on Codecademy

#The Gradebook project demonstrates my use of lists, two-dimensional lists and list methods/functions
#We take a series of lists and modify them using .append and .remove based on changes to the student's
#profile, before printing their final gradebook

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]
gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]

gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])

gradebook[-1][-1] += 5

gradebook[2].remove(85)
gradebook[2].append('Pass')

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)