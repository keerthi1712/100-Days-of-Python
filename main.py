# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_remaining= 90-int(age)

x= (years_remaining)*365
y= int((x*52)/365)
z= int((x*12)/365) 
print(f'You have {x} days, {y} weeks, and {z} months left.')



