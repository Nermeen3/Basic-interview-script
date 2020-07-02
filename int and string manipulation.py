from string import punctuation # this will generate special chars [^ , !, @,,,]
import re
def CheckFile(file):
    if file is None: return "EMPTY FILE"
    string_ct = even_ct = odd_ct = invalid_ct = 0   # counters
    sum_fti, concat_string = 0, ""

    for line in file:
        if line == '\n': # any line that doesnt have even, odd, char will be considered as "invalid"
            print("INVALID LINE")
            invalid_ct+= 1
            continue

        if string_ct + even_ct + odd_ct == 0: min_str = len(line)-1 # this line will initialize the min length of non empty string
        if line.strip().isalpha(): result = line

        elif line[0] in punctuation: # will enter the statement if a string char found at the start of the line
            result = line.strip()
            string_ct+= 1
            if string_ct <= 3: concat_string+= line.strip() + " "  # concat first 3 strings found

        else:
            index, result = 0, ""
            dictionary = {x:line.index(x) for x in re.findall(r"(\d+(?:\.)?\d*)", line)}
            floats = re.findall(r"(\d+\.\d+)", line) # using regular expression to return all floats in current line
            for item in re.findall(r"(\d+\.*\d*)", line):
                if item not in floats: # treating floats as string
                    if even_ct + odd_ct == 0: max_int = int(item) # initialize max int as first int found
                    if int(item) % 2 != 0:
                        integer = int(item)  / 2
                        odd_ct+= 1
                    else:
                        integer = int(item) * 3.25
                        even_ct+= 1
                    if even_ct + odd_ct <= 2: sum_fti+= int(item) # sum of the first two integers found
                    max_int = max(max_int, int(item)) # max int found in whole file
                    result+= line[index:dictionary[item]] # concat string before manipulated int, adding new int, concat what's after it as well
                    result+= str(integer)
                    index+= len(item) + len(line[index:dictionary[item]])
            result+= line[index:] # in case there's string after the last manipulated int as well for the float condition

        min_str = min(min_str, len(line)-1)
        # I'm printing the changes to each line depends on its type as well as the length of each line
        print(str(result).strip() + ' length is: ' + str(len(str(result))-1)) # decrement 1 cuz '\n' is considered as last char in line

    print("################## End of file ##################\n")
    print("Number of lines containing string: ", string_ct)
    print("Number of lines containing even:   ", even_ct)
    print("Number of lines containing odd:    ", odd_ct)
    print("Number of lines containing invalid:", invalid_ct, '\n')

    print("Summation of the first two integers:    ", sum_fti)
    print("Concat. of the first 3 special strings: ", concat_string)
    print("maximum integer found in the file:      ", max_int)
    print("minimum length of non empty string:     ", min_str)

file = open("input.txt", 'r+')
CheckFile(file)
## the time complexity of this code is O(n) as best case senario and O(n^2) as worst case
## n is the number of lines in the input.txt since im checking on at least the first
## character of the line if its a special char, and the whole line if it contains an integer
