import os.path

# takes all the names in invited_names.txt and sames them in a list
name_list = []
with open("Input/Names/invited_names.txt") as names:
    for name in names:
        name = name.strip()
        name_list.append(name)

# re-writes the letter as a list, replaces [name] with a name from the name_list and saves to a new file

save_to_folder = "Output/ReadyToSend/"
i = 0
for name in name_list:
    letter = open("Input/Letters/starting_letter.txt", mode="r")
    letter_list = letter.readlines()
    replacement = letter_list[0]
    fixed = replacement.replace("[name]", name_list[i])
    letter_list[0] = fixed
    file_name = f"finished_letter{i}.txt"
    complete_name = os.path.join(save_to_folder, file_name)
    file = open(complete_name, mode="w")
    for line in letter_list:
        file.write(line)
    i += 1

#
# #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
