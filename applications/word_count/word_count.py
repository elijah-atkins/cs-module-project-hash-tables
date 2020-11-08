def word_count(s):
    #create new dictionary for each string
    dictionary = {}
    #list of characters to strip out of string
    special_characters = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\\"]
    #Remove all caps from string
    lower_case = s.lower()
    #Remove unwanted characters from string
    for i in special_characters:
        lower_case = lower_case.replace(i, "")
    #turn processed string into an array of words
    split_string = lower_case.split()

    #add each word in word array into the dictionary
    for word in split_string:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary.keys()



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))