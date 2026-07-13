from dataclasses import dataclass, asdict


@dataclass
class Tarefa:
    id: int
    titulo: str
    descricao: str
    prioridade: str
    status: str = "Pendente"

    def to_dict(self):
        return asdict(self)
