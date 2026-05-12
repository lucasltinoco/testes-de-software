#!/bin/bash

PYTHONPATH="$PYTHONPATH:$PWD" python3 ../tests/TestAgencia.py
PYTHONPATH="$PYTHONPATH:$PWD" python3 ../tests/TestBanco.py
PYTHONPATH="$PYTHONPATH:$PWD" python3 ../tests/TestConta.py
PYTHONPATH="$PYTHONPATH:$PWD" python3 ../tests/TestDinheiro.py
PYTHONPATH="$PYTHONPATH:$PWD" python3 ../tests/TestSistemaBancario.py
PYTHONPATH="$PYTHONPATH:$PWD" python3 ../tests/TestValorMonetario.py