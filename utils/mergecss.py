#mergecss.py
"""Merge a CSS page into an HTML page"""

def merge_css_into_html(css_file, html_file, output_file):
    """Merge a CSS page into an HTML Page"""
    # Read the CSS content
    with open(css_file, 'r', encoding="any") as css:
        css_content = css.read()

    # Read the HTML content
    with open(html_file, 'r', encoding="any") as html:
        html_content = html.read()

    # Find the position to insert the CSS content
    head_end_index = html_content.find('</head>')

    # Create the new HTML content with embedded CSS
    new_html_content = (
        html_content[:head_end_index] +
        '<style>\n' + css_content + '\n</style>\n' +
        html_content[head_end_index:]
    )

    # Write the new HTML content to the output file
    with open(output_file, 'w', encoding="any") as output:
        output.write(new_html_content)

# Example usage
merge_css_into_html('style.css', 'view.html', 'merged_view.html')
# End-of-file (EOF)
