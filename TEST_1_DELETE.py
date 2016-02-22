# The total number of hours from 12AM Monday to 5PM Friday.
HOURS_IN_WEEK = 24 * 5 - 7

# Global variables.
hours_slept = 0  # total number of hours that the student has slept so far
hours_left = HOURS_IN_WEEK  # number of hours that remain in the week
knols = 0 

def knols_per_hour(subj, is_alert):
    pass  # delete this line and add appropriate comments and code


def attend_lecture(subj, hrs):
    global knols
    global hours_left
    global hours_slept
    if alertness == True:
        if subj == "CSC":
            knols += 4 * hrs
        elif subj == "MAT" or "PHY" or "CIV" or "ESC":
            knols = knols + 2 * hrs
    else:
        if subj == "CSC":
                knols = knols + 2 * hrs
        elif subj == "MAT" or "PHY" or "CIV" or "ESC":                                
                knols = knols + 1 * hrs
    hours_left = hours_left - hrs
    
alertness = True


