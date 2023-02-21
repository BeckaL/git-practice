from main.fizzbuzz import fizzbuzz

def test_returns_fizz_for_multiples_of_three():
    number = 3
    assert "fizz" == fizzbuzz(number)

def test_returns_the_number_for_any_other_number():
    number = 4 
    assert number == fizzbuzz(number)

def test_returns_buzz_for_multiples_of_five():
    number = 5
    assert "buzz" == fizzbuzz(number)

def test_returns_fizzbuzz_for_multiples_of_fifteen():
    number = 30
    assert "fizzbuzz" == fizzbuzz(number)