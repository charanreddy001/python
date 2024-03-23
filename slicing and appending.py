channel = 'charan'
# for numbering we start from 0 for positive numbers
# for negative numbers "which come from backside" start with as usual starting from -1 ;
print(channel[-2])
print(channel[0])
print(channel[:6])
# by adding this colon we can get that number of letters printed from front for positive numbers
print(channel[:-1])
# for negative numbers we can remove that number of letters from back and print remaining ones
print(channel[::-1])
# it is used to print letters from back

add = "charan " + channel
print(add)
print("ll")

# dictionary
information = {'charan': 'very good boy', 'amrutha': 'chala kovvu'}
print(information)
print(information['charan'])
print(information.get('charan'))

print(len(channel))
amrutha = "good"
print("charan" in amrutha)
# if the word is in it, we get true otherwise false
c = [12, 23, 45, 567, 678]
c.append(90)
print(c)
c.extend([34,3445])
# append is for adding single things whereas extend is for adding multiple items
# to add item at a particular place insert is used
# First one is index and second one is word
c.insert(2,"charan")
print(c)
# inserting more than one item at a particular place
c[3:1] = ["chh","ece","mvweio"]
print(c)
c.remove("charan")
print(c)







