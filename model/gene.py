from dataclasses import dataclass
@dataclass
class Gene:
    id:str
    funzione:str
    essenziale:str
    cromosoma:int
    def __str__(self):
        f'{self.id}:{self.funzione}:{self.essenziale}'
    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        return self.id == other.id
