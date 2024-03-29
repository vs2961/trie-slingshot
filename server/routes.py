from flask import Blueprint, jsonify, request, render_template
from models import Trie, db

trie_blueprint = Blueprint(
        'trie', __name__,
        template_folder='templates')


@trie_blueprint.route("/")
def show():
    """Main Page"""
    return render_template('index.html')


@trie_blueprint.route("/dropdb", methods=["GET", "POST"])
def drop_db():
    """Deletes all nodes from the trie - probably O(1) honestly"""
    db.session.query(Trie).delete()
    db.session.commit()
    new = Trie("")
    db.session.add(new)
    db.session.commit()
    return "Deleted all nodes."


@trie_blueprint.route('/dump', methods=["GET", "POST"])
def dump():
    """Returns the trie as a json - O(# of nodes in tree)"""
    node = Trie.query.get(1)
    return jsonify(node.serialize())


@trie_blueprint.route('/search', methods=["GET", "POST"])
def search():
    """Searches for a keyword in the trie (returns True/False) -
       Time Complexity: O(length of keyword)"""
    req_data = request.get_json()
    if not req_data:
        return "No data was found. Did you pass in a JSON with the \
                name/value pair {'data': value}?"
    node = Trie.query.get(1)
    for char in req_data["data"]:
        child = node.in_children(char)
        if child is not None:
            node = child
        else:
            return str(False)
    return str(True) if node.is_leaf else str(False)


@trie_blueprint.route('/insert', methods=["GET", "POST"])
def insert():
    """Inserts one or more keywords into the trie.
       Time Complexity: O(length of all keywords)"""
    req_data = request.get_json()
    if not req_data["data"]:
        return "No data was found. Did you pass in a JSON with the \
                name/value pair {'data': value}?"
    if type(req_data["data"]) == str:
        r = insertWord(req_data["data"])
    else:
        for i in req_data["data"]:
            r = insertWord(i)
    return r


def insertWord(word):
    """Inserts one keyword into the trie - O(length of keyword)"""
    node = Trie.query.get(1)
    for char in word:
        child = node.in_children(char)
        if child is None:
            toAdd = Trie(char)
            db.session.add(toAdd)
            node.children.append(toAdd)
            node = toAdd
        else:
            node = child
    node.is_leaf = True
    db.session.commit()
    return "Done"


@trie_blueprint.route('/delete', methods=["GET", "POST"])
def delete():
    """Deletes one or more keywords from the trie.
       Time Complexity: O(length of all keywords)"""
    req_data = request.get_json()
    if not req_data["data"]:
        return "No data was found. Did you pass in a JSON with the \
                name/value pair {'data': value}?"
    print(req_data["data"])
    if type(req_data["data"]) == str:
        r = deleteWord(req_data["data"])
    else:
        for i in req_data["data"]:
            r = deleteWord(i)
    return r


def deleteWord(word):
    """Deletes a single keyword from the trie, but does not remove
       nodes if other words are using them.
       Time Complexity: O(length of keyword)"""

    node = Trie.query.get(1)

    def helper(curr, key, depth):
        if depth == len(key):
            if len(curr.children) == 0 and curr.value != "":
                db.session.delete(curr)
                return True
            curr.is_leaf = False
            return False
        else:
            child = curr.in_children(key[depth])
            if child is None:
                return False
            remove = helper(child, key, depth + 1)
            if remove and not curr.is_leaf and curr.value != "":
                db.session.delete(curr)
                return True

    helper(node, word, 0)
    db.session.commit()
    return "Done"


@trie_blueprint.route('/autocomplete', methods=["GET", "POST"])
def autocomplete():
    """Returns a list of autocomplete suggestions based on your input.
       Time Complexity: O(# of nodes in tree)"""
    req_data = request.get_json()
    if not req_data:
        return "No data was found. Did you pass in a JSON with the \
                name/value pair {'data': value}?"
    node = Trie.query.get(1)
    for char in req_data["data"]:
        child = node.in_children(char)
        if child is None:
            return "No words found."
        node = child

    def helper(curr, word):
        toReturn = ""
        if curr.is_leaf:
            toReturn += req_data["data"] + word + '\n'
        for child in curr.children:
            toReturn += helper(child, word + child.value)
        return toReturn

    return helper(node, "").strip()
