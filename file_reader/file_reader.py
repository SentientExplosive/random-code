def word_list_maker(name):
    '''Creates the list of words found in the file, removing whitespace and extraneous characters.'''
    word_list = []
    file = open(f'{name}.txt')
    for line in file:
        for word in line.split():
            word = word.lower()
            for w in word.split(','):
                w = w.strip(" ,.\":?")
                if w == '':
                    continue
                else:
                    word_list.append(w)

    return word_list

def compare_words(list1, list2):
    '''Function to compare the words found in both files, and copies the shared words to a new list,
    which is returned at the end of the function.'''
    shared_words = []
    for word in set(list1):
        if word in list2:
            shared_words.append(word)
    
    return shared_words

def frequency_finder(list1, list2, shared_list):
    '''Finds the frequency of the words shared between the given lists.'''
    # Initialize the frequency dictionary
    frequency = {}
    for word in shared_list:
        frequency[word] = 0
    
    # Iterate through list 1
    for key in shared_list:
        for word in list1:
            if key == word:
                frequency[key] += 1

    # Iterate through list 2
    for key in shared_list:
        for word in list2:
            if key == word:
                frequency[key] += 1

    return frequency

def sort_dict(old_dict):
    '''Sorts the dictionary by value.
    (I know this would be a lot simpler with a lambda function, I don't entirely know how they work yet though)'''
    new_dict = {}

    # Get a sorted list of the values in the dict
    values = []
    for val in old_dict.values():
        values.append(int(val))
    values = sorted(values, reverse=True)

    # Compare the values that correspond with each key to the sorted values in order
    # Add the key and its value to the new dictionary
    for i in range(len(old_dict.keys())):
        for key in old_dict.keys():
            if old_dict[key] == values[i]:
                new_dict[key] = values[i]
    
    return new_dict

def printout(dict):
    '''Prints out the input dictionary'''
    print("\nShared Words, Sorted By Frequency")
    for key in dict.keys():
        print(f"{key}: {dict[key]}")

def main():
    '''The main program'''
    # Asks the user for the names of the 2 files, without the file extension.
    file1_name = input("Enter the name of the first file (without the file extension): ")
    file2_name = input("Enter the name of the second file (without the file extension): ")
    
    # Gets lists of each individual word in the files using the word_list_maker() function.
    file1_words = word_list_maker(file1_name)
    file2_words = word_list_maker(file2_name)
    
    # Finds the shared words in each list
    shared_words = compare_words(file1_words, file2_words)
    
    # Finds the Frequency of the shared words, saves as a dictionary
    word_frequency = frequency_finder(file1_words, file2_words, shared_words)
    
    # Sort the dict by value.
    final_frequency = sort_dict(word_frequency)
    
    # Print the sorted dict
    printout(final_frequency)


if __name__== "__main__":
    main()
