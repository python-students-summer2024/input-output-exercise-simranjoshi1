"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    # write your code here.
    vegetable = input("Enter your favorite vegetable: ")
    print("Interesting! I also love "+vegetable+"!")


def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    # write your code here.
    number = input("Enter your favorite number: ")
    print("Interesting! I also love "+number+"!")

def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    # write your code here.
    name = input("Enter your name: ")
    zodiac_sign = input("Enter zodiac sign: ")
    print("Interesting! My name is also "+name+", and I'm also a "+zodiac_sign+"!")


def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    # write your code here.
    name = input("Enter name: ")
    age = input("Enter age: ")
    print("Interesting! My name is also "+name+", and I'm also "+age+" years old!")