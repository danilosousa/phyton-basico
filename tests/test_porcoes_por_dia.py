import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "porcoes_por_dia",
    Path(__file__).resolve().parent.parent / "porcoes-por-dia.py",
)
modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulo)


def test_calcular_porcoes_por_dia():
    resultado = modulo.calcular_porcoes_por_dia(30, 10)
    assert resultado == 3
