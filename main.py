n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")




x = input('Enter a word or sentence: ')

w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes, it is a palindrome")
else:
    print("No, it's not a palindrome")




def pascal_triangle(num):
   trow = [1]
   y = [0]
   for x in range(max(num,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return num>=1
pascal_triangle(5)



str = input('Write a word:')
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False




items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))




class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0




