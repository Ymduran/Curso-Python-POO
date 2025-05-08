"""

Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw"
"This is a test        --> "This is a test"
"This is another test" --> "This is rehtona test"


"""

def spin_words(sentence):
    text = []
    text_final = ""
    for l in sentence:
        if l != " " :
            text.append(l)
        else:
            if len(text) >= 5:
                text.reverse()


            for i in text:
                text_final += i
            text_final+=" "
            text = []

    if len(text) >= 5: #La última palabra
        text.reverse()
    for i in text:
        text_final+=i

    return text_final




if __name__ == '__main__':
    print(spin_words("Welcome"))
    print(spin_words("to"))
    print(spin_words("CodeWars"))
    print(spin_words("Hey fellow warriors"))
