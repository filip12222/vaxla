import os
import vaxla


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t-växlare-\n")

    pris = input("\tMata in pris på varan i kr: ")
    inbet = input("\tMata in inbetalt belopp i kr: ")

    exChangenow(int(pris), int (inbet))

def exChangenow(priset, inbetalning):

    if priset > inbetalning:
        print("\n\tMer prengar tack! ")

    else:

        vaxel_tillbaka_dictionary = vaxla.get_exchange_dict(inbetalning, priset) 
        print("\n\t ----------------------")
        print("\tVäxel tillbak: \n")
        print("\tAntal 500 lappar: " + str(vaxel_tillbaka_dictionary[500]))
        #print("aray: "+ str(vaxel_tillbaka_dictionary))
        print("\tAntal 100 lappar: " + str(vaxel_tillbaka_dictionary[100])) 
        print("\tAntal 50 lappar: " + str(vaxel_tillbaka_dictionary[50])) 
        print("\tAntal 20 lappar: " + str(vaxel_tillbaka_dictionary[20])) 
        print("\tAntal 10 kronor: " + str(vaxel_tillbaka_dictionary[10])) 
        print("\tAntal 5 kronor: " + str(vaxel_tillbaka_dictionary[5])) 
        print("\tAntal 1 kronor: " + str(vaxel_tillbaka_dictionary[1])) 
main()