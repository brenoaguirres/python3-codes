# bool type
done = True  # or False

if done:
    print("yes")
else:
    print("No")

# number -> 0 - False ;; Any number - True
# string, list, sets, tuples, dicts -> if empty then False, else True

print(type(done) == bool)

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
read_all_books = all([book_1_read, book_2_read])
print(read_any_book)
print(read_all_books)


