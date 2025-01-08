import pytest
from fizz_buzz import fizz_buzz



@pytest.mark.parametrize(
    "start, end",
    [
        (1, 101),
        (101, 1),
        (101, 101),
        (0, 0),
        (0, 101),
        (101, 0),
        (-1, -1),
    ],
)
def test_wrong_range_of_chosen_numbers(start, end):
    with pytest.raises(ValueError) as e:
        fizz_buzz(start, end)
    assert str(e.value) == "Both start and end must be between 1 and 100 inclusive."

@pytest.mark.parametrize(
    "start, end",
    [
        (4, 1),
        (15, 10),
        (100, 1),
        (14, 9),
        (100, 99),
    ],
)
def test_start_greater_than_end(start, end):
    with pytest.raises(ValueError) as e:
        fizz_buzz(start, end)
    assert str(e.value) == "Start must be less than or equal to end."

@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 2, ['1', '2']),
        (1, 5, ['1', '2', '3 fizz ', '4', '5 buzz ']),
        (9, 15, ['9 fizz ', '10 buzz ', '11', '12 fizz ', '13', '14', '15 fizz 15 buzz ']),
        (98, 100, ['98', '99 fizz ', '100 buzz ']),
        (7, 29, ['7', '8', '9 fizz ', '10 buzz ', '11', '12 fizz ', '13', '14', '15 fizz 15 buzz ', '16', '17', '18 fizz ', '19', '20 buzz ', '21 fizz ', '22', '23', '24 fizz ', '25 buzz ', '26', '27 fizz ', '28', '29'])
    ],
)
def test_fizz_buzz_output(start, end, expected):
    assert fizz_buzz(start, end) == expected
