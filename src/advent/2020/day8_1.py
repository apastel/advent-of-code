if __name__ == "__main__":
    with open("input/day8.txt") as f:
        instructions = [line.rstrip('\n') for line in f]

        accumulator = 0
        fp = 0
        used_fps = []

        while fp < len(instructions):
            if fp in used_fps:
                break
            used_fps.append(fp)

            operation, argument = instructions[fp].split()
            
            if operation == "acc":
                accumulator += int(argument)
                fp += 1
            elif operation == "jmp":
                fp += int(argument)
            elif operation == "nop":
                fp += 1

        print(accumulator)