import sys
from stats import count_words
from stats import char_count
from stats import chars_to_sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
    
def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    book_text = get_book_text(sys.argv[1])
    
    num_words = count_words(book_text)
    num_char = char_count(book_text)
    rev_list = chars_to_sorted_list(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in rev_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    
    
main()
