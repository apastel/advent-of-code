
def run_program():
    fp = 0
    accumulator = 0
    used_fps = []

    while fp < len(instructions):
        if fp in used_fps:
            return False
        used_fps.append(fp)

        operation, argument = instructions[fp].split()

        if operation == "acc":
            accumulator += int(argument)
            fp += 1
        elif operation == "jmp":
            fp += int(argument)
        elif operation == "nop":
            fp += 1

    return accumulator

if __name__ == "__main__":
    with open("input/day8.txt") as f:
        instructions = [line.rstrip('\n') for line in f]

        for i in range(len(instructions)):
            operation, argument = instructions[i].split()

            if operation == "nop":
                operation = "jmp"
                instructions[i] = operation + " " + argument
            elif operation == "jmp":
                operation = "nop"
                instructions[i] = operation + " " + argument
            else:
                continue

            accumulator = run_program()

            if accumulator:
                print(accumulator)
                break
            else: # reset operation
                if operation == "nop":
                    operation = "jmp"
                    instructions[i] = operation + " " + argument
                elif operation == "jmp":
                    operation = "nop"
                    instructions[i] = operation + " " + argument
