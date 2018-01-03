# Connect 3

- An implementation of a mini-version of the original connect 4 game using Python2 turtle graphics.

- The game playing agent is implemented using the Minimax algorithm. To achieve a substantial speedup, the Alpha-Beta node pruning algorithm is also implemented.

## Screen shot 

![alt text](https://github.com/jbnerd/connect_3/blob/master/Screenshot.png)

## Running the code

- Open the terminal and type in `python run.py` to play the game.
	- The bot plays the first move.
	- Click on the corresponding column to put your coin it.
	- Whenever one episode of the game ends, click on one of the options given below in the GUI.

## Algorithms

### Minimax

```
function MINIMAX-DECISION(state) returns an action
	return arg_max_a ∈ ACTIONS(s) MIN-VALUE(RESULT(state, a))
```

```
function MAX-VALUE(state) returns a utility value
	if TERMINAL-TEST(state) then return UTILITY(state)
	v ← −∞
	for each a in ACTIONS(state) do
		v ← MAX(v, MIN-VALUE(RESULT(s, a)))
	return v
```

```
function MIN-VALUE(state) returns a utility value
	if TERMINAL-TEST(state) then return UTILITY(state)
	v ← ∞
	for each a in ACTIONS(state) do
		v ← MIN(v, MAX-VALUE(RESULT(s, a)))
	return v
```

### Alpha-Beta Pruning

```
function ALPHA-BETA-SEARCH(state) returns an action
	v ← MAX-VALUE(state,−∞,+∞)
	return the action in ACTIONS(state) with value v
```

```
function MAX-VALUE(state,α, β) returns a utility value
	if TERMINAL-TEST(state) then return UTILITY(state)
	v ← −∞
	for each a in ACTIONS(state) do
		v ← MAX(v, MIN-VALUE(RESULT(s,a),α, β))
		if v ≥ β then return v
		α ← MAX(α, v)
	return v
```

```
function MIN-VALUE(state,α, β) returns a utility value
	if TERMINAL-TEST(state) then return UTILITY(state)
	v ← +∞
	for each a in ACTIONS(state) do
		v ← MIN(v, MAX-VALUE(RESULT(s,a) ,α, β))
		if v ≤ α then return v
		β ← MIN(β, v)
	return v
```
