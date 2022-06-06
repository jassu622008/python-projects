import random

rand_num = random.randint(1, 100)

while True: 
  a = int(input("Enter The guess number: "))
  if a > rand_num:
    print("too large")
    
  if a < rand_num:
    print("too small")
    
  if a == rand_num:
    print("you won!")
    break
