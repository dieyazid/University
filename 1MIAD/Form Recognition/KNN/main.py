# Define the data table
# data_table = [[3, 5, 4, 6, 1, 1],
#               [4, 6, 10, 3, 2, 2],
#               [8, 3, 4, 2, 6, 3],
#               [2, 1, 4, 3, 6, 3],
#               [2, 5, 1, 4, 8, 2]]
# input_instance = [3, 12, 4, 7, 8]
###################################
# data_table = [[35,35,3,"non"],
#               [22,50,2,"oui"],
#               [63,200,1,"non"],
#               [59,170,1,"non"],
#               [25,40,4,"oui"]
#     ]
# input_instance = [37,50,2]
###################################
# data_table = [
#     [20, 15, "oui"],
#     [10, 20, "non"],
#     [15, 15, "non"],
#     [15, 20, "oui"],
#     [10, 10, "non"],
#     [20, 10, "non"]
# ]
# input_instance = [15, 10]


def hamming_distance(instance1, instance2):
    distance = 0
    F=0
    for i in range(len(instance1)-1):
        if instance1[i] == instance2[i]:
            F+= 1 / M
        else:
            F+= 0 / M
    distance = 1 - 1/(len(data_table[0])-1) * F
    return distance

def Calculate_Modality():
    unique_values = set()
    for row in data_table:
        for element in row[:-1]:  
            unique_values.add(element)

    M = len(unique_values)
    return M

#################
k = 3
M = Calculate_Modality()
#################
def KNN():
    # Calculate the distance between the input instance and all instances in the data table
    distances = []
    for instance in data_table:
        distance = hamming_distance(input_instance, instance)
        distances.append((instance, distance))

    # Select the k instances with the smallest distances
    nearest_neighbors = sorted(distances, key=lambda x: x[1])[:k]

    # Count the number of instances in each class among the nearest neighbors
    class_counts = {}
    for neighbor in nearest_neighbors:
        if neighbor[0][-1] in class_counts:
            class_counts[neighbor[0][-1]] += 1
        else:
            class_counts[neighbor[0][-1]] = 1

    # Assign the input instance to the class with the most instances among the nearest neighbors
    predicted_class = max(class_counts, key=class_counts.get)
    return predicted_class

print(KNN())