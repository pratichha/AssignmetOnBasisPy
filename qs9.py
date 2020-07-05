#binary search function
def bin_search(arr,l,r,x):
 if r>=l:
    mid = l + (r-1)//2
    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
      return bin_search(arr,l,mid-1,x)
    else:
      return bin_search(arr,mid+1,r,x)
 else:
      return -1
arr = [1,4,5,6,8,9]
x=2      
result = bin_search(arr,0,len(arr)-1,x)
if result != -1:
  print("elemet is present at index % d" % result)      
else:
  print("elemet is not prresent")