# love score calculator
your_name = input("What is your name :-").lower()
their_name = input("What is their name :-").lower()

# counting no. of times t r u e appears
t=your_name.count("t")+their_name.count("t")
r=your_name.count("r")+their_name.count("r")
u=your_name.count("u")+their_name.count("u")
e=your_name.count("e")+their_name.count("e")
digit_1 = t+r+u+e

# counting no. of times l o v e appears
l=your_name.count("l")+their_name.count("l")
o=your_name.count("o")+their_name.count("o")
v=your_name.count("v")+their_name.count("v")
e=your_name.count("e")+their_name.count("e")
digit_2 = l+o+v+e

# calculation love persentage
love_persentage = int((digit_1*10)+digit_2)

# pinting results 
if love_persentage<10 and love_persentage>90:
  print("You are like Coke and Mentos to each other ")
  print(f"Your love persentage is {love_persentage}%")
elif love_persentage>40 and love_persentage<50:
  print("You are compatible with each other")
  print(f"Your love persentage is {love_persentage}%")
else:
  print(f"Your love persentage is {love_persentage}%")

input()