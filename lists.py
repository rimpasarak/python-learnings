list_of_names=["Rimpa","maa","papa", 1, 0.0, True]
print(list_of_names)
list_of_names.append("Sampath")
print(list_of_names)

list_of_list=[['rimpa', 'alone'],['maa', 'papa', 'alone'],['hate','USA'],['love, India']]
print(list_of_list)

print(list_of_list[-1])
print(list_of_list[-2])

#Slicing
print(list_of_list[:-1]) 
print(list_of_list[-2:])

list_of_list[0][1]='cry all the time'
list_of_list[1][2]='cries too'

print(list_of_list)
print("Length of list: "+str(len(list_of_list)))

#popping
remove_from_list = list_of_list.pop(2)
print(list_of_list)
print(remove_from_list)
