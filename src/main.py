import os, shutil
from textnode import TextNode

def main():
    run_cases = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(run_cases.__repr__())


def copy_directory(path_from, path_to):
    pass
    



if __name__ == "__main__":
    main()