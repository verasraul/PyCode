
password = {}

class KeyHolder:
    def __init__(self):
        self.name = name
        self.keyname = keyname



    # Function that stores the key from user input into the empty dictionary defined above
    def keyname():
        print("Enter the password you would like to store")
        key = input("Enter Account Name: ")
        value = input("Enter Password: ")
        # global password
        password[key] = value
        holder.initiate()

    # Prompts usesr to search for stored passwords
    def searchPrompt():
        Prompt = input("Would you like to search for stored Passwords? Y/N ")
        if Prompt.upper() =='Y':
            return holder.searchKey()
        elif Prompt.upper() == 'N':
            print("Thanks, program will now close")
            quit()
        else:
            print("This is not a valid option! Please try again")
            return holder.searchPrompt()

    # Function that searches for existing keys
    def searchKey():
        sKey = input("Enter name of account you would like to view: ")
        # global password
        if sKey in password:
            print(password[sKey])
            return holder.initiate()
        elif sKey not in password:
            print("There is no such password stored")
            return holder.initiate()

    # Function that starts the program, first rule of business
    def initiate():

        start = input("Would you like to save a new password? Y/N ")
        if start.upper() == 'Y':
            print("Ok")
            return holder.keyname()
        elif start.upper() == 'N':
            print("ok")
            return holder.searchPrompt()
            # quit()
        else:
            print("This is not a valid option! Please try again")
            return holder.initiate()


holder = KeyHolder

holder.initiate()
