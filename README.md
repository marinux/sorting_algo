# `sorting_algo`

this is my first and simple sorting algorithm that can do both ascending and descending sorting.

<img src="./example.png" />

---

## `table of contents`
- [`how it works`](https://github.com/marinux/sorting_algo#how-it-works)
- [`time complexity`](https://github.com/marinux/sorting_algo#time-complexity)
- [`license`](https://github.com/marinux/sorting_algo#license)

## `how it works`

here's how it works step by step:

    a - [1, 2, 5, 4] --> original array
    
    
    b - [1], [2, 5, 4] --> sorter finds the smallest number in the array and adds it to the output
    
    
    c - [1, 2], [5, 4] --> sorter finds the second smallest number in the array and adds it to the output
    
    
    d - [1, 2, 4], [5] --> sorter finds the third smallest number in the array and adds it to the output
    
    
    e - [1, 2, 4, 5] --> sorter adds the last item remaining to the output
 
   
## `time complexity`

Every time the current smallest number is found in the remaining numbers which have length `n`, the remaining numbers decrease by one and the new length to search through is n-1. this continues until `n-k = 0` and that's why the total amount of operations done is `n + (n - 1) + (n - 2) + ... + (n - k)`. Let's call this number `t`.

If we use Gauss' Summation to simplify `t`; we get `t = n(n+1)/2 = (n^2 + n)/2`. And since you can calculate time complexity by taking the highest power,
we find out that

    O(t) = O(n^2)

## `license`
This project is protected under the license GPLv3.
