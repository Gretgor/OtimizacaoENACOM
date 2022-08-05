# GENERATE INSTANCES FOR THE INVESTMENT PROGRAM
import sys
import random

# NUMBER OF INVESTMENT OPTIONS
instance_size = int(sys.argv[1])

# there will be at most n/2 conflicts in these test cases
conflict_size = random.randint(0,int(instance_size/2))

# there will be at most n/2 dependencies in these test cases
dependency_size = random.randint(0,int(instance_size/2))

# budget is set to a random number between 30 and 1000*int(instance_size/8):
budget = random.randint(30,1000*max(int(instance_size/8),1))
print(instance_size)
print(budget)

# print costs (between 1 and 600)
for i in range(0,instance_size):
	print(random.randint(1,600))

# print returns (between 1 and 800)	
for i in range(0,instance_size):
	print(random.randint(1,800))

# name generation (just having fun with this one)
for i in range(0,instance_size):
	part1 = random.choice(["Atualização","Aprimoramento","Expansão","Capacitação","Compra","Criação","Reforma","Refatoração","Venda","Anúncio","Reajuste","Palestras sobre a importância"])
	part2 = random.choice([" de pessoal"," de armazém"," de portfolio"," de equipamento"," de máquina"," dos relatórios"," de funcionários"," da remuneração"," da prevenção"])
	part3 = random.choice([" para atividade fim"," para limpeza"," de funcionários"," em relações públicas"," em 10%"," de segurança"," de desenvolvimento"," de suporte"," de aposentadoria"," de acidentes"])
	print(str(i+1)+": "+part1+part2+part3)
	
# conflicts and dependencies: for every one of those, just print two random indices
print(conflict_size)
for i in range(0,conflict_size):
	print(random.randint(0,instance_size-1))
	print(random.randint(0,instance_size-1))
	
print(dependency_size)
for i in range(0,dependency_size):
	print(random.randint(0,instance_size-1))
	print(random.randint(0,instance_size-1))



