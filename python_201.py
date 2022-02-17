import requests
from colorama import Fore, Style
        
QUIT = False

while QUIT == False:
    userinput = input("Enter the name of pokemon : ").lower()
    print("")
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{userinput}")
    if req.status_code==200:
        pokemon = req.json()
        print("Name : " ,Fore.CYAN + Style.BRIGHT+ pokemon["name"])

        print("\n")

        print(Fore.LIGHTCYAN_EX + 'Abilities:')
        for abilities in pokemon["abilities"]:
            print("\t \n",Fore.WHITE +Style.BRIGHT+ abilities['ability']['name'])

        print(Fore.LIGHTBLUE_EX + "\nThe Pokemon height is :" ,  pokemon['height'])

        print("\n")

        print(Fore.LIGHTMAGENTA_EX + "The moves are :")
        for move in pokemon['moves']:
            print(Fore.MAGENTA + move['move']['name'])
            
        print(Style.RESET_ALL,"\n")
        ask = input("Want to quit (yes or no): ")
        if ask == "yes":
            QUIT = True
        elif ask == "no":
            QUIT = False
        else:
            print("Continuing! \n")

    else:
        print(Fore.RED+Style.BRIGHT+'\n Pokemon not found!!')
       
        ask = input("Want to quit ?(yes or no): ")
        print(Style.RESET_ALL)
        
        if ask == "yes":
            QUIT = True
        elif ask == "no":
            QUIT = False
        else:
            print("Continuing! \n")
        