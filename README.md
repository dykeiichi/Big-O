# Big O example

### The problem

In a rap contest, couples have to go on stage and make as many rhymes as possible from a list of words given to each individual contestant.

The rules are as follows:

* Rhymes must be 3 words long
* Words can't be repeated
* Both contestants must speak at least one word in each rhyme

### Input

| Type | Description |
|------|-------------|
|int| number of words by contestant 1 |
|int| number of words by contestant 2 |

### Output

| Function | Type | Description |
|----------|------|-------------|
| Best | int | Maximum number of rymes that can be made |
| Worst | int | Maximum number of rymes that can be made |
| Main | string | Output from Best and Worst functions, plus the time taked from both functions |

### About

In this proyect you can see the difference between two scripts that have the same input, and the same otput, but have a total diferent graphic of use of resources

the function named "worst" has a lineal graphic of resources O(n), while the function names "best" has a constant graphic of resources O(1)

you can try it, as you change the value of the number of words ingresed