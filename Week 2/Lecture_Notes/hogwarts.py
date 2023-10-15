#-------------------------------------------------------------------------------------------------
# Way to print them with lists in string form without integers 
# students = ["Hermione", "Harry", "Ron"]
# for student in students:
#    print(student)
#-------------------------------------------------------------------------------------------------
# Way to print them using indexes with integers
#students = ["Hermione", "Harry", "Ron"]

#for i in range(len(students)): #len will find how long is the list
    #print(i + 1,students[i])
#-------------------------------------------------------------------------------------------------
# more on range
#for i in [0, 1, 2]: # this is the way to print something in the list but it's not gonna work with
    #print("meow")   #long lists

#for i in range(3):  # range will give me the list of 3 things
    #print("meow")   # is another way to do it 
#-------------------------------------------------------------------------------------------------
# Dictionaries in Python | associate KEYS with VALUES
#students = {
#	"Hermione": "Gryffindor",
#	"Harry":"Gryffindor",
#	"Ron":"Gryffindor",
#	"Draco":"Slytherin",
#}

#one way to print
#print(students["Hermione"])#You call dict objects with [] as strings
                            #|
#better way to print        #|
#for student in students:   #↓
#	print(student, students[student], sep = ", ") #student here is an integer value
#-------------------------------------------------------------------------------------------------

# Adding more than one data with dictonaries | creating a list of dictionaries

students = [
	{"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
	{"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
	{"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
	{"name": "Draco", "house": "Slytherin", "patronus": None}
]
for student in students: #student here is dict type
	print(student["name"],student["house"],student["patronus"])
