#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) TIME COMPLEXITY: `O(n)`
The while loop would be `O(n^3)`. But inside the loop, we are getting closer to the base case by `O(n^2)` with each iteration. This can be expressed as `n^3 / n^2 = n`. Hence, the time complexity is `O(n)`.

b) TIME COMPLEXITY: `O(n^2)`
The for loop is `O(n)`. The inside while loop is `O(n/2)`. So `n * n/2` is considered `n^2`, dropping the `1/2` constant.

c) TIME COMPLEXITY: `O(n)`
The number of recursive calls made is approximately `n`. Increasing `n` increases the number linearly.

## Exercise II

The building has an arbitrary number of stories.

Start at floor 1 (0 is ground) and go up until we are at a floor where the egg breaks.
This linear strategy minimizes broken eggs but not *dropped* eggs.

A binary strategy minimizes dropped eggs.
Start at the middle floor. If the egg breaks, eliminate the top half of the building from consideration and go to the midpoint of the remaining half. Or, if the egg does not break, eliminate the lower half and go up to the middle of the remaining top half. 
When the egg breaks, eliminate all above floors. In the remaining space, binary search for a floor where the egg does not break and eliminate all below floors. Do this until one floor remains.

With this strategy, the specific floor can be determined in `O(log n)` time complexity.