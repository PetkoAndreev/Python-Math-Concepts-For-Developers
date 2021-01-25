book_input = input()
counter = 0

while True:
    target_book = input()
    if target_book == book_input:
        print(f'You checked {counter} books and found it.')
        break
    if target_book == 'No More Books':
        print(f'The book you search is not here!\nYou checked {counter} books.')
        break
    counter += 1