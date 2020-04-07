int_codes = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0]
#int_codes = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,99,10,1,19,1,19,6,23]
"""
1. write a for loop that starts on index[0], loops through step 2, then runs the next loop on index[4]
2. write a script that does the following:
    - for position [i]
        i = 0
        if int_codes[i] == 1:
            add the position value int_codes[i+1] and int_codes[i+2]
            # e.g. int_codes[1,3,4,0,2] -> add[3],[4] add(0,2) = 2 and int_codes[3] is where the result goes (index [0])
            # after looping int_codes = [2,3,4,0,2] replaced index[0] with added result
        # elif:
        #   int_codes[0] == 2:
        #       do the same as above except multiple int[1], int[2] and replace in the list in index identified in int[3] 
        # else: break or halt (index[0] == 99)
3. replace index[1] with 12 and index[2] with 2
4. enter the amount in index[0] in advent of code """

i = 0
j = 0
k = 0

for int_code in range (i,len(int_codes),4):
    if int_codes[i] == 1:
        j = int_codes[int_codes[i+1]] + int_codes[int_codes[i+2]] #int_code index of int_code index value
        print("J equals: {}",j)
        k = int_codes[i+3]
        print("K equals: {}", k)
        int_codes[k] = j
        break
    elif int_codes[i] == 2:
        j = int_codes[int_codes[i+1]] * int_codes[int_codes[i+2]] #int_code index of int_code index value
        k = int_codes[i+3]
        int_codes[k] = j
        break
        #print(k)
    elif int_codes[i] == 99:
        break
print(int_codes)
