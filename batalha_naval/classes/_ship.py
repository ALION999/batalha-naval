from dataclasses import dataclass, field


@dataclass
class Navio:
    """Classe que representa um navio no jogo Batalha Naval."""
    nome: str = field(init=False) # nome do navio é definido no __post_init__
    tamanho: int
    coords: list[tuple[int, int]]
    posicoes_atingidas: list[tuple[int, int]] = field(default_factory=list)
    
    def __post_init__(self):
        """Define o nome do navio baseado no seu tamanho."""
        if self.tamanho == 5:
            self.nome = "Carrier"
        elif self.tamanho == 4:
            self.nome = "Battleship"
        elif self.tamanho == 3:
            self.nome = "Cruiser"
        elif self.tamanho == 3:
            self.nome = "Destroyer"
        elif self.tamanho == 2:
            self.nome = "Submarine"
        else:
            raise ValueError("Tamanho do navio inválido")


    def __str__(self):
        return f"Navio(tamanho={self.tamanho}, coords={self.coords}, posicoes_atingidas={self.posicoes_atingidas})"
