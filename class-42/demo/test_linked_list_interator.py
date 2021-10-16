import pytest

from linked_list_iterator import LinkedList

# @pytest.mark.skip("pending")
def test_for_in():
    sith_lords = LinkedList(('Vader', 'Sideous', 'Revan'))
    sith_lords_list = []
    for sith in sith_lords:
        sith_lords_list.append(sith)
    assert sith_lords_list == ['Vader', 'Sideous', 'Revan']

# @pytest.mark.skip("pending")
def test_sum_values():
    ll_values = LinkedList((10,20,30))
    ll_total = 0
    for i in ll_values:
        ll_total += i
    assert ll_total == 60

# @pytest.mark.skip("pending")
def test_list_comprehension():
    sith_lords = LinkedList(('Vader', 'Sideous', 'Revan'))
    cap_sith_lords = [sith.upper() for sith in sith_lords]
    assert cap_sith_lords == ['VADER', 'SIDEOUS', 'REVAN']

# @pytest.mark.skip("pending")
def test_list_cast():
    sith_lords = ['Vader', 'Sideous', 'Revan']
    siths = LinkedList(sith_lords)
    assert list(siths) == sith_lords

# @pytest.mark.skip("pending")
def test_range():
    num_range = range(1,20+1)
    nums = LinkedList(num_range)
    assert len(nums) == 20

# @pytest.mark.skip("pending")
def test_filter():
    nums = LinkedList(range(1,21))
    odds = [num for num in nums if num % 2]
    assert odds == [1,3,5,7,9,11,13,15,17,19]

# @pytest.mark.skip("pending")
def test_next():
    sith_lords = ['Vader', 'Sideous', 'Revan']
    iterator = iter(sith_lords)
    assert next(iterator) == 'Vader'
    assert next(iterator) == 'Sideous'
    assert next(iterator) == 'Revan'

# @pytest.mark.skip("pending")
def test_stop_iteration():
    sith_lords = LinkedList(['Vader', 'Sideous', 'Revan'])
    iterator = iter(sith_lords)
    with pytest.raises(StopIteration):
        while True:
            sith = next(iterator)

# @pytest.mark.skip("pending")
def test_str():
    siths = LinkedList(['Vader', 'Sideous', 'Revan'])
    assert str(siths) == '[ Vader ] -> [ Sideous ] -> [ Revan ] -> None'

# @pytest.mark.skip("pending")
def test_equals(): 
    lla = LinkedList(['Vader', 'Sideous', 'Revan'])
    llb = LinkedList(['Vader', 'Sideous', 'Revan'])
    assert lla == llb

# @pytest.mark.skip("pending")
def test_get_item():
    siths = LinkedList(['Vader', 'Sideous', 'Revan'])
    assert siths[0] == 'Vader'

# @pytest.mark.skip("pending")
def test_get_item_out_of_range():
    siths = LinkedList(['Vader', 'Sideous', 'Revan'])
    with pytest.raises(IndexError):
        siths[100]
