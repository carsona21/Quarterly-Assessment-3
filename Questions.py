import sqlite3

conn = sqlite3.connect('qa_database.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store questions and answers with the name BMGT3510
cursor.execute('''
CREATE TABLE IF NOT EXISTS ACCT2110 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

def insert_qa(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO ACCT2110 (question, answer) VALUES (?, ?)
    ''', (question, f"A. {option_a}\nB. {option_b}\nC. {option_c}\nD. {option_d}\nCorrect Answer: {correct_answer}"))
    conn.commit()

# List of questions (assuming this list has been defined as shown earlier)
questions = [
    ("Which financial statement summarizes a company's assets, liabilities, and equity at a specific point in time?", 
     "Income Statement", "Balance Sheet", "Statement of Cash Flows", "Statement of Retained Earnings", "B"),
    
    ("What is the accounting equation?", 
     "Assets = Liabilities + Revenue", "Assets = Liabilities + Expenses", "Assets = Liabilities + Equity", "Assets = Liabilities - Equity", "C"),
    
    ("Which of the following accounts increases with a debit?", 
     "Revenue", "Liabilities", "Assets", "Common Stock", "C"),
    
    ("What type of account is 'Accounts Payable'?", 
     "Asset", "Liability", "Equity", "Revenue", "B"),
    
    ("Depreciation is recorded to allocate the cost of a fixed asset over:", 
     "Its fair market value", "Its useful life", "A fiscal quarter", "None of the above", "B"),
    
    ("Which financial statement reports a company's revenues and expenses over a period of time?", 
     "Balance Sheet", "Income Statement", "Statement of Cash Flows", "Statement of Changes in Equity", "B"),
    
    ("Which account would typically be debited when paying for office supplies with cash?", 
     "Cash", "Accounts Receivable", "Office Supplies Expense", "Revenue", "C"),
    
    ("The process of recording business transactions in a systematic manner is called:", 
     "Budgeting", "Auditing", "Bookkeeping", "Financial Planning", "C"),
    
    ("What does GAAP stand for?", 
     "Generally Acknowledged Accounting Practices", "Global Accounting Application Protocol", "Generally Accepted Accounting Principles", "Government Approved Accounting Procedures", "C"),
    
    ("Which of the following is considered an asset?", 
     "Accounts Payable", "Inventory", "Retained Earnings", "Revenue", "B")
]


# Inserting questions into the table
for question in questions:
    insert_qa(*question)

# Function to retrieve all questions and answers
def get_all_qa():
    cursor.execute('SELECT * FROM BMGT3510')
    return cursor.fetchall()

# Fetch and print all questions and answers
qa_list = get_all_qa()
for qa in qa_list:
    print(f'ID: {qa[0]}, Question: {qa[1]}, Answer: {qa[2]}')

# Close the connection
conn.close()


# Fetch and print all questions and answers
qa_list = get_all_qa()
for qa in qa_list:
    print(f'ID: {qa[0]}, Question: {qa[1]}, Answer: {qa[2]}')

# Close the connection
conn.close()


import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('qa_database.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store questions and answers with the name BMGT3510
cursor.execute('''
CREATE TABLE IF NOT EXISTS BMGT3510 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# Function to insert a new question and answer
def insert_qa(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO BMGT3510 (question, answer) VALUES (?, ?)
    ''', (question, f"A. {option_a}\nB. {option_b}\nC. {option_c}\nD. {option_d}\nCorrect Answer: {correct_answer}"))
    conn.commit()

# List of questions for BMGT3510
questions = [
    ("What is the primary purpose of strategic management in an organization?", 
     "Managing short-term financial goals", "Setting and achieving long-term objectives", "Maximizing daily productivity", "Developing marketing plans", "B"),
    
    ("Which of the following best defines organizational leadership?", 
     "The ability to manage and control operations", "Influencing and guiding individuals and teams to achieve goals", "Handling payroll and human resources", "Overseeing sales performance", "B"),
    
    ("What does a SWOT analysis evaluate?", 
     "Key stakeholders and operations", "Internal strengths and weaknesses, and external opportunities and threats", "Sales and revenue trends", "Employee performance metrics", "B"),
    
    ("Which of these is a common type of organizational structure?", 
     "Linear", "Matrix", "Profit-driven", "Functional-expansion", "B"),
    
    ("In decision-making, what is considered a 'constraint'?", 
     "A marketing tactic", "A limitation or restriction", "An opportunity for growth", "A variable input", "B"),
    
    ("What role do managers play in motivating employees?", 
     "Reducing salaries", "Providing guidance, incentives, and creating a positive work environment", "Evaluating personal values", "None of the above", "B"),
    
    ("Which of the following is a part of strategic planning?", 
     "Daily task allocation", "Setting vision, mission, and defining strategic goals", "Inventory management", "Salary negotiations", "B"),
    
    ("How is organizational culture best described?", 
     "The process of creating a new product", "Shared values, norms, and practices within an organization", "Daily operational targets", "Financial targets", "B"),
    
    ("Effective communication within an organization leads to:", 
     "More confusion", "Increased productivity, better teamwork, and reduced conflicts", "Loss of focus", "Less motivation", "B"),
    
    ("What is an example of transformational leadership?", 
     "Issuing direct commands", "Inspiring employees through vision and creating change", "Monitoring only tasks", "Offering no feedback", "B")
]

# Inserting questions into the table
for question in questions:
    insert_qa(*question)

# Function to retrieve all questions and answers
def get_all_qa():
    cursor.execute('SELECT * FROM BMGT3510')
    return cursor.fetchall()

# Fetch and print all questions and answers
qa_list = get_all_qa()
for qa in qa_list:
    print(f'ID: {qa[0]}, Question: {qa[1]}, Answer: {qa[2]}')

# Close the connection
conn.close()
