import copy

f = open('input/day2.txt', 'r').read()
starting_array = f.split(',')
starting_array = [int(i) for i in starting_array]

def process(array, i=0):
    if array[i] == 1:
        array[array[i + 3]] = array[array[i + 1]] + array[array[i + 2]]
        return process(array, i + 4)
    elif array[i] == 2:
        array[array[i + 3]] = array[array[i + 1]] * array[array[i + 2]]
        return process(array, i + 4)
    elif array[i] == 99:
        return array
    else:
        raise Exception(f'Something went wrong, opcode was {array[i]}. Array was {array}, i was {i}')

def main():
    for i in range(100):
        for j in range(100):
            modified_array = copy.deepcopy(starting_array)
            modified_array[1] = j
            modified_array[2] = i
            result = process(modified_array)
            if result[0] == 19690720:
                print(result)
                return

if __name__ == '__main__':
    main()
