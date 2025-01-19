# Define global conversion factors  
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  

def convert_to_celsius(fahrenheit):  
    """Convert Fahrenheit to Celsius."""  
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  

def convert_to_fahrenheit(celsius):  
    """Convert Celsius to Fahrenheit."""  
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32  

def main():  
    while True:  # Keep the program running until a valid input is received  
        try:  
            temperature = float(input("Enter the temperature to convert: "))  
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()  
            if unit == 'C':  
                converted_temperature = convert_to_fahrenheit(temperature)  
                original_unit = 'F'  
            elif unit == 'F':  
                converted_temperature = convert_to_celsius(temperature)  
                original_unit = 'C'  
            else:  
                raise ValueError("Invalid unit. Please enter 'C' or 'F'.")  
                
            # Display the result  
            print(f"{temperature:.1f}°{unit} is {converted_temperature:.1f}°{original_unit}")  
            break  # Exit the loop after successful conversion  
        except ValueError as e:  
            print(f"Error: {e}. Please enter a valid numeric value.")  

if __name__ == "__main__":  
    main()
