class BookData:
    isbn10 = str
    isbn13 = str
    title = str
    author = str
    format = str
    copyright_year = str
    pages = str
    description = str

    def __init__(self, isbn10="", isbn13="", title="", author="", format="", copyright_year="", pages="", description=""):
        self.isbn10 = isbn10
        self.isbn13 = isbn13
        self.title = title
        self.author = author
        self.format = format
        self.copyright_year = copyright_year
        self.pages = pages
        self.description = description
    
    # to_string method for testing
    def to_string(self):
        return "ISBN10: " + self.isbn10 + "\n" + \
               "ISBN13: " + self.isbn13 + "\n" + \
                "Title: " + self.title + "\n" + \
                "Author: " + self.author + "\n" + \
                "Format: " + self.format + "\n" + \
                "Copyright year: " + self.copyright_year + "\n" + \
                "Pages: " + self.pages + "\n" + \
                "Description: " + self.description