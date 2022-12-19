# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#TRUE LOVE
name=name1.lower()+name2.lower()
T=name.count("t")
R=name.count("r")
U=name.count("u")
E=name.count("e")
t_score=T+R+U+E
L=name.count("l")
O=name.count("o")
V=name.count("v")
E=name.count("e")
l_score=L+O+V+E
love_score=str(t_score)+str(l_score)
love_score=int(love_score)
if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40<love_score<50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
