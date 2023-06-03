def find_common_elements(ar1, ar2, ar3):
    ptr1 = ptr2 = ptr3 = 0
    result = []

    while ptr1 < len(ar1) and ptr2 < len(ar2) and ptr3 < len(ar3):
        if ar1[ptr1] == ar2[ptr2] == ar3[ptr3]:
            result.append(ar1[ptr1])
            ptr1 += 1
            ptr2 += 1
            ptr3 += 1
        elif ar1[ptr1] < ar2[ptr2]:
            ptr1 += 1
        elif ar2[ptr2] < ar3[ptr3]:
            ptr2 += 1
        else:
            ptr3 += 1

    return result
ar1 = [1, 2, 3, 4, 5]
ar2 = [1, 2, 5, 7, 9]
ar3 = [1, 3, 4, 5, 8]

print(find_common_elements(ar1, ar2, ar3))
