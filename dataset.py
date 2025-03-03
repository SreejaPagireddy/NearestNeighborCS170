#import numpy as np
#lets first do the inputs
import math
import numpy as np
import shutil
import random
def leave_one_out_cross_validation(data, features, value):
        #make a copy of the dataset, use a for loop and if its not the part of the feature, make it equal to 0
    filtered_data=[]
    for row in data:
        filtered_row=[]
        for j in range(len(row)):
            if j in features or j==value or j==0:
                filtered_row.append(row[j])
        filtered_data.append(filtered_row)
    #print(filtered_data)
        #change all occurances of data to filtered_data
    number_correctly_classified =0
    data = filtered_data
    data_size = len(data[1:])
    for k in range(data_size):
        object_to_classify = data[k][1:]
        label_object_to_classify = data[k][0] #
        # text = f'Looping over k at the {k}, location'
        # print(text)
        # text = f'The {k} th object is in class, {label_object_to_classify}'
        # print(text)
        nearest_neighbor_distance = float('inf')
        nearest_neighbor_location = float('inf')
        total =0
        for x in range(data_size):
            if x!=k:
                distance = np.linalg.norm((np.array(data[x][1:]) - np.array(object_to_classify)))
                #print(distances)
                # total = (object_to_classify - data[x][1:]) ** 2
                # distance = math.sqrt(total)
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = x
                    nearest_neighbor_label = data[nearest_neighbor_location][0]
        # print(f'Object {k} is class {label_object_to_classify}')
        # print(f'Its nearest neighbor is {nearest_neighbor_location} which is in class {nearest_neighbor_label}')
        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classified = number_correctly_classified + 1
    accuracy = number_correctly_classified / len(data)
    print(f'This is accuracy {accuracy}')
    return accuracy

# def leave_one_out_cross_validation(data, features, value):
#      random.seed(5)
#      list_values = [0.6, 0.3, 0.9, 0.7, 0.2]
#      value = random.choice(list_values)
#      return value

def feature_search_demo(data):
    track_of_accuracy = []
    num_levels = len(data[0]) #going through the columns, removed the -1
    current_set_of_features = []

    for x in range(1,num_levels):
        text = f'On the {x} th level of the search tree'
        print(text)
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0
        for k in range(1,num_levels):
            if k not in current_set_of_features:    
                text = f'--Considering adding the {k} feature'
                print(text)
                accuracy = leave_one_out_cross_validation(data, current_set_of_features, k+1)

                if accuracy > best_so_far_accuracy:
                     best_so_far_accuracy = accuracy
                     feature_to_add_at_this_level = k
        track_of_accuracy.append(accuracy)
        current_set_of_features.append(feature_to_add_at_this_level)
        text = f'On level {x} i added feature {feature_to_add_at_this_level} to current set'
        print(text)
    max_accuracy = np.argmax(track_of_accuracy)
    print(f'The best feature subset is {current_set_of_features[max_accuracy]}, which has an accuracy of {track_of_accuracy[max_accuracy]}')

def main():
    open_file = open("dataset1.txt")
    data = open_file.readlines()
    data = [[float(x) for x in row.strip().split("  ")] for row in data]
    feature_search_demo(data)
    #leave_one_out_cross_validation(data, 1, 2)

main()