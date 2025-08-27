def read_file(file):
    try:
        with open(file, "r") as file:
            string = file.read()
        if string:
            return string
    except FileNotFoundError:
        print(f"Could not find {file}, exiting script")
        exit()
