# Transfer the runtime and name of tests to separate files to get organize data for graphs

lines = None
with open(f'./test_cases/output.txt', "r") as input_file:
        lines = input_file.readlines()

with open(f'./test_cases/test.txt', "w") as output_file:
    for i in range(1, len(lines), 5):
        line = lines[i -1]
        data = line.split()
        name = data[1].split('/')
        output_file.write(name[1] + '\n')

with open(f'./test_cases/runtime.txt', "w") as output_file:
    for i in range(4, len(lines), 5):
        line = lines[i -1]
        data = line.split()
        time = data[1]
        output_file.write(time + '\n')