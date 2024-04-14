# WordPress Article Extractor

## Description

WordPress Article Extractor is a Python script designed to extract articles from a MySQL database, particularly from a WordPress installation. It saves each article in plain text format to individual text files, which can be useful for tasks such as content analysis, data migration, or archiving blog posts.

## Features

- Connects to a MySQL database to retrieve articles stored in the `wp_posts` table.
- Extracts articles with the post type 'post' and status 'publish'.
- Converts HTML content of articles to plain text using BeautifulSoup.
- Saves each article as a separate text file named with the format `article_{post_id}.txt`.

## Requirements

- Python 3.x
- MySQL Connector/Python
- BeautifulSoup4

## Usage

1. Install the required Python packages:
   pip install mysql-connector-python beautifulsoup4


2. Modify the `db_config` dictionary in the script to match your MySQL database configuration.

3. Run the script:
   python SQL_POST_EXT.py


4. Enter your MySQL password when prompted.

5. The script will extract articles from the database and save each article as a separate text file in the current directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
