def main():
	start = (1, 1)
	end = (7, 7)
	world_map = [
		[" ■ ", " ■ ", " ■ ", " ■ ", " ■ ", " ■ ", " ■ ", " ■ ", " ■ "],
		[" ■ ", "   ", "   ", "   ", " ■ ", "   ", "   ", " ■ ", " ■ "],
		[" ■ ", "   ", " ■ ", "   ", "   ", "   ", " ■ ", "   ", " ■ "],
		[" ■ ", "   ", " ■ ", "   ", " ■ ", "   ", " ■ ", "   ", " ■ "],
		[" ■ ", "   ", " ■ ", "   ", " ■ ", "   ", " ■ ", "   ", " ■ "],
		[" ■ ", "   ", "   ", "   ", "   ", "   ", " ■ ", "   ", " ■ "],
		[" ■ ", " ■ ", " ■ ", "   ", " ■ ", "   ", "   ", "   ", " ■ "],
		[" ■ ", "   ", " ■ ", "   ", " ■ ", "   ", " ■ ", "   ", " ■ "],
		[" ■ ", " ■ ", " ■ ", " ■ ", " ■ ", " ■ ", " ■ ", " ■ ", " ■ "],
	]

	final_path = a_star(world_map, start, end, True)

	for i, row in enumerate(world_map):
		for point in final_path:
			if point[1] == i:
				row[point[0]] = " * "
		print("".join(row))

def a_star(world_map, start_node, end_node, allows_diagonal=False):
	directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
	if allows_diagonal:
		directions += [(1, 1), (1, -1), (-1, -1), (-1, 1)]

	map_height = len(world_map) - 1
	map_width = len(world_map[0]) - 1

	open_nodes = []
	closed_nodes = []

	parent_nodes = {}
	g_scores = {}
	f_scores = {}

	open_nodes.append(start_node)
	f_scores[start_node] = g_scores[start_node] = 0
	f_scores[end_node] = g_scores[end_node] = 0
	parent_nodes[start_node] = None

	while open_nodes:
		current_node = open_nodes[0]
		for node in open_nodes:
			if f_scores[node] < f_scores[current_node]:
				current_node = node

		open_nodes.remove(current_node)
		closed_nodes.append(current_node)

		if current_node == end_node:
			path = []
			current = current_node
			while current is not None:
				path.append(current)
				current = parent_nodes[current]
			return path[::-1]

		children = []
		for direction in directions:
			potential_node = (current_node[0] + direction[0], current_node[1] + direction[1])

			if potential_node[0] > map_width or potential_node[0] < 0 or potential_node[1] > map_height or potential_node[1] < 0:
				continue

			if world_map[potential_node[1]][potential_node[0]] != "   ":
				continue

			children.append(potential_node)

		for child in children:
			if child in closed_nodes:
				continue

			if child not in g_scores:
				g_scores[child] = g_scores[current_node] + ((child[1] - end_node[1]) ** 2) + ((child[0] - end_node[0]) ** 2)
				heuristic_score = g_scores[child]
				f_scores[child] = g_scores[child] + heuristic_score

			for open_node in open_nodes:
				if child == open_node and g_scores[child] > g_scores[open_node]:
					continue

			open_nodes.append(child)
			if child not in parent_nodes:
				parent_nodes[child] = current_node

main()