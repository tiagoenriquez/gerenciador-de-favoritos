class Assunto:
    def __init__(self, nome: str, id = 0) -> None:
        self._nome = nome
        self._id = id
    
    
    @property
    def nome(self) -> str:
        return self._nome
    
    
    @property
    def id(self) -> int:
        return self._id