from parser_classes import BookParser
from data_classes import BookData

if __name__ == '__main__':
    print('-----TXT-----')
    print(BookParser.import_book_from_txt('99_afleveringer/01_file_formats_bonanza/files/book.txt').to_string())

    print('-----CSV-----')
    print(BookParser.import_book_from_csv('99_afleveringer/01_file_formats_bonanza/files/book.csv').to_string())

    print('-----JSON-----')
    print(BookParser.import_book_from_json('99_afleveringer/01_file_formats_bonanza/files/book.json').to_string())

    print('-----XML-----')
    print(BookParser.import_book_from_xml('99_afleveringer/01_file_formats_bonanza/files/book.xml').to_string())

    print('-----YAML-----')
    print(BookParser.import_book_from_yaml('99_afleveringer/01_file_formats_bonanza/files/book.yaml').to_string())