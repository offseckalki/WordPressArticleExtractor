print("""
          __    __                       _              _   _      _  
  ___    / _|  / _|  ___    ___    ___  | | __   __ _  | | | | __ (_) 
 / _ \  | |_  | |_  / __|  / _ \  / __| | |/ /  / _` | | | | |/ / | | 
| (_) | |  _| |  _| \__ \ |  __/ | (__  |   <  | (_| | | | |   <  | | 
 \___/  |_|   |_|   |___/  \___|  \___| |_|\_\  \__,_| |_| |_|\_\ |_| 
                                                                      
""")
import mysql.connector 
from getpass import getpass
from bs4 import BeautifulSoup
import os

# Function to get MySQL username and database name from user input
def get_mysql_credentials():
    username = input("Enter the MySQL username: ")
    database = input("Enter the MySQL database name: ")
    return username, database

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': '',
    'database': ''
}

def connect_to_database():
    try:
        # Get MySQL username and database name from user input
        username, database = get_mysql_credentials()
        password = getpass("Enter the MySQL password: ")
        
        db_config['user'] = username
        db_config['password'] = password 
        db_config['database'] = database
        
        # Connect to MySQL database
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def extract_articles(conn):
    try:
        cursor = conn.cursor()

        # Query to retrieve post title and content from wp_posts table
        query = "SELECT ID, post_title, post_content FROM wp_posts WHERE post_type = 'post' AND post_status = 'publish';"
        cursor.execute(query)

        articles = []
        for (post_id, post_title, post_content) in cursor:
            articles.append((post_id, post_title, post_content))

        cursor.close()
        return articles
    except mysql.connector.Error as e:
        print(f"Error retrieving articles: {e}")
        return []

def convert_to_plain_text(html_content):
    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract plain text
    return soup.get_text()

def save_article_to_file(post_id, post_title, plain_text):
    file_name = f"{post_title}.txt"
    with open(file_name, "w") as file:
        file.write(plain_text)
    print(f"Article {post_title} saved to {file_name}")

def main():
    # Connect to MySQL database
    conn = connect_to_database()
    if conn is None:
        return

    # Extract articles from the database
    articles = extract_articles(conn)

    # Convert HTML content to plain text and save each article to a file
    for post_id, post_title, article_content in articles:
        plain_text = convert_to_plain_text(article_content)
        save_article_to_file(post_id, post_title, plain_text)

    # Close database connection
    conn.close()

if __name__ == "__main__":
    main()
