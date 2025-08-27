def format_data(top_words, total_tokens, unique_words):
    string_list = []
    for i, (word, count) in enumerate(top_words, start=1):
        string_list.append(f"{i}) {word:<10} {count}")
    string_list.append(f"[INFO] Unique words: {unique_words} | Total_tokens: {total_tokens}")
    
    return string_list
