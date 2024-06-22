def merge_list(list1,list2):
    result_list = []
    for i in list1:
        if i % 2 == 0:
            result_list.append(i)
    for i in list2:
        if i % 5 == 0:
            result_list.append(i)
    return result_list
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
print(merge_list(list1,list2))