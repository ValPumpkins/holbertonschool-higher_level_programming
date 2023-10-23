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

# 🆑 CLASSES
## ⚾️ Base

This class will be the **“base”** of all other classes in this project
- Private class attribute : `__nb_objects = 0`
- Public instance attribute : `id`
- Class constructor : `def __init__(self, id=None):`

## 🧳 Rectangle
This class epresents a **rectangle** (inherits from `Base`)
- **Private instance attributes** : `__width`, `__height`, `__x` & `__y`
- **Class constructor** : `def __init__(self, width, height, x=0, y=0, id=None):`
- **Public method** : `def area(self):` that returns the area of the `Rectangle` instance
- **Public method** : `def display(self):` that prints in stdout the `Rectangle` instance with `#`
  - improvement by taking care of `x` & `y`
- Overriding the `__str__` method to print a `Rectangle` instance in the format `[Rectangle] (<id>) <x>/<y>`
-
