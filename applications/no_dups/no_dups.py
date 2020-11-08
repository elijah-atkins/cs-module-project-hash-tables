def no_dups(s):
    word_list = []
    results = ""
    split_string = s.split()
    for word in split_string:
        if word not in word_list:
            word_list.append(word)
            results += f'{word} '
            
    return results

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))