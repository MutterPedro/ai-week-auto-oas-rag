import os

YAML_FILES_FOLDER_PATH = os.path.join(os.path.dirname("main.py"), "yaml_files")

def save_yaml_file(file_name: str, content: str) -> str:
    file_name = file_name + ".yaml" if not file_name.endswith(".yaml") else file_name
    file_path = os.path.join(YAML_FILES_FOLDER_PATH, file_name)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(content)
    
    return file_path

def load_yaml_file(file_name: str) -> str:
    file_name = file_name + ".yaml" if not file_name.endswith(".yaml") else file_name
    file_path = os.path.join(YAML_FILES_FOLDER_PATH, file_name)
    with open(file_path, 'r') as f:
        return f.read()

def delete_yaml_file(file_name: str):
    file_name = file_name + ".yaml" if not file_name.endswith(".yaml") else file_name
    file_path = os.path.join(YAML_FILES_FOLDER_PATH, file_name)
    os.remove(file_path)