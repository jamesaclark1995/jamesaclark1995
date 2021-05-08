print('''
             |\          /|
             | \        / |           ^  ^  ^
             |  \      /  |           |  |  |
             |   \____/   |           |  |  |
             |  \     /   |           |__|__|
             | # \   / #  |              |
             |            |              |
             \     ^      /              | 
              \ \______/ /               |
               \ \____/ /                |
                \______/
        ''')

print('''
         ####################################################################
         #                                                                  #
         #                        Welcome to hell!                          #
         #                                                                  #
         #    You are here for all eternity. I would get comfortable if     #
         #    I were you. No soul has ever left this place. The only        #
         #    way one can leave is to say 'please'. Ha ha ha ha ha!         #
         #                                                                  #
         ####################################################################
     ''')

devil = input("So what will you say, mortal? ")

while devil.lower() != "please":
    devil = input("You are here for all eternity. There's no " \
                  "escape unless you say 'please'.")
else:
    print("Okay, you can go now")
