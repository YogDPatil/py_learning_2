#Concatenation

print(10+10)  #20 valid
print(10.5+12.0) # 22.5 valid
print(10+10.5)  # 20.5  valid

print('welcome'+'python') #welcomepython

print(True+5)   # 6 valid in python true = 1 and false = 0
print(False+5)   # 5 valid
print(True+True)  # 2 valid

# python does not allow + operator to concatinate two diff data types
print(10+'welcome') #Not valid bcoz 2 values are different type
print(10.5+'welcome') #Not valid bcoz 2 values are different type
print(True+'welcome')  #Not valid bcoz 2 values are different type