import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.yaml.snakeyaml.Yaml;

import javax.xml.stream.XMLEventReader;
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLStreamException;
import javax.xml.stream.events.StartElement;
import javax.xml.stream.events.XMLEvent;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.LinkedHashMap;

public class Parser {

    // takes a CSV filepath, returns a BookData object, returns null on error
    public static BookData importBooksFromCSV(String filepath) {
        String delimiter = ",";

        // Create indexes for every data field, remains -1 if not found
        int isbn10Index = -1;
        int isbn13Index = -1;
        int titleIndex = -1;
        int copyrightYearIndex = -1;
        int formatIndex = -1;
        int authorIndex = -1;
        int descriptionIndex = -1;
        int pagesIndex = -1;

        try {
            BufferedReader reader = Files.newBufferedReader(Paths.get(filepath));
            String line = reader.readLine();
            String[] columns = line.split(delimiter);

            // Set indexes for every data field
            for (int i = 0; i < columns.length; i++) {
                switch (columns[i]) {
                    case "isbn_10" -> isbn10Index = i;
                    case "isbn_13" -> isbn13Index = i;
                    case "title" -> titleIndex = i;
                    case "copyrightyear" -> copyrightYearIndex = i;
                    case "format" -> formatIndex = i;
                    case "author" -> authorIndex = i;
                    case "description" -> descriptionIndex = i;
                    case "pages" -> pagesIndex = i;
                }
            }

            // Get values from fields using indexes
            line = reader.readLine();
            if (line != null) {
                columns = line.split(delimiter);
                String isbn10 = isbn10Index >= 0 ? columns[isbn10Index] : "";
                String isbn13 = isbn13Index >= 0 ? columns[isbn13Index] : "";
                String title = titleIndex >= 0 ? columns[titleIndex] : "";
                String author = authorIndex >= 0 ? columns[authorIndex] : "";
                String format = formatIndex >= 0 ? columns[formatIndex] : "";
                String copyrightYear = copyrightYearIndex >= 0 ? columns[copyrightYearIndex] : "";
                String pages = pagesIndex >= 0 ? columns[pagesIndex] : "";
                String description = descriptionIndex >= 0 ? columns[descriptionIndex] : "";

                // Return BookData object created from values
                return new BookData(isbn10, isbn13, title, author, format, copyrightYear, pages, description);
            } else {
                // CSV file did not contain data, return null
                return null;
            }

        } catch (IOException e) {
            // IO error, return null
            return null;
        }
    }

    // takes a JSON filepath, returns a BookData object, returns null on error
    public static BookData importBookFromJSON(String filepath) {

        try {
            JSONArray jsonArray = (JSONArray) (new JSONParser().parse(new FileReader(filepath)));
            JSONObject jsonObject = (JSONObject) jsonArray.get(0);

            String isbn10 = (String) jsonObject.get("isbn_10");
            String isbn13 = (String) jsonObject.get("isbn_13");
            String title = (String) jsonObject.get("title");
            String author = (String) jsonObject.get("author");
            String format = (String) jsonObject.get("format");
            String copyrightYear = (String) jsonObject.get("copyrightYear");
            String pages = (String) jsonObject.get("pages");
            String description = (String) jsonObject.get("description");

            return new BookData(isbn10, isbn13, title, author, format, copyrightYear, pages, description);

        } catch (IOException | ParseException e) {
            System.out.println(e.toString());
            return null;
        }
    }

    // takes a YAML filepath, return a BookData object, returns null on error
    public static BookData importBookFromYAML(String filepath) {

        try {
            InputStream inputStream = new FileInputStream(new File(filepath));
            Yaml yaml = new Yaml();
            ArrayList arrayList = (ArrayList) yaml.load(inputStream);
            LinkedHashMap map = (LinkedHashMap) arrayList.get(0);

            String isbn10 = (String) map.get("isbn_10");
            String isbn13 = (String) map.get("isbn_13");
            String title = (String) map.get("title");
            String author = (String) map.get("author");
            String format = (String) map.get("format");
            String copyrightYear = (String) map.get("copyrightYear");
            String pages = (String) map.get("pages");
            String description = (String) map.get("description");

            return new BookData(isbn10, isbn13, title, author, format, copyrightYear, pages, description);

        } catch (IOException e) {
            return null;
        }
    }

    // takes a XML filepath, returns a BookData object, returns null on error
    public static BookData importBookFromXML(String filepath) {

        try {
            XMLInputFactory xmlInputFactory = XMLInputFactory.newInstance();
            XMLEventReader reader = xmlInputFactory.createXMLEventReader(new FileInputStream(filepath));

            String isbn10 = "";
            String isbn13 = "";
            String title = "";
            String author = "";
            String format = "";
            String copyrightYear = "";
            String pages = "";
            String description = "";

            while (reader.hasNext()) {
                XMLEvent nextEvent = reader.nextEvent();
                if (nextEvent.isStartElement()) {
                    StartElement startElement = nextEvent.asStartElement();
                    switch (startElement.getName().getLocalPart()) {
                        case "isbn_10" -> {
                            nextEvent = reader.nextEvent();
                            isbn10 = nextEvent.asCharacters().getData();
                        }
                        case "isbn_13" -> {
                            nextEvent = reader.nextEvent();
                            isbn13 = nextEvent.asCharacters().getData();
                        }
                        case "title" -> {
                            nextEvent = reader.nextEvent();
                            title = nextEvent.asCharacters().getData();
                        }
                        case "copyrightyear" -> {
                            nextEvent = reader.nextEvent();
                            copyrightYear = nextEvent.asCharacters().getData();
                        }
                        case "format" -> {
                            nextEvent = reader.nextEvent();
                            format = nextEvent.asCharacters().getData();
                        }
                        case "author" -> {
                            nextEvent = reader.nextEvent();
                            author = nextEvent.asCharacters().getData();
                        }
                        case "description" -> {
                            nextEvent = reader.nextEvent();
                            description = nextEvent.asCharacters().getData();
                        }
                        case "pages" -> {
                            nextEvent = reader.nextEvent();
                            pages = nextEvent.asCharacters().getData();
                        }
                    }
                }
            }

            return new BookData(isbn10, isbn13, title, author, format, copyrightYear, pages, description);

        } catch (IOException | XMLStreamException e) {
            System.out.println(e);
            return null;
        }
    }

    // takes a TXT filepath, returns a BookData object, returns null on error
    public static BookData importBookFromTXT(String filepath) {
        try {
            BufferedReader reader = Files.newBufferedReader(Paths.get(filepath));

            String isbn10 = reader.readLine();
            String isbn13 = reader.readLine();
            String title = reader.readLine();
            String copyrightYear = reader.readLine();
            String format = reader.readLine();
            String author = reader.readLine();
            String description = reader.readLine();
            String pages = reader.readLine();

            return new BookData(isbn10, isbn13, title, author, format, copyrightYear, pages, description);

        } catch (IOException e) {
            return null;
        }
    }

}
