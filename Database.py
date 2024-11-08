import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('qa_database.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store questions and answers with the name ACCT2110
cursor.execute('''
CREATE TABLE IF NOT EXISTS ACCT2110 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# Function to insert a new question and answer
def insert_qa(question, answer):
    cursor.execute('''
    INSERT INTO ACCT2110 (question, answer) VALUES (?, ?)
    ''', (question, answer))
    conn.commit()

# Function to retrieve all questions and answers
def get_all_qa():
    cursor.execute('SELECT * FROM ACCT2110')
    return cursor.fetchall()

# Example usage
insert_qa('What is the capital of France?', 'Paris')
insert_qa('What is 2 + 2?', '4')

# Fetch and print all questions and answers
qa_list = get_all_qa()
for qa in qa_list:
    print(f'ID: {qa[0]}, Question: {qa[1]}, Answer: {qa[2]}')

# Close the connection
conn.close()
