#TempConvert.py
#Name: William Headlee
#Date: 2/2/26
#Assignment: Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  print("Fehrenheit to Celsius Converter")
  
  tempF = int(input("Provide a temperature in F: "))

  tempC = round((tempF - 32)/1.8, 1)

  print(tempF, "is", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
