def beautifier_help():
    result = "🐯<b>Available commands: 🐯</b>\n\n •/fox \n •/nasa \n •/g + [text]\n •/zelda + [item]"
    return result


def beautifier_material(user, item):
    result = (f"<b>{user}</b>"
              f"\nCategoria: {item['Categoria']}\n"
              f"Rec. PE: {item['Rec. PE']}\n"
              f"Grado potencia: {item['Grado potencia']}\n"
              f"Duracion: {item['Duracion']}\n"
              f"Ubicacion: {item['Ubicacion']}\n"
              f"<a href='{item['url']}'>Image</a>")
    return result


def beautifier_notfound():
    result = "I don't know this item... 🐯\n(write <b>/list</b> to display the full list)\n " \
             "<a href='https://www.zeldaeurope.de/galerie/albums/userpics/10003/normal_tfh_icon_confused.jpg'>Image</a>"
    return result


def beautifier_nasa(r):
    result = f"🛰<b>{r['title']}</b>🛰(<a href='{r['url']}'>{r['date']}</a>) \n{r['explanation']}"
    return result
