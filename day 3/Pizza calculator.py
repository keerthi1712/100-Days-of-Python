# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
bill=0
if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill=15+2+1
        else:
            bill=15+2
    else:
        if extra_cheese == "Y":
            bill=15+1
        else:
            bill=15        
elif size=="M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill=20+3+1
        else:
            bill=20+3
    else:
        if extra_cheese == "Y":
            bill=20+1
        else:
            bill=20  
elif size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill=25+3+1
        else:
            bill=25+3
    else:
        if extra_cheese == "Y":
            bill=25+1
        else:
            bill=25  
print(f"Your final bill is: ${bill}.")

