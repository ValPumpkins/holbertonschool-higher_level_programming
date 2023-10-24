# <p align="center">🐍 Python - Almost a circle</p>
## <p align="center">🎓 Holberton School Program - Lille</p>

In this project, we will review everything about Python :
- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

and we will also learn about :
- args and kwargs
- Serialization/Deserialization
- JSON

# 🟥 CLASSES
## 🟧 Base

This class will be the **“base”** of all other classes in this project
- Private class attribute : `__nb_objects = 0`
- Public instance attribute : `id`
- Class constructor : `def __init__(self, id=None):`

## 🟩 Rectangle
This class represents a **rectangle** (inherits from `Base`)
- **Private instance attributes** : `__width`, `__height`, `__x` & `__y`
- **Class constructor** : `def __init__(self, width, height, x=0, y=0, id=None):`
- **Public method** : `def area(self):` that returns the area of the `Rectangle` instance
- **Public method** : `def display(self):` that prints in stdout the `Rectangle` instance with `#`
  - improvement by taking care of `x` & `y`
- Overriding the `__str__` method to print a `Rectangle` instance in the format `[Rectangle] (<id>) <x>/<y>`
- **Public method** : `def update(self, *args, **kwargs):`  that updates an instance of a `Rectangle` with the given attributes :
    - 1st argument should be the `id` attribute
    - 2nd argument should be the `width` attribute
    - 3rd argument should be the `height` attribute
    - 4th argument should be the `x` attribute
    - 5th argument should be the `y` attribute
  - `**kwargs` can be thought of as a double pointer to a dictionary : *key/value* and must be skipped if `*args` exists and is not empty
- **Public method** : `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle`
    - Must contain :
      -  `id`
      -  `width`
      -  `height`
      -  `x`
      -  `y`

## 🟪 Square
This class represents a **square** (inherits from `Rectangle`)
- **Class constructor** : `def __init__(self, size, x=0, y=0, id=None):`
- **`__str__` method** should return `[Square] (<id>) <x>/<y> - <size>` - in our case, `width` or `height`
- **Public** getter and setter `size`
- **Public method** : `def update(self, *args, **kwargs)`

