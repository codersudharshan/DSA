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