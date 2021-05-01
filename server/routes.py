from flask import Blueprint, jsonify, request
from models import Trie, db

trie_blueprint = Blueprint(
        'trie', __name__,
        template_folder='templates')


@trie_blueprint.route('/dump', methods=["GET", "POST"])
def dump():
    node = Trie.query
    nodeList = [nodes.serialize() for nodes in node]
    return jsonify(nodeList[0])


@trie_blueprint.route('/find', methods=["GET", "POST"])
def find():
    req_data = request.form
    node = Trie.query.get(1)
    for char in req_data["Key"]:
        child = node.in_children(char)
        if child is not None:
            node = child
        else:
            return str(False)
    return str(True) if node.isLeaf else str(False)


@trie_blueprint.route('/insert', methods=["GET", "POST"])
def insert():
    """Insert key/value pair into node."""
    req_data = request.form
    node = Trie.query.get(1)
    for char in req_data["Key"]:
        child = node.in_children(char)
        if child is None:
            toAdd = Trie(char)
            db.session.add(toAdd)
            node.children.append(toAdd)
            node = toAdd
        else:
            node = child
    node.isLeaf = True
    db.session.commit()
    return "Done"


@trie_blueprint.route('/delete', methods=["GET", "POST"])
def delete():
    req_data = request.form
    node = Trie.query.get(1)

    def helper(curr, key, depth):
        if depth == len(key):
            if len(curr.children) == 0:
                db.session.delete(curr)
                return True
            curr.isLeaf = False
            return False
        else:
            child = curr.in_children(key[depth])
            if child is None:
                return False
            remove = helper(child, key, depth + 1)
            if remove and len(curr.children) <= 1 and curr.value != "":
                db.session.delete(curr)
                return True

    helper(node, req_data["Key"], 0)
    db.session.commit()
    return "Done"


@trie_blueprint.route('/autocomplete', methods=["GET", "POST"])
def autocomplete():
    req_data = request.form
    node = Trie.query.get(1)
    for char in req_data["Key"]:
        child = node.in_children(char)
        if child is None:
            return "No words found."
        node = child

    def helper(curr, word):
        if not curr.children:
            return req_data["Key"] + word + '\n'
        else:
            toReturn = ""
            for child in curr.children:
                toReturn += helper(child, word + child.value)
            return toReturn

    return helper(node, "")
