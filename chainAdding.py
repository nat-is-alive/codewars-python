# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python

def overallSpeed(baseClock, numberOfCores):
    def calcCoreSpeed(multiplier):
        return baseClock * multiplier
    return calcCoreSpeed
print(overallSpeed(280,1)(15))
