usage: n_puzzle.py [-h] [--algorithm {a,ida}]
                   [--heuristic {misplacedTiles,manhattan,linearConflicts}]

N-puzzle solver using A* or IDA algorithm

optional arguments:
  -h, --help            show this help message and exit
  --algorithm {a,ida}   Specify the algorithm to solve the puzzle between A*
                        and IDA*
  --heuristic {misplacedTiles,manhattan,linearConflicts}
                        Specify the heuristic used
