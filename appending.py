text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as f:
    f.write(text_to_write + '\n')
print("Data successfully written to output.txt.\n")

additional_text = input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(additional_text)
print("Data successfully appended.")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as f:
    content = f.read()
print(content)