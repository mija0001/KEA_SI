from data_classes import BookData
import csv
import json
import xmltodict
import yaml

class BookParser:
    @staticmethod
    def import_book_from_txt(filepath):

        file = open(filepath, "r")
        lines = file.readlines()
        
        isbn10 = lines[0].rstrip('\n');
        isbn13 = lines[1].rstrip('\n');
        title = lines[2].rstrip('\n');
        copyright_year = lines[3].rstrip('\n');
        format = lines[4].rstrip('\n');
        author = lines[5].rstrip('\n');
        description = lines[6].rstrip('\n');
        pages = lines[7].rstrip('\n');

        return BookData(isbn10,isbn13,title,author,format,copyright_year,pages,description)

    def import_book_from_csv(filepath):
        file = open(filepath, "r")
        dict_reader = csv.DictReader(file)
        book_dict = next(dict_reader)
        return BookData(book_dict['isbn_10'],book_dict['isbn_13'],book_dict['title'],book_dict['author'],book_dict['format'],book_dict['copyrightyear'],book_dict['pages'],book_dict['description'])
        
    def import_book_from_json(filepath):
        file = open(filepath, "r")
        json_str = file.read()
        book_dict = json.loads(json_str)[0]
        return BookData(book_dict['isbn_10'],book_dict['isbn_13'],book_dict['title'],book_dict['author'],book_dict['format'],book_dict['copyrightyear'],book_dict['pages'],book_dict['description'])
    
    def import_book_from_xml(filepath):
        file = open(filepath, "r")
        xml_str = file.read()
        book_dict = xmltodict.parse(xml_str)['book']
        return BookData(book_dict['isbn_10'],book_dict['isbn_13'],book_dict['title'],book_dict['author'],book_dict['format'],book_dict['copyrightyear'],book_dict['pages'],book_dict['description'])

    def import_book_from_yaml(filepath):
        file = open(filepath, "r")
        yaml_str = file.read()
        book_dict = yaml.load(yaml_str, Loader=yaml.FullLoader)[0]
        return BookData(book_dict['isbn_10'],book_dict['isbn_13'],book_dict['title'],book_dict['author'],book_dict['format'],book_dict['copyrightyear'],book_dict['pages'],book_dict['description'])