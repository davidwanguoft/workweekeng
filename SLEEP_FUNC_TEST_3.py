hours_slept = 0
hours_left = 100

def sleep(hrs):
    global hours_slept, hours_left
    hours_slept = hrs    
    hours_left = hours_left - hours_slept
    if hrs < 0:
        return "Cannot sleep for negative time."
    elif hrs > hours_left:
        return "Cannot sleep for that long."
