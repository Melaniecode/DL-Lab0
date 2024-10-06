import json
import os
import numpy as np
import matplotlib.pyplot as plt


for i in range(1, 11):  
    input_file_path = f"input/input{i}.json"; 
    output_file_path = f"output/output{i}.json"; 

    # load data from inputfile
    with open(input_file_path, mode='r') as input_file:
        data = json.load(input_file); 

    result_matrix = np.array(data[0]['matrix']); # list -> array

    #list to store value
    top_left = []; 
    bottom_right = []; 

    for datum in data[1:]:
        matrix = datum['matrix']; 
        result_matrix = np.dot(result_matrix, matrix) % 100000; #multiply

        #store values
        top_left.append(result_matrix[0, 0] % 100000); 
        bottom_right.append(result_matrix[-1, -1] % 100000); 

    result_matrix = result_matrix.tolist(); # array -> list
    
    # write data to outputfile
    with open(output_file_path, mode='w') as output_file:
        json.dump(result_matrix, output_file); 

    #plot the values
    plt.plot(range(1, len(top_left) + 1), top_left, label='top - left', color='blue'); 
    plt.plot(range(1, len(bottom_right) + 1), bottom_right, label='bottom - right', color='green'); 
    plt.legend(loc="lower right"); 
    plt.savefig(f'output/output{i}.png'); 
    plt.clf(); 
