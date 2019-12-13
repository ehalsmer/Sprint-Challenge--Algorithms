## Strategy for robot sorting:

We can use something similar to selection sort. Except instead of always selecting the smallest item: as we move to the right, we select the largest item, and as we move to the left, we select the smallest. Gradually the two ends of the array will be sorted, and our range of movement will shrink towards the middle.

We can use the light to keep track of whether we're moving to the right (selecting largest, light on), or moving to the left (selecting smallest, light off).

Since the robot starts at position 0, we'll have him pick up the item there and turn on the light (selecting for largest). Then move right, at each step comparing what it is carrying to the item in front of it. If what is in front of him is larger than what he's carrying, he swaps. He continues moving right until he reaches the end of the search space. At the end, if the item in front is smaller, he swaps, if not, he does not swap. Because he's at the end, he now turns his light off and starts to move left, selecting for smallest. This time, he will stop when he reaches a blank spot, and drop the smallest item (which he should be carrying) in that spot. The search space now shrinks by two (both the far right and far left items are sorted). He moves to the right, and repeats the above process. 

Base case will be if the search space is 1 item long. Or maybe 2 items long?

Recursive process:
1. turn light on, pick up item
2. While moving right/selecting for largest (while self position is < end ) [while loop]
    1. move right
    2. compare item in front to item carried. If item in front is larger, swap.
3. turn light off
4. While moving left/selecting for smallest (until we find empty spot) [while loop]
    1. move left
    2. compare item in front to item carried. If item in front is smaller, swap.
5. Put item down (should be smallest into empty spot at far left)
6. Repeat steps 1-5 with subarray: list[1:len(list)-2] (the two ends are now sorted)

Steps 2 and 4 could be generalized by checking if the light is on:

if light on:
    1. move right
    2. compare item in front to item carried. If item in front is larger, swap.

if light off:
    1. move left
    2. compare item in front to item carried. If item in front is smaller, swap. If spot is empty: drop.

We could also use the light to indicate whether the robot is carrying something. We shouldn't need to do this unless there are empty spots in some of the arrays. We want 'none' to be an indication the robot is at an empty spot.