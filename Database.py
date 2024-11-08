import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('qa_database.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS qa_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# Function to insert a new question and answer
def insert_qa(question, answer):
    cursor.execute('''
    INSERT INTO qa_table (question, answer) VALUES (?, ?)
    ''', (question, answer))
    conn.commit()

# Function to retrieve all questions and answers
def get_all_qa():
    cursor.execute('SELECT * FROM qa_table')
    return cursor.fetchall()


# Fetch and print all questions and answers
qa_list = get_all_qa()
for qa in qa_list:
    print(f'ID: {qa[0]}, Question: {qa[1]}, Answer: {qa[2]}')

# Close the connection
conn.close()

import sqlite3

def read_database(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Retrieve all table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Print all tables
    print("Tables in the database:")
    for idx, table in enumerate(tables):
        print(f"{idx + 1}. {table[0]}")
    
    # Ask the user to select a table
    table_index = int(input("Enter the number of the table you want to view: ")) - 1
    selected_table = tables[table_index][0]
    
    # Retrieve and print all data from the selected table
    print(f"\nData from table '{selected_table}':")
    cursor.execute(f"SELECT * FROM {selected_table}")
    rows = cursor.fetchall()
    
    # Print column headers
    column_names = [description[0] for description in cursor.description]
    print("\t".join(column_names))
    
    # Print each row of data
    for row in rows:
        print("\t".join(str(cell) for cell in row))
    
    # Close the connection
    conn.close()

# Call the function and specify the database file name
read_database('qa_questions.db')
