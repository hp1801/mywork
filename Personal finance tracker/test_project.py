import pytest
import pandas as pd
import sys
import io
from project import add_income, add_expense,balance

def test_add_income(monkeypatch):
    inputs = ["2022-01-01", "Salary", "Monthly salary", "1000"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    add_income()
    sys.stdout = sys.__stdout__
    assert "Data successfully added\n"in capturedOutput.getvalue()

def test_add_expense(monkeypatch):
    inputs = ["2022-01-01", "Rent", "Monthly rent", "500"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    add_expense()
    sys.stdout = sys.__stdout__
    assert "Data successfully added\n" in capturedOutput.getvalue()

def test_balance():
    file_name = [{"Type": "Income", "Amount": 1000}, {"Type": "Expense", "Amount": 500},
                 {"Type": "Income", "Amount": 2000}, {"Type": "Expense", "Amount": 300}]
    import project
    project.file_name = pd.DataFrame(file_name)
    sys.stdout = io.StringIO()
    project.balance()
    output = sys.stdout.getvalue()
    assert 'Balance:2200.00\nAverage income:1500.00\nAverage expense:400.00\n\n' in output

    sys.stdout = sys.__stdout__
