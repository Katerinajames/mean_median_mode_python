
import statistics

grades = [85, 93, 45, 89, 85]
print("PRINT LIST VALUES")

for i in range (0,len(grades)):
	 print(grades[i])



print ("The average of the numbers in our list is",statistics.mean(grades))

print("----------------------------------------------")

print("The middle element of our list is",(statistics.median(grades)))

print("----------------------------------------------")

print("The most freguent met element of our list is",(statistics.mode(grades)))
