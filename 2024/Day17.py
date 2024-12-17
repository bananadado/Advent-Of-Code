# oh my days that was awful - 379/1911
# I just couldn't see the pattern. tons of printing and i just didn't spot it for 1.5 HOURS. AHHHHHHH
# Tim Kolesniiiii beat me today, if i didnt help him with part 1 i wouldve beaten him (my mistake)
# "i was finally beaten by my master" - tim to me to put in the comments (i dont get how he would be my master but ok)
# refactoring was very short today, decent solution already. tim told me to use >> operators instead of // and 2**
with open("input.txt", "r") as file:
    lines = file.readlines()

a = int(lines[0].split(": ")[1])
b = int(lines[1].split(": ")[1])
c = int(lines[2].split(": ")[1])
program = list(map(int, lines[4].split(": ")[1].split(",")))

def run(av):
    ra, rb, rc = av, b, c

    def combo(op):
        if op == 4:
            return ra
        if op == 5:
            return rb
        if op == 6:
            return rc
        return op

    ip = 0
    output = []
    while ip < len(program):
        opcode, operand = program[ip], program[ip + 1]

        match opcode:
            case 0: ra >>= combo(operand)
            case 1: rb ^= operand
            case 2: rb = combo(operand) % 8
            case 3:
                if ra != 0:
                    ip = operand
                    continue
            case 4: rb ^= rc
            case 5: output.append(combo(operand) % 8)
            case 6: rb = ra >> combo(operand)
            case 7: rc = ra >> combo(operand)

        ip += 2
    return output


print(f"Part 1: {",".join(map(str, run(a)))}")

# the key is that the nth value from the start of the program is affected by the 8^n value a
# the end of the program is less volatile so you can hone in from the end of the program rather than the start
# also you need to keep doubling a to make the output length the same as the program length
a = 1
while True:
    out = run(a)
    if out == program:
        print(f"Part 2: {a}")
        quit()
    if len(out) < len(program):
        a *= 2
    if len(out) == len(program):
        for j in range(len(program) - 1, -1, -1):
            if program[j] != out[j]:
                a += 8**j
                break
