# --------------
##File path for the file 
file_path 


#Code starts here

def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    file = open(path,'r')
    #Reading of the first line of the file and storing it in a variable
    sentence = file.readline()
    #Closing of the file
    file.close()
    #Returning the first line of the file
    return sentence
    

#Calling the function to read file
sample_message = read_file(file_path)
#Printing the line of the file
print("Sample Msg: ",sample_message)


# --------------
#Code starts here

def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quotient = int(message_b)//int(message_a)
    #Returning the quotient in string format
    return str(quotient)
#Calling the function to read file  
message_1 = read_file(file_path_1)
print("Msg 1: ", message_1)
#Calling the function to read file
message_2 = read_file(file_path_2)
print("Msg 2: ",message_2)
#Calling the function 'fuse_msg'
secret_msg_1 = fuse_msg(message_1,message_2)

#Printing the secret message 
print("Secret Msg 1: ",secret_msg_1)





# --------------
#Code starts here
def substitute_msg(message_c):
    
    #If-else to compare the contents of the file
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'
    
    #Returning the substitute of the message
    return sub
    

#Calling the function to read file
message_3 = read_file(file_path_3)
print("Msg 3: ",message_3)

#Calling the function 'substitute_msg'
secret_msg_2 = substitute_msg(message_3)

#Printing the secret message
print("Secret Msg2: ",secret_msg_2)



# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

def compare_msg(message_d,message_e):
    
    #Splitting the message into a list
    a_list =  list(message_d.split(" "))
    print(a_list)
    #Splitting the message into a list
    b_list =  list(message_e.split(" "))
    print(b_list)
    
    #Comparing the elements from both the lists
    c_list = [i for i in a_list if i not in b_list]
    
    #Combining the words of a list back to a single string sentence
    final_msg = " ".join(c_list)
    
    #Returning the sentence
    return final_msg
    

#Calling the function to read file
message_4 = read_file(file_path_4)
print("Msg 4: ",message_4)
#Calling the function to read file
message_5 = read_file(file_path_5)
print("Msg 5: ",message_5)

#Calling the function 'compare messages'
secret_msg_3 = compare_msg(message_4,message_5)

#Printing the secret message
print("Secret Messsage 3: ",secret_msg_3)






# --------------
#Code starts here

def extract_msg(message_f):
    
    #Splitting the message into a list
    a_list = message_f.split(" ")
    print(a_list)
    #Creating the lambda function to identify even length words
    even_word = lambda x : (len(x)%2 == 0)
    
    #Splitting the message into a list
    
    b_list = (filter(even_word,a_list))
    #print(b_list)
    
    #Combining the words of a list back to a single string sentence
    final_msg = " ".join(b_list)
    
    #Returning the sentence
    return final_msg
    
#Calling the function to read file
message_6 = read_file(file_path_6)
print(message_6)
#Calling the function 'filter_msg'
secret_msg_4 = extract_msg(message_6)

#Printing the secret message
print("Secret msg 4: ", secret_msg_4)





# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

final_path= user_data_dir + '/secret_message.txt'

print(message_parts)

secret_msg = " ".join(message_parts)
print(secret_msg)

def write_file(secret_msg,path):
    
    
    file = open(path,'a+')
    
    file.writelines(secret_msg)
    
    file.close()
    
write_file(secret_msg,final_path)    


#Code starts here



