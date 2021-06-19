# Leetcode
My solutions to Leetcodes
## Category
### Binary search
- 35 Search Insert Position
- 34 Find First and Last Position of Element in sorted Array
- 704 binary search
- 981 Time Based Key-Value Store
- 33 Search in Rotated Sorted Array
- 81 Search in Rotated Sorted Array II
- 153 Find Minimum in Rotated Sorted Array
- 154 Find Minimum in Rotated Sorted Array II


- 852 Peak index in a mountain Arragy
- 69 sqrt(x)
- 74 search a 2D matrix
- 875 KoKo Eating Bananas
- 1011 Capactity To Ship Packages Within D days
- 4 Median of Two sorted Arrays
- 378 Kth Smallest Element in a Sorted Matrix
- 668 Kth Smallest Number in Multiplication Table
- 719 Find Kth Smallest Pair Distance
- 786 Kth Smallest Prime Fraction
### Two pointers
- 11 Container With most Water
- 15 3sum
- 16 3sum closet
- 4sum
- 26 Remove Duplicates from sorted Array
- 27 Remove element
- 28 Implement str
- 42 Trapping Rain Water
- 75 sort colors
- 80 Remove Duplicates from sorted Array
- 88 Merge sorted Array
- 125 Valid Palindrome
- 167 Two Sum II - Input array is sorted
### Sorting
- 1 Selection sort
    This program sorts the list by finding theminimum of the list, removing it from the original list, and appending it onto the output list. As it finds the minumum during each iteration, the length of the original list gets shorter by one and the length of the output list gets longer one. This program uses the min function with a lambda function to find the index of the minmum valuein the unsorted list. The output list is created using a list comprehension. This algorithm is O(n2).
- 2 Bubble Sort
    This program sorts the list by looping through the original list and finding any adjacent pairs of numbers that are out of order. If it finds such a pair, it switches their locations. It continues to check for adjacent pairs that are out of order until it has completed the pass through the list. This algorithm is O(n2). 
- 3 Insertion Sort
    This program sorts the list by sequentially inserting each element into the proper location within the sorted front portion of the original list. It starts by inserting the second number into the proper location within the firt two numbers. It then inserts the third number into the proper location within the first three numbers. After each iteration, the front portion of the list(i.e. the sorted portion) will grow in length by 1. A number is removed from the back portion of the list(i.e. the unsorted portion) and placeed into the appropriate location in the sorted portion of the list. Once we place the last number into the correct location within the sorted numbers, the entire list will have become sorted. This algorithm is O(n2).
- 4 Binary Inseration Sort
    This program sorts the list by sequentially inserting each element into the proper location within the sorted front portion of the original list. It starts by inserting the second number into the proper location within the first two numbers. It them inserts the third number into the proper location within the first two numbers. It then inserts the third number into the proper location with the first three numbers. After each interation, the front portion of the list(i.e. the sorted portion) will gro in length by 1. A number is removed from the back portion of the list(i.e. the unsorted portion) and placed into the appropriate location in the sorted portion of the list. Once we place the last number into the correct location within the sorted numbers, the entire list will have become sorted. This still O(n2).
- 5 Counting Sort
This program starts by creating a dictionary of key-value pairs that records the total count of each element of the original list. The minimum and maximum value of the list is also found. The program then loops through every integer between the min and max value(in order) and appends that number to the cutput list based on its count within the original list, then the output list will be extended by [3,3,3,3]. The output will be the sorted form of the original list as it consists of an ordered list of the numbers in the original lsit. this approach is linear time sorting algorithm that sorts in O(n+k) time, where n is the number of elements and k is the 
### Binary Tree Divide & Conquer
### BST Iterator
### BFS

### DFS
-
### Dynamic Programming
### Heap
### Union Find
### Trie
### List


