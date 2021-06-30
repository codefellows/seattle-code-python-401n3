## Code Challenge
> Given a 2 linked lists, return the count of duplicate values

Given 2 ll, return the count of duplicate values

```text
Algo
def function count_common_nodes
  current1 assigned to ll1 head
  current2 assigned to ll2 head
  set count to 0

while current1 is not None
   while current2 is not None
      if (current1 == current2):  We want to look at values
          count = count + 1
      Move current2 to current2.next
    increment current1 to current1.next
    current2 to ll_2.head
return count
```

```python
# o(n^2) time
def count_common_nodes(ll_1, ll_2):
    current1 = ll_1.head
    current2 = ll_2.head
    count = 0

    while current1:
        while current2:
            if current1.value == current2.value:
                count += 1
            current2 = current2.next
        current1 = current1.next
        current2 = ll_2.head

    return count
```

```python
# o(2n) time
def count_common_nodes(ll_1, ll_2):
    current1 = ll_1.head
    current2 = ll_2.head
    list1 = []
    count = 0

    while current1:
        list1.append(current.value)
        current1 = current1.next
    
    while current2:
        if current1.value in list1:
            count += 1
        current2 = current2.next

    return count
```