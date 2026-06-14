def reverse(num,low,high):
    while low<high:
        temp=num[low]
        num[low]=num[high]
        num[high]=temp
        low+=1
        high-=1
nums =[-1]
k=2
n=k%len(nums)
reverse(nums,0,len(nums)-1)
reverse(nums,0,n-1)
reverse(nums,n,len(nums)-1)
print(nums)