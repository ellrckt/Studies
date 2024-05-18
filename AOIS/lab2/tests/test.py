import pytest
from lab.main import TruthTable

@pytest.fixture
def expression():
    return "(a|b)&(!c)"

def test_evaluate(expression):
    table = TruthTable(expression)
    assert table.evaluate([0, 0, 0]) == 0
    assert table.evaluate([0, 0, 1]) == 0
    assert table.evaluate([0, 1, 0]) == 1
    assert table.evaluate([0, 1, 1]) == 0
    assert table.evaluate([1, 0, 0]) == 1
    assert table.evaluate([1, 0, 1]) == 0
    assert table.evaluate([1, 1, 0]) == 1
    assert table.evaluate([1, 1, 1]) == 0

def test_sknf(expression):
    table = TruthTable(expression)
    assert table.sknf() == '(a ∨ b ∨ c) ∧ (a ∨ b ∨ (¬c)) ∧ (a ∨ (¬b) ∨ (¬c)) ∧ ((¬a) ∨ b ∨ (¬c)) ∧ ((¬a) ∨ (¬b) ∨ (¬c))'

def test_sdnf(expression):
    table = TruthTable(expression)
    assert table.sdnf() == '((¬a) ∧ b ∧ (¬c)) ∨ (a ∧ (¬b) ∧ (¬c)) ∨ (a ∧ b ∧ (¬c))'

def test_num_sknf(expression):
    table = TruthTable(expression)
    assert table.num_sknf() == [0,1,3,5, 7]

def test_num_sdnf(expression):
    table = TruthTable(expression)
    assert table.num_sdnf() == [2,4,6]

def test_ind_view(expression):
    table = TruthTable(expression)
    assert table.ind_view() == '00101010'
