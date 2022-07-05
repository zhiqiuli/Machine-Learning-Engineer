import math

def euclidean_distance(row1, row2):
    if len(row1) != len(row2):
        raise Exception('')
    dist = 0.0
    for i in range(len(row1) - 1): # last column is the label
        dist += (row1[i] - row2[i]) ** 2
    return math.sqrt(dist)

def get_neighbors(train, test_row, num_neighbors):
    distance = []
    for row in train:
        dist = euclidean_distance(row, test_row)
        distance.append((row, dist))
    # distance is like [(complete row, distance to simple), ...]
    distance.sort(key=lambda x: x[1])
    res = []
    for i in range(num_neighbors):
        res.append(distance[i][0])
    return res

def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    # a fast way to get the top count
    return max(set(output_values), key=output_values.count)


# Test euclidean_distance
dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]
row0 = dataset[0]
for row in dataset:
    distance = euclidean_distance(row0, row)
    print(distance)



# Test get_neighbors 
neighbors = get_neighbors(dataset, dataset[0], 3)
for neighbor in neighbors:
	print(neighbor)


# Test predict_classification
prediction = predict_classification(dataset, dataset[0], 3)
print('Expected %d, Got %d.' % (dataset[0][-1], prediction))

# A real example below
import pandas as pd

df = pd.read_csv('KNN-iris.csv', names=['sepal length','sepal width','petal length','petal width','class'])

mapping = {'Iris-virginica' :0,
           'Iris-setosa'    :1,
           'Iris-versicolor':2}

df['class_new'] = df.apply(lambda row: mapping[row['class']], axis=1)
df.drop(columns=['class'], inplace=True, axis=1)

# define model parameter
num_neighbors = 5
# define a new record
row = [4.5, 2.3, 1.3, 0.3, None]
# predict the label
label = predict_classification(df.values, row, num_neighbors)
print('Data=%s, Predicted: %s' % (row, label))