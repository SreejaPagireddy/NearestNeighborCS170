#import numpy as np
#lets first do the inputs
import math
import shutil
# def leave_one_out_cross_validation(data, features, value):

#     #make a copy of the dataset, use a for loop and if its not the part of the feature, make it equal to 0
#     filtered_data=[]
#     for k in data:
#         filtered_row=[]
#         for j in data:
#             if j in features or j==value:
#                 filtered_row.append(data[k][j])
#         filtered_data.append(filtered_row)
#         #change all occurances of data to filtered_data
#     data_size = len(filtered_data)
#     for k in range(data_size):
#         #object_to_classify = filtered_data[k][2:]
#         object_to_classify = filtered_data[k][0:]
#         label_object_to_classify = data[k][0]
#         nearest_neighbor_distance = float('inf')
#         nearest_neighbor_location = float('inf')
#         for x in range(data_size):
#             if x!=k:  
#                 distance = math.sqrt(sum((object_to_classify)- filtered_data[x][0:])).__pow__(2)
#                 if distance < nearest_neighbor_distance:
#                     nearest_neighbor_distance = distance
#                     nearest_neighbor_location = k
#                     nearest_neighbor_label = data[nearest_neighbor_location]
#         if label_object_to_classify == nearest_neighbor_label:
#             number_correctly_classified = number_correctly_classified + 1
#     accuracy = number_correctly_classified / len(data)
#     return accuracy

def leave_one_out_cross_validation(data, features, value):
    data_size = len(data[1:])
    for k in range(data_size):
        object_to_classify = data[k][1:]
        label_object_to_classify = data[k][0] #
        text = f'Looping over k is at the, {k}, location'
        print(text)
        text = f'The {k} th object is in class, {label_object_to_classify}'
        print(text)



def feature_search_demo(data):
    num_feature = len(data[0])-1
    current_set_of_features = []

    for x in range(1,num_feature):
        text = f'On the {x} th level of the search tree'
        print(text)
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0
        for k in range(1,num_feature):
            #if k not in current_set_of_features:    
                text = f'--Considering adding the {k} feature'
                print(text)
                # accuracy = leave_one_out_cross_validation(data, current_set_of_features, k+1)

                # if accuracy > best_so_far_accuracy:
                #     best_so_far_accuracy = accuracy
                #     feature_to_add_at_this_level = k
        #current_set_of_features.append(feature_to_add_at_this_level)
        #text = f'On level {x} i added feature {feature_to_add_at_this_level} to current set'

def main():
    open_file = open("dataset1.txt")
    data = open_file.readlines()
    data = [[float(x) for x in row.strip().split("  ")] for row in data]
    #feature_search_demo(data)
    leave_one_out_cross_validation(data, 1, 2)

main()