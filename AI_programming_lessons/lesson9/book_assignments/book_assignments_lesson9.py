from pathlib import Path
#10-1
path = Path("txt_files/learning_python.txt")
contents = path.read_text()
print(contents)


line_content = ""
for line in contents.splitlines():
    line_content += line.strip()
    print(line_content)

#10-2
contents = contents.replace("Python", "C#")
print(contents)
#10-3
#Done

#10-4
prompt = input("What is your name? ")
path = Path("txt_files/guest.txt")
content = f"Hello {prompt}, you have been invited to my birthday party!"
path.write_text(content)

#10-5
path = Path("txt_files/guest_book.txt")
names = ""
while True:
    prompt = input("What is your name? ")
    names += prompt+"\n"
    if len(names) > 20:
        break
path.write_text(names)

#10-6
