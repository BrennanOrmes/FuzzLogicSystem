print(data['crisp'])

    fuzzy_values = []
    for i in range(2, len(read_in)-1, 2):

        memberShips = []
        groups = read_in[i+1].split("\n")

        for z in range(0,len(groups)):
            x = groups[z].split(" ")
            print(x)

            #0 = Name, 1 = a, 2 = b, 3 = alpha, 4 = beta
            y = membershipCurves(x[0],x[1],x[2],x[3],x[4])
            for value in crisp:
                print(y.name)
                print(value['name'])
                if y.name == value['name']:
                    fuzzy_value = y.membership(value['value'] )
                    fuzzy_values.append(fuzzy_value)
            
            memberShips.append(y)

        memberClasses[read_in[i].strip()] = memberShips
    
    print(fuzzy_values)