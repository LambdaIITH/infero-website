+++
title = "Binary Search"
date = "2021-08-12"
author = "x, y, z"
description = ""
weight = 4
+++

### What is binary search? ###
Binary search is a search algorithm which finds the position of a certain element (the target value) in a sorted array. It is an important alogrithm as it has a low time complexity. While the idea of the algorithm is very simple, one must be careful while implementing it as it is very easy to make errors.

### The idea of binary search ###
Let us try finding the position of 8 in the given sorted array of 7 integers.  

1 3 4 6 8 9 10  

Initially our search space contains numbers from index 0 to 6. Let us look at the middle element (at index 3). Since the array is sorted and 6 < 8(target value), we can ignore the numbers with index 0 to 3. So now our search space consists of numbers from index 4 to 6.  

8 9 10  

Again we look at the middle element in the search space( at index 5). This time since 8(target value) < 9, we can ignore the numbers from index 5 to 6. So now our search space only consists of the number with index 4.  

8  

Now we check again and see that the remaining element is the same as our target value so we save the position and finish the search. It is also possible to not find the target value if it is not in the array. In that case the final search space will be empty. So we end the search and say that there is no such value in the array.

### The code ###
```cpp
long long binarySearch(long long arr[], long long l, long long r,long long x)  
{  
	long long pos =-1;  
	while(l<=r)  
	{  
		long long m = l + (r-l)/2;  
		if(arr[m]==x)  
		{  
			pos = m;  
			break;  
		}  
		else if(arr[m]>x)  
			r = m-1;  
		else  
			l = m+1;  
	}  
	return pos;  
}  

```
 

We use l + (r-l)/2 instead of (l+r)/2 to avoid overflow in the case of large numbers. To search through the entire array(assuming size n), you can pass l as 0 and r as n-1.

### Complexity ###
At each iteration we are dividing the search space by 2.
So if after k iterations our search space has 1 element, we can say that  
n/(2^k) = 1,  
which gives n = 2^k.  
Therefore, k = log_2(n).   
Hence we can say that the time complexity is O(log n).

### Discrete binary search ###
The real power of binary search is that it can be used on monotonic(non increasing or non decreasing) functions, normally when the domain is the set of integers. For example we can use binary search to find first x for which a given property is true or last x for which a given property is false. It also works if we have a true or false question where we have a series of false answers followed by a series of true answers or the opposite.

### Finding first x for which a property is true ###
The basic concept is that once we find m such that the property is true, our search space reduces to numbers with index from l to m. For example if we have a sorted array of elements and we want to find the index of the first number greater than the target value, once we find a number greater than the target value, we ignore all numbers to its right and if we find a number lesser than the target value, we ignore all numbers to its left, including the current number.  

```cpp  
long long binarySearch(long long arr[], long long l, long long r)  
{  
	while(l<r)  
	{  
		long long m = l + (r-l)/2;  
		if(p(arr[m])==true)  
			r = m;  
		else  
			l = m+1;  
	}  
	if(p(arr[l])==false)  
		return -1;  
	return 1;  
}  
```

### Finding last x for which a property is false ###

The concept is similar to the previous case where once we find m such that the property is false, our search space reduces to numbers with index from m to r. For example if we have a sorted array of elements and we want to find the index of the last number lesser than the target value, once we find a number lesser than the target value, we ignore all numbers to its left and if we find a number greater than the target value, we ignore all numbers to its right, including the current number.  
```cpp
long long binarySearch(long long arr[], long long l, long long r)  
{  
	while(l<r)  
	{  
		long long m = l + (r-l+1)/2;  
		if(p(arr[m])==false)  
			l = m;  
		else  
			r = m-1;  
	}  
	if(p(arr[l])==true)  
		return -1;  
	return 1;  
}  
``` 

In this case we are using l + (r-l+1)/2 instead of l + (r-l)/2. To undestand the reasoning behind this, consider the case where we have an array of size 2 where the value at index 0 gives false and value at index 1 gives true. If we use l+(r-l)/2, we get m as 0. Since it is false, our l will become m but in this case it remains the same i.e. l remains 0. This means that there is no change and now we have an infinite loop. To avoid this, instead of rounding down, we round up. This is why we use l + (r-l+1)/2.

### Rotated sorted array ###

If a sorted array has been rotated(shifted), we can still apply binary search on it. However, it is not enough to just look at the middle element. Suppose we are searching for the smallest element in the rotated array.Consider the rotated sorted array  

