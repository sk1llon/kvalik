import os


def main(cur_path, volume):
    for i_file in os.listdir(cur_path):
        my_path = os.path.abspath(os.path.join(cur_path, i_file))
        if os.path.isfile(i_file):
            volume += os.path.getsize(i_file)
        elif os.path.isdir(i_file):
            path_result = main(my_path, volume)
            if path_result:
                break
    else:
        path_result = None
    return path_result, volume


volume_of_files = 0
path = os.path.abspath(os.path.join('..', '..', 'Module21'))
volume_of_files = round(main(path, volume_of_files)[1] / 1024, 3)
print(volume_of_files)

