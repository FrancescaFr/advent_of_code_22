
# 1. Import calorie file
with open("./input", 'r') as file:
    data = file.read()

#2. create list of elfs (grouped calories)
elf_list = data.split("\n\n")
# print(elf_list)

#3. Sum calories carried by each elf and save to list of totals
elves_calorie_list = []
for elf in elf_list:
    calorie_sum = 0
    calorie_list = elf.split("\n")
    #print(calorie_list) 
    for calories in calorie_list:
        if calories != '': #ignore empty calorie strings
            calorie_sum += int(calories)
    elves_calorie_list.append(calorie_sum)
#print(elves_calorie_list)

#4. sort elves' calories by size (sort in place - insertion_sort)
for i in range(1,len(elves_calorie_list)):
    to_insert = elves_calorie_list[i]
    insertion_index = i
    while insertion_index > 0 and elves_calorie_list[insertion_index -1] > to_insert:
        elves_calorie_list[insertion_index] = elves_calorie_list[insertion_index -1]
        insertion_index -= 1
    elves_calorie_list[insertion_index] = to_insert
    i+= 1
#print(elves_calorie_list)
    
#5 Sum top three elves
top_three_elves = sum(elves_calorie_list[-3:len(elves_calorie_list)+1])
#check_sum = 69228 + 71481 + 71780
#print(check_sum)
print(top_three_elves)
# Answer: 212489