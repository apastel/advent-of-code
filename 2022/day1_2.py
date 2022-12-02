if __name__ == "__main__":
    with open("input/day1.txt") as f:
        lines = f.read().split("\n\n")
        elf_calories_list = [elf.split("\n") for elf in lines]
        elf_calories_list = [[int(x) for x in elf] for elf in elf_calories_list]
        print(sum(sorted([sum(elf) for elf in elf_calories_list], reverse=True)[:3]))
        
