counter =1
while True:
  lyrics = input("In the ______ of the night")
  if lyrics == "middle":
    print("You got it")
  else:
    print("Nope, try again")
    counter +=1
  if lyrics == "middle":
    break
print("You got it right in",counter,"attempt(s)")

