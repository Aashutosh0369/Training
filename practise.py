# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(my_list[0:5])
#
# my_tuple = (1,2,3,4,5,6,4,85,2,3)
# print(my_tuple[0:5])
#
# my_string = 'get5letter'
# print(my_string[0:5])
#
# for i in my_list:
#     if i%2 != 0:
#         my_list.remove(i)
#
# print(my_list)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# my_list1 = []
#
# num = int(input()) # define number of integer to input
#
# for i in range(num):
#     number = int(input())
#     my_list1.append(number)
#
# print(my_list1)
#
# my_list2 = []
#
# n =int(input())# define number of integer to input
# input_n = input("Enter the integer separested by commas: " )
# split_n = input_n.split(',')# Split the input string into individual integers
#
# print(split_n)
# for i in split_n:
#     my_list2.append(int(i))
#
# # print(my_list2)
# my_list11 = [1, 2, 3, 4, 5, 6, 7, 8]
# my_list22 = [4, 5, 6, 7, 8, 9, 10]
#
# new_list = []
# new_list.extend(set(my_list11).intersection(my_list22)) # 'extent' is catch here
# print(new_list)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////

# my_list3 = [46,87,654,2,87,5,35,487,35,4984]
# my_list3.sort(reverse=True)
# print(my_list3)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////
#
# x=(1,2,3,4,5)
# y=(4,5,6,7)
# z = tuple(set(x).intersection(set(y)))
# print(z)
#
# diff = tuple(set(x).symmetric_difference(set(y)))
# print(diff)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
#
# set1 = {'apple', 'banana', 'cherry'}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}
# print(set1)
#
# thisset = {'apple' , 'banana' , 'cherry' , 'apple'}# no duplicate
# print(thisset)
# print(len(thisset))# even duplicate will not count
#
# set4 = {"abc", 34, True, 40, "male"}
# print(type(set4))
#
# set5 = (('apple', 'banana', 'cherry'))# constructor
# print(set5)
#
# for i in set1:
#     print(i)
#
# print('banana' in set1)
# print('mango' in set1)
#
# set1.add('orange')
# print(set1)
#
# # add items from another set
# set1.update(set2)
# print(set1)
#
# # Note: If the item to remove does not exist, remove() will raise an error.
# # Note: If the item to remove does not exist, discard() will NOT raise an error.
#
# set6 = {1, 5, 7, 9, 3}
# set6.remove(9)
# print(set6)
# # set6.remove(2)#will give error
#
# set6.discard(1)
# print(set6)
# set6.discard(1)#will not give error
# print(set6)
#
# set6.clear()
# print(set6)
#
# del set6
# # print(set6) # will delete set and  give error because it does not exit

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# set7 = {1, 5, 7, 9, 3}
# for i in set7:
#     print(i)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////

# # All set operation
# set8 = {"a", "b", "c"}
# set9 = {1, 2, 3}
#
# set10 = set8.union(set9)
# print(set10)
#
# set11 = set8 | set9
# print(set11)
#
#
# sets1 = {"a", "b", "c"}
# sets2 = {1, 2, 3}
# sets3 = {"John", "Elena"}
# sets4 = {"apple", "bananas", "cherry"}
# sets5 = {'car','bike','apple'}
#
# myset = sets1.union(sets2,sets3,sets4)
# print(myset)
#
# myset1 = sets1 | sets2 | sets3 | sets4
# print(myset1)
#
# x = {"a", "b", "c"}
# y = (1, 2, 3)
#
# z = x.union(y)
# print(z)
#
# sets1.update(sets2)
# print(sets1)
#
# print(sets4.intersection(sets5))
# # print(sets6)
# print(sets4 & sets5) # similar with intersection
#
# sset1 = {"apple", "banana", "cherry"}
# sset2 = {"google", "microsoft", "apple"}
#
# sset1.intersection_update(sset2)
# print(sset1)
#
# # Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates
# mset1 = {"apple", 1,  "banana", 0, "cherry"}
# mset2 = {False, "google", 1, "apple", 2, True}
#
# mset3 = mset1.intersection(mset2)
#
# print(mset3)
#
#
# mset4 = {"apple", "banana", "cherry"}
# mset5 = {"google", "microsoft", "apple"}
#
# mset6 = mset4.difference(mset5)
# mset61 = mset4 - mset5
# print(mset6)
# print(mset61)
#
#
# # The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
# mset4 = {"apple", "banana", "cherry"}
# mset5 = {"google", "microsoft", "apple"}
# mset4.difference_update(mset5)
# print(mset4)
#
# mset4 = {"apple", "banana", "cherry"}
# mset5 = {"google", "microsoft", "apple"}
#
# sett = mset4.symmetric_difference(mset5)
# print(sett)
#
# sett2 = mset4 ^ mset5
# print(sett2)
#
# mset4.symmetric_difference_update(mset5)
# print(mset4)

# # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# d = {1 : 1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1}
#
# n = int(input("Enter the maximum key value: "))  # Get the maximum key value from the user
#
# mydict = dict.fromkeys(range(1,n+1),1)# Generate the dictionary using dict.fromkeys()
# print(mydict)
#
# for key in mydict:
#     print(key,end=" ")
# print()
# for val in mydict.values():
#     print(val,end=" ")

# # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# x = {'a':1,'b':2,'c':3}
# y = {'a':4,'d':5,'e':6}
#
# merge_dict = x.copy()
# merge_dict.update(y)
# merge_dicts = {**x , **y}
#
# print(merge_dict)
# print(merge_dicts)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

l = [1,2,3,45,6,8,92,5,6,8]
t = ('fvdf',54,'0m5m4m2',65,6,2,3,'ppppp',True)
st = 'jnf'

print(l[-1])
print(l[len(l)-1])

print(t[-1])

print(st[-1])