def bubble_sort(nlist):

    for passnum in range(len(nlist)-1,0,-1):

        for j in range(passnum):

            if nlist[j]>nlist[j+1]:

                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]

nlist = [14,46,43,27,57,41,45,21,70]

bubble_sort(nlist)

print(nlist)#  14, 21, 27, 41, 43, 45, 46, 57, 70