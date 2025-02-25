#lets first do the inputs

def feature_search_demo(num_of_lines):
    size_data = len(num_of_lines)-1
    for x in range(1,size_data):
        text = f'On the {x} th level of the search tree'
        print(text)
def main():
    open_file = open("dataset1.txt")
    num_of_lines = open_file.readlines()
    feature_search_demo(num_of_lines)

main()