
def read1():
    file = open("file.txt", "r")
    l_d = {}
    list_id = 1
    for line in file:
        line = line.replace("\n", "")
        l_d.update({list_id: line.split(",")})
        list_id = list_id + 1
    file.close()
    return l_d

def table():
    file = open("file.txt", "r")
    a = 0
    for line in file:
        print(a+1, "\t\t" + line.replace(",", "\t\t"))
        a = a + 1
        if(a == 5):
            break
    file.close()
