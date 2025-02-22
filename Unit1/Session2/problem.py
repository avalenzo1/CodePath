# len(matrix) = rows
# matrix[0] = cols

def transpose(matrix):
    if matrix is None:
        return []
    
    rows, cols = (len(matrix), len(matrix[0]))
    print(rows)
    print(cols)
    #transposed = [[0]*cols]*rows
    transposed = [[0] * rows for _ in range(cols)]  # Proper 2D list initialization
    #can you try running now?
    # it works!
    #Instead of [[0] * cols] * rows, use [[0] * rows for _ in range(cols)] to ensure each row is a separate list in memory.
    #Never thought such simple things could be problematic! I need to fix my basics!
    # thank you! 
    # frr would u guys be down to connect on linkedin?- yesss!
    # good job guys!!!! www.linkedin.com/in/damontan-6150192b2 - Sent!  lol
    print(transposed) # hope to see yall later!
    # also I figured out why the window was moving, it was because I was following your cursor i think 😭- LOL
    
    # my linked in is https://www.linkedin.com/in/avalenzo/- Sent!

    #print([[0 for i in range(cols)] for j in range(rows)])
    #arr = [[0]*cols]*rows
    
    # bye yall!!
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            print(transposed)
            
            
    return transposed

matrix = [
    [1, 2, 3], # matrix[0]
    [4, 5, 6],
    [7, 8, 9]
]

updated = transpose(matrix)

# nest 

# i in range(M, N):

# expected return
# []
# []
# []
# print the matrix after

print(updated)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
updated = transpose(matrix)

print(updated)