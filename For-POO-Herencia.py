class medio:
    def __init__(self,formato,idioma,NumeroHojas,autor,editorial):
        self.formato=formato
        self.idioma=idioma
        self.NumeroHojas=NumeroHojas
        self.autor=autor
        self.editorial=editorial

    def __str__(self):
        return f"FORMATO:\t {self.formato}\n" \
               f"IDIOMA:\t {self.idioma}\n" \
               f"NUMERO DE PAGINAS:\t {self.NumeroHojas}\n" \
               f"AUTOR:\t {self.autor}\n" \
               f"EDITORIAL:\t {self.editorial}\n"


class Comic(medio):
    artista = ""
    Casaeditorial = ""

    def __str__(self):
        return f"FORMATO:\t {self.formato}\n" \
               f"IDIOMA:\t {self.idioma}\n" \
               f"NUMERO DE PAGINAS\t {self.NumeroHojas}\n" \
               f"AUTOR:\t {self.autor}\n" \
               f"EDITORIAL:\t {self.editorial}\n" \
               f"ARTISTA:\t {self.artista}\n" \
               f"CASA EDITORIAL:\t {self.Casaeditorial}\n"


class Manga(medio):
    mangaka = ""

    def __str__(self):
        return f"FORMATO:\t {self.formato}\n" \
               f"IDIOMA:\t {self.idioma}\n" \
               f"NUMERO DE PAGINAS:\t {self.NumeroHojas}\n" \
               f"AUTOR:\t {self.autor}\n" \
               f"EDITORIAL:\t {self.editorial}\n" \
               f"MANGAKA:\t {self.mangaka}\n" \



class Libro(medio):
    editor = ""
    serie  = ""

    def __str__(self):
        return f"FORMATO:\t {self.formato}\n" \
               f"IDIOMA:\t {self.idioma}\n" \
               f"NUMERO DE PAGINAS:\t {self.NumeroHojas}\n" \
               f"AUTOR:\t {self.autor}\n" \
               f"EDITORIAL:\t {self.editorial}\n" \
               f"EDITOR:\t {self.editor}\n" \
               f"SERIE:\t {self.serie}\n"




comic = Comic("Escrito", "Español", 24, "Charles Soule", "Smash")
comic.artista = "Jim Lee"
comic.Casaeditorial = "Marvel"
print(comic)

manga = Manga("Escrito", "Japones", 224, "ONE", "Shonen Jump")
manga.mangaka = "Hiroyuki Takei"
print(manga)

libro = Libro("Escrito", "Español", 457, "J.K Rowling", "Planeta")
libro.editor = "Salinger"
libro.serie = "Harry Potter"
print(libro)

material = [comic, libro, manga]
for mater in material:
    print(mater, "\n")