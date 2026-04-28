# ABC455

## C - Vanish

**Time Limit**: 2 sec / **Memory Limit**: 1024 MiB  
**Score**: 300 points

### Problem Statement

You are given an integer sequence A = (A_1, A_2, \ldots, A_N).

Find the minimum possible sum of all elements of A after performing the following operation exactly K times.

- Choose an integer x. For each i such that A_i = x, replace the value of A_i with 0.

### Constraints

- 1 \le K \le N \le 3 \times 10^5
- 1 \le A_i \le 10^9
- All input values are integers.

### Input

```
N K
A_1 A_2 \ldots A_N
```

### Output

Output the answer.

### Sample Input 1

```
6 2
7 2 7 2 2 9
```

### Sample Output 1

```
6
```

Initially, A = (7, 2, 7, 2, 2, 9).

Performing the operation with x = 9 gives A = (7, 2, 7, 2, 2, 0).

Next, performing the operation with x = 7 gives A = (0, 2, 0, 2, 2, 0).

At this point, the sum is 0+2+0+2+2+0 = 6.

### Sample Input 2

```
8 6
1 2 3 4 1 2 3 4
```

### Sample Output 2

```
0
```

### Sample Input 3

```
10 2
3 3 4 1 1 3 3 1 5 1
```

### Sample Output 3

```
5
```

---

## D - Card Pile Query

**Time Limit**: 2 sec / **Memory Limit**: 1024 MiB  
**Score**: 400 points

### Problem Statement

There are N cards and N piles of cards.

The cards and the piles are numbered 1, 2, \ldots, N. Initially, pile i contains only card i.

Perform the following operation for each i = 1, 2, \ldots, Q in order:

- Move card C_i and all cards stacked on top of card C_i, preserving their order, on top of card P_i. It is guaranteed that immediately before performing the operation, cards C_i and P_i are in different piles, and card P_i is on top of some pile.

Find the number of cards in each pile after all operations are completed.

### Constraints

- 1 \le N, Q \le 3 \times 10^5
- 1 \le C_i, P_i \le N
- When the operations are performed in order, immediately before each operation, cards C_i and P_i are in different piles.
- When the operations are performed in order, immediately before each operation, card P_i is on top of some pile.
- All input values are integers.

### Input

```
N Q
C_1 P_1
C_2 P_2
\vdots
C_Q P_Q
```

### Output

Let A_i be the number of cards in pile i at the end. Output A_1, A_2, \ldots, A_N in this order, separated by spaces.

### Sample Input 1

```
5 4
1 3
4 5
1 4
4 2
```

### Sample Output 1

```
0 3 1 0 1
```

### Sample Input 2

```
7 8
3 1
5 4
2 5
5 7
2 3
6 2
3 4
5 1
```

### Sample Output 2

```
2 0 0 4 0 0 1
```
