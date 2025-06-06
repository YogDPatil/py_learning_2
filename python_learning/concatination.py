# CONCATINATION 1

print(10+10)  #20 valid
print(10.5+12.0) # 22.5 valid
print(10+10.5)  # 20.5  valid

print('welcome'+'python') #welcomepython

print(True+5)   # 6 valid in python true = 1 and false = 0
print(False+5)   # 5 valid
print(True+True)  # 2 valid

# python does not allow + operator to concatinate two diff data types
# print(10+'welcome') #Not valid bcoz 2 values are different type
# print(10.5+'welcome') #Not valid bcoz 2 values are different type
# print(True+'welcome')  #Not valid bcoz 2 values are different type



# CONCATINATION - FORMATING OUTPUT

# name="john"
# age=30
# sal=5000.50
name,age,sal="john",30,5000.50

#Approach 1
# print(name)
# print(age)
# print(sal)
#print(name,age,sal)


#Approach2
# Name is: john
# Age is: 30
# Sal is: 5000.5
# print("Name is:",name)
# print("Age is:",age)
# print("Sal is:",sal)

#Approach3
#print("Name is:%s  Age is:%d  Salary is:%g" %(name,age,sal))

#Approach4   {}
# print("Name is:{}  Age is:{}  Salary is:{}" .format(name,age,sal))
# print("Age is:{} Name is:{}   Salary is:{}" .format(age,name,sal))

#Approach5
print(f"Name is: {name} Age is: {age} Salary is: {sal}")


