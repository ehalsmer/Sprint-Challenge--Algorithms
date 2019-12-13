#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

```python
    a = 0
    while (a < n * n * n): 
      a = a + n * n
```
The time complexity for a = 0 is O(1), since it's simply an assignment operator. The while loop has time complexity O(n). This is because the steps needed for a to reach n^3 by adding n^2 each step is n^3 / n^2 = n. We then take O(1) + O(n). Over all, (a) has time complexity O(n) because O(1) is insignificant in comparison.


b) O(n log n)
```python
    sum = 0 # O(1)
    for i in range(n): # O(n)
      j = 1 # O(1)
      while j < n: # O(log n)
        j *= 2 # O(1)
        sum += 1 # O(1)
```
O(1) + O(n) * (O(1) + O(log n) * (O(1) + O(1))) ---> simplifies to: O(n log n)

Taking the two largest time complexities (annotated above), we multiply them because one loop is nested inside the other. Over all, the time complexity is O(n log n).


c) O(n)
```python
    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
This one also has time complexity of O(n), because it will take n times to subtract 1 from n until we get to 0 (at which point the function stops recursing). 



## Exercise II

Essentially what we're doing is searching for the highest floor on which the egg won't break, and we want to find it as efficiently (with fewest drops and breaks) as possible. Because the floors are sorted, we can use a binary search to do this. 

1. Drop an egg from the middle floor.
2. If it breaks, move to the lower half's middle floor and repeat
3. Else move to the higher half's middle floor and repeat. 

Repeat steps 1-3 until we've found the highest floor on which the egg doesn't break. We'll know when we've reached it because the number of floors is finite (they can't be divided indefinitely).

The runtime complexity for this algorithm is O(log n), because each loop reduces the search space by half. 