# IPL Team ELimination Detection

This project aims to determine if a particular team in the Indian Premier League (IPL) has a chance of finishing the season with the most wins. The focus is on the group stage of the tournament, where the top 4 teams qualify for the playoffs.


## Problem Statement

The problem statement is to identify which teams have a chance of finishing the season with the most wins. We will consider a simplified scenario with a set of teams contending for the top position.


## Approach

The approach involves creating a flow network and applying the max flow algorithm to determine team elimination. The steps are as follows:

1. Consider the team of interest, referred to as team z, and assume they win all their remaining games.
2. Introduce a source node (s) and a sink node (t) in the flow network.
3. Add edges from the source node to game nodes, representing the remaining games between teams (excluding team z).
4. Connect the game nodes to the corresponding team nodes with edges of infinite capacity.
5. Connect the team nodes to the sink node, with edge capacities indicating the maximum number of games other teams can win while allowing team z to finish with the most wins.
6. Calculate the max flow in the flow network.
7. If the max flow saturates all edges leaving the source node, team z is not eliminated; otherwise, they are eliminated.


## Usage

To use this project, input the standings and win counts of the teams in the IPL group stage. The implementation will determine if a specific team can finish with the most wins or if they are eliminated.

This project can also be adapted for other sports or competitions by modifying the graph input. By changing the graph to represent the standings and remaining matches in a different tournament, the project can be used to detect team elimination scenarios in various sports.

To get input from user modify main.py

```python
from graph import Graph

def get_graph_from_user():
    graph = []
    rows = int(input("Enter number of rows: "))
    for i in range(rows):
        row = list(map(int, input(f"Enter row values {i+1}: ").split()))
        graph.append(row)
    return graph

def main():
    graph = get_graph_from_user()

    g = Graph(graph)

    source = 0
    sink = 7

    print("Max Flow: %d " % g.ford_fulkerson(source, sink))

if __name__ == "__main__":
    main()
```

## Credits

This project is based on the concept described in an article. The idea was implemented and adapted for the specific problem of IPL team elimination detection.