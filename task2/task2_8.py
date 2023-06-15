# 8. Given two sets of favorite video games of two students, return the intersection set of them.

def get_intersection(set1, set2):
	intersect = games_student2.intersection(games_student1)
	if len(intersect) != 0:
		return intersect
	else:
		print("students don't have intersecting games")

games_student1 = set(("game1", "game2", "game4", "game7"))
games_student2 = set(("game3", "game2", "game7", "game8"))

# print(type(games_student1))
# print(type(games_student2))

# print(get_intersection(games_student1, games_student2))


similar_games = [i for i in games_student1 if i in games_student2]
print(similar_games)