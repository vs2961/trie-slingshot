from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Trie(db.Model):
    __tablename__ = 'trie'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    is_leaf = db.Column(db.Boolean)
    parent_id = db.Column(db.Integer, db.ForeignKey('trie.id'))
    children = db.relationship('Trie',
                               backref=db.backref('parent', remote_side=[id]),
                               uselist=True)

    def __init__(self, value, is_leaf=False, children=[]):
        self.value = value
        self.children = children
        self.is_leaf = is_leaf

    def serialize(self):
        """Turns Trie Object into json-convertible format"""
        return {
            "VALUE": self.value,
            "ISLEAF": self.is_leaf,
            "CHILDREN": [node.serialize() for node in self.children],
        }

    def in_children(self, val):
        """Returns child node if value found in children"""
        for child in self.children:
            if child.value == val:
                return child
        return None


def init_db():
    """Creates and initializes db with first node"""
    db.create_all()

    initial_node = Trie('')
    db.session.add(initial_node)
    db.session.commit()
