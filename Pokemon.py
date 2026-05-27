#miguel
#int
pokemon_level=1
import random
pokemon_name="Gastly"
random_outcome=0
#Main
def gastly():
    print((r"                            _\n"))
    print((r"                         .\"' `..._\n"))
    print((r"                        '         `.\n"))
    print((r"                      .'      ___..'\n"))
    print((r"                _   .\"       '   .__,-.,\"\", ,----.\n"))
    print((r"     ,.-\"\"''-..\" :  :        `--'        ' :      :\n"))
    print((r"   .'            :_,'                    ._\"--. ;\n"))
    print((r"   :              _,.--'\"'\"\"--._           .  `\"\n"))
    print((r"  j             ,'               `-.      ,._.'  ,\"\".\n"))
    print((r"  :           ,'                   ,-.   .   __  `..'\n"))
    print((r"  --.    .'.'                   ,'   . :_,\"  `.\n"))
    print((r",.   ;   .   \\                 ,'      |         `.\n"))
    print(("' :  :    |    .             ,'        |\\         .  _\n"))
    print((r".   ._  |      \\         _.'          | .      ___ \" :\n"))
    print((r"       : '     . \\      ,'  .          ' |     :   `...'\n"))
    print((r"      ,'  \\       `.   .             ,'  |     '  __\n"))
    print((r"     .    .       |    \\          .'    '    .  (  .\n"))
    print((r"   .'      \\.___,'      -.____.-'     '     :   `-.'\n"))
    print((r"    .   ,\". \\ ..___              _     /      :    .\n"))
    print((r"    :   . :  \\|/\\  \"'--------+\"|,'  ,'       -..' :\n"))
    print((r"     -\" .'   : `\"-.._______,.\\|  .'               '\n"))
    print((r"         --. _ ._             _,'        ,\"\"-.__,'\n"))
    print((r"             \" :   `\"--.....--\"'     __   .\n"))
    print((r"             ,-'                 ,.-\"  `-'\n"))
    print((r"            :   ,..             .    ,\"\".\n"))
    print((r"           .'   .  :   __..._   `\"-. :   :\n"))
    print((r"           .._  : ' ,'      \"--..' `--\"\n"))
    print((r"               -' \" mh\n"))


def haunter():

    print((r"              -._                                   _.\n"))
    print((r"               \\ `-.._                           _,' |\n"))
    print((r"                \\     `-._    ,.--------..  _.\"    '\n"))
    print((r"                 \\        `--'              ``.     /\n"))
    print((r"                  \\                                j    __\n"))
    print(("__         __       \\                               |.-\"' /\n"))
    print((r".-.-.__.`'\"----\"\\                              |    /\n"))
    print((r"   .       .       '        ._                       /\n"))
    print((r"   ..        \\               | .               /|   /\n"))
    print((r"     .        .             |   `._          .' |  /\n"))
    print((r"       .  .-----            |      `.       /   ' '\"\"''\n"))
    print((r"         . .            .    ._      `_    /  ,'    .'\n"))
    print((r"           . .           ._   '\"\"'\"'     \"\"' ,  ,'\n"))
    print((r"             . .          ..              ,-/ ,'       _..\n"))
    print((r"               . .          \\|,---..  ,--\"./ / ,--------\".  \\\n"))
    print((r"                 ._           .     / , ..',:           \\  \\\n"))
    print((r"                    ._          ..\".,./ ' _.' :            \\  `.\n"))
    print((r"                  ,-'\" -._              _.\"     .   |.-\".   \\  |\n"))
    print((r"                 .         -..........-'        |   ..   \\   |_'\n"))
    print((r"                 |           \".                 .._   .  '  ,'\n"))
    print((r"                 |         |   |                     `\"'    .'\n"))
    print((r"                 |   /\\    |'  '\n"))
    print((r"                 '  /  \\   ||   .\n"))
    print((r"                '   \\  '   |'   ;\n"))
    print((r"                 \\  '  \\   `...'\n"))
    print((r"                  \"\"   ,' mh\n"))


