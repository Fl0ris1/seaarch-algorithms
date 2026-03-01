names=["Alice", "Bob", "Charlie", "David","Eve"]
targetName=input("Who are you looking for?\n")

def linear_search(names,targetName):
    r=-1
    for i in range(len(names)):
        if names[i]==targetName:
            return i
    return r    


result=linear_search(names,targetName)

if result==-1:
    print("Name not in the list")
else: 
    print(f"The Name {targetName} Was Found At Index {result}")