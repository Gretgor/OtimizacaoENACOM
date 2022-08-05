from science_optimization.builder import (
    BuilderOptimizationProblem,
    Variable,
    Constraint,
    Objective,
    OptimizationProblem
)
from science_optimization.function import (
    FunctionsComposite, 
    LinearFunction,
)
from science_optimization.solvers import Optimizer
from science_optimization.algorithms.linear_programming import Glop
from typing import List
import numpy


# Problem class
class InvestmentProblem(BuilderOptimizationProblem):
	# First reading of the problem info:
	# prices and returns are converted to numpy because we will
	# need to use them as coefficients in the restrictions and
	# objective function.
	def __init__(self, prices: List[int], returns: List[int], 
	             budget: int, conflicts: List[List[int]],
	             dependencies: List[List[int]]):
		self.__varnum = len(prices)
		self.__prices = numpy.array([x for x in prices])
		self.__returns = numpy.array([x for x in returns])
		self.__budget = budget
		self.__conflicts = conflicts
		self.__dependencies = dependencies
		print(self.__conflicts,self.__dependencies)
		
	# building variables: pretty much the same thing we saw in the
	# second class.
	def build_variables(self):
		lower = numpy.zeros((self.__varnum, 1))
		upper = numpy.ones((self.__varnum, 1))
		# all discrete, naturally
		types = ['d']*self.__varnum
		variables = Variable(lower, upper, types)
		return variables
		
	# building constraints: making sure to add the conflicts and
	# dependencies
	def build_constraints(self):
		cons_set = FunctionsComposite()
		# first: budget constraint. Pretty much the same as the knapsack
		# example we saw in class
		budgetary = LinearFunction(c=self.__prices.reshape(-1,1), d=-self.__budget)
		cons_set.add(budgetary)
		
		# "base" for the coefficients in the rest of the constraints:
		# set all coefficients to 0 at first, and then change only the
		# coefficients of the relevant variables.
		base = numpy.zeros((self.__varnum, 1))		
		# conflict constraints.
		# basically, if a and b conflict, then
		# a+b <= 1, that is, a+b-1 <= 0
		for item in self.__conflicts:
			a = item[0]
			b = item[1]
			base[a] = 1
			base[b] = 1
			newcons = LinearFunction(c=base.reshape(-1,1),d=-1)
			cons_set.add(newcons)
			base = numpy.zeros((self.__varnum, 1))
			
		# dependency constraints.
		# if a depends on b, then
		# -b+a <= 0		
		for item in self.__dependencies:
			a = item[0]
			b = item[1]
			base[a] = 1
			base[b] = -1
			newcons = LinearFunction(c=base.reshape(-1,1),d=0)
			cons_set.add(newcons)
			base = numpy.zeros((self.__varnum, 1))
			
		# ALRIGHT, WRAP IT UP, IT'S DONE.		
		constraints = Constraint(ineq_cons=cons_set)
		return constraints
		
	def build_objectives(self):
		fun = LinearFunction(c=-self.__returns.reshape(-1,1),d=0)
		funs = FunctionsComposite()
		funs.add(fun)
		obj = Objective(objective=funs)
		return obj


# DEFINITION OF THE TEST CASE BELOW

# INPUTS (prices, returns, budget, conflict, dependencies)
# All separated by a line break
# (it ties into the instance generator I made in Bash)
instance_size = int(input()) # investment options number
prices = []
returns = []
names = []
budget = int(input())
for i in range(0,instance_size):
	prices.append(int(input()))
for i in range(0,instance_size):
	returns.append(int(input()))
# names array: only important for the console output
for i in range(0,instance_size):
	names.append(input())	
# conflict array: for every item [a,b] in the array, a and b cannot be
# chosen at the same time.
conflict_size = int(input())
conflicts = []
for i in range(0,conflict_size):
	arrayzinha = [-1,-1]
	arrayzinha[0] = int(input())
	arrayzinha[1] = int(input())
	conflicts.append(arrayzinha)	
# dependency array: for every item [a,b] in the array, item a can only be
# picked if b also is.
depends_size = int(input())
dependencies = []
for i in range(0,depends_size):
	arrayzinha = [-1,-1]
	arrayzinha[0] = int(input())
	arrayzinha[1] = int(input())
	dependencies.append(arrayzinha)

# Computation of the tests:
problem = InvestmentProblem(prices,returns,budget,conflicts,dependencies)
opt = OptimizationProblem(builder=problem)
optimizer = Optimizer(opt_problem=opt,algorithm=Glop())
results = optimizer.optimize()
whichones = results.x.ravel()
totalcost = 0
print("Investmentos escolhidos:")
for i in range(0,len(prices)):
	if whichones[i] == 1.:
		print(names[i])
		totalcost += prices[i]
print("Retorno total: ",-int(results.fx[0]))
print("Custo total: ",totalcost)
