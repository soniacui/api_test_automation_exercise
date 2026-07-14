import os
import json

methods = ['get', 'post', 'put', 'patch', 'delete']
endpoints = ['posts', 'comments', 'albums', 'photos', 'todos', 'users']

methods_status = {
    'get': '200',
    'post': '201',
    'put': '200',
    'patch': '200',
    'delete': '200'
}

inputs_read = {}
expected_read = {}

for m in methods:
    input_path = f"fixtures/input/{m}.json"
    expected_path = f"fixtures/expected/{m}.json"
    
    with open(input_path, 'r', encoding='utf-8') as f:
        inputs_read[m] = json.load(f)
        
    with open(expected_path, 'r', encoding='utf-8') as f:
        expected_read[m] = json.load(f)

created_count = 0

for ep in endpoints:
    os.makedirs(f"fixtures/input/{ep}", exist_ok=True)
    os.makedirs(f"fixtures/expected/{ep}", exist_ok=True)
    
    for m in methods:
        status = methods_status[m]
        test_name = f"test_{m}_{ep}_returns_{status}_and_expected_structure"
        
        input_filename = f"fixtures/input/{ep}/input_{test_name}.json"
        expected_filename = f"fixtures/expected/{ep}/expected_{test_name}.json"
        
        ep_input = inputs_read[m][ep]
        input_data = {"endpoint": ep_input["endpoint"]}
        if m in ['post', 'put', 'patch']:
            input_data["payload"] = ep_input.get("payload", {})
            
        expected_data = expected_read[m][ep]
        
        with open(input_filename, 'w', encoding='utf-8') as f:
            json.dump(input_data, f, indent=2)
            created_count += 1
            
        with open(expected_filename, 'w', encoding='utf-8') as f:
            json.dump(expected_data, f, indent=2)
            created_count += 1

# Delete old combined files
deleted_count = 0
for m in methods:
    input_path = f"fixtures/input/{m}.json"
    expected_path = f"fixtures/expected/{m}.json"
    if os.path.exists(input_path):
        os.remove(input_path)
        deleted_count += 1
    if os.path.exists(expected_path):
        os.remove(expected_path)
        deleted_count += 1

print(f"Created files: {created_count}")
print(f"Deleted files: {deleted_count}")
