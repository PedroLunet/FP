def intro():
    print("After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.\nA. Grab a nearby rock and throw it at the orc\nB. Lie down and wait to be mauled\nC. Run")   
    ans = input()
    if ans == "B" or ans == "b":
        print("Welp, that was quick. You died!")
        return
    elif ans == "A" or ans == "a":
       option_rock()
    
    elif ans == "C" or ans == "c":
        option_run()

def option_rock():
    print("The orc is stunned, but regains control. He begins running towards you again.\nA. Run\nB. Throw another rock\nC. Run towards a nearby cave")
    ans = input()
    if ans == "B" or ans == "b":
        print("Welp, that was quick. You died!")
        return
    elif ans == "A" or ans == "a":
       option_run()
    
    elif ans == "C" or ans == "c":
        option_cave()

def option_cave():
    print("Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?")
    sword = input()
    print("What do you do next?\nA. Hide in silence\nB. Fight\nC. Run")
    ans = input()
    if ans == "B" or ans == "b":
        if sword == "Y" or sword == "y":
            print("As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!")
            return
        else:
            print("You're defenseless. You died!")
            return
    elif ans == "A" or ans == "a":
       print("I think orcs can see very well in the dark, right? You died!")
       return
    
    elif ans == "C" or ans == "c":
        print("The orc turns around and sees you running.")
        option_run()

def option_run():
    print("You run as quickly as possible.\nA. Hide behind boulder\nB. Trapped, so you fight\nC. Run towards an abandoned town")
    ans = input()
    if ans == "B" or ans == "b":
        print("You're no match for an orc. You died!")
        return
    elif ans == "A" or ans == "a":
       print("You're easily spotted. You died!")
       return
    
    elif ans == "C" or ans == "c":
        option_town()

def option_town():
    print("You notice a purple flower near your foot. Do you pick it up? Y/N")
    ans = input()
    if ans == "Y" or ans == "y":
        print("You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!")
        return
    if ans == "N" or ans == "n":
        print("Maybe you should have picked up the flower. You died!")
        return

intro()
