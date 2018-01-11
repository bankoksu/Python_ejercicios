import refactorizarYatzy

if __name__ == "__main__":
	assert 15== Yatzy.chance(1,2,3,4,5),"falla chance"
	assert 15== Yatzy.chance(5,4,3,2,1),"falla chance"
	assert 23== Yatzy.chance(6,6,4,4,3),"falla chance"