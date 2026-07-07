import json
import os

ARQUIVO = "data/tarefas.json"


def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON."""
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)