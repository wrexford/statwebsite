import os, shutil
from textnode import TextNode

def main():
    #run_cases = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #print(run_cases.__repr__())
    print("Copying ")
    copy_static_to_public()

def copy_static_to_public():
    path_from = "/static"
    path_to = "/public"
    
    for src_dir, dirs, files in os.walk(path_from):
        dst_dir = src_dir.replace(path_from, path_to, 1)
        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)
        for data in files:
            src_file = os.path.join(src_dir, data)
            dst_file = os.path.join(dst_dir, data)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copy(src_file, dst_file)
            print(f'Copying {src_dir}\{src_file} to {src_dir}')



if __name__ == "__main__":
    main()