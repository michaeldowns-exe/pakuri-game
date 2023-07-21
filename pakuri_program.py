from pakudex import Pakudex
from pakuri import Pakuri

#menu for efficiency
def printMenu():
    print()
    print('Pakudex Main Menu')
    print('-----------------')
    print('1. List Pakuri')
    print('2. Show Pakuri')
    print('3. Add Pakuri')
    print('4. Evolve Pakuri')
    print('5. Sort Pakuri')
    print('6. Exit')
    print()

def main():
    userInput = ''
    end = 0
    userSpecies = ''
    userCap = ''

    print('Welcome to Pakudex: Tracker Extraordinaire!')
    
    #try block for unwanted input(looks for pos int)
    while True:
        try:
            userCap = int(input("Enter max capacity of the Pakudex: "))
            if userCap <= 0:
                print("Please enter a valid size.")
                continue
            else:
                break
        except ValueError:
            print('Please enter a valid size.')

    userPaku = Pakudex(userCap)
    print(f'The Pakudex can hold {Pakudex.get_capacity(userPaku)} species of Pakuri.')

    

    #ends when user input 6
    while end == 0:
        printMenu()
        userInput = input('What would you like to do? ')
        count = 1

        #view entire pakudex contents
        if userInput == '1':
            pakuList = Pakudex.get_species_array(userPaku)
            if pakuList == None:
                print("No Pakuri in Pakudex yet!")
            else:
                print('Pakuri In Pakudex: ')
                for i, pakur in enumerate(pakuList):
                    print(f'{i+1}. {pakur}')       

        #looks for specific pakuri in pakudex
        elif userInput == '2':
            inputs = input('Enter the name of the species to display: ')
            stats = Pakudex.get_stats(userPaku, inputs)
            if stats == None:
                print("Error: No such Pakuri!")
            else:
                print(f"Species: {inputs}")
                print("Attack:", stats[0])
                print("Defense:", stats[1])
                print("Speed:", stats[2])
            
        #adds pakuri to pakudex
        elif userInput == '3':
            
            
            if Pakudex.get_size(userPaku) == Pakudex.get_capacity(userPaku):
                print("Error: Pakudex is full!")

            else:
                userSpecies = input('Enter the name of the species to add: ')
                if Pakudex.add_pakuri(userPaku, userSpecies) == True:
                    print(f'Pakuri species {userSpecies} successfully added!')

            
                else:
                    print("Error: Pakudex already contains this species!")
        #evolves pakuri species in pakudex
        elif userInput == '4':
            userSpec = input("Enter the name of the species to evolve: ")
            
            if Pakudex.evolve_species(userPaku, userSpec) == True:
                Pakudex.evolve_species(userPaku, userSpec)
                print(f'{userSpec} has evolved!')
            elif Pakudex.evolve_species(userPaku, userSpec) == False:
                print('Error: No such Pakuri!')


        #sorts pakuri
        elif userInput == '5':
            Pakudex.sort_pakuri(userPaku)
            print('Pakuri have been sorted!')

        #end
        elif userInput == '6':
            print('Thanks for using Pakudex! Bye!')
            end = 1

        else:
            print('Unrecognized menu selection!')

main()