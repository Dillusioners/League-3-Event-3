# method for uppercasing everything
def capitalize(text):
    text = text.upper()
    print(f"Formatted text: \n{text}")

# method for lowercasing everything
def lowercase(text):
    text = text.lower()
    print(f"Formatted text: \n{text}")

# method for capitalizing sentences
def capitalize_Sentence(text):
    var = 0 # var is used to make sure to capitalize the character itself and not the space between it
    formatted = ""
    array = {} # array for formatting text
    for i in range(0, len(text)):
        array[i] = text[i]
    for i in range(0, len(text)):
        char = text[i] # stores the character value of a specific member of array
        asc = ord(char) # stores the ascii value of char
        if(i == 0):
            char = char.upper()
            array[i] = char
        elif(var == 1 and asc == 32):
            var += 1
        elif(var == 2):
            char = char.upper()
            array[i] = char
            var = 0
        elif(asc == 46):
            var = 1
    for i in range(0, len(text)):
        formatted += array[i]
    print(f"Formatted text: \n{formatted}")

# method for capitalising every first letter of word
def capitalize_Word(text):
    var = 0 # use of var, asc, char and array are the same as the above function
    formatted = ""
    array = {}
    for i in range(0, len(text)):
        array[i] = text[i]
    for i in range(0, len(text)):
        char = text[i]
        asc = ord(char) 
        if(i == 0):
            char = char.upper()
            array[i] = char
        elif(var == 1):
            char = char.upper()
            array[i] = char
            var = 0
        elif(asc == 32):
            var = 1
    for i in range(0, len(text)):
        formatted += array[i]
    print(f"Formatted text: \n{formatted}")

# main function of the program
def main():
    print("\n\t\t\tText Formatter\n")
    while True:
        text = input("Enter your text or 0 to exit program: ")
        if(text == "0"):
            break
        print("\nWhat would you like to do with your text?\nEnter 1 to Capitalize everything, 2 to lowercase, 3 to Capitalize after sentences, 4 to Capitalize every word")
        ch = int(input())
        if(ch == 1):
            capitalize(text)
        elif(ch == 2):
            lowercase(text)
        elif(ch == 3):
            capitalize_Sentence(text)
        elif(ch == 4):
            capitalize_Word(text)
        else:
            print("Wrong Choice. Try Again!!!!\n")

main()