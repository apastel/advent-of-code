f = open('input/day2.txt', 'r').read()
starting_array = f.split(',')
starting_array = [int(i) for i in starting_array]
starting_array[1] = 12
starting_array[2] = 2

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
        raise Exception(f'Something went wrong, opcode was {array[i]}')

print(process(starting_array))
print(process([1,0,0,0,99]))
print(process([2,3,0,3,99]))
print(process([2,4,4,5,99,0]))
print(process([1,1,1,4,99,5,6,0,99]))