file_name = "docs/file_for _write.txt"
text = "some text"

with open(file_name,"w") as text_file:
    print(text, file=text_file)