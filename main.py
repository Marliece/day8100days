print("Wholesome Positivity Machine")
print()
name = input("Who are you? ")
print()
achieve = input("What do you want to achieve? ")
print()
feel = input("On a scale of 1 - 10 how do you feel today? (1: 😢, 10: 😁) ")
print()
if feel == "1" or feel == "2" or feel == "3" or feel == "4" or feel == "5" or feel == "6" or feel == "7" or feel == "8" or feel == "9" or feel == "10":
  print("Hey", name, ", keep your chin up! Today you're going to", achieve, "in the most amazing way, simply by being you - YOU ROCK!")
else:
  print("Please enter a number between 1 and 10")
print()
print()
weekDay = input( "What day of the week is it? ")
if weekDay == "Monday" or weekDay == "monday":
  print("Happy Monday!")
  print(weekDay, "is a great day to start the week with a smile!")
elif weekDay == "Tuesday" or weekDay == "tuesday":
  print("Happy Tuesday!")
  print(weekDay, "is a great day to start the day with a smile!")
elif weekDay == "Wednesday" or weekDay == "wednesday":
  print("Happy Wednesday!")
  print(weekDay, "is a great day to start the day with a smile!")
elif weekDay == "Thursday" or weekDay == "thursday":
  print("Happy Thursday!")
  print(weekDay, "is a great day to start the day with a smile!")
elif weekDay == "Friday" or weekDay == "friday":
  print("Happy Friday!")
  print(weekDay, "is a great day to start the day with a smile!")
elif weekDay == "Saturday" or weekDay == "saturday":
  print("Happy Saturday!")
  print(weekDay, "is a great day to start the weekend with a smile!")
elif weekDay == "Sunday" or weekDay == "sunday":
  print("Happy Sunday!")
  print(weekDay, "is a great day to end the week with a smile!")
else:
  print("Please enter a day of the week")
print()
favorites = input("What are some of your favorite things? ")
print()
print("Thanks for sharing!")
print()
print("The affirmation of the day is: It is", weekDay, "and I am going to", achieve, "and I am going to do it with", favorites, "in my mind as a motivation!")
print("Have a great", weekDay, "and keep smiling!")
print()
print("Thank you for using the Wholesome Positivity Machine!")
