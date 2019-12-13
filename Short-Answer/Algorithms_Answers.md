#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

```python
    a = 0
    while (a < n * n * n): 
      a = a + n * n
```
The time complexity for a = 0 is O(1), since it's simply an assignment operator. The while loop has time complexity O(n). This is because the steps needed for a to reach n^3 by adding n^2 each step is n^3 / n^2 = n. We then take O(1) + O(n). Over all, (a) has time complexity O(n) because O(1) is insignificant in comparison.


b)


c)

## Exercise II


