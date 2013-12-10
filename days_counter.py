def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
      month == 8 or month == 10 or month == 12:
        return 31
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    return 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    else:
        if month1 < month2:
            return True
        else:
            if day1 < day2:
                return True
    return False
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gergorian calendar, and the first date is not after
       the second."""
        
    # YOUR CODE HERE!
    counter = 0
    assert dateIsBefore(year1, month1, day1, year2, month2, day2)
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        counter += 1
    return counter

def test():
    assert daysBetweenDates(2013,7,23,2013,7,24) == 1
    assert daysBetweenDates(2012,1,1,2013,1,1) == 366
    #assert daysBetweenDates(2000,1,2,2000,1,1) == AssertionError
    print "Testing is finished."

test()

#print daysBetweenDates(1973, 5, 22, 2013, 7, 23)
#print daysBetweenDates(2014, 7, 23, 2013, 7, 23)
print "Nancy: "
print daysBetweenDates(1973, 10, 4, 2013, 12, 9)
print "Emma: "
print daysBetweenDates(2007,12,31, 2013, 12, 9)
print "Nora: "
print daysBetweenDates(2006,4,28,2013,12,9)
print "Chris: "
print daysBetweenDates(1973, 5, 22, 2013, 9, 12)

