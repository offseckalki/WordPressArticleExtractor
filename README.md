
# WordPress Article Extractor

## Description

WordPress Article Extractor is a Python script designed to extract articles from a MySQL database, particularly from a WordPress installation. It saves each article in plain text format to individual text files, which can be useful for tasks such as content analysis, data migration, or archiving blog posts.

## Features

- Connects to a MySQL database to retrieve articles stored in the `wp_posts` table.
- Extracts articles with the post type 'post' and status 'publish'.
- Converts HTML content of articles to plain text using BeautifulSoup.
- Saves each article as a separate text file named with the format `article_{post_id}.txt`.

## Requirements

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL Connector/Python](https://dev.mysql.com/downloads/connector/python/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install MySQL Connector/Python and BeautifulSoup4 using pip:
   ```sh
   pip install mysql-connector-python beautifulsoup4
   ```

## Usage

1. Modify the `db_config` dictionary in the script to match your MySQL database configuration.

2. Run the script:
   ```sh
   python SQL_POST_EXT.py
   ```

3. Enter your MySQL password when prompted.

4. The script will extract articles from the database and save each article as a separate text file in the current directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

