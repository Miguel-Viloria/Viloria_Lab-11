My_list= [] 
for i in range(10):
    word= input("Enter an element to add to the list:")
    if i <= 10:
     My_list.append(word)
    else:
     continue
        

length= int(input("Type character length:"))
New_list= []
for character in My_list:
    if len(character) == length:
        New_list.append(character)
        
    else: 
        continue
    
print(f"elements with  character length:  {length}  \n {New_list}"  )

        
        
    
