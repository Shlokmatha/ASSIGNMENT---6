#1
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")



#2
x = input('Enter a word or sentence: ')

w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes, it is a palindrome")
else:
    print("No, it's not a palindrome")



#3
from math import factorial
n = int(input("Enter number of rows of Pascal Triangle : "))


for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()



#4
alphabets = "abcdefghijklmnopqrstuvwxyz"

def ispangram(userstr):
    for x in alphabets:
        if x not in userstr.lower():
            return False
    return True

input_str = str(input("Enter string to be checked if pangram or not : "))

if(ispangram(input_str)==True):
    print("Yes, it is a pangram.")
else:
    print("No, it is not a pangram.")



#5
user_str = str(input("Enter hyphen separated sequence of words : "))

word_list = [n for n in user_str.split("-")] # creating a list of all words after separating them
print(word_list)
word_list.sort()
print(word_list)

print("Alphabetically sorted hyphen separated list is : ")
print("-".join(word_list))



#6
def student_data(student_id,**kwargs):
    print(f'\nstudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name]}")

    if 'student_name' and 'student_class' in kwargs:
        print(f"\nStudent Name: $ {kwargs['student_name']}")
        print(f"Student Class: $ {kwargs['student_name']}")

student_data(student_id= 'PEC12', student_name='Shlok Matha'
student_data(student_id= 'PEC12', student_name='Shlok Matha', student_class = 'V'




#7
class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student)
print(isinstance(marks1, Marks)
print(isinstance(marks1, Marks)
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print (issubclass(Student, object)
print(issubclass(Marks, object)



#8
def findTriplets(arr, n):   
found = True

for i in range(0, n-2):
   for j in range(i+1, n-1):
      for k in range(j+1, n):
         if (arr[i] + arr[k] == 0):
            print(arr[i], arr[j], arr[k])
            found = True

# if no triplet with 0 sum
# found in array
if (found == False):
   print("not exist")

arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr, n)



#9
def checkBalance(str1):
    count=0
    ans=False
    for i in str1:
        if i=="(" or i=="{" or i=="[":
            count+=1
        elif i == ")" or i=="}" or i=="]":
            count-=1
        if count<0:
            return ans
    if count==0:
        return not ans
    return ans
str1=input('Enter a string of brackets:')
print('Given string is balanced:',checkBalance(str1))













