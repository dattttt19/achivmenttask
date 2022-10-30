def tempConversion(temp, tempUnit):#firstly making def function
    if tempUnit == 'C':  # checks if temperature unit is C
        convertedTemperature = ((9 * temp) / 5 + 32)  # converts temperature to fahrenheit
    
    elif tempUnit == 'F': # checks if temperature unit is F
        convertedTemperature = ((temp - 32) * 5 / 9)  # Using converts temperature to celcius formula
        
    return convertedTemperature  # returns the converted temperature

def speedConversion(speed, speedUnit):
    if speedUnit == 'kmh':  # checks if speed unit is kmh
        convertedSpeed = 0.6214 * speed  # Using converts speed to miles per hour fromula
    
    elif speedUnit == 'mph': # checks if speed unit is mph
        convertedSpeed = speed * 1.60934;  # Using converts speed to kilometer per hour fromula
        
    return convertedSpeed  # returns the converted speed



# below code is the main section for taking inputs and passing to function
def main():
    conversionType = int(input("What do you want to convert: Enter 1 for temperature or 2 for speed :: "))
    if conversionType == 1:
        inputTemperature = float(input("\nEnter the temperature you want to convert :: "))
        tempUnit = input("Enter the current unit for the temperature :: ")
        tempUnit = tempUnit.strip().lower()  # converts unit to lowercase and removes if any trailing or leading spaces
        # below line calls function tempConversion and prints the returned value
        print("Converted temperature is :: {:.2f}".format(tempConversion(inputTemperature, tempUnit)))
        
    elif conversionType == 2:    
        inputSpeed = float(input("\nEnter the speed you want to convert :: "))
        speedUnit = input("Enter the current unit for the speed :: ")
        speedUnit = speedUnit.strip().lower() # converts unit to lowercase and removes if any trailing or leading spaces 
        # below line calls function speedConversion and prints the returned value
        print("Converted speed is :: {:.3f}".format(speedConversion(inputSpeed, speedUnit)))
        
    else:
        print("Wrong input entered for conversion!!")

main()    