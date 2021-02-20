answer = None
while answer not in ("y", "n", "yes", "no"): 
    answer = input("Process the tire folders: yes or no ? (y/n)") 
    if answer == "yes" or answer == "y" or answer == "Y": 
        print("yes")
    elif answer == "no" or answer == "n" or answer == "N": 
        print("no")
    else: 
    	print("Please enter yes(y) or no(n)") 
