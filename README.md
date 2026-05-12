# README

- [x] Aula 1

- [x] Aula 2

```sh
cd /home/lucasltinoco/workspace/testes-de-software/aula2/src
./test.sh
```

- [x] Aula 3

```sh
cd /home/lucasltinoco/workspace/testes-de-software/aula3/EightPuzzleGame-Python/EightPuzzle
PYTHONPATH=src:tests coverage run --branch -m unittest tests.TestPuzzleGame
coverage report
coverage html
```

- [x] Aula 4

```sh
cd /home/lucasltinoco/workspace/testes-de-software/aula3/EightPuzzleGame-Python/EightPuzzle
PYTHONPATH=src:tests coverage run --branch -m unittest tests.TestPuzzleGame
coverage report
coverage html
```

- [x] Aula 5

- [x] Aula 6

```sh
cd /home/lucasltinoco/workspace/testes-de-software/aula6/EightPuzzle/src
PYTHONPATH="$PYTHONPATH:$PWD" python3 ../tests/test_puzzlegame.py
PYTHONPATH="$PYTHONPATH:$PWD" python3 ../tests/test_puzzlegame_with_mock.py 
```
