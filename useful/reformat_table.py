f = open("input_table.txt")
table = ''.join(f.readlines())
f.close()

to_replace = []
replace_with = []
for d1 in range(10):
    for d2 in range(10):
        to_replace.append(f"{d1}.{d2}")
        replace_with.append(f"{d1},{d2}")

for i in range(len(to_replace)):
    table = table.replace(to_replace[i], replace_with[i])
    table = table.replace("\$", "$")
    table = table.replace("$\\backslash$", "\\")
    table = table.replace("\\_", "_")

f = open('output_table.txt', "w")
f.write(table)
f.close()