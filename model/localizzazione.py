from dataclasses import dataclass
@dataclass
class Localizzazione:
    id_gene:int
    localizzazione:str

    def __str__(self):
        f'{self.localizzazione}: {self.id_gene}'
    def __hash__(self):
        return hash(self.id_gene)
    def __eq__(self, other):
        return self.id_gene == other.id_gene
