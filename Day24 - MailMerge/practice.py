
# opens in read only, relative file path

with open("../../../../krymo/Desktop/sample_text.txt") as file:
    contents = file.read()
    print(contents)

# opens in write mode (replaces everything in the file, absolute file path
with open("C:\Users\krymo\Desktop\sample_text.txt", mode="w") as file:
    file.write("Line 2: Test go!")
#
# # opens in write mode and appends the text
#
with open("sample_text.txt", mode="a") as file:
    file.write("Line 3?")

