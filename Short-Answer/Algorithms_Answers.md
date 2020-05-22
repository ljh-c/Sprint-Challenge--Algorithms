#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) TIME COMPLEXITY: `O(n)`
The while loop would be `O(n^3)`. But inside the loop, we are getting closer to the base case by `O(n^2)` with each iteration. This can be expressed as `n^3 / n^2 = n`. Hence, the time complexity is `O(n)`.

b) TIME COMPLEXITY: `O(n^2)`
The for loop is `O(n)`. The inside while loop is `O(n/2)`. So `n * n/2` is considered `n^2`, dropping the `1/2` constant.

c) TIME COMPLEXITY: `O(n)`
The number of recursive calls made is approximately `n`. Increasing `n` increases the number linearly.

## Exercise II


