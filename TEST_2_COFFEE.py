alertness = False
hrs_coffee_drank = 0

def drink_coffee():
    global alertness
    global hrs
    global hrs_coffee_drank
    global caffiene
    if alertness == False:
        if hrs - hrs_coffee_drank >= 3:
            caffiene = True 
            hrs_coffee_drank = hrs
            alertness = False
        elif hrs - hrs_coffee_drank < 3:
            caffiene = False
            alertness = True
            print("You are no longer alert.")
            hrs = hrs_coffee_drank            
    else:        
        return "You are no longer alert."    
            
hrs = 5
