def print_book_info(title, author=None, year=None):
    #  Write your code here
    info = f'"{title}"'
    has_author = author is not None and author != ""
    has_year = year is not None and year != ""

    if has_author or has_year:
        info += " was written"
    if has_author:
        info += f" by {author}"
    if has_year:
        info += f" in {year}"

    print(info)
