# Extremely powerful and have a lot of applications in data science and machine learning.
# In math there is a concept called matrix which is like a rectangular array of numbers.
#[
    #123
    #456            This is a 3 by 3 matrix in math
    #789 
#] This can be displayed using a 2 dimentional list
# A two dimentional item is where each item in that list is another list.
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]    
]
#matrix[0][1] = 20
#print(matrix[0][1])

# Here is where we can use nested loops to iterate over all the items.
for row in matrix:
    for item in row:
        print(item)