def gengar():

    print((r"                |`._         |\\\n"))
    print((r"                   .  .    | .    |.\n"))
    print((r"                 .    .|-. |   `-..'  \\           _,.-'\n"))
    print((r"                 '      -. .           \\ /|   _,-'   /\n"))
    print((r"             .--..'        ._           ` |.-'      /\n"))
    print((r"              \\   |                                  /\n"))
    print((r"           ,..'   '                                 /\n"))
    print((r"           `.                                      /\n"))
    print((r"           _`.---                                 /\n"))
    print((r"       ,-'               `.                 ,-  /\"-.\n"))
    print((r"     ,\"                   | .             ,'|       `.\n"))
    print((r"   .'                     |   .         .'  |    .     .\n"))
    print((r" ,'                       '   ().     ,'()  '    |       .\n"))
    print(("'-.                    |.  .....-'    -----' _   |         .\n"))
    print((r"/ ,   ________..'     '  `-._              _.'/   |         :\n"))
    print((r" '-\"\" _,.--\"'         \\   | \"+--......-+' //   j `\"--.. , '\n"))
    print((r"   .'\"    .'           . |   |     |   / //    .       ` '\n"))
    print((r"     .   /               '   |    j   /,.'     '\n"))
    print((r"       \\ /                  `-.|_   |_.-'       /\\\n"))
    print((r"        /                        `\"\"          .'  \\\n"))
    print((r"       j                                           .\n"))
    print((r"       |                                 _,        |\n"))
    print((r"       |             ,^._            _.-\"          '\n"))
    print((r"       |          .'    '\"\"----\"'   .       '\n"))
    print((r"       j__     _,'                         -.'-.\"\n"))
    print((r"         ',-.,' mh\n"))

def main():
    while True:


        action=input("what would you like to do today train/gym_battle/display_info/exit] ")
        global pokemon_level
        if pokemon_level==10 or pokemon_level==11:
            global pokemon_name
            pokemon_name= "Haunter"
            evolve()
            haunter()
        if pokemon_level==20 or pokemon_level==21:
            pokemon_name="gengar"
            evolve()
            gengar()
        if action=="train":
            train()
            continue
        if action=="exit":
            exit()
            break
        if action=="gym_battle":
            battle=input("would you like to do a regular battle or a final boss battle and beat the game! regular/final_boss: ")
            if battle=="regular":
                gym_battle()
                continue
            if battle=="final_boss":
                final_boss()
                break


        if action=="display_info":
            info()
            continue
def train():
    global pokemon_level
    pokemon_level= pokemon_level + 1
    print (("your pokemon level is now level ") + str(pokemon_level))

def exit():
    print("good bye")

def gym_battle():
    global pokemon_level

    outcome = random.randint(1,3)
    if outcome==1 or 3:
        pokemon_level= pokemon_level + 2
        print (("YOU WON!!! your pokemon level is now level ") + str(pokemon_level))
    if outcome==2:
        print ("you lose")
def info():
    print("Your Pokemon Info________________________________________________________________")
    print (pokemon_level)
    print (pokemon_name)
    print("____________________________________________________________________________________")
def final_boss():
    global random_outcome
    global pokemon_level
    if pokemon_level<=9:
        random_outcome= random.randint(1,100)
    if random_outcome!=1:
        print("play again and get to a higher level")
    if random_outcome==1:
        print("YOU BEAT THE GAME CONGRATULATIONS!!!!!")
    if pokemon_level>=20:
        random_outcome= random.randint(1,2)
        print("YOU BEAT THE GAME CONGRATULATIONS!!!!!")
    if random_outcome!=1:
        print("Not a high enough level")
    if pokemon_level>=10:
        random_outcome=random.randint(1,5)
    if random_outcome!=1:
        print("not high enought level you failed try again")
    if random_outcome==1:
        print("CONGRADULATIOND YOU BEAT THE GAME")



def evolve():
    print("it looks like your pokemon is evolving")





print ("welcome to  the world of pokemon, your starter pokemon is Gastly")
print("try and become the stongest!!!!! Your pokemone can evoleve into a bigger stonger beast if you evolve your pokemon get your pokemon to level 10 to evolve it to stage 1 and 20 for stage 2")
gastly()
main()
