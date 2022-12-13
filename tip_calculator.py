#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill= float(input("what was the total bill? "))
percent= int(input("what percentage tip would you like to give ? 10 or 12 or 15? "))
people=int(input("how many will split the bill? "))
final_bill= (bill/people)*(1+(percent/100))
f_bill= "{:.2f}".format(final_bill)
print(f"each person should pay a bill of {f_bill} dollars")