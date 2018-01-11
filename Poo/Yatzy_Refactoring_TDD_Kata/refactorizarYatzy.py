class Yatzy:

    def chance(dice):
        return sum(dice)


    def yatzy(dice):
    	if dice.count(dice[0]) == len(dice):
    		return 50

    	return 0
#código que se cambio
    """ counts = [0]*(len(dice)+1)
        for die in dice:
            counts[die-1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0"""


    def ones( d1,  d2,  d3,  d4,  d5):
        sum = 0
        if (d1 == 1):
            sum += 1
        if (d2 == 1):
            sum += 1
        if (d3 == 1):
            sum += 1
        if (d4 == 1):
            sum += 1
        if (d5 == 1): 
            sum += 1

        return sum



	
if __name__ == "__main__":
	assert 15== Yatzy.chance([1,2,3,4,5]),"falla chance"
	assert 15== Yatzy.chance([5,4,3,2,1]),"falla chance"
	assert 23== Yatzy.chance([6,6,4,4,3]),"falla chance"

	assert 50 == Yatzy.yatzy([1,1,1,1,1]),"falla yatzy"
	assert 50 == Yatzy.yatzy([5,5,5,5,5]),"falla yatzy"
	assert 0 == Yatzy.yatzy([1,1,1,1,3]),"falla yatzy"
	assert 0 == Yatzy.yatzy([1,2,3,4,5]),"falla yatzy"

	assert 5 == Yatzy.ones(1,1,1,1,1),"falla ones"
	assert 3 == Yatzy.ones(1,1,1,5,6),"falla ones"
	assert 1 == Yatzy.ones(2,4,6,3,1),"falla ones"
	assert 0 == Yatzy.ones(2,3,4,5,6),"falla ones"
