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
  - **6-model_state.py** : link class to table in database
- **7-model_state_fetch_all.py** : script that lists all `State` objects from the database `hbtn_0e_6_usa`
- **8-model_state_fetch_first.py** : script that prints the first `State` object from the database `hbtn_0e_6_usa`
- **9-model_state_filter_a.py** : script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`
- **10-model_state_my_get.py** : script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`
- **11-model_state_insert.py** : script that adds the `State` object *“Louisiana”* to the database `hbtn_0e_6_usa`
- **12-model_state_update_id_2.py** : script that changes the name of a `State` object from the database `hbtn_0e_6_usa`
- **13-model_state_delete_a.py** : script that deletes all `State` objects with `a` name containing the letter a from the database `hbtn_0e_6_usa`
- **model_city.py** : contains the class definition of a `City`
  - **14-model_city_fetch_by_state.py** : prints all `City` objects from the database `hbtn_0e_14_usa`


