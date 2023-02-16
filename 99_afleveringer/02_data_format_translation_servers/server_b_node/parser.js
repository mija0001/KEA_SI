import fs from 'fs';
import YAML from 'yaml';

export function importBookFromJSON(path){
    var data = fs.readFileSync(path, "utf8");
    return JSON.parse(data);
}

export function importBookFromYAML(path){
    var data = fs.readFileSync(path, "utf8");
    return YAML.parse(data);
}

