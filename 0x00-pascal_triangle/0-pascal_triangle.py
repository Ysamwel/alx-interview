
#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        #Start of rows
        row = [1]
        for j in range(1, i):
            #sum the two numbers above our current position/row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
            
        row.append(1)

        triangle.append(row)

    return triangle
