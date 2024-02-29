file_name = "docs/file_for _write.txt"

with open(file_name, 'r+') as files:
    data = files.read()
    print(data)