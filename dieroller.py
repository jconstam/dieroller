#!/usr/bin/python3
import random

# For checking normalization https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.stats.shapiro.html

def getNumber( prompt ):
    while( True ):
        try:
            result = int( input( prompt ) )
            break
        except:
            pass
    return result

if __name__ == "__main__":
    random.seed( )

    dieCount = getNumber( 'How many: ' )
    dieType = getNumber( 'Which die to roll: ' )
    modifier = getNumber( 'Modifier: ' )
    print( str( dieCount ) + 'd' + str( dieType ) )
    sum = 0
    for i in range( 1, dieCount + 1 ):
        current = random.randrange( 1, dieType + 1 )
        sum = sum + current
        print( str( current ), end=' ' )
    print( )
    print( 'Total: ' + str( sum + modifier ) )