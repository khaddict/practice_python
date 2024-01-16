'''
Exercise 22

Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

Extra :

Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.
'''

def exercise_22():
    '''
    Exercise 22 method
    '''
    empty_dict = {}

    with open('nameslist.txt', 'r', encoding="utf-8") as open_file:
        nameslist = open_file.read().split()
        for name in nameslist:
            if name not in empty_dict:
                empty_dict[name] = 0
            if name in empty_dict:
                empty_dict[name] += 1

    print(empty_dict)

def extra_1():
    '''
    Extra 1 method
    '''
    empty_dict = {}

    with open('Training_01.txt', 'r', encoding="utf-8") as open_file:
        images_list = open_file.read().split()
        for line in images_list:
            parameters_list = line.strip().split("/")
            if parameters_list[2] not in empty_dict:
                empty_dict[parameters_list[2]] = 0
            if parameters_list[2] in empty_dict:
                empty_dict[parameters_list[2]] += 1

    print(empty_dict)

def main():
    '''
    Main method
    '''
    print("Exercise 3 :\n")
    exercise_22()
    print("\nExtra 1 :\n")
    extra_1()

if __name__ == "__main__":
    main()
