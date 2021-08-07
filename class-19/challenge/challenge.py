# Given a LL, sum the values in the LL.
# Raise an expection if the ll was empty
# could negative values
# have access to LL stuff

# 10 -> 2 -> -2 -> 5 -> None  15
#                       ^
# ll_sum: 0 10 12 10 15


def get_sum_of_ll(ll):
    if not ll:
        raise ValueError('The Linked List Cannot be Empty')
    ll_sum = 0
    current = ll.head
    while current:
        ll_sum += current.value
        current = current.next
    return ll_sum