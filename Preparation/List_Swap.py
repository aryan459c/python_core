# my_list=[1,2,3,4,5,6]
# index1=1
# index2=3
# my_list[index1],my_list[index2]=my_list[index2],my_list[index1]
# print(my_list)

# ========================================================================================================

"""Create List Assending as alphabetical Without buieltin Function (Swap)"""

# word_list=["cat","egg","bat","apple"]
# def bubble_short(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# print(bubble_short(word_list))

# =============================================================================================================
"""Assending alphabetical Order Using Buieltin Function"""

li=["Cat","Egg","Dog","Bat","Apple"]
li.sort(reverse="T")
print(li)