def save_to_file(save, data):
    if save:
        with open(save, "w") as file:
            for line in data:
                file.write(line + "\n")
        print(f"[DONE] Save")