7 9 11 15 1 4  

The value of the middle element(in this case 11) does not tell us where the smallest element is. Even the neighbours doesn't help us. To solve this problem, we can compare the middle element with the first or last element and turn this problem into a true or false question. We check if the middle element is greater than or equal to the first element.If true our search space will consists of numbers with index m+1 to r and if false we can store that position and our search space will consist of numbers with index l to m-1. We will get a series of true followed by a series of false. Now it simply becomes a problem of finding the first false. However in this case, if we are given a sorted array, all the elements would give true. We could fix this by giving an extra condition. 

Instead of this we could check if the middle element is greater than the last element. Here in the case of sorted array, all elements would give false so it is correct to simply search for first false. Using the given idea one can now code it. This will be left as an exercise for the reader :)

### Binary search on real numbers ###

We can also use binary search when the domain consists of real numbers. Since the set of real numbers is dense, we must avoid using the equality condition and instead check if the absolute difference between the current value and the target value is smaller than some number which is very small(depending on the precision required).

### STL Support 

C++ have in built function implemented for arrays and also maps and sets they can be quite use-full at times, specially when you are adding or removing along the way of searching. 

Mainly there is 3 functions `binary_search` , `lower_bound`, `upper_bound` .

**`binary_search`** : This can be used on a vector or array object, it takes the range on which you want to search in the starting and ending address of the array or vector, the value you want to search for and also it can compare the element using custom compare function it returns a `bool` variable denoting the existence of the value in the given range. Example :
```cpp
int array[] = {1,4,5,8,9,11,20};  
int n = sizeof(array)/sizeof(array[0]);  
int val = 4;  
if(binary_search(array,array+n,val))  
	cout<<val<<" found"<<endl;  
else  
	cout<<val<<" not found"<<endl;  
```



**`lower_bound` & `upper_bound`**:  These two work in a similar fashion, to under how they works lets assume u have a shorted array or vector with repeated elements and you are searching for some value in the array. Lets say 
```cpp
int arr[] = {1,2,2,3,4,4,4,5,6,8};  
					 ^   ^
```



now those arrows denotes the starting and ending of the range of value 4. `lower_bound` returns the lowest iterator for with the array element is greater or equal to value, In other words it returns the starting of the range, for our example   
```cpp
auto pos = lower_bound(a,a+10,4);  
cout<<pos-arr<<endl;  //4  
```



In case of `upper_bound` it returns the pointer of element with is strictly greater than the value;

```cpp
auto pos = upper_bound(a,a+10,4);  
cout<<pos-arr<<endl;  //7  
```



These are also member function of `set` and `map` class. You can use them as `set.upper_bound(value)`.

For more information visit these pages.

[set lower bound](http://www.cplusplus.com/reference/set/set/lower_bound/), [set upper bound](http://www.cplusplus.com/reference/set/set/upper_bound/)

### Conclusion ###

Now that you have reached here, you should go ahead and solve problems to help you get used to recognizing when and how to use binary search to solve problems.  
Few things to keep in mind   

1. You can use the given time limit to help you identify if binary search is required.  
2. Decide on what you are looking for and make a condition which effectively searches for the target value.  

### Some practice problems ###

Basic binary search: [Implement binary search](https://practice.geeksforgeeks.org/problems/who-will-win-1587115621/1)  
Rotated sorted array: [Finding minimum](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)  
Extension of previous problem: [Search in rotated array](https://leetcode.com/problems/search-in-rotated-sorted-array/)  
Finding square root: [sqrt](https://leetcode.com/problems/sqrtx/)    
[Sushi for two](https://codeforces.com/problemset/problem/1138/A)  
[K-divisible sum](https://codeforces.com/problemset/problem/1476/A)  
[Worms](https://codeforces.com/problemset/problem/474/B)  
[Computer game](https://codeforces.com/problemset/problem/1183/C)  
[Anton and fairy tail](https://codeforces.com/problemset/problem/785/C)  
[Boxes packing](https://codeforces.com/problemset/problem/1066/D)
###Resourses used###
[https://www.youtube.com/watch?v=GU7DpgHINWQ&t=1s](https://www.youtube.com/watch?v=GU7DpgHINWQ&t=1s)  
[https://www.topcoder.com/thrive/articles/Binary%20Search](https://www.topcoder.com/thrive/articles/Binary%20Search)    
[https://www.geeksforgeeks.org/binary-search/](https://www.geeksforgeeks.org/binary-search/)
