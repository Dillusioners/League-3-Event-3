import json
import st

print("                             Welcome to file simulator!")
print("What would you like to do?")
print("1. Create File\n2. View File\n")
userChoice = int(input("Enter your choice: "))
try:
    while True:
        if userChoice == 1:
            fileName = input("What would you like your file name to be? ")
            fileName =  fileName + ".json"
            datadict = {

            }
            valuestore = []
            dataAmt = int(
                input("How much data (in the form of keys and values) would you like to enter?(Enter a number): "))
            while dataAmt != 0:
                key = input("Enter your data(key): ")
                value = input("Enter the value for the key " + key + ": ")
                if key == "" or value == "":
                    print("Please enter your data with it's value again. (Error: Invalid data or its value)")
                else:
                    datadict[key] = value
                    valuestore.append(int(value))
                    dataAmt -= 1
            dumper = json.dumps(datadict)
            with open(fileName, "w") as f:
                f.write(dumper)
            try:
                opt = int(input("Type 1 if there is any numerical value in the dataset or type any other keys: "))
                while opt == 1:
                    mean = st.mean(valuestore)
                    median = st.median(valuestore)
                    mode = st.mode(valuestore)
                    stdev = st.stdev(valuestore)
                    print("The Standard Deviation of the dataset with numerical value is: ", stdev)
                    print("The mean of the dataset with numerical value is: ", mean)
                    print("The median of the dataset with numerical value is: ", median)
                    print("The mode of the dataset with numerical value is: ", mode)
                    opt = 0
            except:
                print("Calculated and Stored the Details.")

            break
        elif userChoice == 2:
            fileName = input("Enter the file name you want to view: ")
            try:
                f = open(fileName+".json", "r")
                reader = json.reads(f)
                print(reader)
            except:
                print("File doesnt exist")
                break
except:
    print("Ran into an error.")
