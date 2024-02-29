file_name = "docs/file.txt"
data = "Какой-то текст"

# fw = open(file_name, 'a')
# fw.write(data)
# fw.close()

with open(file_name, 'r+') as files:
    files.write(data)