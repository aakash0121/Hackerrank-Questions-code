def spaces(x):
    for i in range(1, x):
        print(" ", end = "")

def sierpinski_triangle(n):
    global pascal_triangle

    for i in range(1, n + 1):
        spaces(n - i + 1)
        temp = []
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print("*", end = " ")
                temp.append(1)
            else:
                val = pascal_triangle[i - 2][j - 2] + pascal_triangle[i - 2][j - 1]
                if val % 2 != 0:
                    print("*", end = " ")
                else:
                    print(" ", end = " ")

                temp.append(val)

        print("\n")        
        pascal_triangle.append(temp)

n = int(input("enter the number for number of lines: "))
pascal_triangle = []
sierpinski_triangle(n)