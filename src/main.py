from textnode import TextNode

def main():
    run_cases = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #TextNode("This is a second text node", "italics", "https://www.boot.dev/italics")
    print(run_cases.__repr__())



if __name__ == "__main__":
    main()