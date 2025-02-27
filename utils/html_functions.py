#html_functions.py
"""functions commonly used in html files"""

from bs4 import BeautifulSoup

def get_title_from_html(html_file):
    """get a title from an html file"""
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        title = soup.title.string if soup.title else 'output'
        return title.strip().replace(' ', '_') + '.pdf'

    # End-of-file (EOF)
