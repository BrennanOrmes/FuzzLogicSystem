import re
import math

def main():
    print("Please input a file name ( for example data.txt)")
    txt = input(">: ")
    data = dictionaryInit(txt)

    rList = data["rules"]
    ruleProcess(rList)


def dictionaryInit(txt):

    data = (txt.replace("\n",""))
    ruleBaseList = []

    read_in = open(txt, "r")
    read_in = (re.split(r'\n\n',read_in.read()))

    memberClasses = {}
    #ruleBaseList = read_in[1]
    crispValues = read_in[len(read_in)-1]

    # Open data file with name given by user input
    with open(txt, 'r') as datafile:
        #For each line in the txt file
        for line in datafile.readlines():
            #If a  line starts with the string Rule
            if line.startswith('Rule'):
                #Use regular expression to remove ("Rule followed by any int 0-9") on the current line
                line = re.sub("^Rule(.+)?[0-9]", "", line)
                #Remove white space
                line = line.strip()
                #Add that rule to the list Rules
                ruleBaseList.append(line)
            #If a line containing Rule base as part of a word is detected
            if ("Rulebase" or "rulebase") in line:
                ruleBaseName = line


    #Initiate Dictionary
    data = {}
    data['rules'] = ruleBaseList
    return data

def ruleProcess(rList):  
    print("Parsed Rules: ")
    for y in rList:
            #print(y)
            splitRule = y.split(" ")
            ruleConditions = {splitRule[2]: splitRule[4], "conjunctive": splitRule[5], splitRule[7]: splitRule[9], splitRule[12]: splitRule[15]}
            
            print(ruleConditions)

if __name__ == '__main__':
    main()