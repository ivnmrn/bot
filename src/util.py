def beautifier_help():
    result = "🐯<b>Available commands: 🐯</b>\n\n •/fox \n •/nasa \n •/g + [text]\n •/zelda + [item]"
    return result


def beautifier_material(user, item):
    result = (f"🍜<b>{user}</b>🍜(<a href='{item['url']}'>{user}</a>)\n"
              f"\nCategoria: {item['Categoria']}\n"
              f"Rec. PE: {item['Rec. PE']}\n"
              f"Grado potencia: {item['Grado potencia']}\n"
              f"Duracion: {item['Duracion']}\n"
              f"Ubicacion: {item['Ubicacion']}")
    return result


def beautifier_nasa(r):
    result = f"🛰<b>{r['title']}</b>🛰(<a href='{r['url']}'>{r['date']}</a>) \n{r['explanation']}"
    return result
