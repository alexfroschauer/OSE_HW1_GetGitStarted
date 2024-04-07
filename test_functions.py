from functions import isGanzeZahl
from functions import isNaturalNumber
from functions import isPrimeNumber

def test_isGanzeZahl():
    assert isGanzeZahl(1) == True
    assert isGanzeZahl(-1) == True
    assert isGanzeZahl(0.5) == False

def test_isNaturalNumber():
    assert isNaturalNumber(1) == True
    assert isNaturalNumber(10) == True
    assert isNaturalNumber(0.5) == False
    assert isNaturalNumber(-1) == False

def test_isPrimeNumber():
    assert isPrimeNumber(-3) == False
    assert isPrimeNumber(1.3) == False
    assert isPrimeNumber(3) == True
