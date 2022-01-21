
#Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number less than the asked number.
num = input("choose a number: ")
for x in range (1, int(num), 2):
  print(int(num) % x == 0)
  
#Consider the following string: nums = '10,20,30,40,50'. Create a Python script that creates a list of integers from the string. The resulting list will be: [10, 20, 30, 40, 50]

nums = '10,20,30,40,50'

def createlist():
  newlist = nums.split(",")
  return newlist
createlist()
##split

##Afanwi Mabo
#amabo1@student.gsu.edu
#dsci 1302 programming for data science 2
#started working on 1/19 on google colab
