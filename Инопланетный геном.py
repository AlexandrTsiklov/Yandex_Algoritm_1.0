gen1 = input()
gen2 = input()
gen_dict1 = {}
gen_dict2 = {}

for i in range(len(gen1) - 1):
    if gen1[i:i + 2] not in gen_dict1:
        gen_dict1[gen1[i:i + 2]] = 0
    gen_dict1[gen1[i] + gen1[i + 1]] += 1

for i in range(len(gen2) - 1):
    if gen2[i:i + 2] not in gen_dict2:
        gen_dict2[gen2[i:i + 2]] = 0
    gen_dict2[gen2[i:i + 2]] += 1

count = 0
for i in gen_dict1:
    if i in gen_dict2:
        count += gen_dict1[i]
print(count)
