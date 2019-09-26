def getUsername():
    username = 'admin'
    return username

def getPassword():
    password = 'password'
    return password

def getUserfail():
    userfail = ''
    return userfail

def getPassfail():
    passfail = ''
    return passfail

def getFilename():
    filename = 'assignment.md'
    return filename

def getFilefail():
    filename = ''
    return filename

def getCloseDate():
    return "2019-10-28"

def getCanSubmit():
    currentDate = "2019-10-26"
    closeDate = getCloseDate()
    if (currentDate <= closeDate):
        return True
    
    else:
        return False

def getCanSubmitFail():
    newCurrentDate = "2019-10-29"
    closeDate = getCloseDate()
    if (newCurrentDate > closeDate):
        return True
    
    else:
        return False

def getOccup():
    occupation = 'Instructor'
    return occupation

def getOccupFail():
    occupation = 'Student'
    return occupation

def get():
    yoyoyoy

def getFail();
    yooyoyyo