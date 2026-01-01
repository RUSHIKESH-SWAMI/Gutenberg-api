from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="gutenberg",
        user="rushikesh",
        password="1234r"
    )

@app.route("/")
def home():
    return "API is running"

@app.route("/books")
def books():
    page = int(request.args.get("page", 1))
    limit = 25
    offset = (page - 1) * limit

    conn = get_db_connection()
    cur = conn.cursor()

    query = """
    SELECT
        b.id,
        b.title,
        a.name,
        l.code,
        s.name
    FROM books_book b
    LEFT JOIN books_book_authors ba ON b.id = ba.book_id
    LEFT JOIN books_author a ON ba.author_id = a.id
    LEFT JOIN books_book_languages bl ON b.id = bl.book_id
    LEFT JOIN books_language l ON bl.language_id = l.id
    LEFT JOIN books_book_subjects bs ON b.id = bs.book_id
    LEFT JOIN books_subject s ON bs.subject_id = s.id
    ORDER BY b.download_count DESC
    LIMIT %s OFFSET %s;
    """

    cur.execute(query, (limit, offset))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    books = {}

    for book_id, title, author, language, subject in rows:
        if book_id not in books:
            books[book_id] = {
                "id": book_id,
                "title": title,
                "authors": [],
                "languages": [],
                "subjects": []
            }

        if author and author not in books[book_id]["authors"]:
            books[book_id]["authors"].append(author)

        if language and language not in books[book_id]["languages"]:
            books[book_id]["languages"].append(language)

        if subject and subject not in books[book_id]["subjects"]:
            books[book_id]["subjects"].append(subject)

    return jsonify(list(books.values()))

if __name__ == "__main__":
    app.run(debug=True)
