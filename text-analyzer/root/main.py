from root.parse_args import parse_args
from root.read_file import read_file
from root.normalize import normalize
from root.tokenize import tokenize
from root.counter import counter
from root.format_data import format_data
from root.save import save_to_file
from root.print_data import print_data

def main():
    args = parse_args()    

    file = args.file.strip()
    top = int(args.top.strip()) if args.top else 10
    save = args.save.strip() if args.save else None

    string = read_file(file)
    print(rf"[INFO] Analyzing {file} ...")

    normalized_string = normalize(string)
    tokens = tokenize(normalized_string)
    top_words, unique_words = counter(tokens, top)
    data = format_data(top_words, len(tokens), unique_words) 
    print_data(data)
    save_to_file(save, data)
