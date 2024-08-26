from src.models.Assunto import Assunto


class Favorito:
    def __init__(self, nome: str, url: str, assunto_id: int, assunto: Assunto | None = None, id = 0) -> None:
        self._nome = nome
        self._url = url
        self._assunto_id = assunto_id
        self._assunto = assunto
        self._id = id
    
    
    @property
    def nome(self) -> str:
        return self._nome
    

    @property
    def url(self) -> str:
        return self._url
    
    
    @property
    def assunto_id(self) -> int:
        return self._assunto_id
    
    
    @property
    def assunto(self) -> Assunto | None:
        return self._assunto
    
    
    @property
    def id(self) -> int:
        return self._id