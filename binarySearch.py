nums=[1,3,5,7,9,10,14,15,20]
target=int(input("Input The Number You Want To Search\n"))


left=0
right=len(nums)-1

def binarySearch(nums,target):
    global right, left
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        if nums[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return -1

result=binarySearch(nums,target)

if result!=-1:
    print(f"Element Found At Index {result}")

else: 
    print("Element Not Found")

