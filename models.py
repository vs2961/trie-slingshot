from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Trie(db.Model):
    __tablename__ = 'trie'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    isLeaf = db.Column(db.Boolean)
    parent_id = db.Column(db.Integer, db.ForeignKey('trie.id'))
    children = db.relationship('Trie',
                               backref=db.backref('parent', remote_side=[id]),
                               uselist=True)

    def __init__(self, value, isLeaf=False, children=[]):
        self.value = value
        self.children = children
        self.isLeaf = isLeaf

    def serialize(self):
        return {
            "VALUE": self.value,
            "ISLEAF": self.isLeaf,
            "CHILDREN": [node.serialize() for node in self.children],
        }

    def in_children(self, val):
        for child in self.children:
            if child.value == val:
                return child
        return None


def init_db():
    db.create_all()

    initial_node = Trie('')
    db.session.add(initial_node)
    db.session.commit()
