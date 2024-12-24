# brutal day today, hardest day this year - 287/550
# still, this year feels easier than the last
from collections import defaultdict
with open("input.txt") as f:
	inp = f.read().split("\n\n")
	values = {k: int(v) for k, v in (line.split(": ") for line in inp[0].splitlines())}
	gates = [line.split(" -> ") for line in inp[1].splitlines()]
	gates = [(ins.split(), out) for ins, out in gates]


pending = gates[:] # deepcopy
while pending:
	for i, ((a, op, b), out) in enumerate(pending):
		if a in values and b in values:
			av, bv = values[a], values[b]
			match op:
				case "AND": values[out] = av & bv
				case "OR": values[out] = av | bv
				case "XOR": values[out] = av ^ bv
			pending.pop(i)
			break

print(f"Part 1: {int("".join(str(values[k]) for k in sorted(values)[::-1] if k.startswith("z")), 2)}")


# I've made some minor improvements to part 2 for the refactor after looking at a few different solutions (especially for naming).
# However, the basic idea is the same.

# Part 2
# Notice that it is a ripple carry adder (https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder);
# yes this took me until 6:15am to spot :(
# go through the gates and identify the proper type of each wire
# then identify which wires are out of place (hopefully 8)
# don't need to bother with swapping any wires as it's just some combination of these wires


from enum import Enum
WT = Enum("WireType", "OUT INT_CARRY EXT_CARRY SUM_BIT CARRY_BIT") # debatable on whether this improves readability
# OUT – output of XOR or gates
# INT_CARRY – internal carry from AND gates
# EXT_CARRY – external carry from OR gates
# SUM_BIT – sum from addition (X^Y)
# CARRY_BIT – carry from addition (X&Y)

# the input and output types of each wire (these should match up to that of a ripple carry adder as below - if they don't, the wire is out of place):
# if the input is an external carry, it becomes an internal carry or carry bit
# ext_carry's are the combination of an OUT and an INT_CARRY, giving the carry to the next adder in the chain
# sum_bit = (a XOR b) XOR INT_CARRY
# z wires if and only if OUT and no IN
in_type = defaultdict(set)
out_type = defaultdict(set)

for (a, op, b), d in gates:
	a, b = sorted((a, b))
	if a.startswith("x") and b.startswith("y"):
		if a == "x00" and b == "y00":  # special case, x00 and y00 start the adder and were correct in my input
			continue
		out_type[d].add(WT.SUM_BIT if op == "XOR" else WT.CARRY_BIT)
	else:
		match op:
			case "AND": type = WT.INT_CARRY
			case "OR": type = WT.EXT_CARRY
			case "XOR": type = WT.OUT
		in_type[a].add(type)
		in_type[b].add(type)
		out_type[d].add(type)


swaps = []
for wire in out_type:
	it = in_type[wire]
	ot = out_type[wire]

	# if the wire doesn't obey the rules above
	# z45 is a special case as it is the output of the last adder
	if not (wire == "z45"
			or not it and wire.startswith("z") and ot == {WT.OUT}
			or it == {WT.OUT, WT.INT_CARRY} and (ot == {WT.SUM_BIT} or ot == {WT.EXT_CARRY})
			or it == {WT.EXT_CARRY} and (ot == {WT.CARRY_BIT} or ot == {WT.INT_CARRY})):
		swaps.append(wire)

print("Part 2: " + ",".join(sorted(swaps)))