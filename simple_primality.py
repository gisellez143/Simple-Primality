"""
Filename: simple_primality.py
Author: <Giselle, Zavala>
Created: <3/10/2026>
Instructor: Holtslander
"""

def prime():
    # Write your code here
    num = input("Enter a non negativew whole number: \n")
    num= int(num)
    prime = True
    for i in range(1, num):
        if num % i == 0:
            primew = False
    if num < 1:
        print(num, "is not a prime number")
    else:
        print(num, "is not a prime number")
def main():
    print("This program will determine the primality of a number.")
    running = "y"
    while running == "y":
        prime()
        running = input("Check another number? (y/N)\n").lower()
    print("Thank you for using this primality program!")

if __name__ == "__main__":
    main()