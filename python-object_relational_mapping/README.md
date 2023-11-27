# <p align="center">🐍 Python - Object-relational mapping</p>
## <p align="center">🎓 Holberton School Program - Lille</p>

<img src="https://i.imgur.com/DRPXtkk.jpg" width='100%' />

### Learning Objectives
- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script
- What **ORM** means : *Object-relational Mappers*
- How to map a Python Class to a MySQL table

### Tasks
- **0-select_states.py** : script that lists all `states` from the database `hbtn_0e_0_usa`
- **1-filter_states.py** : script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`
- **2-my_filter_states.py** : script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument
- **3-my_safe_filter_states.py** : script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where name matches the argument, safe from *MySQL injections*
- **4-cities_by_state.py** : script that lists all `cities` from the database `hbtn_0e_4_usa`
- **5-filter_cities.py** :  script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`
- **model_state.py** : python file that contains the class definition of a `State` and an instance `Base = declarative_base()`
