nums=[0,1,2,3,4,5,6,8,9]

def smallest_number(x):
    for i in range(len(x)):
        if i!=x[i]:
            return i
            

print(smallest_number(nums))
