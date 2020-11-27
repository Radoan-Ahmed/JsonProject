import json
def read_info_from_file():

    try:
        file = open("information.json","r")
        file_info_as_text = file.read()
        info = json.loads(file_info_as_text)
        file.close()
        return info
    except:
        return []

def write_info_to_file(info):
    file = open("information.json","w+")
    json_text = json.dumps(info,indent = 4)
    file.writelines(json_text)
    file.close()

def add_info(fulName,id,course,status):
    info_array = read_info_from_file()
    newInfo = dict()
    newInfo['fulName'] = fulName
    newInfo['id'] = id
    newInfo['course'] = course
    newInfo['status'] = status
    info_array.append(newInfo)
    write_info_to_file(info_array)




def search_info(query):
    info_array = read_info_from_file()
    for info in info_array:
        if info.get("fulName") == query:
            print("The id of",query,"is:",info.get("id"))
            print("The course of", query, "is:", info.get("course"))
            return info.get("status")
        elif info.get("id") == query:
            print("The name of the student of this id:",query, "is:", info.get("fulName"))
            print("The course of",info.get("fulName"), "is:", info.get("course"))
            return info.get("status")
    return None

def view():
    file = open("information.json", "r")
    file_info_as_text = file.read()
    info = json.loads(file_info_as_text)
    lenth = len(info)
    for data in info:
        name = data['fulName']
        id = data['id']
        course = data['course']
        status = data['status']

        print("Student Name:", name)
        print("Student Id:",id)
        print("Courses:",course)
        print("Status:",status)
        print("....................")
        print("....................")
    print(lenth)



def delete(delvalue):
    info_array = read_info_from_file()
    for info in info_array:
        if info.get('id')==delvalue:
            info_array.remove(info)

        elif info.get('fulName') == delvalue:
            info_array.remove(info)

        elif info.get('course') == delvalue:
            info_array.remove(info)
        elif info.get('status') == delvalue:
            info_array.remove(info)

    write_info_to_file(info_array)




def update(old,new,chooseUp):
    info_array = read_info_from_file()
    if chooseUp == 1:
        for info in info_array:
            if info.get('fulName') == old:
                name = new
                id = info['id']
                course = info['course']
                status = info['status']
                delete(info.get('fulName'))
                add_info(name, id, course, status)
    elif chooseUp == 2:
        for info in info_array:
            if info.get('id') == old:
                name = info['fulName']
                id = new
                course = info['course']
                status = info['status']
                delete(info.get('fulName'))
                add_info(name, id, course, status)

    elif chooseUp == 3:
        for info in info_array:
            if info.get('course') == old:
                name = info['fulName']
                id = info['id']
                course = new
                status = info['status']
                delete(info.get('fulName'))
                add_info(name, id, course, status)

    elif chooseUp == 4:
        for info in info_array:
            if info.get('status') == old:
                name = info['fulName']
                id = info['id']
                course = info['course']
                status = new
                delete(info.get('fulName'))
                add_info(name, id, course, status)

    print("update successful")



while True:
    print("1.Add Information")
    print("2.Search Information")
    print("3.view data")
    print("4.Update data")
    print("5.Delete data")
    print("6.For exit")
    choice = int(input())

    if choice == 1:
        fname = str(input("Enter Student Name:"))
        id = str(input("Enter Student Id:"))
        course = str(input("Enter Course:"))
        status = str(input("Enter Status:"))
        add_info(fname,id,course,status)
        print("Information Added\n")

    elif choice == 2:
        print("Enter the name or id that you want to search:")
        query = str(input())
        number = search_info(query)
        print("Status of {} is : {}\n".format(query,number) if number is not None else "Contact Not Found\n")

    elif choice == 3:
        view()


    elif choice == 4:
        print("Enter 1 for update name:")
        print("Enter 2 for update id:")
        print("Enter 3 for update course:")
        print("Enter 4 for update status:")
        chooseUp = int(input())
        if chooseUp == 1:
            old = input("Enter the name that you want to change:")
            new = input("Enter the new name:")
            update(old, new,chooseUp)
        elif chooseUp == 2:
            old = input("Enter the Id that you want to change:")
            new = input("Enter the new Id:")
            update(old, new,chooseUp)
        elif chooseUp == 3:
            old = input("Enter the course that you want to change:")
            new = input("Enter the new course:")
            update(old, new, chooseUp)

        elif chooseUp == 4:
            old = input("Enter the status that you want to change:")
            new = input("Enter the new status:")
            update(old, new, chooseUp)


    elif choice == 5:
        value = str(input("Enter Student Id to delete his\her information:"))
        delete(value)


    elif choice == 6:
        exit()

