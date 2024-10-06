import json
import os
import numpy as np

for i in range(1, 11):
    input_file_path = f"input/input{i}.json"; 
    output_file_path = f"output/output{i}.json"; 

    with open(input_file_path, mode='r') as input_file:
        data = json.load(input_file); 

    result_matrix = np.array(data[0]['matrix']); 

    for datum in data[1:]:
        matrix = np.array(datum['matrix']); 
        result_matrix = np.dot(result_matrix, matrix) % 100000; 

    result_matrix = result_matrix.tolist(); 

    with open(output_file_path, mode='w') as output_file:
        json.dump(result_matrix, output_file); 
