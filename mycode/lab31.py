#!/usr/bin/env python3
wordbank= ["indentation", "spaces"] 
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
wordbank.append(4)
num_input = int(input("Give me a number between 1 and 20:\n"))
student_name = tlgstudents[num_input -1] # subtract 1 because of indexing

choice= int(input("Pick a student number!:\n"))
student_name= tlgstudents[choice -1]

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent")
