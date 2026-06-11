import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "main",
    Path(__file__).resolve().parent.parent / "main.py",
)
modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulo)


def test_mensagem_futuro():
    mensagem = modulo.mensagem_futuro("Ana", 20)
    assert mensagem == "Olá, Ana daqui 5 anos você tera 25 anos de idade"
