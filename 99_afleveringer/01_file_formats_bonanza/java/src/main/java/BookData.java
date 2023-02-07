// Book data object
public class BookData {

    public String isbn10;
    public String isbn13;
    public String title;
    public String author;
    public String format;
    public String copyrightYear;
    public String pages;
    public String description;

    public BookData() {
    }
    public BookData(String isbn10, String isbn13, String title, String author, String format, String copyrightYear, String pages, String description) {
        this.isbn10 = isbn10;
        this.isbn13 = isbn13;
        this.title = title;
        this.author = author;
        this.format = format;
        this.copyrightYear = copyrightYear;
        this.pages = pages;
        this.description = description;
    }

    // toString method for testing if data was correctly imported
    @Override
    public String toString() {
        return "BookData{" + '\n' +
                "isbn10 = " + isbn10 + '\n' +
                "isbn13 = " + isbn13 + '\n' +
                "title = " + title + '\n' +
                "author = " + author + '\n' +
                "format = " + format + '\n' +
                "copyrightYear = " + copyrightYear + '\n' +
                "pages = " + pages + '\n' +
                "description = " + description + '\n' +
                '}';
    }
}