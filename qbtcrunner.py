#!/usr/bin/env python3

from pathlib import Path
import re

class TestCaseRunner():
	"""
	Runs the solver script with an input and accumulates the output in an output file.
	It need the solver script packed in `Path` object.
	The name of solver script should include a number indicating its order in the assignment.
	"""
	firstObj = True
	def __init__(self, solver: Path):
		assert isinstance(solver, Path), "Solver script must be sent as a `Path` object."
		if not TestCaseRunner.firstObj: print()
		TestCaseRunner.firstObj = False
		self.counter = 1
		self.solver = solver
		self.pnum = re.findall('\d+', solver.name)[0] # problem number
		self.path = Path(solver.parent.absolute()/f"p{self.pnum}")
		for p in ('in', 'out'):
			if not (self.path/p).is_dir():
				(self.path/p).mkdir(parents=True, exist_ok=True)
		print(f"Generating test cases for {solver} ... ")

	def __print_redirect__(self, *args, **kwrds):
		self.output = []
		if 'end' not in kwrds: kwrds['end'] = '\n'
		if 'sep' not in kwrds: kwrds['sep'] = ' '
		self.output.append( kwrds['sep'].join([ str(i) for i in args ]) + kwrds['end'] )

	def run(self, ins):
		# quera.ir does not accept more than 100 test cases!
		if self.counter > 100: return
		open(f"{self.path}/in/input{self.counter}.txt" ,'w').write( ins )
		with open( self.solver ) as T:
			exec( ''.join(T) ,
				{'input': ins.split('\n')[::-1].pop,
				'print': self.__print_redirect__}
			)
		open(self.path/f"out/output{self.counter}.txt",'w').write( ''.join(self.output) )
		print (f'\r#{self.pnum}: input/output file {self.counter} finished!', end='')
		self.counter += 1

	__call__ = run # calling the object instead of the `run` method


####################     Generating Test Cases and their answers     ####################
# name of the solution program should contains at list one digit
# which will be used as a suffix for `p` folder including `in` and `out` folders

# gen = TestCase(Path("sol-1.py"))
# for i in range(100):
# 	INPUT = 'an input in the domain of problem.'
# 	gen(INPUT)