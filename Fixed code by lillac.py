ready = input("This is a math trick. Are you ready? Y/N ")
if ready == "Y":
  print("Ok. You will now begin the trick. Once you have each step worked out, type Ok.")
  a=input("Think of a number between 1 and 10.")
else:
  print("Well, go away then.")
  
if a == "Ok":
  print("Next step")
  b = input("Multiply that number by 2. ")
  
if b == "Ok":
  print("Next step")
  c = input("Now, times that new number by 5. ")
  
if c == "Ok":
  print("Next step")
  d = input("Divide that new number by your original number. ")
  
if d == "Ok":
  print("Final step")
  e = input("Subtract 7 from that number. ")
  
if e == "Ok":
  print("Well done! Now I will guess your final answer.")
  f = input("Is your answer 3? Y/N ")
  
if f == "Y":
  print("Yay, I guessed your number!")
  
else:
  print("Well you must have messed up the calculations somewhere. Redo this with the same number.")
