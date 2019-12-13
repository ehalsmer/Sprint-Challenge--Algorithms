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


