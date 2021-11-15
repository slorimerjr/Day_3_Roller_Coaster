




# You must be 120 cm to ride
# Ticket cost varies based on age (12 and under = 5; 13 - 17 = 7; 18+ = 12)
# Riders have the option of taking a photo for an additional $3
print("Welcome to the roller coaster!")
bill = 0
height = int(input("How tall are you (cm)? "))
if height >= 120:
  age = int(input("How old are you? "))
  if age <= 12:
    print("Child tickets are $5.")
    bill = 5
  elif age <= 17:
    print("Youth tickets are $7.")
    bill = 7
  else:
    print("Adult tickets are $12.")
    bill = 12
    
  wants_picture = input("Would you like to take a picture? Y or N ")
  if wants_picture == "Y":
    bill += 3

  print(f"Your total today will be ${bill}.")

else:
  print("Sorry, you need to be taller to ride the ride.")



