grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Jonny','Bilbo','Steve','Khendrik','Aaron'}
#print(type(students)) - proverka
students = list(students)
#print(type(students)) - proverka perevoda tipa dannih
#print(students) - proverka vivoda dannih
students.sort()
#print(students) - proverka sortirovki
ever0 = (sum(grades[0])/len(grades[0]))
ever1 = (sum(grades[1])/len(grades[1]))
ever2 = (sum(grades[2])/len(grades[2]))
ever3 = (sum(grades[3])/len(grades[3]))
ever4 = (sum(grades[4])/len(grades[4]))
#print(ever0 , ever1 , ever2 , ever3 , ever4) - proverka podscheta srednego bala
classbook = {students[0] : ever0, students[1] : ever1, students[2] : ever2 ,
             students[3] : ever3 , students[4] : ever4}
print(classbook)
