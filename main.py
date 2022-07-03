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
def pascal_triangle(num):
   trow = [1]
   y = [0]
   for x in range(max(num,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return num>=1
pascal_triangle(5)



#4
import string
def ispangram(sentence, alphabet=string.ascii_lowercase):
    return set(alphabet) <=set(sentence.lower())

print(ispangram(input('Sentence: ')))



#5
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))



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
class validity:
 
    def f(str):
        a= ['()', '{}', '[]']
  
        while any(i in str for i in a):
            
            for j in a:
                str = str.relace(j,'')
        return not str
s = input('enter: )

print(s, "-", "is balanced"

     if validity.f(s) else "is unbalnced")














