Plan is to make hex. Try not to make the same mistake as with chess. Main one (I think) was:
- Don't focus on GUI. Game should work without GUI and without user input in general.


So how does hex work:
- It's just and 11x11 square lattice. The only hexagonal thing is which ones are neighbours. Which ones are neighbours?
- (0,0) has 2 neighbours namely: (1,0) and (0,1) for (x,y).
- (1,0) has 4 neighbours (0,0), (2,0), (0,1), (1,1)
- (0,1) has 4 neighbours (0,0), (0,2), (1,0), (1,1)
- (1,1) has 6 neighbours (1,0), (2,0), (2,1), (1,2), (0,2), (0,1)
All the the ones not on the side behave the same. So it's just a square lattice with a preference for bottom left and top right. So let's do an example and check:
(4,5) has neighbours (4,4),(4,6),(3,5),(5,5) + preferences of the lattice (3,6),(5,4). Alright makes sense.

We can just implement the board as a 11x11 square lattice/array. And really the only thing we need is a win condition and something that says you can't move if there's already something there. And then build a GUI. Which draws an hexagonal lattice from a square one.

We'll implement an empty square as 0. white square as 1, black square as 2

Features:
- flexible board size.
- GUI works in a browser
- Have multiple folder and have it work
- Play on github(?)


Hard part is to check if the game is over
https://www.geeksforgeeks.org/find-whether-path-two-cells-matrix/
one way is to use Breadth First Search. maybe Depth-first search is faster. Gotta handle multiple goals and starting points.

# Web
Let's make a web version using Flask
