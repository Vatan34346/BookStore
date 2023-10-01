# this queries are for dummy data. To create initial data in newly created db.
table_queries = {
    'create_user_table': '''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL
        )
    ''',
    'create_authors_table': '''
        CREATE TABLE IF NOT EXISTS Authors (
            id INTEGER PRIMARY KEY,
            author_name TEXT UNIQUE NOT NULL
        )
    ''',
    'create_genres_table': '''
        CREATE TABLE IF NOT EXISTS Genres (
            id INTEGER PRIMARY KEY,
            genre_name TEXT UNIQUE NOT NULL
        )
    ''',
    'create_conditions_table': '''
        CREATE TABLE IF NOT EXISTS Conditions (
            id INTEGER PRIMARY KEY,
            condition_name TEXT UNIQUE NOT NULL
        )
    ''',
    'create_retrieval_info_table': '''
        CREATE TABLE IF NOT EXISTS Contacts (
            id INTEGER PRIMARY KEY,
            address TEXT UNIQUE NOT NULL,
            phone TEXT UNIQUE,
            coordinates TEXT
        )
    ''',
    'create_books_table': '''
        CREATE TABLE IF NOT EXISTS Books (
            id INTEGER PRIMARY KEY,
            book_title TEXT NOT NULL,
            book_description TEXT NOT NULL,
            authors_id INTEGER,
            genres_id INTEGER,
            conditions_id INTEGER,
            contacts_id INTEGER,
            users_id INTEGER,
            listOfInterestedUsers TEXT,
            FOREIGN KEY (authors_id) REFERENCES Authors (id),
            FOREIGN KEY (genres_id) REFERENCES Genres (id),
            FOREIGN KEY (conditions_id) REFERENCES Conditions (id),
            FOREIGN KEY (contacts_id) REFERENCES RetrievalInformation (id),
            FOREIGN KEY (users_id) REFERENCES User (id)
        )
    '''
}
