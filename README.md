```
	usage: n_puzzle.py [-h] [-a {a,ida}]
	                   [--heuristic {misplacedTiles,manhattan,linearConflicts}]
	                   [-s {heuristic,greedy,uniform}] [-g {fill,snake}]
	
	N-puzzle solver using A* or IDA algorithm
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -a {a,ida}, --algorithm {a,ida}
	                        Specify the algorithm to solve the puzzle between A*
	                        and IDA*
	  --heuristic {misplacedTiles,manhattan,linearConflicts}
	                        Specify the heuristic used
	  -s {heuristic,greedy,uniform}, --search {heuristic,greedy,uniform}
	                        Specify the searching logic
	  -g {fill,snake}, --goal {fill,snake}
	                        Specify the goal state
```
