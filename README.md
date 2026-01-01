####  Assignment Description  ##

This assignment is a simple backend REST API built using Python Flask and PostgreSQL.
It uses Project Gutenberg books database to fetch and return book information in JSON format.

The API provides a /books endpoint which returns a paginated list of books ordered by popularity (download count).
Each book contains its title, authors, languages, and subjects.


###  Features Implemented ####

   Flask-based REST API.

   PostgreSQL database connection using psycopg2.

   Pagination support (25 books per request).

   Books sorted by download count (most popular first).

   Aggregation of multiple authors, languages, and subjects per book.

   JSON formatted response.


   ################################################################################################################################
   Run the Application   :   python app.py

   Flask server will start on:   http://127.0.0.1:5000/

   ###################################################################################################################################


   Sample OutPut::

   [
  {
    "authors": [],
    "id": 54859,
    "languages": [],
    "subjects": [],
    "title": "Piccole anime"
  },
  {
    "authors": [],
    "id": 1,
    "languages": [],
    "subjects": [],
    "title": null
  },
  {
    "authors": [
      "Austen, Jane"
    ],
    "id": 1343,
    "languages": [
      "en"
    ],
    "subjects": [
      "Domestic fiction",
      "Love stories",
      "Courtship -- Fiction",
      "Social classes -- Fiction",
      "Sisters -- Fiction",
      "England -- Fiction",
      "Young women -- Fiction"
    ],
    "title": "Pride and Prejudice"
  },
  {
    "authors": [
      "Twain, Mark"
    ],
    "id": 75,
    "languages": [
      "en"
    ],
    "subjects": [
      "Boys -- Fiction",
      "Sawyer, Tom (Fictitious character) -- Fiction",
      "Child witnesses -- Fiction",
      "Humorous stories",
      "Bildungsromans",
      "Male friendship -- Fiction",
      "Missouri -- Fiction",
      "Runaway children -- Fiction",
      "Mississippi River Valley -- Fiction",
      "Adventure stories"
    ],
    "title": "The Adventures of Tom Sawyer"
  },
  {
    "authors": [
      "Carroll, Lewis"
    ],
    "id": 12,
    "languages": [
      "en"
    ],
    "subjects": [
      "Fantasy literature"
    ],
    "title": "Alice's Adventures in Wonderland"
  },
  {
    "authors": [
      "Dickens, Charles"
    ],
    "id": 99,
    "languages": [
      "en"
    ],
    "subjects": [
      "Paris (France) -- History -- 1789-1799 -- Fiction",
      "Historical fiction",
      "Lookalikes -- Fiction",
      "Executions and executioners -- Fiction",
      "British -- France -- Paris -- Fiction"
    ],
    "title": "A Tale of Two Cities"
  }
]
