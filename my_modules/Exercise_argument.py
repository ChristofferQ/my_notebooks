import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('file_destination', help='The destination to the program')
    parser.add_argument('-d', '--file_name', help='The name of the file')

    args = parser.parse_args()
    print('file_destination:', args.file_destination)
    print('file_name:', args.file_name)
                                     