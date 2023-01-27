#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("Hey! How much was the bill? ")
tip = input("And what percentage will the tip be? ")
people = input("How many people will pay the bill? ")
total = float(bill) * (1 + int(tip)/100.0)
share = round(total / int(people),2)
print(f"Everybody pays {share} $")