


graphIdea={
    "A":["B","C"],
    "B":["F"],
    "C":["D","E"],
    "F":["G","H"]
}

checked=[]

def depthFirst(tempgraph, alp):

    for i in tempgraph:

        if(i not in checked):

            if i == alp:
                print("Match Found")
                break

            else:
                checked.append(i)
                print(checked)
                if i in graphIdea:
                    depthFirst(graphIdea[i], alp)


                
depthFirst(graphIdea, "F")