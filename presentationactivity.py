grocery_list = [] #CREATES AN EMPTY LIST

grocery_list.insert(0, "Milk") #ADDS A VALUE AT THE BEGINNING OF THE LIST, LISTS START AT INDEX 0

while True: #RUNS INDEFINITELY UNTIL BROKEN
    user_input = input("What do we want on our grocery list? ") #ASKS THE USER FOR A GROCERY TO ADD TO THE LIST
    user_input_info = user_input.strip().lower() #STRING FUNCTION TO MAKE IT MORE READABLE FOR THE COMPUTER
    
    if user_input_info == "no more": #CHECKS IF THE USER DOESN'T WANT TO ADD ANYMORE
        break #BREAKS THE LOOP, MAKES IT STOP WORKING

    grocery_list.append(user_input.title().strip()) #ADDS IT TO THE END OF THE LIST AND MAKES IT READABLE

    print(grocery_list, len(grocery_list)) #PRINTS THE LIST AND THE LENGTH OF THE LIST

print(grocery_list, len(grocery_list)) #PRINTS OUT LIST OF GROCERIES + LENGTH OF LIST

for i in range(len(grocery_list)):
    print(i, grocery_list[i])