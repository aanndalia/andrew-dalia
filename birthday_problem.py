def birthdayProblem(numberOfPeople, numOfDaysInAYear):
    probabilityOfASharedBirthday = 1
    for i in range(0, numberOfPeople):
        term = float(numOfDaysInAYear - i) / numOfDaysInAYear
        probabilityOfASharedBirthday *= term
    probabilityOfNoSharedBirtdays = 1 - probabilityOfASharedBirthday
    return probabilityOfNoSharedBirtdays

def main():
    p = birthdayProblem(23, 365)
    print p
    
main()