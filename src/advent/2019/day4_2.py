
def main():
    numPasswords = 0
    passwords = []
    for password in range(147981, 691424):
        valid = True
        password = [int(d) for d in str(password)]
        for x in range(5):
            if password[x] > password[x + 1]:
                valid = False
                break
        if valid and checkConsecutive(password):
            numPasswords += 1
            passwords.append(password)
    # print(passwords)
    print(numPasswords)

# just see if there are any digits that occur exactly twice in the password
# this works because the digits are already guaranteed to be in increasing order
# e.g. if there are two 6s in the list, they're going to be next to each other
def checkConsecutive(l):
    for i in l:
        if l.count(i) == 2:
            return True

if __name__ == '__main__':
    main()