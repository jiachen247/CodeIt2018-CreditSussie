import logging

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)




@app.route('/skill-tree', methods=['POST','GET'])
def evaluate_skill():
    class Node:
        def __init__(self, s, parent, parent_offense, parents_points):
            self.skill_name = s.get("name")
            self.offence = s.get("offense")
            self.points = s.get("points")
            self.total_points = int(self.points) + parents_points
            self.total_offense = int(self.offence) + parent_offense
            self.ratio = self.total_offense / self.total_points
            self.requireSkill = s.get("require_skill")
            self.parent = parent

        def get_next(self):
            if self.skill_name in indexes:
                return indexes[self.skill_name]
            else:
                return []

    data = request.get_json()

    target = data.get("boss").get("offense")
    print("target: {} ".format(target))

    skills = data.get("skills")

    indexes = {}
    skillz = {}

    best_ratio = 0
    best_skill = None

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

    frontier = [Node(skillz.get(index), None, 0, 0) for index in indexes[None]]
    explored = []
    visited = 0

    while True:

        if len(frontier) == 0:
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
            new_node = Node(skillz.get(sk), node, node.offence, node.points)
            if new_node not in frontier and new_node not in explored:
                # use bisect to insert the node at the proper place in the frontier
                # bisect.insort(frontier, new_node)
                frontier.insert(0, new_node)

        explored.append(node)

    moves = []
    while True:
        moves.append(best_skill.skill_name)
        if best_skill.parent is not None:
            best_skill = best_skill.parent
        else:
            break
    moves.reverse()
    print(moves)


    return jsonify(moves)



