import os, shutil
from textnode import TextNode
from markdown_blocks import markdown_to_html_node

def main():
    #run_cases = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #print(run_cases.__repr__())
    print("Copying files")
    copy_static_to_public()

def copy_static_to_public():
    path_from = "static"
    path_to = "public"
    
    for src_dir, dirs, files in os.walk(path_from):
        dst_dir = src_dir.replace(path_from, path_to, 1)

        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)
        elif os.path.exists(dst_dir):
            shutil.rmtree(dst_dir)
            os.mkdir(dst_dir)

        for data in files:
            src_file = os.path.join(src_dir, data)
            dst_file = os.path.join(dst_dir, data)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copy(src_file, dst_file)
            #print(f"Copying {src_file} to {src_dir}")


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")


if __name__ == "__main__":
    main()