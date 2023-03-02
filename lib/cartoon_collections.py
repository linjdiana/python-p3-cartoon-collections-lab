def roll_call_dwarves(names):
    for i in range(len(names)):
        print(f"{i+1}. {names[i]}")

def summon_captain_planet(planeteer_calls):
    newlist = []
    for call in planeteer_calls:
        newlist.append(call[0].upper() + call[1:]
                       + "!")
    return newlist

def long_planeteer_calls(callz):
    for call in callz:
        if len(call) > 4:
            return True
    else: 
        return False

def find_the_cheese(cheezes):
    for i in range(len(cheezes)):
        if cheezes[i]  == 'cheddar' or cheezes[i] == 'gouda' or cheezes[i] == 'camembert':
            return cheezes[i]
    return None
