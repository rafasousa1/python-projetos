import pyshorteners

url_grande = input("Digite o link aqui: ")
type_tiny = pyshorteners.Shortener()
url_curta = type_tiny.tinyurl.short(url_grande)
print(f"URL reduzida: {url_curta}")