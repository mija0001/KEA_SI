--- Task ---
Create at least two servers (this week you can start with one) in two different programming languages with REST APIs.
Create endpoints that read the files that you created last week, parse them and send them as response.
You must figure out what data format to send as response.

You are allowed to split the responsibility between the servers if you are pressed for time.
I.e. ServerA reads XML, CSV. ServerB reads YAML, TXT, JSON.

--- Data files ---
99_afleveringer\02_data_format_translation_servers\server_a_python\data
99_afleveringer\02_data_format_translation_servers\server_b_node\data

---Python solution (Server A)---
99_afleveringer\02_data_format_translation_servers\server_a_python\main.py
Webserver accessible on localhost:8000/book_from_[FILEFORMAT] parses file of the format given in the endpoint, and returns it as a JSON/Dict
Fileformat endpoints available: txt, csv, json, yaml, xml

---Node solution (Server B)---
99_afleveringer\02_data_format_translation_servers\server_b_node\app.js
Webserver accessible on localhost:8001/book_from_[FILEFORMAT] parses file of the format given in the endpoint, and returns it as a JSON
Fileformat endpoints available: json, yaml
