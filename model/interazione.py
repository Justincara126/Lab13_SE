from dataclasses import dataclass
@dataclass
class Interazione:
    id_gene1:int
    id_gene2:int
    tipo:str
    correlazione:float

    def __str__(self):
        return f"{self.id_gene1} {self.id_gene2}:     {self.tipo} {self.correlazione}"