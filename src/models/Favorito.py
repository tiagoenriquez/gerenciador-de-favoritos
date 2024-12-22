class Favorito:
    def __init__(self, nome: str, url: str, id: int | None = None):
        self.nome = nome
        self.url = url
        self.id = id
    
    def data_inserted(self):
        return [self.nome, self.url]
    
    def data_updated(self):
        return [self.nome, self.url, self.id]