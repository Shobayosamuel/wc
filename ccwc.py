import sys, argparse

def count_bytes(filename):
    with open(filename, 'rb') as file:
        byte_cnt = len(file.read())
    return byte_cnt

def main():
    parser = argparse.ArgumentParser(description='Count the number of bytes in a file.')
    parser.add_argument('-c', '--count', action='store_true', help='Count bytes')
    parser.add_argument('filename', help='Input file name')

    args = parser.parse_args()

    if args.count:
        byte_count = count_bytes(args.filename)
        print(f'{byte_count} {args.filename}')

if __name__=="__main__":
    main()
