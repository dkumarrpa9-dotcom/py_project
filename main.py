def get_book_text(file_path):
    result_text = ""
    try:
        with open(file_path, encoding='utf-8') as path:
            result_text = path.read()
            num_words = len(result_text.split())
            print(f"{num_words} words found in the document")

    except Exception as e:
        print(e)

    return result_text


get_book_text("books/frankenstein.txt")
