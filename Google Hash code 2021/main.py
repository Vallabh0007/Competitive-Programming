
samples = {"A": "testcase/a.txt", "B": "testcase/b.txt", "C": "testcase/c.txt", "D": "testcase/d.txt", "E": "testcase/e.txt", "F": "testcase/f.txt"}
# samples is a dict to store the path of the testcases


def get_entries(source, filepath=None):
	""" Get the entries of the test case and return them
	source: a string to specify if entries come from input or a textfile
	filepath: a string to indicate the location of the file containing the entries """
	
	if source.upper() == "INPUT":
		D, I, S, V, F = list(map(int, input().split(" ")))
		B, E, streets_descriptions = [], [], []
		for i in range(S):
			b, e, name, l = input().split(" ")
			b, e, l = int(b), int(e), int(l)
			streets_descriptions.append((b, e, name, l))

		car_paths = []
		for i in range(V):
			p, names = input().split(" ")
			p = int(p)
			car_paths.append((p, names))
	else:
		with open(filepath, "r") as file:
			D, I, S, V, F = list(map(int, file.readline()[:-1].split(" ")))
			B, E, streets_descriptions = [], [], []
			for i in range(S):
				b, e, name, l = file.readline().split(" ")
				b, e, l = int(b), int(e), int(l)
				streets_descriptions.append((b, e, name, l))

			car_paths = []
			for i in range(V):
				line = file.readline().split(" ")
				p, names = int(line[0]), line[1:]
				car_paths.append((p, names))
		
	return D, I, S, V, F, car_paths, streets_descriptions


def rad_print(filepath=None, *params, **params_dict):
	""" Work as the built-in print,the difference is that we first give a filepath where the output will be stock. If you want to display the output at screen just set filepath to None """
	
	if filepath:
		with open(filepath, "w") as file:
			print(file=file, *params, **params_dict)
	else:
		print(*params, **params_dict)


def create_submissions(sample=("A", "B", "C", "D", "E", "F")):
	""" Create the submissions files for the specify sample.
	sample: a tuple containing the cases for which we want submissions files """
	
	for i in sample:
		filepath = samples[i.upper()]
		output = "submissions/"+i
		entries = get_entries("FILE",filepath)
		solution(*entries, output)
		
	print("All submissions file has been created in a folder call submissions!!")


def execute_solution(sample=("A", "B", "C", "D", "E", "F"), mode="FILE"):
	""" Execute our solution on all the specify sample
	sample: a tuple containing all the cases for which we want to execute our solution
	mode: a string specifying the way the entries are retrieve, FILE if it's from a file or INPUT if it's from keyboard typing """
	
	output = None
	
	if mode == "INPUT":
		sample = ()
		entries = get_entries(mode)
		solution(*entries, output)
		
	for i in sample:
		filepath = samples[i.upper()]
		entries = get_entries(mode,filepath)
		solution(*entries, output)


def solution(D, I, S, V, F, car_paths, streets_descriptions, filepath):
### Your code goes here##
# use rad_print instead of print with filepath as first argument
# ex:	rad_print(filepath, M, T2, T3, T4)
	print(D, I, S, V, F, car_paths, streets_descriptions)
	
def main():
	###Here goes the action you want to do###
	create_submissions()
	execute_solution(("A"))

if __name__ == "__main__":
	main()