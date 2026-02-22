arr=[24,56,6,3,67,7]
target=int(input("Input The Number You Want To Search: "))

def linear_search(arr,target):
    c=-1
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return c    


result=linear_search(arr,target)

if result==-1:
    print("The Number Is Not In The Array")
else: 
    print(f"{target} Found At Index {result}")