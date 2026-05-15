# ABC452

## C - Fishbones

**Time Limit**: 2 sec / **Memory Limit**: 1024 MiB  
**Score**: 300 points

### Problem Statement

Artist Takasago has created an object in the shape of a fish skeleton. The object consists of N ribs and one spine.

He wants to write one string on each of the N+1 bones, satisfying all of the following conditions.

- The length of the string written on the spine is N.
- For each rib i = 1, …, N, the following hold.
  - The length of the string written on rib i is A_i.
  - The B_i-th character of the string written on rib i equals the i-th character of the string written on the spine.
- Each of the strings written on the N+1 bones is one of S_1, …, S_M (duplicates allowed).

S_1, …, S_M are strings consisting of lowercase English letters, and they are all distinct.

For each j = 1, …, M, answer the following question.

Among the ways to write strings satisfying the conditions, is there one where the string written on the spine is S_j?

### Constraints

- N is an integer. 1 ≤ N ≤ 10
- A_i and B_i are integers. (1 ≤ i ≤ N)
- 1 ≤ B_i ≤ A_i ≤ 10 (1 ≤ i ≤ N)
- M is an integer. 1 ≤ M ≤ 200,000
- S_j is a string consisting of lowercase English letters. (1 ≤ j ≤ M)
- 1 ≤ |S_j| ≤ 10 (1 ≤ j ≤ M)
- S_1, …, S_M are pairwise distinct.

### Input

```
N
A_1 B_1
⋮
A_N B_N
M
S_1
⋮
S_M
```

### Output

Output M lines. The j-th line (1 ≤ j ≤ M) should contain `Yes` if there exists a way to write strings satisfying the conditions with S_j written on the spine, and `No` otherwise.

### Sample Input 1

```
5
5 3
5 2
4 1
5 1
3 2
8
retro
chris
itchy
tuna
crab
rock
cod
ash
```

### Sample Output 1

```
Yes
Yes
No
No
No
No
No
No
```

By writing chris, retro, tuna, retro, cod on ribs 1,2,3,4,5 respectively, the conditions are satisfied with retro written on the spine.

The length of retro is 5. For each rib, the following hold.
- The string written on rib 1 is chris, which has length 5. Its third character is r, which equals the first character of retro.
- The string written on rib 2 is retro, which has length 5. Its second character is e, which equals the second character of retro.
- The string written on rib 3 is tuna, which has length 4. Its first character is t, which equals the third character of retro.
- The string written on rib 4 is retro, which has length 5. Its first character is r, which equals the fourth character of retro.
- The string written on rib 5 is cod, which has length 3. Its second character is o, which equals the fifth character of retro.

---

## D - No-Subsequence Substring

**Time Limit**: 2 sec / **Memory Limit**: 1024 MiB  
**Score**: 400 points

### Problem Statement

You are given strings S and T consisting of lowercase English letters.

Among the non-empty substrings s of S, count those that do not contain T as a (not necessarily contiguous) subsequence.

Here, two substrings of S are distinguished if they are taken from different positions, even if they are equal as strings.

What is a substring? A substring of a string X is a string obtained by deleting zero or more characters from the beginning and zero or more characters from the end of X.

What is a subsequence? A subsequence of a string X is a string obtained by deleting zero or more elements from X and arranging the remaining elements in their original order.

### Constraints

- S is a string consisting of lowercase English letters.
- 1 ≤ |S| ≤ 2 × 10^5
- T is a string consisting of lowercase English letters.
- 1 ≤ |T| ≤ 50

### Input

```
S
T
```

### Output

Output the answer.

### Sample Input 1

```
abrakadabra
aba
```

### Sample Output 1

```
51
```

For example, the substring abr consisting of the first through third characters of S does not contain T as a subsequence. Including this, there are 51 substrings satisfying the condition, such as k (only the fifth character of S) and akada (the fourth through eighth characters of S).

Note that the string abr can be obtained both as the substring from the first to third characters of S and as the substring from the eighth to tenth characters of S, but they are taken from different positions, so they are counted separately.

### Sample Input 2

```
aaaaa
a
```

### Sample Output 2

```
0
```

All non-empty substrings of S contain T as a subsequence. Thus, there are no substrings satisfying the condition, so output 0.

### Sample Input 3

```
rdddrdtdcdrrdcredctdordoeecrotet
dcre
```

### Sample Output 3

```
263
```
