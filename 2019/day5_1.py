import copy

f = open('input/day5.txt', 'r').read()
starting_array = f.split(',')
starting_array = [int(i) for i in starting_array]

def process(array, i=0):
    if int(str(array[i])[-2:]) == 1: #opcode 1
        firstParam = 0 #position mode
        secondParam = 0 #position mode
        thirdParam = 0 #position mode
        try:
            if int(str(array[i])[-3]) == 1:
                firstParam = 1
        except:
            True
        try:
            if int(str(array[i])[-4]) == 1:
                secondParam = 1
        except:
            True
        try:
            if int(str(array[i])[-5]) == 1:
                thirdParam = 1
        except:
            True
        if thirdParam == 1:
            array[i + 3] = array[(i + 1) if firstParam else array[i + 1]] + array[(i + 2) if secondParam else array[i + 2]]
        else:
            array[array[i + 3]] = array[(i + 1) if firstParam else array[i + 1]] + array[(i + 2) if secondParam else array[i + 2]]
        return process(array, i + 4)
    elif int(str(array[i])[-2:]) == 2: #opcode 2
        firstParam = 0 #position mode
        secondParam = 0 #position mode
        thirdParam = 0 #position mode
        try:
            if int(str(array[i])[-3]) == 1:
                firstParam = 1
        except:
            True
        try:
            if int(str(array[i])[-4]) == 1:
                secondParam = 1
        except:
            True
        try:
            if int(str(array[i])[-5]) == 1:
                thirdParam = 1
        except:
            True
        if thirdParam == 1:
            array[i + 3] = array[(i + 1) if firstParam else array[i + 1]] * array[(i + 2) if secondParam else array[i + 2]]
        else:
            array[array[i + 3]] = array[(i + 1) if firstParam else array[i + 1]] * array[(i + 2) if secondParam else array[i + 2]]
        return process(array, i + 4)
    elif int(str(array[i])[-2:]) == 3: #opcode 3
        firstParam = 0 #position mode
        try:
            if int(str(array[i])[-3]) == 1:
                firstParam = 1
        except:
            True
        array[(i + 1) if firstParam else array[i+1]] = 5 # input value is 1
        return process(array, i + 2)
    elif int(str(array[i])[-2:]) == 4: #opcode 4
        firstParam = 0 #position mode
        try:
            if int(str(array[i])[-3]) == 1:
                firstParam = 1
        except:
            True
        output = array[(i + 1) if firstParam else array[i + 1]]
        if output != 0:
            print(f"Output was {output}")
        else:
            print(output)
        return process(array, i + 2)
    elif int(str(array[i])[-2:]) == 5: #opcode 5
        firstParam = 0 #position mode
        secondParam = 0 #position mode
        try:
            if int(str(array[i])[-3]) == 1:
                firstParam = 1
        except:
            True
        try:
            if int(str(array[i])[-4]) == 1:
                secondParam = 1
        except:
            True
        if firstParam:
            if array[i + 1] != 0:
                i = array[(i + 2) if secondParam else array[i + 2]]
                return process(array, i)
            else:
                return process(array, i + 3)
        else:
            if array[array[i + 1]] != 0:
                i = array[(i + 2) if secondParam else array[i + 2]]
                return process(array, i)
            else:
                return process(array, i + 3)
    elif int(str(array[i])[-2:]) == 6: #opcode 6
        firstParam = 0 #position mode
        secondParam = 0 #position mode
        try:
            if int(str(array[i])[-3]) == 1:
                firstParam = 1
        except:
            True
        try:
            if int(str(array[i])[-4]) == 1:
                secondParam = 1
        except:
            True
        if firstParam:
            if array[i + 1] == 0:
                i = array[(i + 2) if secondParam else array[i + 2]]
                return process(array, i)
            else:
                return process(array, i + 3)
        else:
            if array[array[i + 1]] == 0:
                i = array[(i + 2) if secondParam else array[i + 2]]
                return process(array, i)
            else:
                return process(array, i + 3)
    elif int(str(array[i])[-2:]) == 7: #opcode 7
        firstParam = 0 #position mode
        secondParam = 0 #position mode
        thirdParam = 0
        try:
            if int(str(array[i])[-3]) == 1:
                firstParam = 1
        except:
            True
        try:
            if int(str(array[i])[-4]) == 1:
                secondParam = 1
        except:
            True
        try:
            if int(str(array[i])[-5]) == 1:
                thirdParam = 1
        except:
            True
        if (array[i + 1] if firstParam else array[array[i + 1]]) < (array[i + 2] if secondParam else array[array[i + 2]]):
            if thirdParam:
                array[i + 3] = 1
            else:
                array[array[i + 3]] = 1
        else:
            if thirdParam:
                array[i + 3] = 0
            else:
                array[array[i + 3]] = 0
        return process(array, i + 4)
    elif int(str(array[i])[-2:]) == 8: #opcode 8
        firstParam = 0 #position mode
        secondParam = 0 #position mode
        thirdParam = 0
        try:
            if int(str(array[i])[-3]) == 1:
                firstParam = 1
        except:
            True
        try:
            if int(str(array[i])[-4]) == 1:
                secondParam = 1
        except:
            True
        try:
            if int(str(array[i])[-5]) == 1:
                thirdParam = 1
        except:
            True
        if (array[i + 1] if firstParam else array[array[i + 1]]) == (array[i + 2] if secondParam else array[array[i + 2]]):
            if thirdParam:
                array[i + 3] = 1
            else:
                array[array[i + 3]] = 1
        else:
            if thirdParam:
                array[i + 3] = 0
            else:
                array[array[i + 3]] = 0
        return process(array, i + 4)
    elif int(str(array[i])[-2:]) == 99: # halt
        return array
    else:
        raise Exception(f'Something went wrong, opcode was {array[i]}. Array was {array}, i was {i}')

def main():
    process(starting_array)

if __name__ == '__main__':
    main()