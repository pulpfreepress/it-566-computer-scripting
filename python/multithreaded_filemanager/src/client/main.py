from client import Client

def main():
    c1 = Client("127.0.0.1", 5000)
    keep_going = True
    while keep_going:
        c1.send("ADD_PERSON:Rick, W, Miller")
        input_str = input("Keep Going? (y/n): ")
        if input_str == "n":
            keep_going = False
if __name__ == "__main__":
    main()