import bisect

import array

skills = [
    {
      "name": "Grapple Gun",
      "offense": 5,
      "points": 1,
      "require": None
    },
    {
      "name": "Hacking Device",
      "offense": 6,
      "points": 2,
      "require": "Grapple Gun"
    },
    {
      "name": "Remote",
      "offense": 7,
      "points": 3,
      "require": "Hacking Device"
    },
    {
      "name": "Bomb",
      "offense": 20,
      "points": 5,
      "require": "Remote"
    },
    {
      "name": "Inverted takedown",
      "offense": 5,
      "points": 1,
      "require": None
    },
    {
      "name": "Shockwave attack",
      "offense": 8,
      "points": 3,
      "require": "Inverted takedown"
    }
]

target = 11






for skill in skills:
    name = skill.get("name")
    require = skill.get("require")

    skillz[name] = skill
    if require in indexes:
        indexes[require].append(name)
    else:
        indexes[require] = [name]

print(indexes)
print(skillz)
# start with the first none

frontier = [Node(skillz.get(index), None , 0, 0) for index in indexes[None]]
explored = []
visited = 0

while True:

    if len(frontier) == 0 :
        break

    node = frontier.pop(0)
    visited += 1
    print("visiting : {}".format(node.skill_name))

    if node.total_offense >= target:
        print(node.ratio)
        if node.ratio > best_ratio:
            best_ratio = node.ratio
            best_skill = node



    for sk in node.get_next():
        new_node = Node(skillz.get(sk),node, node.offence, node.points )
        if new_node not in frontier and new_node not in explored:
            # use bisect to insert the node at the proper place in the frontier
            #bisect.insort(frontier, new_node)
            frontier.insert(0, new_node)

    explored.append(node)



moves = []
while True:
    moves.append(best_skill.skill_name)
    if best_skill.parent != None:
        best_skill = best_skill.parent
    else:
        break
moves.reverse()
print(moves)



