print("Lets begin with the code")
Owner = input ("Press start :")


import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i==0: 
            return False
    return True
    
            
def sum_of_primes(start, end):
    return sum(n for n in range(start, end + 1) if is_prime(n))


def length_converter(value, direction):
    direction = direction.upper()  # Convert to uppercase to avoid errors
    conversion_factor = 3.28
    if direction == 'M': # convert meter to feet
        return round(value * conversion_factor, 2)
    elif direction == 'F': # convert feet to meter
        return round(value / conversion_factor, 2)
    return "Invalid direction"


def consonant_counter(text):
    consonant = 0
    num_vowels = "aeiouAEIOU" # IF we use this we do not have to use lower or upper common
    for ch in text:     # convert text to lowercase
        if ch.isalpha() and ch not in num_vowels: # check if it's a consonant
            consonant+= 1
    return consonant# return count back

def min_max_finder(numbers):
    if not numbers: #checks if the numbers list is empty or not.
        return "No numbers provided."
    return min(numbers), max(numbers)

def is_palindrome(text):
    if text == text[::-1]: #Check if the string is the same forwards and backwards
        return True
    else:
        return False
    #word counter 
import requests 

def Count_word(TextFile_url): # fetch the text from the url
    response = requests.get(TextFile_url) #ensure the request is successful
    if response.status_code == 200: #The request was successful, and the response contains the requested data
        text = response.text.lower()
        lst = ["the","was","and"]
        word_count= {word: text.count(word) for word in lst}
        return word_count
    else:
        return f"Failed to fetch the file. Status code: {response.status_code}"



def main():
    while True:
        print("\nMenu:")
        print("select a function (1-7)")
        print("1. Sum of prime numbers")
        print("2. Length converter") 
        print("3. Count consonants")
        print("4. Find minimum and maximum")
        print("5. Check palindrome")
        print("6. Word counter")
        print("7.Exit")
        
        choice = input("Choose an option you want to know: ")

        if choice == '1':
            try:
                start = int(input("Starting Value: "))
                end = int(input("End Value: "))
            
                print("Sum:", sum_of_primes(start, end))
            except ValueError:
                print("Please enter valid numbers.")

        elif choice == '2':
            try:
                value = float(input("Enter a value: "))
                print("Choose conversion type:")
                print("M = Meters to Feet")
                print("F = Feet to Meters")
                direction = input("Enter M or F: ").upper()
                print("Converted:", length_converter(value, direction))
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            text = input("Enter text : ")
            results = consonant_counter(text)
            print(f"number of consonants : {results}")

        elif choice == '4':
            try:
                numbers = list(map(int, input("Enter numbers separated by space: ").split()))
                if numbers:
                    smallest, largest = min_max_finder(numbers)
                    print("The minimum value:", smallest)
                    print("The maximum value", largest)
                else:
                    print("No numbers entered.")
            except ValueError:
                print("Please enter only numbers.")

        elif choice == '5':
            text = input("Enter text: ")
            print("Palindrome:", is_palindrome(text))

        elif choice == '6':
            url = input("Enter a URL :").strip()
            try:
                results = Count_word(url)
                print(f'word count: {results}')
            except requests.exceptions.RequestException as e:
                print(f'Error fetching the file : {e}')
                        

        elif choice == '7':
            print("Thank you.....Goodbye!")
        else : 
            print("invalid")
        choice = input("do you want to continue your programm (yes/no) : ")
        if choice != 'yes': # != it's mean it does not agree
            print("THANK YOU! ")
            break
            

if __name__ == "__main__":
    main()
