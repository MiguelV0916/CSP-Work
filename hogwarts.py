#Miguel

#Init
import time
import random
#Funcs
def main():
    print("Welcome to Hogwarts")
    name=input("What is your name:")
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(house(name))

#This Function checks a name and returns a house from harry potter
def house(name):
     if name == "Harry" or name == "Ron" or name== "Hermione":
         return "Gryffindor"
     if name == "Newt" or name == "Nymphadora" or name== "Pomona":
         return "Hufflepuff"
     if name== "luna" or name == "Cho" or name== "Filius":
         return "Ravenclaw"
     if name== "Voldermort" or name == "Draco" or name == "severus":
         return "Slytherin"
     else:
         x=random.randint(1,4)
         if x==1:
             return"Gryffindor"
         if x==2:
             return"Hufflepuff"
         if x==3:
             return "Ravenclaw"
         if x==4:
             return "Slytherin"




#Main
main()
