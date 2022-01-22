import sys

str = input("Enter for loop to check syntax: \n")
striped_string = str.replace(" ","")
in_pos = str.find("in")
col_pos = str.find(":")
range_exist = [1 if striped_string.find("inrange") != -1 else 0][0]

#check if for exist
print("Checking for keyword exist.....")
if str[0:3] != "for":
    print("What are you trying to do?\n")
    sys.exit()
    
#check if space after for exist
print("Checking space after for .....")
if str[3] != " ":
    print("Forgot a space after for...")
    sys.exit()

#check for counter variable 
print("Checking if counter variable exist .....")
if striped_string.find("forin") != -1:
    print("Forgot to give a counter varible to loop ..")
    sys.exit()
    
#check if space before in exist
print("Checking if space before in exist .....")
if str[in_pos-1] != " ":
    print("Forgot the space before in...")
    sys.exit()
    
#check if in exist
print("Checking if in keyword exist .....")
if in_pos == -1:
    print("Forgot the in...")
    sys.exit()
    
#check if space after for exist
print("Checking if sapace after in  exist .....")
if str[in_pos+2] != " ":
    print("Forgot a space after in...")
    sys.exit()
    


#check if colon at the end exist
print("Checking if in : exist at the end of the string.....")
if col_pos+1 != len(str.strip()):
    print("Forgot the : ...",)
    sys.exit()

#checking if counter variable exist
print("Checking if counter variable exist.....")   
for_in  = str[3:in_pos].replace(" ","")
if len(for_in) > 1:
    print("Something is wrong")
    sys.exit()

#check for loop variable or range variable
print("Checking if loop type is a range based.....")   
if range_exist == 1:
    #check if range exist
    print("Checking if range is provided or not....")   
    if striped_string.find("range:") != -1:
        print("Forgot the give a the range")
    else:
        #check if space after range exist
        print("Checking if range is provided after range keyword....") 
        range_pos = striped_string.find("range")
        print("Checking range type....") 
        if striped_string.find("range(") != -1:
            print("Checking if ( exist....") 
            open_pos = striped_string.find("range(")+5
            print("Checking if ) exist....") 
            close_pos = striped_string.rindex(")")
            print("Checking if ( is before ) exist....") 
            #if ( is after range
            if open_pos < range_pos:
                print("Where did you even put the ( ?")
            #if ) is afrer ( and range
            elif close_pos < range_pos or close_pos < open_pos:
                print("Where did you even put the ) ?")
            else:
                print("Checking if two ranges exist....") 
                list_range = striped_string[open_pos+1:close_pos].replace(" ","")
                #check if comma seprating is not at start
                if list_range.find(",") == 0:
                    print("What is the start of the range ?")
                #check if comma seprating is not at end
                elif list_range.find(",") == len(list_range)-1:
                    print("What is the end of the range ?")
                    sys.exit()
                    
elif range_exist == 0:
    print("Checking if loop variable is provided.....")   
    if striped_string.find("in:") != -1:
        print("Forgot to give a iterable  ..")
        sys.exit()

print("No errors")
