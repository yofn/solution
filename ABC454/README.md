# ABC454

## C - Straw Millionaire

**Time Limit**: 2 sec / **Memory Limit**: 1024 MiB  
**Score**: 300 points

### Problem Statement

There are N types of items, item 1 through item N. Initially, Takahashi has only item 1.

He has M friends. If he gives item A_i to the i-th friend (1 \le i \le M), he will receive item B_i.

Find how many types of items he can obtain, including item 1.

### Constraints

- 2 \le N \le 3 \times 10^5
- 1 \le M \le 3 \times 10^5
- 1 \le A_i, B_i \le N
- A_i \neq B_i
- All input values are integers.

### Input

```
N M
A_1 B_1
A_2 B_2
...
A_M B_M
```

### Output

Output the answer.

### Sample Input 1

```
5 5
1 2
2 3
3 4
2 4
5 2
```

### Sample Output 1

```
4
```

For example, Takahashi can obtain item 4 by acting as follows:
- Give item 1 to the first friend. Receive item 2.
- Give item 2 to the fourth friend. Receive item 4.

He can obtain four types of items: items 1,2,3,4. Thus, output 4.

### Sample Input 2

```
3 2
2 1
3 2
```

### Sample Output 2

```
1
```

He can obtain one type of item: item 1.

### Sample Input 3

```
7 8
2 6
2 5
3 6
1 6
1 2
5 6
2 3
3 7
```

### Sample Output 3

```
6
```

---

## D - (xx)

**Time Limit**: 2 sec / **Memory Limit**: 1024 MiB  
**Score**: 425 points

### Problem Statement

You are given a string A consisting of `(`, `x`, `)`.

You can perform the following two types of operations on A any number of times in any order.

- Choose one occurrence of the substring `(xx)` in A and replace it with `xx`.
- Choose one occurrence of the substring `xx` in A and replace it with `(xx)`.

You are given a string B consisting of `(`, `x`, `)`. Determine whether you can make A equal to B.

You are given T test cases; solve each of them.

### Constraints

- 1 \le T \le 3 \times 10^5
- A and B are strings of length between 1 and 2 \times 10^6, consisting of `(`, `x`, `)`.
- The sum of |A| + |B| over all test cases is at most 2 \times 10^6.

### Input

```
T
case_1
case_2
...
case_T
```

Each test case:
```
A
B
```

### Output

Output T lines. The i-th line should contain the answer to the i-th test case.

For each test case, output `Yes` if you can make A equal to B, and `No` otherwise.

### Sample Input 1

```
6
(xx)x
x(xx)
(x)x
(xx)
)x()x(
)x()x(
x
(x)
(((((xx)))))x
x((((((((((xx)))))))))
((xx)xx)xx
(x((xx))x)(xx)
```

### Sample Output 1

```
Yes
No
Yes
No
Yes
Yes
```

For example, in the first test case:
- Replace `(xx)` (1st to 4th characters) with `xx`. A becomes `xxx`.
- Replace `xx` (2nd to 3rd characters) with `(xx)`. A becomes `x(xx)`.
