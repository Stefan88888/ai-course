books = [
    {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
    {"title": "Farrenheit 451", "author": "Ray Bradbury", "year": 1953},
    {"title": "The picture of Dorian Grey", "author": "Oskar White", "year": 1891}
]

after = 0

for book in books:
    print(book["title"], "was written by", book["author"], "in", book["year"])
    print(f"{book['title']} by {book['author']}({book['year']})")
    if book["year"] > 1950:
        after += 1
print(after)