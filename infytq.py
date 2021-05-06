def merge_list(list1, list2):
    merged_data=""
    #write your logic here
    
    len_1 = len(list1)    
    j = len_1 - 1
    
    for i in rangr(len_1):
        # print(i)      //index 0- 7 
        data1 = ""
        data2 = ""
        
        if list1[i]:
            data = list1[i]
        if list2[j]:
            data2 = list2[j]
        j -= 1 
        
        merged_data  += data1 + data2 
        
        if i < (len_1 -1):
            merged_data += " "
    return merged_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)