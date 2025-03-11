import numpy as np
import time

def leave_one_out_cross_validation(data, features, value):
    filtered_data=[]
    for row in data:
        filtered_row=[]
        for j in range(len(row)):
            if j in features or j==value or j==0:
                filtered_row.append(row[j])
        filtered_data.append(filtered_row)
    number_correctly_classified =0
    data = filtered_data
    data_size = len(data)
    for k in range(data_size):
        object_to_classify = data[k][1:]
        label_object_to_classify = data[k][0]
        nearest_neighbor_distance = float('inf')
        nearest_neighbor_location = float('inf')
        for x in range(data_size):
            if x!=k:
                distance = np.linalg.norm(np.array(object_to_classify)-(np.array(data[x][1:])))
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = x
                    nearest_neighbor_label = data[nearest_neighbor_location][0]
        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classified = number_correctly_classified + 1
    accuracy = number_correctly_classified / len(data)
    return accuracy

def forward_search_demo(data):
    start = time.time()
    num_levels = len(data[0]) #going through the columns, removed the -1
    num_rows = len(data)
    print(f'This dataset has {num_levels-1} (not including the class attribute, with {num_rows} instances\n')
    total_features=[x for x in range(1,num_levels)] #this is all the features
    current_set_of_features = []
    total_accuracy = leave_one_out_cross_validation(data, total_features, 0)
    print(f'Running nearest neighbor with all {num_levels-1} features, using leaving-one-out evaluation, I get an accuracy of {total_accuracy}\n')
    accuracy = leave_one_out_cross_validation(data, current_set_of_features, 0)
    print( f'Uisng features {current_set_of_features} with accuracy of {accuracy}')

    max_ac = 0
    max_features = []

    for x in range(1,num_levels):
        text = f'On the {x} th level of the search tree'
        print(text)
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0
        for k in range(1,num_levels):
            if k not in current_set_of_features:   
                accuracy = leave_one_out_cross_validation(data, current_set_of_features, k)   
                text = f'--Considering adding the {",".join([str(x) for x in current_set_of_features])}, {k} feature with accuracy {accuracy}'
                print(text)
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = k
        current_set_of_features.append(feature_to_add_at_this_level)
        if(best_so_far_accuracy > max_ac):
            max_ac = best_so_far_accuracy
            max_features = [x for x in current_set_of_features]
        text = f'On level {x} i added feature {",".join(str(x) for x in current_set_of_features)} to current set'
        print(text)
    print(f'The best feature subset is {max_features}, which has an accuracy of {max_ac}')
    end = time.time()
    length = end - start
    print(f'It took, {length} seconds')

def backward_search_demo(data):
    start = time.time()
    num_levels = len(data[0]) #going through the columns, removed the -1
    num_rows = len(data)
    print(f'This dataset has {num_levels-1} (not including the class attribute, with {num_rows} instances\n')
    current_set_of_features = [x for x in range(1,num_levels)] #this is all the features
    max_features = current_set_of_features
    accuracy = leave_one_out_cross_validation(data, current_set_of_features, 0)
    print(f'Running nearest neighbor with all {num_levels-1} features, using leaving-one-out evaluation, I get an accuracy of {accuracy}\n')
    max_ac = accuracy
    print( f'Uisng features {current_set_of_features} with accuracy of {accuracy}')

    for x in range(1,num_levels):
        text = f'On the {x} th level of the search tree with accuracy'
        print(text)
        best = 0
        feature_to_add_at_this_level = []
        for f in current_set_of_features:
            new_feature = []
            for x in current_set_of_features:
                if(x != f):
                    new_feature.append(x)
            accuracy = leave_one_out_cross_validation(data, new_feature, 0)
            print(f'Using feature {new_feature} with accuracy {accuracy}')
            if(accuracy > best):
                feature_to_add_at_this_level = new_feature
                best = accuracy
        current_set_of_features = feature_to_add_at_this_level 
        if(best > max_ac):
            max_ac = best
            max_features = [x for x in current_set_of_features]
        text = f'On level {x} i added feature {",".join(str(x) for x in current_set_of_features)} to current set with accuracy {best}'
        print(text)
    print(f'The best feature subset is {max_features}, which has an accuracy of {max_ac}')
    end = time.time()
    length = end - start
    print(f'It took, {length} seconds')

def main():
    open_file = open("dataset1.txt")
    data = open_file.readlines()
    data = [[float(x) for x in row.strip().split("  ")] for row in data]
    forward_search_demo(data)
    #backward_search_demo(data)
    #leave_one_out_cross_validation(data, 1, 2)
main()