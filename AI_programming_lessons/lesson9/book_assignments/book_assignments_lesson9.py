from pathlib import Path
import json
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
# prompt = input("What is your name? ")
# path = Path("txt_files/guest.txt")
# content = f"Hello {prompt}, you have been invited to my birthday party!"
# path.write_text(content)

#10-5
# path = Path("txt_files/guest_book.txt")
# names = ""
# while True:
#     prompt = input("What is your name? ")
#     names += prompt+"\n"
#     if len(names) > 20:
#         break
# path.write_text(names)

#10-6
# message = ("Enter 2 numbers, and I will be able to add them together!"
#            "Enter q to quit program")
# print(message)
# while True:
#     num1, num2 = 0, 0
#     try:
#         num1 = input("What is the first number? ")
#         num2 = input("What is the second number? ")
#         if "q" in [num1, num2]:
#             break
#         num1 = int(num1)
#         num2 = int(num2)
#     except (ValueError, TypeError):
#         print("That is not a number!")
#     else:
#         print(f"The answer is {num1 + num2}")

#10-7
#lmao already done

#10-8
path1 = Path("txt_files/cats.txt")
path2 = Path("txt_files/dogs.txt")

try:
    cats = path1.read_text()
    print(cats)

    dogs = path2.read_text()
    print(dogs)
except FileNotFoundError:
    pass

#10-9
path = Path("txt_files/sexual_ethics.txt")
content = path.read_text(encoding="utf-8")
count = content.count("sex")
count2 = content.count("the")
print(f"the word 'sex' appears {count} times")
print(f"the word 'the' appears {count2} times")

#10-10
path = Path("txt_files/fav_num.json")
with open("txt_files/fav_num.json", "a"):
    prompt = int(input("What is you favorite number? "))
    content = json.dumps(prompt)
    path.write_text(content)

#10-11


