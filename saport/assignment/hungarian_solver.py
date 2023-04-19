import numpy as np
from .model import Assignment, AssignmentProblem, NormalizedAssignmentProblem
from typing import List, Dict, Tuple, Set
from numpy.typing import ArrayLike

class Solver:
    '''
    A hungarian solver for the assignment problem.

    Methods:
    --------
    __init__(problem: AssignmentProblem):
        creates a solver instance for a specific problem
    solve() -> Assignment:
        solves the given assignment problem
    extract_mins(costs: ArrayLike):
        substracts from columns and rows in the matrix to create 0s in the matrix
    find_max_assignment(costs: ArrayLike) -> Dict[int,int]:
        finds the biggest possible assinments given 0s in the cost matrix
        result is a dictionary, where index is a worker index, value is the task index
    add_zero_by_crossing_out(costs: ArrayLike, partial_assignment: Dict[int,int])
        creates another zero(s) in the cost matrix by crossing out lines (rows/cols) with zeros in the cost matrix,
        then substracting/adding the smallest not crossed out value
    create_assignment(raw_assignment: Dict[int, int]) -> Assignment:
        creates an assignment instance based on the given dictionary assignment
    '''
    def __init__(self, problem: AssignmentProblem):
        self.problem = NormalizedAssignmentProblem.from_problem(problem)

    def solve(self) -> Assignment:
        costs = np.array(self.problem.costs)

        while True:
            self.extracts_mins(costs)
            max_assignment = self.find_max_assignment(costs)
            if len(max_assignment) == self.problem.size():
                return self.create_assignment(max_assignment)
            self.add_zero_by_crossing_out(costs, max_assignment)

    def extracts_mins(self, costs: ArrayLike):
        #TODO: substract minimal values from each row and column
        n, m = costs.shape

        for row_i in range(n):
            costs[row_i] -= costs[row_i].min()
        
        for col_i in range(m):
            costs[:, col_i] -= costs[:, col_i].min()

        # raise NotImplementedError()

    def add_zero_by_crossing_out(self, costs: ArrayLike, partial_assignment: Dict[int,int]):
        # TODO:
        # 1) "mark" columns and rows according to the instructions given by teacher
        # 2) cross out marked columns and not marked rows
        # 3) find minimal uncrossed value and subtract it from the cost matrix
        # 4) add the same value to all crossed out columns and rows
        n, m = costs.shape

        marked_rows = np.zeros(n)
        marked_cols = np.zeros(m)
        
        zeros_in_rows = np.array([n-np.count_nonzero(costs[i]) for i in range(n)])
        zeros_in_cols = np.array([m-np.count_nonzero(costs[:,i]) for i in range(m)])
        
        for task, cheapes_worker in partial_assignment.items():
            if zeros_in_rows[cheapes_worker] <= zeros_in_cols[task]:
                marked_rows[cheapes_worker] = 1
                for col in range(m):
                    if costs[cheapes_worker, col] == 0:
                        zeros_in_cols[col] -= 1
            else:
                marked_cols[task] = 1
                for row in range(n):
                    if costs[row, task] == 0:
                        zeros_in_rows[row] -= 1

        for i in range(n):
            if marked_rows[i] == 1 or marked_cols[i] == 1:
                costs[i] = 0
        
        min_cost = -2137
        for i in range(m):
            for j in range(n):
                if marked_cols[i] == 1 or marked_rows[j] == 1:
                    if costs[i, j] == 0:
                        continue
                    if min_cost == -2137 or min_cost > costs[i, j]:
                        min_cost = costs[i, j]

        if min_cost == -2137:
            return
        
        costs -= min_cost

        marked_rows_indexes = np.where(marked_rows == 1)
        marked_cols_indexes = np.where(marked_cols == 1)
        
        for i in marked_rows_indexes:
            costs[i] += min_cost
        
        for i in marked_cols_indexes:
            costs[:,i] += min_cost

        # raise NotImplementedError()

    def find_max_assignment(self, costs) -> Dict[int,int]:
        partial_assignment = dict()
        # TODO: find the biggest assignment in the cost matrix
        # 1) always try first the row with the least amount of 0s
        # 2) then use column with the least amount of 0s
        # TIP: remember, rows and cols can't repeat in the assignment
        #      partial_assignment[1] = 2 means that the worker with index 1
        #                                has been assigned to task with index 2
        return partial_assignment

    def create_assignment(self, raw_assignment: Dict[int,int]) -> Assignment:
        # TODO: create an assignment instance based on the dictionary
        # tips:
        # 1) use self.problem.original_problem.costs to calculate the cost
        # 2) in case the original cost matrix (self.problem.original_problem.costs wasn't square)
        #    and there is more workers than task, you should assign -1 to workers with no task
        assignment = None
        total_cost = None
        return Assignment(assignment, total_cost)