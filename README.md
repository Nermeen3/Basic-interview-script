# Basic-interview-script

A TCL script that reads a file on the filesystem ( named input.txt ), the script should process each line using the below rules:
        lines start with a string character, print the line as is without any changes.
        lines that present an odd integer value, divide the value with 2 and print it.
        lines that present an even integer value, multiply the value with 3.25 and print it.
        after printing all lines, print a small report with a number of lines that are found to be containing string, odd number, even number, or invalid.
        print the summation of the first 2 integer values occurring in the file.
        print the concatenation of first 3 lines starting with the string character.
        print all lines with the length of each line.
        print a line with maximum integer value found in the file, and the minimum length of "non-empty string" in the whole file. 

Rules:
        Consider floats as string.
        Any line that doesn't apply to any previous rule, print "INVALID LINE" message.
        You must run your code in a TCL interpreter, you should deliver a running and a "syntax errors" free script.
Note:
        the problem is solved in python as well as TCL
