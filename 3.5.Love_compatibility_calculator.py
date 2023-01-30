# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower=name1.lower()
name2_lower=name2.lower()
name_together=name1_lower+name2_lower
T=name_together.count("t")
R=name_together.count("r")
U=name_together.count("u")
E=name_together.count("e")
L=name_together.count("l")
O=name_together.count("o")
V=name_together.count("v")
E=name_together.count("e")
score = (T+R+U+E)*10+L+O+V+E
if score <10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

