Dear Student,

I'm happy to announce that you've managed to get **5** out of 10 points for this assignment.
<details><summary>You have already managed to pass 4 tests, so that is encouraging!</summary>&emsp;☑&nbsp;[1p] Maximization problem should be converted to minimization problem<br>&emsp;☑&nbsp;[1p] Rectangular problem should be padded with constant to make it square<br>&emsp;☑&nbsp;[2p] Simplex should be able to solve assignment problems<br>&emsp;☑&nbsp;[1p] Should subtract min values in every row and column in cost matrix</details>

There still exist some issues that should be addressed before the deadline: **2023-05-10 07:59:00 CEST (+0200)**. For further details, please refer to the following list:

<details><summary>[2p] Should find partial assignment in cost matrix &gt;&gt; partial assignment is incorrect:</summary>- got: {}<br>- expected: {0: 0, 2: 2, 1: 1}<br>- for cost matrix: <br>&nbsp;&nbsp;&nbsp;&nbsp;[[0 3 4]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1 0 0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3 3 0]]<br>tip. remember that smaller index wins ties</details>
<details><summary>[2p] Should perform crossing algorithm on cost matrix &gt;&gt; crossing algorithm is not performed properly:</summary>- got: <br>&nbsp;&nbsp;&nbsp;&nbsp;[[-3  9 -3  1]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 0  3  0  0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 0  3  0  0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-3  3  2  0]]<br>- expected: <br>&nbsp;&nbsp;&nbsp;&nbsp;[[1 9 0 4]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0 6 5 0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3 0 0 0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0 2 4 2]]<br>- for cost matrix: <br>&nbsp;&nbsp;&nbsp;&nbsp;[[0 9 0 4]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0 7 6 1]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2 0 0 0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0 3 5 3]]<br>- and partial assignment: {1: 0, 0: 2, 2: 1}</details>
<details><summary>[1p] Should create proper assignment based on dict of assignments &gt;&gt; hungarian algorithm returns incorrect objective:</summary>- got: None<br>- expected: 12<br>- for cost matrix: <br>&nbsp;&nbsp;&nbsp;&nbsp;[[4 9 8]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6 7 5]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4 6 1]]<br>- and assignment: None</details>

-----------
I remain your faithful servant\
_Bobot_