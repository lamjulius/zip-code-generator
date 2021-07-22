import random
import time

def script():
  x = int(input("How many zip-codes would you like to have?"))
  for i in range(0, x):
    n = random.randint(10**4, 10**5)
    print(n)
while True:
  restart = str(input("Press Enter to continue or type X and press Enter to shut down"))
  if restart == "" \
                "":
    script()
  if restart == "x":
    print("See you next time!")
    time.sleep(2)
    quit()
