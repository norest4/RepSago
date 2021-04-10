
def sumOddLengthSubarrays(arr):
    """
    :type arr: List[int]
    :rtype: int
    """  
    total_amount = sum(arr)
    for onumber in range(2,len(arr)+1):
        if onumber%2 != 0:
            fnum = 0
            snum = onumber
            for itr in range((len(arr)-onumber)+1):
                total_amount += sum(arr[fnum:snum])
                fnum += 1
                snum += 1
    print(total_amount)

arr = [1,4,2,5,3]
sumOddLengthSubarrays(arr)
arr1 = [1,2,5,6,6]

arr2 = [1,1,1,1,0,0,1,0,1,0,1,1]

arr3 = [132,423,43,234,554,864,256]

arr4 = [0,0,0,0,0]

arr5 = [100000, 200000, 23423543]

# def oddNumFinder(arr):
#     total_amount = 2*sum(arr)
#     for onumber in range(2,len(arr)+1):
#         if onumber%2 != 0: return(onumber)
#         fnum = 0
#         snum = onumber
#         for itr in range(len(arr)-onumber):
#             total_amount =+ sum(arr[fnum:snum])
#             fnum += 1
#             snum += 1



