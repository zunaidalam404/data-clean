# num=[3,4,1,0,8,1,2,3,4,5]
# z=sum(num)
# print(z)

# print(max(num))
# print(min(num))
# for n in num:
#     if n%2==0:
#         print(n,end=", ")

# num.reverse()
# print(num)

# name=10
# exist=name in num
# print(exist)

# z=set(num)
# print(z)

# tuple=[14,42,4,55,3,5,12,58,41,5]
# z=len(tuple)
# print(z)
# k=5
# a=tuple[k]
# print(a)
# z=list(tuple)
# print(z)

# name=("zunaid is a  king")
# l=set(tuple)
# print(sorted(l))
# print(max(l))
# z=name.replace("is", "powerfull")
# y=tuple.index(55)
# print(y)

# name="aaabbbccc"
# z=name.count("a")
# y=name.count("b")
# x=name.count("c")
# a="a"+"b"+"c"
# print(f"a{z}b{y}c{x}")


# print(sorted(tuple))
# tuple.sort()
# print(tuple[-2])

# l=[1,2,2,3,1]
# freq={}
# for ch in l:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq)

# frequnce of number is list
# from collections import Counter
# l=[1,2,2,3,4,5,4,4,4,2,2,1,1,4,5,6]
# freq=Counter(l)
# print(freq)

# a=[1,2,3]
# b=[4,6,7]
# add=(a+b)
# print(add)

# comman elements
# a=[1,2,3]
# b=[2,3,4]
# add=(a+b)
# freq=Counter(add)
# print(freq)
# print(freq.most_common(2))

# l=[1,2,3,4,5,6,7,8]
# rotate=l[-1:]+l[:-1]
# print(rotate)

# list=[[1,2,3],[4,5,6]]
# add=sum(list,[])
# print(add)

#  Return true if list reads same forward and backward.
# list=[1,2,3,2,1]
# if list[::+1]==list[::-1]:
#     print(True)
# else:
#     print(False)

# Convert tuple to list.
# tuple=(1,2,3)
# z=list(tuple)
# print(z)

# tuple=(1,2,2,3)
# c=tuple.count(3)
# print(c)
# list=[1,2,3,4,5]
# z=list.index(4)
# print(z)

# l=[1,2,3,4,5]
# target=4
# for i in range(len(l)):
#     if l[i]==target and i+1<len(l):
#         print(l[i],l[i+1])



# def check_num(nums, target):
#     pairs=[]
#     seen=set()

#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             for k in range(j+1,len(nums)):
#                  if nums[i]+nums[j]+nums[k]==target:
#                      pair=tuple(sorted((nums[i],nums[j],nums[k])))
#                      if pair not in  seen:
#                          seen.add(pair)
#                          pairs.append(pair)
#     return pairs
         
# nums=[1,2,3,4,5,6]
# target=15
# result=check_num(nums,target)
# print(result)


# def check_num(matrix):
#     pairs=[]
#     seen=set()
#     for i in range(len(matrix[0])):
#         pair=[matrix[0][i],matrix[1][i]]
#         if tuple(pair) not in seen:
#             seen.add(tuple(pair))
#             pairs.append(pair)
            
#     return pairs

# matrix=[[1,2,3],[4,5,6]]
# result=check_num(matrix)
# for row in result:
#     print(row,end='')


# def sort_num(num):
#     n=len(num)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if num[j]>num[j+1]:
#                 num[j],num[j+1]=num[j+1],num[j]
#     return num 

# num=[4,1,3,2,45,64,33,34,543,5,334,676,445,]
# result=sort_num(num)
# print(result)

  
#Problem: Generate all possible pairs from list elements.
# def check_num(nums, target):
#     pairs=[]
#     seen=set()
    
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j]:
#                 pair=tuple(sorted((nums[i],nums[j])))
#                 if pair not in  seen:
#                     seen.add(pair)
#                     pairs.append(pair)
#     return pairs
         
# nums=[1,2,3]
# target=5
# result=check_num(nums,target)
# print(result)


# Problem: List contains numbers from 1 to n with one missing. Find missing.
# list=[1,2,3,4,5,6,7,9,11,14]
# missing_num=range(min(list),max(list)+1)
# miss=[]
# for ch in missing_num:
#     if ch not in list:
#         miss.append(ch)
# print("missing number",miss)                   


# 1. Check if Two Tuples Are Equal
#     Problem: Return true if both tuples contain same elements in same order.
# tuple_1=(1,2,3,4)
# tuple_2=(7,7,9,8)
# def check_num(tuple_1,tuple_2):
#     for ch in tuple_1:
#         if ch in tuple_2:
#             return True
#         return False
# print(check_num(tuple_1,tuple_2))

# Problem: Check if one list is sublist of another.
# main= [1,2,3,4,5]
# sub= [3,4]
# for ch in main:
#     if ch in sub:
#         print(ch,end=" ")
 
# main= [1,2,3,2,4]       
# while 2 in main:
#     main.remove(2)
# print(main)

# main=[x for x in main if x!=2]
# print(main)


# Problem: Count number of pairs (i, j) such that i < j and nums[i] > nums[j].
# def check_num(nums):
#     pairs=[]
#     seen=set()
#     count=0
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j]:
#                 count+=1
#                 pair=tuple(sorted((nums[i],nums[j]))) 
#                 if pair not in  seen:
#                     seen.add(pair)
#                     pairs.append(pair)
#     print("count is a number",count)
#     return pairs 
           
# nums=[1,2,3,4,5,6,7,8]
# result=check_num(nums)

from collections import Counter
nums= [1,1,2,2,2,3]
freq=Counter(nums)
sorted_list=sorted(nums,key=lambda x: (freq[x],x))
print(sorted_list)