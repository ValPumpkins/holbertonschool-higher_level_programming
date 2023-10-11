# <p align="center">🐍 Python - Classes & Objects</p>
## <p align="center">🎓 Holberton School Program - Lille</p>

- **0-square.py**
  - Empty class `Square` that defines a square
- **1-square.py**
  - Class `Square` that defines a square by: (based on `0-square.py`) :
      - Private instance attribute `size`
      - Instantiation with `size`
- **2-square.py**
  - Class `Square` that defines a square by: (based on `1-square.py`) :
      - Instantiation with optional `size`: `def __init__(self, size=0):`
- **3-square.py**
  - Class `Square` that defines a square by: (based on `2-square.py`) :
      - Public instance attribute `def area(self):` that returns the current square area
- **4-square.py**
  - Class `Square` that defines a square by: (based on `3-square.py`) :
      - Property `def size(self):` to retrieve the private instance attribute `self`
      - Property setter `def size(self, value):` to set `self`.
- **5-square.py**
  - Class `Square` that defines a square by: (based on `4-square.py`) :
      - Public instance method `def my_print(self):` that prints the square with the character `#` to standard output
- **6-square.py**
  - Class `Square` that defines a square by: (based on `5-square.py`) :
      - Private instance attribute `position`
      - Property `def position(self):` to retreive `position`
      - Property setter `def position(self, value):` to set `position`
      - Instantiation with optional `size` and `position`: `def __init__(self, size=0, position=(0, 0)):`
