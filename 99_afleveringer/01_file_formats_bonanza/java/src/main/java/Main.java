// Main class for testing purposes
public class Main {
    public static void main(String[] args) {
        // Test CSV import
        System.out.println("-----CSV-----");
        System.out.println("" + Parser.importBooksFromCSV("99_afleveringer/01_file_formats_bonanza/files/book.csv"));

        // Test JSON import
        System.out.println("-----JSON----");
        System.out.println("" + Parser.importBookFromJSON("99_afleveringer/01_file_formats_bonanza/files/book.json"));

        // Test YAML import
        System.out.println("-----YAML----");
        System.out.println("" + Parser.importBookFromYAML("99_afleveringer/01_file_formats_bonanza/files/book.yaml"));

        // Test XML import
        System.out.println("-----XML-----");
        System.out.println("" + Parser.importBookFromXML("99_afleveringer/01_file_formats_bonanza/files/book.xml"));

        // Test TXT import
        System.out.println("-----TXT-----");
        System.out.println("" + Parser.importBookFromTXT("99_afleveringer/01_file_formats_bonanza/files/book.txt"));
    }
}