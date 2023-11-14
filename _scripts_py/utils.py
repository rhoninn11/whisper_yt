import os

def ensure_paths_exist(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

def find_files(directory, extension):
    file_list = []
    for subdir, dirs, files in os.walk(directory):

        for file in files:
            if file.endswith(extension):
                filepath = os.path.relpath(os.path.join(subdir, file), directory)
                file_list.append(filepath)
    return file_list