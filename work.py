#Simple attendants registration app:

#capture the number of users allowed
ptpNumber = int(input("How many participants are allowed to attend? \n"))
minAge = int(input("What is the minimum age for attendees? \n"))

#List to store the participants
participants = []

#Let's keep the initial value of the participarts 0
initialMembers = 0

curYr = 2021

#Open up the external file to write to:
ptpOutFile = open("Participants", "w")

while(initialMembers < ptpNumber):
    #A temporally list to keep the details:
    tempData = [] #Keeps the name, major and age
    #Capture the name
    name = input("Enter the name: \n")     
    major = input("Enter the major: \n")
    yob = int(input("In which year were you born? \n"))
    age = curYr - yob
    if age > minAge:
        #Add the name to the temp list.
        tempData.append(name)
        tempData.append(major)
        tempData.append(age)
        #Add tempData to the Participants' list and increase the counter by 1
        participants.append(tempData)
        initialMembers +=1 
        print(name + " Registered successfully. your ID is: " + str(initialMembers))
        
        for student in tempData:
            print(student)
            #"Name: \n" +student[0] + " Major: \n" + student[1] + " Age: \n" +str(student[2])
    else:
        print("sorry, " + name + " you are under age.")
    
#Write everything to the external file:
#Each participant is kept in the list.
for participant in participants:
    #loop over the students' data
    for study in participant:
        ptpOutFile.write(str(study)) #Convert everything into a string before writting
        #Provide some space
        ptpOutFile.write(" ")
    #Add each participant to a new file:
    ptpOutFile.write("\n")
print(str(initialMembers) + " Students were registered successfully")
#Close the external file.
ptpOutFile.close()

#Reading the names in the file:
ptpFile = open("Participants", "r")
for line in ptpFile:
    print(line)

ptpFile.close()