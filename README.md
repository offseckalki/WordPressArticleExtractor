# WordPressArticleExtractor
MySQL Article Extractor

This Python script is a tool designed to extract articles from a MySQL database, particularly from a WordPress installation, and save each article in plain text format to individual text files. It can be useful for tasks such as content analysis, data migration, or archiving blog posts.
Features:

    Connects to a MySQL database to retrieve articles stored in the wp_posts table.
    Extracts articles with the post type 'post' and status 'publish'.
    Converts HTML content of articles to plain text using BeautifulSoup.
    Saves each article as a separate text file named with the format article_{post_id}.txt.

Requirements:

    Python 3.x
    MySQL Connector/Python
    BeautifulSoup4

Usage:

    Install the required Python packages:

pip install mysql-connector-python beautifulsoup4

Modify the db_config dictionary in the script to match your MySQL database configuration.

Run the script:

python SQL_POST_EXT.py

Enter your MySQL password when prompted.

The script will extract articles from the database and save each article as a separate text file in the current directory.
