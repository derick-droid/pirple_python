"""
creating a note taking program where the user enters a file if the exits the user is allowed to do some task on it
if the file is not there the user writes something then the file is saved
"""
file_list = []
while True:
    filename = input("enter the file name: ")
    if filename in file_list:
        task = input("what do you want to do with the file: ")
        if task == "read":
            filename = open(filename, "r")
            for items in filename:
                print(items)

        elif task == "delete":
            file_list.remove(filename)
        elif task == "append":
            filename = open(filename, "a")
            append_text = input("enter your notes: ")
            filename.write(append_text)

    else:
        # file not existing is being saved
        file_list.append(filename)
        print(file_list)
        text = input("enter message : ")
        filename = open(filename, "w")
        filename.write(text)
        filename.write(" ")
        filename.write(" \n")
        filename.close()


