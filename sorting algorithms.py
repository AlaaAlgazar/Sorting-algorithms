def seq_sort(mylist):
    for i in range(len(mylist)):
        min_index=i
        for j in range(i+1,len(mylist)):
            if mylist[j]< mylist[min_index]:
                min_index = j
        # mylist[min_index],mylist[i]=mylist[i],mylist[min_index]
        old_val=mylist[i]
        mylist[i]=mylist[min_index]
        mylist[min_index]=old_val
    return mylist


def bubble_sort(mylist):
    for i in range(len(mylist)-1):
        swap=False
        for j in range(len(mylist)-i-1):
            if (mylist[j]> mylist[j+1]):
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
                swap=True
        if swap == False:
            return mylist
    return mylist


def insertion_sort(mylist):
    for i in range(1,len(mylist)):
        for j in reversed(range(i)):
            if mylist[i]> mylist[j]:
                value=mylist[i]
                for k in reversed(range(j+2,i+1)):
                    mylist[k]=mylist[k-1]
                mylist[j+1]=value
                break
            
            elif j ==0:
                value=mylist[i]
                for k in reversed(range(1,i+1)):
                    mylist[k]=mylist[k-1]
                mylist[0]=value

    return mylist


# def merge(left_list,right_list):
#     if len(left_list)>1:
#         left_list=merge(left_list[:len(left_list)//2],left_list[len(left_list)//2:])
#     if len(right_list)>1:
#         left_list=merge(right_list[:len(right_list)//2],right_list[len(right_list)//2:])
#     new_list=[0]*(len(left_list)+len(right_list))
#     i=j=k=0
#     while i<len(left_list) and j < len(right_list):
#         if left_list[i] <= right_list[j]:
#             new_list[k]=left_list[i]
#             i+=1
#         else:
#             new_list[k]=right_list[j]
#             j+=1
#         k+=1
    
#     while i < len(left_list):
#         new_list[i]=left_list[i]
#         i+=1
#     while j < len(right_list):
#         new_list[j]=right_list[j]
#         j+=1
    
#     return new_list


# def merge_sort(mylist):
#     return merge (my_list[:len(mylist)//2], mylist[len(mylist)//2:])

def quick_sort(mylist):
    if len(mylist)==1:
        return mylist
    pivot=mylist[0]
    i=0
    j=len(mylist)-1
    while i != j:
        if mylist[j]<mylist[i]:
            mylist[i],mylist[j]=mylist[j],mylist[i]

        if mylist[j]== pivot:
            i+=1
        else:
            j-=1
    if i==0:
        mylist[1:]=quick_sort(mylist[1:])
    elif i ==len(mylist)-1:
        mylist[:-1]=quick_sort(mylist[:-1])
    else:
        mylist[:i]=quick_sort(mylist[:i])
        mylist[i+1:]=quick_sort(mylist[i+1:])
    return mylist


def heap_sort(mylist):
    if len(mylist)==1:
        return mylist
    else:
        length=len(mylist)
        for i in range(length):
            if 2*i+1 < length and mylist[i] > mylist [2*i+1]:
                mylist[i],mylist[2*i+1]=mylist[2*i+1],mylist[i]
                mylist=heap_sort(mylist)
                
            if 2*i+2 < length and mylist[i] > mylist [2*i+2]:
                mylist[i],mylist[2*i+2]=mylist[2*i+2],mylist[i]
                mylist=heap_sort(mylist)
        sub_list=mylist
        sub_list.remove(sub_list[-1])
        sub_list[0]=mylist[-1]
        mylist[1:]=heap_sort(sub_list)
    return mylist

                
















# from random import randint
# main_list=[]
# for i in range(20):
#     main_list.append(randint(0,100))
main_list=[38, 54, 88, 77, 17, 68, 90, 53, 53, 16, 11, 30, 12, 7, 64, 21, 86, 78, 80, 5]

print(f"main list:\n{main_list}")
# print(f"sorted list:\n{sorted(main_list)}")

# seq_list=seq_sort(main_list)
# print(f"seq_list :\n{seq_list}")
# print(seq_list == sorted(main_list))

# bubble_list=bubble_sort(main_list)
# print(f"bubble sort :\n{bubble_list}")
# print(bubble_list == sorted(main_list))

# insertion_list=insertion_sort(main_list)
# print(f"insertion sort :\n{insertion_list}")
# print(insertion_list == sorted(main_list))

# merge_list=merge_sort(main_list)
# print(f"merge sort :\n{merge_sort(main_list)}")
# print(merge_list == sorted(main_list))

# quick_list=quick_sort(main_list)
# print(f"quick sort :\n{quick_list}")
# print(quick_list == sorted(main_list))

print(f"sorted list :\n{sorted(main_list)}")
heap_list=heap_sort(main_list)
print(f"heap sort :\n{heap_list}")
print(heap_list == sorted(main_list))

# if seq_list==bubble_list==insertion_list==quick_list==sorted(main_list):
#     print("All algorithms return the same output")
# else:
#     print("Different algorithms return different outputs")




