import price_info as info

def test_total_cost_shopping():
    result = info.total_cost_shopping()
    assert(result ==46.75)


def test_cost_of_fruits():
    result = info.cost_of_fruits('apple', 10)
    assert(result==12)

def test_cost_of_fruits_orange():
    expected_result = 14
    result = info.cost_of_fruits('orange',10)
    assert(expected_result == result)

