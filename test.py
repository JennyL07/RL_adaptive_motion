import scipy.io

mat_data = scipy.io.loadmat('data2.mat')
print(type(mat_data))
A_matrix = mat_data['A_matrix']
r = mat_data['r']
theta = mat_data['theta']
Bn = mat_data['Bn']

A_dict = {}
Bn_dict = {}

# Use a for loop to build the dictionary
for i in range(len(A_matrix[0])):
    A_dict[i + 1] = A_matrix[0,i]  # Keys start at 1, values are from the list
    Bn_dict[i + 1] = Bn[i]


# print(A_dict[1])
print(Bn_dict)