
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

1. Run the script:
   ```sh
   python SQL_POST_EXT.py
   ```

2. Enter your MySQL User when prompted.
   
   ![Screenshot from 2024-04-15 00-49-11](https://github.com/offseckalki/WordPressArticleExtractor/assets/61248381/dbd73c0b-a319-4ad4-a4b3-e0cbff77d8b7)

3. Enter your MySQL Password when prompted.
   ![Screenshot from 2024-04-15 00-49-42](https://github.com/offseckalki/WordPressArticleExtractor/assets/61248381/fff04ce6-ab87-4ce4-9c82-2e856b7367d3)

4. Enter your MySQL Database_Name when prompted.
   ![Screenshot from 2024-04-15 00-49-58](https://github.com/offseckalki/WordPressArticleExtractor/assets/61248381/2ef3f24e-b9cf-4560-8641-44692cbede28)

5. The script will extract articles from the database and save each article as a separate text file in the current directory.
   ![Screenshot from 2024-04-15 00-50-38](https://github.com/offseckalki/WordPressArticleExtractor/assets/61248381/6263bec8-a4a9-43d9-9400-6be1d98aa0a0)


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

