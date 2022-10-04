
number = 2
color = "orange"

greater_than_5 = number > 5
color_is_orange = color == "orange"
color_not_yellow = color != "yellow"
between_5_and_10 = number > 5 and number < 10

print(greater_than_5)
print(color_is_orange)
print(color_not_yellow)
print(between_5_and_10)

########################################################

if number > 5:
    print("number is greater than 5")
    
if color == "orange":
    print("the color is orange!")
else:
    print("the color is not orange...")
    
grade_score = 70

if grade_score >= 90 and grade_score <= 100:
    print("Grade: A")
elif grade_score >= 80 and grade_score <= 89:
    print("Grade: B")
elif grade_score >= 70 and grade_score <= 79:
    print("Grade: C")
elif grade_score >= 60 and grade_score <= 69:
    print("Grade: D")
elif grade_score >= 50:
    print("Grade: F")
else:
    print("Off the grade scale!")
