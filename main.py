import json
import os

for i in range(1,11):
  input_file_path = f"input/input{i}.json"; 
  output_file_path = f"input/output{i}.json"; 
  
  with open(input_file_path, mode='r') as input_file:
    data = json.load(input_file); 
    print(data); 