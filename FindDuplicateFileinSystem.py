from collections import defaultdict

def findDuplicate( paths) :
    dic = defaultdict(list)
    for path in paths:
        groups = path.split(" ")
        group = groups[0]
        for i in range(1, len(groups)):
            file = groups[i].split("(")
            dic[file[1]].append(group + "/" + file[0])
    result = []

    for key in dic:
        if len(dic[key]) > 1:
            result.append(dic[key])
    return result


data = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
print(findDuplicate(data))

