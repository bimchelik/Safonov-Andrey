volume_disk_Mbit = 1.44
pages = 100
lines = 50
symbols = 25
size_symbol_byte = 4

volume_disk_byte = volume_disk_Mbit * 1024 * 1024
size_book_byte = size_symbol_byte * symbols * lines * pages

print("Количество книг, помещающихся на дискету:", int((volume_disk_byte/size_book_byte) // 1))