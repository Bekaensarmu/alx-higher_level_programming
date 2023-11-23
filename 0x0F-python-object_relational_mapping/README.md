# Python - Object-relational mapping
 
In this project, I became familiar with using MySQLdb and SQLAlchemy to
query, create, edit, and delete tables in MySQL.

## Tests

Folder of SQL and Python scripts for setting up test tables
for all files. Provided by ALX.

## Tasks 
* **0. Get all states**
* Usage: `./0-select_states.py <mysql username> <mysql password>
  <database name>`.
* Results are ordered by ascending `states.id`.

* **1. Filter states**
* Usage: `./1-filter_states.py <mysql username> <mysql password>
  <database name>`.
* Results are ordered by ascending `states.id`.

* **2. Filter states by user input**
* Usage: `./2-my_filter_states.py <mysql username> <mysql password>
  <database name> <state name searched>`.
* Results are ordered by ascending `states.id`.
* Uses string formatting to construct the SQL query.

* **3. SQL Injection**
* Usage: `./3-my_safe_filter_states.py <mysql username> <mysql password>
  <database name> <state name searched>`.
* Results are ordered by ascending `states.id`.
* Safe from SQL injections.

* **4. Cities by states**
* Usage: `./4-cities_by_state.py <mysql username> <mysql password>
  <database name>`.
* Results are ordered by ascending `cities.id`.


* **5. All cities by state**
* Usage: `./5-filter_cities.py <mysql username> <mysql password>
  <database name>`.
* Results are sorted by ascending `cities.id`.

* **6. First state model**
* [model_state.py](./model_state.py): Python module defining a class `State`
  that inherits from SQLAlchemy `Base` and links to the MySQL table `states`.

* **7. All states via SQLAlchemy**
* Usage: `./7-model_state_fetch_all.py <mysql username> <mysql password>
  <database name>`.
* Results are sorted by ascending `states.id`.

* **8. First state**
* Usage: `./8-model_state_fetch_first.py <mysql username> <mysql password>
  <database name>`.
* If the `states` table is empty, prints `Nothing`.

* **9. Contains `a`**
* Usage: `./9-model_state_filter_a.py <mysql username> <mysql password>
  <database name>`.
* Results are ordered by ascending `states.id`.

* **10. Get a state**
* Usage: `./10-model_state_my_get.py <mysql username> <mysql password>
  <database name> <state searched name>`.
* Displays the `id` of the matched `State`.
* If no match is found, prints `Not found`.

* **11. Add a new state**
* Usage: `./11-model_state_insert.py <mysql username> <mysql password>
  <database name>`.
* Prints the `id` of the new `State` after creation.

* **12. Update a state**
* Usage: `./12-model_state_update_id_2.py <mysql username> <mysql password>
  <database name>`.

* **13. Delete states**
* Python script that uses SQLAlchemy to delete all `State` objects with a name containing the
  letter `a` from the database `hbtn_0e_6_usa`.
* Usage: `./13-model_state_delete_a.py <mysql username> <mysql password>
  <database name>`.

* **14. Cities in state**
* Python module defining a class `City`
  that inherits from SQLAlchemy `Base` and links to the MySQL table `cities`.
* Includes class attribute `state_id` that is a foreign key to
    `states.id`.
* [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py):
  Python script that uses SQLAlchemy to list all `City` objects in the database
  `hbtn_0e_14_usa`.
* Usage: `./14-model_city_fetch_by_state.py <mysql username> <mysql password>
  <database name>`.
* Results are sorted by ascending `cities.id`.  

* **15. City relationship**
* Python module defining a
  class `State` that inherits from SQLAlchemy `Base` and links to the MySQL table
  `states`.
* Identical to the `State` class defined in [model_state.py](./model_state.py).
* Includes class attribute `classes` that represents a relationship with
    the class `City`. If the `State` object is deleted, all linked `City` objects
    are also deleted. `State` objects are backreferenced to `City` objects as
    `state`.
* [relationship_city.py](./relationship_city.py): Python module defining a
  class `City` that inherits from SQLAlchemy `Base` and links to the MySQL table
  `cities`.
* Identical to the `City` class defined in [model_city.py](./model_city.py).
* [100-relationship_states_cities.py](./100-relationship_states_cities.py):
  Python script that uses SQLAlchemy to add the `State` "California" with `City`
  "San Francisco" to the database `hbtn_0e_100_usa`.
* Usage: `./100-relationship_states_cities.py <mysql username>
  <mysql password> <database name>`.
* Uses the `cities` relationship for all `State` objects.

* **16. List relationship**
* Python script that uses SQLAlchemy to list all `State` and corresponding
  `City` objects in the database `hbtn_0e_101_usa`.
* Usage: `./101-relationship_states_cities_list.py <mysql username>
  <mysql password> <database name>`.
* Uses the `cities` relationship for all `State` objects.
* Results are sorted by ascending `states.id` and `cities.id`.

* **17. List city**
* Python script that uses SQLAlchemy to list all `City` objects from the database
  `hbtn_0e_101_usa`.
* Usage: `./102-relationship_cities_states_list.py <mysql username>
  <mysql password> <database name>`.
* Uses the `state` relationship to access the `State` objects linked to `City` objects.
* Results are sorted by ascending `cities.id`.
