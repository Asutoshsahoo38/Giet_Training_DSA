# complete the sentence by concatinating list1 with reverse of list2
list1 = ['A','app','a','d','ke','th','doc','awa']
list2 = ['y','tor','e','eps','ay',None,'le','n']
list2rev = list2[::-1]

for i in range(len(list1)):
    if(list2rev[i] == None):
        print(list1[i] + '',end=" ")
    else:
        
        print(list1[i]+list2rev[i],end = " ")
        
        
