import numpy as np
from .model import AssignmentProblem, Assignment, NormalizedAssignmentProblem
from ..simplex.model import Model
from ..simplex.expressions.expression import Expression
from dataclasses import dataclass
from typing import List 



class Solver:
    '''
    A simplex solver for the assignment problem.

    Methods:
    --------
    __init__(problem: AssignmentProblem):
        creates a solver instance for a specific problem
    solve() -> Assignment:
        solves the given assignment problem
    '''
    def __init__(self, problem: AssignmentProblem):
        self.problem = NormalizedAssignmentProblem.from_problem(problem)

    def solve(self) -> Assignment:
        model = Model("assignment")
        # TODO:
        # 1) creates variables, one for each cost in the cost matrix
        # 2) add constraint, that sum of every row has to be equal 1
        # 3) add constraint, that sum of every col has to be equal 1
        # 4) add constraint, that every variable has to be <= 1
        # 5) create an objective expression, involving all variables weighted by their cost
        # 6) add the objective to model (minimize it!)
        #
        #  tip. model.add_constraint(Expression.from_vectors([x1,x2,x3], [3,2,1]) < 3))
        #       accepts lists as arguments and gives the same result as:
        #       model.add_constraint(3*x1 + 2*x2 + x3 < 3) 
        solution = model.solve()

        # TODO:
        # 1) extract assignment for the original problem from the solution object
        # tips:
        # - remember that in the original problem n_workers() not alwyas equals n_tasks()
        assigned_tasks = None 
        org_objective = None

        return Assignment(assigned_tasks, org_objective)



