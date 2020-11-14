import csv 

# the a stands for append
file = open("phonebook.csv", "a")

name = raw_input("Name: ")
number = raw_input("Number: ")

writer = csv.writer(file)
writer.writerow((name, number))

file.close()
