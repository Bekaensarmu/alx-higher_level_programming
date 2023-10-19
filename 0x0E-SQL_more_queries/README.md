# SQL - More queries

 I continued to practicing SQL queries

## Description
What you should learn from this project:

* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

## Tasks

* **0. My privileges!**
MySQL script that lists all privileges of the users

* **Root user**
* Write a script that creates the database hbtn_0d_2 and the user user_0d_2. 

* **2. Read user**
MySQL script that creates the database
  `hbtn_0d_2` and user `user_0d_2` with password `user_0d_2_pwd`.
  * `user_0d_2` only has SELECT privilege on the database `hbtn_0d_2`.

* **3. Always a name**
MySQL script that creates the table `force_name`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256) (cannot be null)

* **4. ID can't be null**
* Write a script that creates the table id_not_null on your MySQL server

* **5. Unique ID**
* Write a script that creates the table unique_id on your MySQL server.

* **6. States table**
MySQL script that creates the database `hbtn_0d_usa`
  with a table `states`.
  * `states` description:
    * `id`: INT (unique, auto-generated, cannot be null and is a primary key)
    * `name`: VARCHAR(256) (cannot be null)

* **7. Cities table**
* Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

* **8. Cities of California**
 MySQL script that lists all the cities of California that can be found in the
  database `hbtn_0d_usa`, ordered by ascending city id.

* **9. Cities by States**
* Write a script that lists all cities contained in the database hbtn_0d_usa.

* **10. Genre ID by show**
MySQL script that lists all
  shows contained in `hbtn_0d_tvshows` that have at least one genre linked, in order of ascending
`tv_shows.title` and `tv_show_genres.genre_id`.

* **11. Genre ID for all shows**
* Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)

* **12. No genre**
MySQL script that lists all shows contained in
  `hbtn_0d_tvshows` without a genre linked, in order of ascending `tv_shows.title` and `tv_show_genres.genre_id`.

* **13. Number of shows by genre**
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)

* **14. My genres**
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)

* **15. Only Comedy**
 MySQL script that lists all comedy shows in the
  database `hbtn_0d_tvshows`, in order of ascending show title.

* **16. List shows and genres**
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)

* **17. Not my genre**
MySQL script that uses the `hbtn_0d_tvshows`
  database to list all genres not linked to the show Dexter, in order of ascending genre name.

* **18. No Comedy tonight!**
MySQL script that lists all shows without the
  genre comedy in the database `hbtn_0d_tvshows`, in order of ascending show title.

* **19. Rotten tomatoes**
MySQL script that lists all shows from
  `hbtn_0d_tvshows_rate` by their rating, in order of descending rating.

* **20. Best genre**
 MySQL script that lists all genres in the
  database `hbtn_0d_tvshows_rate` by their rating, in order of descending rating.

## Author
* **Beka Gerbaba**

