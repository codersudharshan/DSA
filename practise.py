'''
pizza = int(input("Enter the no of pizzas bought: "))
puffs = int(input("Enter the no of puffs bought: "))
cooldrinks = int(input("Enter the no of cool drinks bought: "))

print("Bill Details")
summ = pizza*100 + puffs*20 + cooldrinks*10
print(f"-No of pizzas:{pizza}")
print(f"-No of puffs:{puffs}")
print(f"-No of cooldrinks:{cooldrinks}")
print(f"Total Price ={summ}")
print("ENJOY THE SHOW!!!")

'''
'''
print("Enter the digits : ")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

#output:
print(f"{a}"+ "-" + chr(a))
print(f"{b}"+ "-" + chr(b))
print(f"{c}"+ "-" + chr(c))
print(f"{d}"+ "-" + chr(d))

'''
'''
CSE = int(input("Enter the no of students placed in CSE: "))
ECE = int(input("Enter the no of students placed in ECE: "))
MECH = int(input("Enter the no of students placed in MECH: "))

#output

print("- Highest placement")
maxx = max(CSE, ECE, MECH)
if CSE == maxx:
    print("CSE")
if ECE == maxx:
    print("ECE")
if MECH == maxx:
    print("MECH")

'''

#taking n as a input as printing its output of multiple till 10
'''
n = int(input("Enter the number: "))


for i in range(0, 11):
    multi = n * i
    print(f"{n} x {i} = ",multi)
'''

#Take a string as input and count how many times each character appears:
'''
inputt = str(input("Enter a string: "))

count = {}

for i in inputt:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for key, values in count.items():
    print(f"{key}: {values}")
'''
#counter way
'''
from collections import Counter

strr = str(input("Enter a string : "))

count = Counter(strr)

for key, values in count.items():
    print(f"{key} : {values}")
'''
'''
#Take a sentence as input and reverse the order of words (not the letters inside):

n = str(input("Enter a sentence: "))

splited = n.split()
reversed_words = splited[::-1]
join_back = " ".join(reversed_words)

print(join_back)
'''
'''
n = str(input("Enter the string : "))

count = {}

for i in n:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for keys, values in count.items():
    print(f"{keys} : {values}")
    for i in keys, values in count.items():
        if count[i] > count[i + 1]:
            print(f"the second highest value is : {count[i]}")
'''
'''
import string 

n = str(input("Enter a string: "))
letters = set(n.lower())
alphabets = set(string.ascii_lowercase)

if alphabets.issubset(letters):
    print(True)
else:
    print(False)
'''
'''
def factorial(n):
    result = 1

    i = 1
    while i < n:
        multi = n * result

    return result


'''
'''
#first question:
s = str(input("Enter a string: "))
n = len(s)
l = 0
r = n - 1

while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        print(False)
        break
else:
    print(True)
'''
'''
#third question
s = str(input("Enter a string: "))
seen  =  {}
n = len(s)

for i in range(n):
    if s[i] in seen:
        seen[s[i]] += 1
    else:
        seen[s[i]] = 1

for keys, values in seen.items():
    print(f"{keys}, {values}")

'''
'''
nums = list(map(int, input("Enter a list of nums: ").split()))

unique_nums = list(set(nums))

unique_nums.sort(reverse = True)

print(unique_nums[1])
'''
'''
#fibonacii series:
x = int(input("Enter lower bound: "))
y = int(input("Enter Upper Bound: "))

a, b = 0, 1

while a <= y:
    if a > x:
        print(a, end = " ")

    next = a + b
    a = b
    b = next
'''
'''
#Uniuqe strings and thier counts:

s = input("Enter the words: ").split()
Unique_s = set(s)
count = {}
for i in range(len(s)):
    if s[i] in count:
        count[s[i]] += 1
    else:
        count[s[i]] = 1
print(Unique_s)
for keys, values in count.items():
    print(f"{keys}, {values}")
'''
'''
#bill question: 

pizza = int(input("Enter the number of pizzas: "))
puffs = int(input("Enter the number of puffs: "))
cool_drinks = int(input("Enter the number of cool drinks: "))

summ = pizza * 100 + puffs * 20 + cool_drinks * 10

print("YOUR BILL SIR")
print(f"YOUR TOTAL AMOUNT IS : {summ}")
'''
'''
liters = float(input("Enter the no of liters: "))
distance = float(input("Enter the no of distance traveled :"))

if liters <=0 or distance <=0:
    print("Invalid Input")
else:
    l_per_100km = (liters / distance)* 100

    miles = distance * 0.621371
    gallons = liters * 0.264172
    mgp = miles / gallons 

    print(f"Liters/100: {l_per_100km:.2f}")
    print(f"Miles/gallon: {mgp:.2f}")
'''
'''''''''
n = list(map(int, input("Enter ASCII codes separated by space: ").split()))

for code in n:
    print(f"{code} - {chr(code)}")
'''
'''
# Number of students
no_s = int(input("Enter the number of students: "))
# Shelf capacity
k = int(input("Enter the maximum no of books a shelf can hold: "))

# Input list of books for each student
no_books = []
for i in range(no_s):
    temp = int(input(f"Enter the no of books for student {i+1}: "))
    no_books.append(temp)

n_shelves = 0
carry = 0

# Loop through each student
for i in range(no_s):
    books = no_books[i] + carry   # add carry from previous student

    # Shelves filled by current student's books
    n_shelves += books // k  

    # Update carry (leftover books)
    carry = books % k  

    # Special case: if last student → discard leftover
    #if i == no_s - 1:
     #   carry = 0  

print("Total shelves completely filled:", n_shelves)

'''
'''
n = input("Enter a string: ")
vovels = ["a", "e", "i", "o", "u"]
count = 0 

for i in range(len(n)):
    if n[i].lower() in vovels:
        count += 1

print(count)
'''
'''
n = list(map(int, input("Enter the numbers: ").split()))

uniuqe_nos = sorted(set(n),  reverse=True)

if len(set(n)) == 1:
    print(- 1)
else:
    print(uniuqe_nos[1])
'''
'''
strr = str(input("Enter the string: ")).replace(" ", "").lower()
n = len(strr)
l = 0
r = n - 1
is_planidrome = True

while l < r:
    if strr[l] != strr[r]:
        is_planidrome = False
        break
    l += 1
    r -= 1

print(is_planidrome)  
'''
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
'''
'''
s = str(input("enter : "))
splited = s.split()
len_of_last = splited[-1]
print(len(len_of_last))
'''

i = 1
j = 4
mid = (i + j) // 2
print(mid)