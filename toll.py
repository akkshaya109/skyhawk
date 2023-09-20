import builtins
from datetime import datetime
from pytz import timezone

des = input("Enter the destination - ")
current = datetime.now(timezone("Asia/Colombo"))
hour = current.hour
if 6 < hour < 8 or 14 < hour < 15 or 18 < hour < 20:
  print("HIGH TOLL - $20")
  print("PEAK TIME")
  choices = [bus, train, car]
  print(choices)
  choice = input("Enter one - ")
  if choice == "bus":
    print("Bus times - ")
    print("9am")
    print("10:45am")
    print("12:30pm")
    print("2:00pm")
    print("4:25pm")
    print("6:50pm")
  elif choice == "train":
    print("Train times")
    print("9am")
    print("10:45am")
    print("12:30pm")
    print("2:00pm")
    print("4:25pm")
    print("6:50pm")
  else:
    print("If you wish to go by car then you must pay the toll and carpool")
    print("Go to Uber.com")
else:
  print("LOW TOLL - $5")
  print(
      "Although the toll is low we recommend to carpool or use public transportation - "
  )
  yes1 = input("Do you wish to carpool? (y/n) - ")
  if yes1 == "y":
    print("Go to Uber.com")
  else:
    yes2 = input("Do you wish to use public transport (y/n) - ")
    if yes2 == "y":
      torb = input("Do you wish to go by train or bus")
      if torb == "bus":
        print("Bus times - ")
        print("9am")
        print("10:45am")
        print("12:30pm")
        print("2:00pm")
        print("4:25pm")
        print("6:50pm")
      else:
        print("Train times")
        print("9am")
        print("10:45am")
        print("12:30pm")
        print("2:00pm")
        print("4:25pm")
        print("6:50pm")
    else:
      print("Have a nice day")
