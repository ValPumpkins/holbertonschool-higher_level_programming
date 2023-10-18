# <p align="center">🐍 Python - Input/Output</p>
## <p align="center">🎓 Holberton School Program - Lille</p>

- **0-read_file.py** : Function that reads a text file `(UTF8)` and prints it to stdout:
- **1-write_file.py** : Function that writes a string to a text file `(UTF8)` and returns the number of characters written
- **2-append_write.py** : Function that appends a string at the end of a text file `(UTF8)` and returns the number of characters added
- **3-to_json_string.py** : Function that returns the JSON representation of an object (string)
- **4-from_json_string.py** : Function that returns an object (Python data structure) represented by a JSON string
- **5-save_to_json_file.py** : Function that writes an Object to a text file, using a JSON representation
- **6-load_from_json_file.py** : Function that creates an Object from a “JSON file”
- **7-add_item.py** : Script that adds all arguments to a Python list, and then save them to file `add-item.json`
- **8-class_to_json.py** : Function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object
- **9-student.py**: class `Student` that defines a student by :
  - Public instance attributes:
    - `first_name`
    - `last_name`
    - `age`
  - Instantiation with `first_name`, `last_name` and `age` : `def __init__(self, first_name, last_name, age):`
  - Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
- **10-student.py** : class `Student` that defines a student by: (based on `9-student.py`)
  - Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
- **11-student.py** : class `Student` that defines a student by: (based on `10-student.py`)
  - Public method `def reload_from_json(self, json):`` that replaces all attributes of the `Student` instance
- **12-pascal_triangle.py** : Function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`

![Pascal Triangle](https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcSKVtpfhR3P8fSksNi8NQrSztSfxpVqJU_CXhcpuTmb4gi_Xl6e3Qg5OcQ1ujP6GRsq)
size 6
