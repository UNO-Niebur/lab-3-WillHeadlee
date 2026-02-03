#ApproxPi.py
#Name: William Headlee
#Date: 2/2/26
#Assignment: Lab 3
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal precision (up to 10)

  precision = int(input("How precise would you like to be (up to 10, anything over 4 takes a bit): "))
  roundedPi = round(realPi, precision)
  attempts = 0
  calculatedPi = 0
  series = [1]
  n = 1
  alternation = -1
  print("Calculating... ")

  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of precision is reached

  while roundedPi != round((calculatedPi*4), precision):
    calculatedPi = 0
    for i in series:
      calculatedPi += i
    attempts += 1
    n += 2
    series.append((1/n)*alternation)
    alternation *= -1

  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
