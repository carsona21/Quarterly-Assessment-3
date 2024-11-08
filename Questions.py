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

import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('qa_database.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store questions and answers with the name ECON4900
cursor.execute('''
CREATE TABLE IF NOT EXISTS ECON4900 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# Function to insert a new question and answer
def insert_qa(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO ECON4900 (question, answer) VALUES (?, ?)
    ''', (question, f"A. {option_a}\nB. {option_b}\nC. {option_c}\nD. {option_d}\nCorrect Answer: {correct_answer}"))
    conn.commit()

# List of questions for ECON4900
questions = [
    ("What is the definition of Gross Domestic Product (GDP)?", 
     "The total value of all goods produced by a country in a year", "The total market value of all final goods and services produced within a country in a year", "The sum of all exports minus imports", "A measure of a country's foreign investment", "B"),
    
    ("Which of the following best describes a market economy?", 
     "An economy controlled entirely by the government", "An economy where supply and demand determine prices", "An economy based on barter and trade", "An economy with a fixed currency value", "B"),
    
    ("What does the law of demand state?", 
     "As the price of a good decreases, quantity demanded decreases", "As the price of a good increases, quantity demanded decreases", "Demand is always constant", "The relationship between supply and demand is fixed", "B"),
    
    ("What is opportunity cost?", 
     "The financial cost of a product", "The benefits of the next best alternative forgone when making a decision", "A cost incurred by all decisions", "A tax levied on trade", "B"),
    
    ("Which of the following is an example of a public good?", 
     "National defense", "A new car", "Private tutoring services", "A cup of coffee", "A"),
    
    ("What is inflation?", 
     "A decrease in the level of prices", "An increase in the overall level of prices of goods and services", "The value of a country's currency in the global market", "The level of wages over time", "B"),
    
    ("What is the purpose of fiscal policy?", 
     "To control the amount of money in circulation", "To manage the government's budget, taxes, and spending to influence the economy", "To set fixed interest rates", "To balance international trade", "B"),
    
    ("What is an example of a positive externality?", 
     "Pollution from a factory", "A person gaining knowledge from another's education", "A company losing market share", "A factory closure", "B"),
    
    ("Which of these is a characteristic of perfect competition?", 
     "One firm controls the market", "Many firms selling identical products", "Firms with significant market power", "Barriers to entry are high", "B"),
    
    ("Which economic term describes a prolonged period of declining economic activity?", 
     "Inflation", "Recession", "Depression", "Boom", "C")
]

# Inserting questions into the table
for question in questions:
    insert_qa(*question)

# Function to retrieve all questions and answers
def get_all_qa():
    cursor.execute('SELECT * FROM ECON4900')
    return cursor.fetchall()

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

# Create a table to store questions and answers with the name FIN3210
cursor.execute('''
CREATE TABLE IF NOT EXISTS FIN3210 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# Function to insert a new question and answer
def insert_qa(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO FIN3210 (question, answer) VALUES (?, ?)
    ''', (question, f"A. {option_a}\nB. {option_b}\nC. {option_c}\nD. {option_d}\nCorrect Answer: {correct_answer}"))
    conn.commit()

# List of questions for FIN3210
questions = [
    ("What is the primary goal of financial management in a corporation?", 
     "Maximizing revenue", "Maximizing shareholder wealth", "Minimizing expenses", "Maintaining market share", "B"),
    
    ("Which of the following represents a company's debt obligation?", 
     "Common stock", "Accounts payable", "Bonds", "Retained earnings", "C"),
    
    ("What is the time value of money?", 
     "Money has the same value over time", "Money loses its value over time", "The concept that money available now is worth more than the same amount in the future due to its earning capacity", "Money always appreciates over time", "C"),
    
    ("What is a bond's coupon rate?", 
     "The interest rate stated on the bond when issued", "The current market value of the bond", "The maturity date of the bond", "The risk rating of the bond", "A"),
    
    ("Which of the following best defines a stock's dividend yield?", 
     "Total dividends paid during the year divided by the price of the stock", "The annual interest earned on a bond", "The difference between stock's buying and selling price", "The tax rate on dividends", "A"),
    
    ("What is diversification in investing?", 
     "Investing in only one type of asset", "Reducing risk by investing in a variety of assets", "Maximizing returns on a single investment", "Consolidating assets in one portfolio", "B"),
    
    ("Which financial statement shows a company's financial position at a specific point in time?", 
     "Income statement", "Cash flow statement", "Balance sheet", "Statement of retained earnings", "C"),
    
    ("What does 'liquidity' refer to in finance?", 
     "A firm's ability to pay off its long-term debt", "The ease with which an asset can be converted into cash", "The profit a firm earns", "The degree of market competition", "B"),
    
    ("What is net present value (NPV)?", 
     "The sum of all cash inflows", "The difference between the present value of cash inflows and outflows over a period of time", "The interest earned on a bond", "The rate of return on equity", "B"),
    
    ("Which of the following best describes 'capital budgeting'?", 
     "Managing a company's capital structure", "The process of planning and managing a firm's long-term investments", "Issuing new stocks and bonds", "Day-to-day expense management", "B")
]

# Inserting questions into the table
for question in questions:
    insert_qa(*question)

# Function to retrieve all questions and answers
def get_all_qa():
    cursor.execute('SELECT * FROM FIN3210')
    return cursor.fetchall()

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

# Create a table to store questions and answers with the name MKT3400
cursor.execute('''
CREATE TABLE IF NOT EXISTS MKT3400 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# Function to insert a new question and answer
def insert_qa(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO MKT3400 (question, answer) VALUES (?, ?)
    ''', (question, f"A. {option_a}\nB. {option_b}\nC. {option_c}\nD. {option_d}\nCorrect Answer: {correct_answer}"))
    conn.commit()

# List of questions for MKT3400
questions = [
    ("What is the definition of marketing?", 
     "The process of creating, communicating, and delivering value to customers", "Selling products at discounted prices", "Manufacturing new products", "The process of managing supply chain logistics", "A"),
    
    ("Which of the following is considered a marketing mix element?", 
     "Price", "Customer feedback", "Company culture", "Employee salaries", "A"),
    
    ("What is market segmentation?", 
     "The process of developing new products", "Dividing a market into distinct groups of buyers with different needs or characteristics", "Setting price levels", "Promoting a single product to everyone", "B"),
    
    ("What does SWOT analysis stand for in marketing?", 
     "Standards, Weighting, Optimization, and Targets", "Sales, Work, Objectives, and Tactics", "Strengths, Weaknesses, Opportunities, and Threats", "Supply, Waste, Organization, and Training", "C"),
    
    ("Which of the following best describes a brand?", 
     "A legal term for a product", "A distinguishing name, term, design, or symbol that identifies a product or service", "The manufacturing location of a product", "An organization's profit margins", "B"),
    
    ("What is the purpose of a promotional strategy?", 
     "To manage internal operations", "To communicate and persuade target customers to purchase products", "To hire new employees", "To decrease production costs", "B"),
    
    ("Which marketing strategy focuses on satisfying the needs and wants of consumers better than competitors?", 
     "Sales-driven approach", "Product-driven approach", "Market-oriented approach", "Profit-maximization approach", "C"),
    
    ("What is 'positioning' in marketing?", 
     "Creating a product", "Establishing the image or identity of a product in the minds of the target market", "Setting price levels", "Improving supply chain logistics", "B"),
    
    ("What is consumer behavior?", 
     "The way organizations plan sales strategies", "The study of how individuals make purchasing decisions", "The process of distributing products", "Analyzing competitor strengths", "B"),
    
    ("Which of the following is a type of promotion?", 
     "Discounts and sales", "Product manufacturing", "Supply chain analysis", "Inventory management", "A")
]

# Inserting questions into the table
for question in questions:
    insert_qa(*question)

# Function to retrieve all questions and answers
def get_all_qa():
    cursor.execute('SELECT * FROM MKT3400')
    return cursor.fetchall()

# Fetch and print all questions and answers
qa_list = get_all_qa()
for qa in qa_list:
    print(f'ID: {qa[0]}, Question: {qa[1]}, Answer: {qa[2]}')

# Close the connection
conn.close()
