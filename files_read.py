#создаём файл чтобы поместить туда информацию
fw = open("doc/file.txt", "a")
fw.write("Hello, world\n")
fw.close()

# a - запись новых данных в конец файла
# w - запись новых данных с удалением старых

fw = open("doc/file2.txt", "w")
#пишем в файл
fw.write("Hello2\n")
#закрываем запись
fw.close()