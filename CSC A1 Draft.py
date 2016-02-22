"""3.3.5 (v3.3.5:62cf4e77f785, Mar  9 2014, 10:37:12) [MSC v.1600 32 bit (Intel)]
Python Type "help", "copyright", "credits" or "license" for more information.
[evaluate untitled-4.py]"""

"""The Student Life Simulator starter code.
You should complete every incomplete function,
and add more functions and variables as needed.
Also add comments as required.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author: Michael Guerzhoy.  Last modified: Sept. 22, 2014

"""


# The total number of hours from 12AM Monday to 5PM Friday.
HOURS_IN_WEEK = 24 * 5 - 7

# Global variables.
hours_slept = 0  # total number of hours that the student has slept so far
hours_left = HOURS_IN_WEEK  # number of hours that remain in the week
knols = 0   # number of knols assigned
alertness = True

def knols_per_hour(subj, is_alert):
    pass  # delete this line and add appropriate comments and code


def attend_lecture(subj, hrs):
    global alertness, knols, hours_left, hours_slept    # defining global variables needed for function to operate
    if alertness == True:   # if alert (as defined by sleep and coffee), maximum knol earnings as described below
        if subj == "CSC":   # if subject studied is CSC
            knols += 4 * hrs
        elif subj == "MAT" or "PHY" or "CIV" or "ESC":  # all these subjects have same knol earnings per hour
            knols = knols + 2 * hrs
            
    else:                   # if not alert
        if subj == "CSC":   #knol earnings are halved
                knols = knols + 2 * hrs
        elif subj == "MAT" or "PHY" or "CIV" or "ESC":                                
                knols = knols + 1 * hrs
    hours_left = hours_left - hrs                       # set new value for hours 
    

            
def drink_coffee():                                     # function for drinking coffee
    if alertness == True:                               # if alert;
        
        if hrs - hrs_since_coffee >= 3:                 # if hours since drinking a coffee is greater than 3
            caffiene = True                             # set caffiene to True
            hrs = hrs_since_coffee                      # updating time 
            
        else:                                           # for every other case;
            caffiene = False                            # set caffiene to False
            alertness = False                           # not alert; reduces knol earnings by half
            
    else:
        return "You are no longer alert."               # notifies you that you aren't alert

def is_alert():
    
    pass  # delete this line and add appropriate comments and code


def get_knol_amount():                                  # function returns no. of knols
    return knols                                        # returns number of knols up to current time

def sleep(hrs):
    """Update the global variables hours_left and hours_slept by
    respectively subtracting and adding hrs to each one, to account for hrs
    hours of sleep, as long as hrs is non-negative and there are enough
    hours left in the workweek.  Otherwise, do nothing.
    
    """
    
    # Declare hours_left and hours_slept as global so we can modify
    # these global variables.
    global hours_left, hours_slept                      # defines global variables
    
    # If hours is negative or there is not enough time in the week, we do
    # nothing and return right away.
    if hrs < 0 or hours_left < hrs:
        return
    
    # If we've reached this point, we should update hours_left and
    # hours_slept.
    hours_left -= hrs       #NOTE: this is the same as 
                            #hours_left = hours_left - hrs
    hours_slept += hrs


def get_hours_left():
    """Return the number of hours left in the workweek (the amount is stored
    in the variable hours_left, which should be kept up-to-date by the
    other functions).
    
    """
    
    return hours_left


if __name__ == '__main__':
    # You should thoroughly test all of your functions.  Here, we show how
    # to test sleep().
    
    # Test 1: Call sleep() once.
    print('Test 1')
    hours_slept = 0  # Note: no need to declare hours_slept global since
                     # we're not inside a function.
    hours_left = HOURS_IN_WEEK
    sleep(5)
    print('Hours slept:', hours_slept)     # should be 5
    print('Hours left:', hours_left)  # should be 108 (24 * 5 - 7 - 5)
    
    # Test 2: Call sleep() several times, see if the sleep accumulates.
    print('Test 2')
    hours_slept = 0
    hours_left = HOURS_IN_WEEK
    sleep(5)
    sleep(2)
    sleep(10)
    print('Hours slept:', hours_slept)     # should be 17 (2 + 5 + 10)
    print('Hours left:', hours_left)  # should be 96
    
    # Test 3: Call sleep() with more hours than there are in the workweek.
    print('Test 3')
    hours_slept = 0
    hours_left = HOURS_IN_WEEK
    sleep(200)
    print('Hours slept:', hours_slept)     # should be 0
    print('Hours left:', hours_left)  # should be 113
    
    # Test 4: Call sleep() with more hours than there are in the workweek.
    print('Test 4')
    sleep(100)
    sleep(100)  # shouldn't have an effect
    print('Hours slept:', hours_slept)     # should be 100
    print('Hours left:', hours_left)  # should be 13
    
    # Code from the handout.  It might be useful as a test case (if you
    # want to use it that way).
    #NOTE: it doesn't work yet: you have to implement the appropriate functions!
    print("Test 5")
    hours_slept = 0
    hours_left = HOURS_IN_WEEK
    sleep(8)                   # sleep from 12AM to 8AM on Monday
    attend_lecture("CSC", 2)   # attend the CSC lecture for 2 hours,
                               # gain 2*4 = 8 knols
    attend_lecture("MAT", 30)  # attend the MAT lecture for 30 hours,
                               # gain 30*2 = 60 knols (note that since the
                               # student was alert at the start of the
                                # lecture, they gain two knols per hour for
                                # the entire 30 hours)
    print(get_knol_amount())    # should print 68
    print(get_hours_left())     # should print 73 (24 * 5 - 7 - 40)
    
    # Test 6: 
    