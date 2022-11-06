import random

def PiMonteKarlo():
    circleRadius = 1
    circlePointsCount = 0
    amountOfPoints = int(input('Enter the amount of points: '))

    i = 0
    while i < amountOfPoints:       
        x = random.randint(1,999) / 1000 * circleRadius
        y = random.randint(1,999) / 1000 * circleRadius

        if (pow(x, 2) + pow(y, 2) <= pow(circleRadius, 2)):
           circlePointsCount += 1

        i += 1

    return 4 * circlePointsCount / amountOfPoints

print(PiMonteKarlo())