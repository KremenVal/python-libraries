import pandas as pd


authors = pd.DataFrame({
    'author_id': [1, 2, 3],
    'author_name': ['Тургенев', 'Чехов', 'Островский'],
})
book = pd.DataFrame({
    'author_id': [1, 1, 1, 2, 2, 3, 3],
    'book_title': [
        'Отцы и дети',
        'Рудин',
        'Дворянское гнездо',
        'Толстый и тонкий',
        'Дама с собачкой',
        'Гроза',
        'Таланты и поклонники'
    ],
    'price': [450, 300, 350, 500, 450, 370, 290],
})
print(authors)
print(book)
