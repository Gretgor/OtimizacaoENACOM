# GENERATE INSTANCES FOR THE INVESTMENT PROGRAM
import sys
import random

# NUMBER OF INVESTMENT OPTIONS
instance_size = int(sys.argv[1])

# there will be at most n/2 conflicts in these test cases
conflict_size = random.randint(0,int(instance_size/2))

# there will be at most n/2 dependencies in these test cases
dependency_size = random.randint(0,int(instance_size/2))

# budget is set to a random number between 30 and 1000:
budget = random.randint(30,1000)
print(budget,dependency_size,conflict_size)


