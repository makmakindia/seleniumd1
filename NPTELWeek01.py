
#1. Which of the arithmetic operators given below cannot be used with ‘strings’ in Python?
s1,s2 = "str1","str2"
result =""

result=s1+s2
print(result)
result=2*s2
print(result)
# result=s1-s2
# print(result) # TypeError: unsupported operand type(s) for -: 'str' and 'str
print("--------------------------- 2 ------------- -------------------------------")
# 2. When the following statement is executed, what type of error is obtained?
# Var@check=11
# print(var@check)
# syntax error

print("-------------------------------3 --------- -------------------------------")
# 3. Two variables X and Y were assigned the following values initially. X = 3 and Y = 6. Which of the following statements will help swap the values between these two variables?

x,y=1,2
print(x,y)
x,y=y,x
print(x,y)

print("-------------------------- 4 -------------- -------------------------------")

#. 4. From the following set of statements, what will be the value of variable y in the final print statement?
y=1**2**3**2
print(y)
print("-------------------------- 5 -------------- -------------------------------")
# 5. Consider j = 5 and k = 11. We change the values from j = 7 and k remains constant.

j,k=5,11
print(j|k)
j=7
print(j|k)

print("--------------------------------------6- -------------------------------")
# 6. What would be the output of the following statements?
log_exp= not not True and False or not False
print(log_exp)
print("-------------------------- 7 -------------- -------------------------------")
# 7. What does k = 4%7 evaluate to and what is the type of variable k?
k=4%7
print(k)
print(type(k))

print("-------------------------- 8 -------------- -------------------------------")
# 8. j = 6 and g = 3.3. If normal division and floor division was done between j and k, what would be the type of the resultant variable?
j,g=6,3.3
print(j/g)
print(j//g)
print("-------------------------- 9 -------------- -------------------------------")
# 9. Consider two answers to a question; answer1 and answer2. What is the output of the following set of statements?
ans1=True
ans2=False
print(ans1*ans2)
print("-------------------------- 10 -------------- -------------------------------")
# 10. Consider the list of instructions and resulting outputs given below. Pick the set that is incorrect.

print("Good",end="")
word1="Trail"
print("Word is %s"%word1)
num1=23
print("Number:%f"%num1)
print("ready\nsteady\ngo")
