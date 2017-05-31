from xml.dom import minidom

doc = minidom.parse('book.xml')
root = doc.documentElement
#print(dir(root))
#print(root.nodeName)
books = root.getElementsByTagName('book')
#print(books)
#print(type(books))
#print(books[0].childNodes[0].nodeValue)
for book in books:
    titles = book.getElementsByTagName('title')
    prices = book.getElementsByTagName('price')
    print(titles[0])
    print(type(titles[0]))
    print(titles[0].childNodes[0])
    print(type(titles[0].childNodes[0]))
    print(titles[0].childNodes[0].nodeValue)
