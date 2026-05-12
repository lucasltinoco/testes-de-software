Aula 1 - OK
Aula 2 - TBD
cd /home/lucasltinoco/workspace/testes-de-software/aula2/src
./test.sh
Aula 3 - TBD
cd /home/lucasltinoco/workspace/testes-de-software/aula3/EightPuzzleGame-Python/EightPuzzle
PYTHONPATH=src:tests coverage run --branch -m unittest tests.TestPuzzleGame
coverage report
coverage html
Aula 4 - TBD
cd /home/lucasltinoco/workspace/testes-de-software/aula3/EightPuzzleGame-Python/EightPuzzle
PYTHONPATH=src:tests coverage run --branch -m unittest tests.TestPuzzleGame
coverage report
coverage html
Aula 5 - OK
Aula 6 - TBD
cd /home/lucasltinoco/workspace/testes-de-software/aula6/EightPuzzle/src
PYTHONPATH="$PYTHONPATH:$PWD" python3 ../tests/test_puzzlegame.py 
PYTHONPATH="$PYTHONPATH:$PWD" python3 ../tests/test_puzzlegame_with_mock.py 
