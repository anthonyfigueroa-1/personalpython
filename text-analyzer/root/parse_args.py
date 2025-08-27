import argparse

def parse_args():
    args = argparse.ArgumentParser()

    args.add_argument("file", help="(Required) File to analyze text from")
    args.add_argument("--top", help="Create a list of top <x> words in file.(Default is 10)")
    args.add_argument("---save", help="Filepath where to save output to")

    return args.parse_args()
