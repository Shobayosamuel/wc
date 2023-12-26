import sys, argparse

def count_bytes(filename):
    with open(filename, 'rb') as file:
        byte_cnt = len(file.read())
    return byte_cnt

def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        line_cnt = sum(1 for line in file)
    return line_cnt

def count_words(filename):
    with open(filename, 'rt', encoding='utf-8') as file:
        word_cnt = len(file.read().split())
    return word_cnt

def count_mbytes(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            char_cnt = len(file.read())
        return char_cnt
    except UnicodeDecodeError:
        return count_bytes(filename)

def main():
    parser = argparse.ArgumentParser(description='Count the number of bytes in a file.')
    parser.add_argument('-c', '--count', action='store_true', help='Count bytes')
    parser.add_argument('-l', '--lines', action='store_true', help='Count lines')
    parser.add_argument('-w', '--word', action='store_true', help='Count words')
    parser.add_argument('-m', '--multiByte', action='store_true', help='Count chars')
    parser.add_argument('filename', help='Input file name')

    args = parser.parse_args()

    if args.count:
        byte_count = count_bytes(args.filename)
        print(f'{byte_count} {args.filename}')

    if args.lines:
        line_count = count_lines(args.filename)
        print(f'{line_count} {args.filename}')
    
    if args.word:
        word_count = count_words(args.filename)
        print(f'{word_count} {args.filename}')
    
    if args.multiByte:
        chars_count = count_mbytes(args.filename)
        print(f'{chars_count} {args.filename}')
    
    if not args.word and not args.lines and not args.count:
        byte_count = count_bytes(args.filename)
        line_count = count_lines(args.filename)
        word_count = count_words(args.filename)
        print(f"{byte_count} {line_count} {word_count} {args.filename}")
if __name__=="__main__":
    main()
