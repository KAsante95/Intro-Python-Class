from datetime import *
#Look up today’s date
today = date.today()

#Ask a friend when their birthday is 
dob_str = input("What is your Date of Birth? mm/dd/yyyy")

#Determine if today is your friend’s birthday
dob_data = dob_str.split("/")
dob_day = int(dob_data[0])
dob_month = int(dob_data[1])
dob_year = int(dob_data[2])
dob = date(dob_year, dob_month, dob_day)

this_year = today.year
next_birthday = date(this_year, dob_month, dob_day)

#If today is your friend’s birthday, say “Happy Birthday!” 
#Otherwise, tell them “Today is not your Birthday”
if today == next_birthday:
    print("Happy Birthday")
else:
    print("Today is not your Birthday")



####################################################################

welcome = "Welcome LOL. Can I tell you a joke?"
print(welcome)
print("welcome")

joke = '''I was wondering why the ball kept
getting bigger and bigger,
and then it hit me!'''
print(joke)

tornado_joke = "What do you get if you say \"tornado\" ten times backward and forward?...A real tongue twister!"
#tornado_joke = 'What do you get if you say "tornado" ten times backward and forward?...A real tongue twister!'
print(tornado_joke)

print("I had a talking parrot.\n But it didn’t say it was hungry,\n\n so it died")






