+++
title = "Java Libraries"
date = "2021-08-12"
author = "x, y, z"
description = ""
weight = 3
+++

### Data Structures
- **ArrayList**: [ArrayList](https://www.geeksforgeeks.org/arraylist-in-java/) is present in the `java.util` package.
The advantage of using ArrayList is, it provides dynamic arrays (whose size can be changed). But, it is slightly slower compared to the normal arrays.
  #### 1. Adding elements
  * **add(Object)**: To add an object at the end of the list
  * **add(int index, Object)**: To add an object at a specific index
  #### 2. Changing elements
  * **set(int index, Object)**: To change the element at an specified index.
  #### 3. Removing elements
  * **remove(Object)**: To remove the first occurrence of the given element.
  * **remove(int index)**: To remove the element at the specified index.

  **Example code**:
```java
import java.io.*;
import java.util.*;

class ArrayListExample {

	public static void main(String[] args){
		//Declaring an ArrayList of size 0
		//The parenthesis is used to declare the size of the ArrayList initially				
		ArrayList<Character> arrli = new ArrayList<Character>();

		arrli.add('a');
		arrli.add('c');
		arrli.add('d');

		//Printing the ArrayList
		System.out.println(arrli);

		//Adding 'b' at index 1 (Remember, it is 0-indexing)
		arrli.add(1,'b');
		System.out.println(arrli);

		//Changing the element at index 2 to 'e'
		arrli.set(2,'e');
		System.out.println(arrli);

		//Removing the element at index 1
		arrli.remove(1);
		System.out.println(arrli);
	}
}
```
**Output**:

```
[a, c, d]
[a, b, c, d]
[a, b, e, d]
[a, e, d]
```
- **HashMap**: [HashMap](https://www.geeksforgeeks.org/java-util-hashmap-in-java-with-examples/) is present in the `java.util` package. It stores the data in <key, value> pairs. The keys in the map are always unique, while, the values may repeat.
  #### 1. Adding elements
  * **put(Key, Value)**: To add a <key, value> pair to the map.
  #### 2. Changing elements
  * **put(Key,Value)**: We can use the same function to change the value of an existing <key, value> pair.
  #### 3. Removing elements
  * **remove(Key)**: To remove the <key,value> pair given the key.

  **Example code**:
```java
import java.util.*;
import java.io.*;

class HashMapExample {

	public static void main(String[] args) {
		HashMap<String, Integer> map = new HashMap<String, Integer>();

		//Adding elements
		map.put("abc", 1);
		map.put("def", 2);
		map.put("ghi", 4);
		map.put("xyz", 7);
		System.out.println(map);

		//Changing elements
		//Here, we changed the value of "ghi" to 3
		map.put("ghi", 3);
		System.out.println(map);

		//Removing elements
		map.remove("def");
		System.out.println(map);

		//Traversing throgh the map
		for(Map.Entry<String, Integer> e : map.entrySet()){
			//e is a <key, value> pair
			//getKey() is usde to return the key of the <key, value> pair
			//getValue() is usde to return the value of the <key, value> pair
			System.out.println("Key: " + e.getKey() + " Value: " + e.getValue());
		}
	}
}
```
**Output**:

```
{abc=1, def=2, xyz=7, ghi=4}
{abc=1, def=2, xyz=7, ghi=3}
{abc=1, xyz=7, ghi=3}
Key: abc Value: 1
Key: xyz Value: 7
Key: ghi Value: 3
```
- **Stack**: [Stack](https://www.geeksforgeeks.org/stack-class-in-java/) is a linear data structure which follows the LIFO (Last In, First Out) principle. This can be thought of as books being placed one on top of the other. We can only take the topmost book of the stack easily.
  #### 1. Adding elements
  * **push(Object)**: To put an element at the top of the stack
  #### 2. Accessing elements
  * **peek()**: Returns the topmost element of the stack
  #### 3. Removing elements
  * **pop()**: Returns and removes the element from the top of the stack

  **Example code**:

```java
import java.util.*;
import java.io.*;

class StackExample {

	public static void main(String[] args) {
		//Declaring a stack of integer type
		//It can be written like this as well
		//Stack<Integer> s = new Stack<Integer>();
		Stack<Integer> s = new Stack();

		//Adding elements
		s.push(4);
		s.push(7);
		s.push(11);
		s.push(13);
		System.out.println(s);
		//Returning the topmost element
		System.out.println("The topmost element is " + s.peek());

		//Removing topmost element
		s.pop();
		//Stack is [4, 7, 11]
		System.out.println("The topmost element of updated stack(pop) is " + s.pop());
		//Stack is [4, 7]
		System.out.println("The topmost element of updated stack(peek) is " + s.peek());
	}
}
```
**Output**:
```
[4, 7, 11, 13]
The topmost element is 13
The topmost element of updated stack(pop) is 11
The topmost element of updated stack(peek) is 7
```

- **Queue**: [Queue](https://www.geeksforgeeks.org/queue-interface-java/) is a linear data structure which follows the FIFO (First In, First Out) principle. It is present in ```java.util``` package.
  #### 1. Adding elements
  * **add(Object)**: To put an element at the back of the queue
  #### 2. Accessing elements
  * **peek()**: Returns the front element of the queue
  #### 3. Removing elements
  * **poll()**: Returns and removes the element from the front of the queue. ```pop()``` can be used as well.


**Example code**:

```java
import java.util.*;
import java.io.*;

class QueueExample {
	public static void main(String[] args) {
		//Declaring a queue of integer type
		//For priority queue, use,
		//Queue<Integer> s = new PriorityQueue<Integer>();
		Queue<Integer> q = new LinkedList();

		//Adding elements
		q.add(4);
		q.add(7);
		q.add(11);
		q.add(13);
		System.out.println(q);
		//Returning the front element of the queue
		System.out.println("The front element is " + q.peek());

		//Removing front element
		q.poll();
		//Queue is [7, 11, 13]
		System.out.println("The front element of updated stack(pop) is " + q.poll());
		//Queue is [11, 13]
		System.out.println("The front element of updated stack(peek) is " + q.peek());
	}
}
```
**Output**:
```
[4, 7, 11, 13]
The front element is 4
The front element of updated stack(pop) is 7
The front element of updated stack(peek) is 11
```

### Useful in-built functions
1. **sort(arr)**: It is used to sort the array in either increasing or decreasing order. We can also use it sort a part of the array aka. subarray. It can also be used to sort strings as well. It is present in ```java.util``` package
**Example part of code**:
```java
int[] a = {15,6,3,5,9,10};
// This sorts in increasing order
Arrays.sort(a);
System.out.printf("Sorted array: %s\n", Arrays.toString(a));

//We need a Integer object array to sort it in decreasing order
Integer[] objectArray = new Integer[a.length];

for(int i= 0; i< a.length; i++) {
	//This converts the int element to Integer type
	objectArray[i] = Integer.valueOf(a[i]); // returns Integer value
}

//This sorts in decreasing order
Arrays.sort(objectArray, Collections.reverseOrder());
System.out.printf("Sorted array: %s", Arrays.toString(objectArray));
```
**Output**:
```
Sorted array: [3, 5, 6, 9, 10, 15]
Sorted array: [15, 10, 9, 6, 5, 3]
```

1. **binarysearch(arr, key)**: It is used to do a binary search on the given sorted array and element. It returns the position of the element. And, it returns -1 if the element is not present in the array. It is present in ```java.util``` package
**Example part of code**:
```java
int[] a = {15,6,3,5,9,10};
// Sort the array
Arrays.sort(a);
System.out.printf("Sorted array: %s\n", Arrays.toString(a));

int key = 9;
//Store the position of 9 in the given array
int res = Arrays.binarySearch(a, key);
if(res >= 0){
	System.out.println("The element is present at " + res);
} else {
	System.out.println("Element not found");
}
```
**Output**:
```
Sorted array: [3, 5, 6, 9, 10, 15]
The element is present at 3
```

3. **gcd()**: This returns the gcd of two numbers. This function is present in ```java.math.BigInteger``` class.

	**Example code**:
```java
import java.math.*;

class GCDExample {
	public static void main(String[] args) {
		String integer1 = "4";
		String integer2 = "18";
		//We convert the strings to BigInteger type to use this function
		BigInteger a = new BigInteger(integer1);
		BigInteger b = new BigInteger(integer2);
		System.out.println("GCD of " + integer1 + " and " + integer2 + " is " + a.gcd(b));
	}
}
```

**Output**:

```
GCD of 4 and 18 is 2
```

4. **isProbablePrime()**: It is used to determine if the number is prime or not. The parameter inside the function is the certainty. It is present in the ```java.math.BigInteger``` class.

**Example code**:

```java
import java.math.*;

class PrimalityExample {
	public static void main(String[] args) {
		BigInteger int1 = BigInteger.valueOf(7);
		BigInteger int2 = BigInteger.valueOf(15);
		System.out.println(int1.isProbablePrime(1));
		System.out.println(int2.isProbablePrime(1));
	}
}
```
**Output**:
```
true
false
```

**Note**:
1. It is advised to solve few problems based on each data structure so that you can use the right data structure for a problem.
2. It is recommended to use BufferedReader to read inputs as it is faster than Scanner.
3. Google is your best friend ;). You can always search how to do a certain functionality which would help you solve the problem.

### Problems:
- **Array/ArrayList**:
	1. https://www.codechef.com/problems/TLG
	2. https://www.codechef.com/problems/KJCP01
	3. https://www.codechef.com/problems/MSNSADM1
- **HashMap**:
	1. https://www.codechef.com/problems/CHFPLN
	2. https://www.codechef.com/problems/ATTND
	3. https://www.codechef.com/problems/TOTCRT
- **Stack**:
	1. https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/fun-game-91510e9f/
	2. https://www.codechef.com/LRNDSA02/problems/ZCO12001
- **Queue**:
	1. https://www.codechef.com/problems/FEMA2
	2. https://codedrills.io/contests/icpc-amritapuri-2020-preliminary-round/problems/break-merge-and-sort
----------------------------------------------------

<div align="right">By Srikaran </div>
