Dear Student,

I regret to inform you that you've received only **0** out of 10 points for this assignment.

There still exist some issues that should be addressed before the deadline: **2023-05-10 07:59:00 CEST (+0200)**. For further details, please refer to the following list:

<details><summary>[1p] Maximization problem should be converted to minimization problem &gt;&gt; type object &#x27;AssignmentProblem&#x27; has no attribute &#x27;costs&#x27;</summary></details>
<details><summary>[1p] Rectangular problem should be padded with constant to make it square &gt;&gt; type object &#x27;AssignmentProblem&#x27; has no attribute &#x27;costs&#x27;</summary></details>
<details><summary>[2p] Simplex should be able to solve assignment problems &gt;&gt; Tested code raises EmptyModelError in model.py:84</summary></details>
<details><summary>[1p] Should subtract min values in every row and column in cost matrix &gt;&gt; Tested code raises NotImplementedError in hungarian_solver.py:42</summary></details>
<details><summary>[2p] Should find partial assignment in cost matrix &gt;&gt; partial assignment is incorrect:</summary>- got: {}<br>- expected: {0: 0, 2: 2, 1: 1}<br>- for cost matrix: <br>&nbsp;&nbsp;&nbsp;&nbsp;[[0 3 4]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1 0 0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3 3 0]]<br>tip. remember that smaller index wins ties</details>
<details><summary>[2p] Should perform crossing algorithm on cost matrix &gt;&gt; Tested code raises NotImplementedError in hungarian_solver.py:50</summary></details>
<details><summary>[1p] Should create proper assignment based on dict of assignments &gt;&gt; hungarian algorithm returns incorrect objective:</summary>- got: None<br>- expected: 12<br>- for cost matrix: <br>&nbsp;&nbsp;&nbsp;&nbsp;[[4 9 8]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6 7 5]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4 6 1]]<br>- and assignment: None</details>

-----------
I remain your faithful servant\
_Bobot_