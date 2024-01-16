'''
Exercise 23 : File Overlap  

Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)
'''

def exercise_23():
    '''
    Exercise 23 method
    '''

    happynumbers_list = []
    primenumbers_list = []
    overlapping_list = []

    with open('happynumbers.txt', 'r', encoding="utf-8") as open_file:
        happynumbers_data = open_file.read().split()
        for i in happynumbers_data:
            happynumbers_list.append(i)

    with open('primenumbers.txt', 'r', encoding="utf-8") as open_file:
        primenumbers_data = open_file.read().split()
        for i in primenumbers_data:
            primenumbers_list.append(i)

    for i in happynumbers_list:
        if i in primenumbers_list:
            overlapping_list.append(i)

    print(f"overlapping_list : {overlapping_list}")

def main():
    '''
    Main method
    '''
    print("Exercise 23 :\n")
    exercise_23()

if __name__ == "__main__":
    main()
