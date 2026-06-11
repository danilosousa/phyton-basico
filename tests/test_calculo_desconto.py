import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "calculo_desconto",
    Path(__file__).resolve().parent.parent / "calculo-desconto.py",
)
modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulo)


def test_calcular_desconto_padrao():
    desconto, preco_final = modulo.calcular_desconto(100)
    assert desconto == 10
    assert preco_final == 90


def test_calcular_desconto_taxa_customizada():
    desconto, preco_final = modulo.calcular_desconto(200, taxa=0.25)
    assert desconto == 50
    assert preco_final == 150
