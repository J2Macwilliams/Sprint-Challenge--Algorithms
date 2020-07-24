#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    a = 0 is -> O(1)
    while (a < n * n * n): is -> O(n * 1) is O(n)
      a = a + n * n is -> O(1)

    Big O Equation O(1) * O(n) * O(1) -> O(n)
    It is a linear Algorithm. It is still dependent on the size of n. a will grow and reach n as if in n^3 didn't exist, because the n * n in the re-assignment of a basically cancels out 2 of the n's in the while loop. .
b)
    sum = 0 is -> O(1)
    for i in range(n): is -> O(n)
      j = 1 is O(1)
      while j < n: is -> O(n)
        j *= 2 is -> O(1)
        sum += 1 is -> O(1)

    Big O Equation O(1) * O(n) * O(1) * O(n) O(1) * O(1) -> O(n) * O(n) -> O(n^2)
    The result is polynomial : O(n^2).
    There are nested loops, which depend on the size of n twice. Both will have to run till completion.
c)
    def bunnyEars(bunnies):
      if bunnies == 0: -> single check -> O(1)
        return 0 -> O(1)

      return 2 + bunnyEars(bunnies-1) -> O(n)

    Big O Equation focus on the recursion which is O(n)  
    It is a linear Algorithm. The recursion is specifically based on the size of bunnies. which will cease when bunnies are equal to 0.

## Exercise II

Understanding:
- n-story building (don't know the full height)
- plenty of eggs? (there doesn't seem to be a limit to these eggs
- don't know if more eggs are broken the higher above f stories are climbed
- egg gets broken if thrown of floor >= f
- egg not broken if dropped off floor < f
- devise strategy to determine f

Plan
create a function for fewer_broken_eggs
searching for finding floor if
- f -> floor at which eggs are broken

function takes in 3 args: 
 - n -> height of building ,
 
 - e -> number of eggs

assign a variable to eggs
assign a variable to height
use logical operators 
- if no eggs are broken or height is less than f
    return 'Not at floor f yet'
- if height is greater than or equal to f
    decrement an egg
- if an egg is broken (compare to eggs variable to original )
    floor f will be equal to floor n  minus 1
    return floor f


create a recursive case - > O(n)
That increases the floors (n) one at a time until it reaches the top of the building

This will be a linear O(n) recursive algorithm
 
