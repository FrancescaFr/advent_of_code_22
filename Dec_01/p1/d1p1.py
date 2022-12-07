
# 1. Import calorie file
with open("./input", 'r') as file:
    data = file.read()

#2. create list of elfs (grouped calories)
elf_list = data.split("\n\n")
# print(elf_list)


#3. Sum calories carried by each elf
max_calories = 0
for elf in elf_list:
    calorie_sum = 0
    calorie_list = elf.split("\n")
    #print(calorie_list) 
    for calories in calorie_list:
        if calories != '': #ignore empty calorie strings
            calorie_sum += int(calories)
    if calorie_sum > max_calories:
        max_calories = calorie_sum
print(max_calories)

# Answer: 71780



