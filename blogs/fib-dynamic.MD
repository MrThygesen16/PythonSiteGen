
# Dynamic Programming: Fibonacci Sequence

______

## Background

> The Fibonnaci Sequence is a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.


## Recursive Approach

Using the above defintion we can define a recursive formula for generating numbers in the fibonacci sequence as follows:


``` 
fib (n) = fib(n-1) + fib(n-2) 
```

The resulting function in a program might look like:
```
def fib(n: int) -> int {

	match n {
		1 		=> 0,
		2 | 3	=> 1,
		_ 		=> { return fib(n-1) + fib(n-2); }, 
	}
}
```
*Note: I've chosen to implement this in a Rust/Scala like fashion. Structural pattern matching is just too good. I will definitely be doing a writeup on it in the future.* 



For reference, the first 15 Fibonacci numbers are:
```
1	2	3	4	5	6	7	8	9	10	11	12	13   14   15
0	1	1	2	3	5	8	13	21	34	55	89	144	 233  377
```

Unfortunately, calculating numbers in the fibonacci sequence using the function or formula above extremely inefficient. The time complexity of this algorithm (in terms of worst case) is `O(2^n)`. 

To put that in perspective, calcuating the `50th` fibonacci number in the sequence would take:
```
2 ^ 42 = 4398046511104 units of time 

(if the unit is milliseconds, it would take 50903 days!)
```


The reason for this extremely large cost is due to recalculating values we have already seen.

As a tree, finding the 5th number of the sequence would look like the following:
```
										   f(5)
									  /           \
								    f(4)	      f(3)
	    						  /     \         / \
								f(3)    f(2)   f(2)  1
								/ \     / \     / \
							  f(2) 1   1   0   1   0
							  / \
							 1   0
```

To calcuate the `5th` fibonacci number we are recaclulating:
```
f(3) -> 2 times
f(2) -> 3 times
```




## Tabulation Approach
As the name would suggest, tabulation relies heavily on understanding arrays.

The following snippet of code takes an array of length `2` and a target `n` (in this case our target is 15). The total complexity for this approach is `O(n)`. Since all we are doing is iterating through a loop from `2` to `n`, hence a linear time complexity.


```java
Long[] fibList = {(long) 0 , (long) 1};

int target = 15;
 
System.out.println("1: 0 \n2: 1");

// this is known as tabulation:
// aka bottom-up
for (int i = 2; i < target; i++){

	long temp = fibList[0] + fibList[1];
	System.out.println((i+1) + ": " + temp);
	
	fibList[0] = fibList[1];
	fibList[1] = temp;
}

 System.out.println("=== Target Found ===");
```

The array is initialized to the first and second numbers of the sequence `{0,1}`. From here we calculate the value of the next number of the sequence by adding the previous two numbers together. Not only is this highly-efficient in terms of time complexity when compared to the naive approach above, it is also extremely efficient in terms of memory usage. One of the issue with the recursive approach is that for each recursive call we are pushing a frame onto the stack. For a large enough value of `n`, this may cause a stack overflow error. In which case the program will crash.

For `target = 15`, the output of the program displays:

```
1: 0
2: 1
3: 1
4: 2
5: 3
6: 5
7: 8
8: 13
9: 21
10: 34
11: 55
12: 89
13: 144
14: 233
15: 377
=== Target Found ===
```

If we refer to the sequence provided above, we can verify that this result is correct.  


```
										   5   [t]
									     /      ^     
									    3	    |       
	    						       /        |     
								      2         |     
								     /          | 
							        1        	|
							       / 			|
							      1   			|
								 /			Start with
								0			  1 & 0
											And work up
```

This is what is known as a "bottom-up" approach. Rather than trying to start at the target index and work our way down to our base cases `{0,1}`, we instead start at these cases and work our way to our target index. 

