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
        
        n = self.problem.size()

        variables = [[model.create_variable(f'c{i}{j}') for j in range(n)] for i in range(n)]
        varaibles = np.array(variables)

        for i in range(n):
            model.add_constraint(Expression.from_vectors(varaibles[i], [1]*n) == 1)
            model.add_constraint(Expression.from_vectors(varaibles[:,i], [1]*n) == 1)

            for j in range(n):
                model.add_constraint(varaibles[i, j] <= 1)
        
        model.minimize(Expression.from_vectors(varaibles.flatten(), self.problem.costs.flatten()))

        solution = model.solve()

        # TODO:
        # 1) extract assignment for the original problem from the solution object
        # tips:
        # - remember that in the original problem n_workers() not alwyas equals n_tasks()

        wynik = solution.assignment(model)

        num_workers = self.problem.original_problem.n_workers()

        assigned_tasks = np.full(num_workers, -1)
        org_objective = 0

        for i in range(num_workers):
            for j in range(n):
                if wynik[varaibles[i, j].index] == 1.0:
                    assigned_tasks[i] = j
                    org_objective += self.problem.original_problem.costs[i, j]
                    break

        return Assignment(assigned_tasks, org_objective)



