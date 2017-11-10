import re
import sys
import math

txtLines = []

def main():
    txt = input("Please input a file name (remember extensions as well!):")
    rule_base = RuleExtraction(txt)
    RuleExtraction(txt)
    MemberExtraction(rule_base)
    

def RuleExtraction(txt):

    ruleBaseList = []


    # with open(txt, 'r') as datafile:
    #     for lines in datafile,readlines():
    #         txtLines.append(lines)


    read_in = open(txt, "r")
    read_in = (re.split(r'\n\n',read_in.read()))

    memberClasses = {}
    crispValues = read_in[len(read_in)-1]
    
    #print(read_in)

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
                #Assign that line to ruleBaseName
                ruleBaseName = line
    #print(ruleBaseList)
    return ruleBaseList

    #Initiate Dictionary
    # data = {}

    # for i in range(2,len(read_in)-1,2):

    #     memberShips = []
    #     Groups = read_in[i+1].split("\n")

    #     for j in range(0,len(Groups)):
    #         x = Groups[j].split(" ")

    #         y = {x[1],x[2],x[3],x[4],x[0]}

    #         memberShips.append(y)

    #     memberClasses[read_in[i].strip()] = memberShips


    # crispValues = crispValues.split("\n")
    # crisp = []
    # for i in range(0,len(crispValues)):
    #     x = crispValues[i].split(" = ")
    #     if x is not None:
    #         crisp.append(dict({"name" : x[0], "value":x[1]}))

    # data['ruleBaseName'] = ruleBaseName
    # data['curves'] = memberClasses
    # data['crisp'] = crisp #Juicy crip values 
    # data['rules'] = ruleBaseList.split("\n")

    # print(ruleBaseName)
    # print(memberClasses)
    # print(realWorld)
    # print(rules.split("\n"))
    #print(data)
    #return data

def MemberExtraction(rule_base):
    memberClasses = []
    hits = []

    for x in rule_base:
        try: 
            foundMember = re.search('If the (.+?) is', x).group(1)
            if foundMember in hits:
                break
            else:
                #print(hits)
                hits.append(foundMember)
                memberClasses.append(foundMember)
        except AttributeError:
            foundMember = ""
            print("No member found for " + x)

    for x in rule_base:
        try: 
            foundMember = re.search('[and|or] the (.+?) is', x).group(1)
            if foundMember in hits:
                break
            else:
                #print(hits)
                hits.append(foundMember)
                memberClasses.append(foundMember)
        except AttributeError:
            foundMember = ""
            print("No member found for " + x)


    for x in rule_base:
        try: 
            foundMember = re.search('then the (.+?) will be', x).group(1)
            if foundMember in hits:
                break
            else:
                #print(hits)
                hits.append(foundMember)
                memberClasses.append(foundMember)
        except AttributeError:
            foundMember = ""
            print("No member found for " + x)
            

    print(memberClasses)


if __name__ == '__main__':
    main()




expression = ("^Rule(.+)?[0-9] If the (<member1>.+?) is (<mValue1>.+?) [and|or] the (<member2>.+?) is (<mValue2>.+?) then the (<member3>.+?) will be (<mValue3>.+?)")