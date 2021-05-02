import click
import requests

LINK = "http://trie-slingshot.eba-rmufyux3.us-east-2.elasticbeanstalk.com/"


@click.group()
def cli():
    pass


@cli.command()
@click.option('-f', '--file', is_flag=True, help="Use word file")
@click.argument('string')
def add(file, string):
    """Adds STRING/the words in your file to the trie"""
    if file:
        x = open(string)
        words = []
        for i in x:
            words.append(i.strip())
        r = requests.post(LINK + "insert", json={'data': words})
        if r.text == "Done":
            print("Added all words from file")
        else:
            print("Something went wrong. Try again later.\n" + r.text)
    else:
        r = requests.post(LINK + "insert", json={'data': [string.strip()]})
        if r.text == "Done":
            print(f"Added {string}")
        else:
            print("Something went wrong. Try again later.\n" + r.text)


@cli.command()
@click.option('-f', '--file', is_flag=True, help="Use word file")
@click.argument('string')
def delete(file, string):
    """Deletes STRING from the trie"""
    if file:
        x = open(string)
        words = []
        for i in x:
            words.append(i.strip())
        r = requests.post(LINK + "delete", json={'data': words})
        if r.text == "Done":
            print("Deleted all words from file")
        else:
            print("Something went wrong. Try again later.\n" + r.text)
    else:
        r = requests.post(LINK + "delete", json={'data': [string.strip()]})
        if r.text == "Done":
            print(f"Deleted {string}")
        else:
            print("Something went wrong. Try again later.\n" + r.text)


@cli.command()
@click.argument('string')
def search(string):
    r = requests.post(LINK + "find", json={'data': string})
    if r.text == "True":
        print(f"{string} was found in the trie")
    else:
        print(f"{string} was not found.")


@cli.command()
@click.argument('string')
def autocomplete(string):
    """Returns a list of autocomplete suggestions based on your input"""
    r = requests.post(LINK + "autocomplete", json={'data': string})
    print(r.text)


@cli.command()
def display():
    """Displays the Trie"""
    PIPE = "│"
    ELBOW = "└──"
    TEE = "├──"
    PIPE_PREFIX = "│   "
    SPACE_PREFIX = "    "

    class TreeGenerator:
        def __init__(self, root):
            self.tree = []
            self.root = root

        def build_tree(self):
            self.tree.append(self.root['VALUE'])
            self.tree.append(PIPE)
            self.tree_body(self.root, "")
            return self.tree

        def tree_body(self, node, word, prefix=""):
            children = [child for child in node['CHILDREN']]
            for ind, child in enumerate(children):
                connector = ELBOW if ind == len(children) - 1 else TEE
                self.add_branch(
                    child, ind, len(children), word, prefix, connector
                )

        def add_branch(self, node, index, count, word, prefix, connector):
            toAppend = f"{prefix}{connector} {node['VALUE']}"
            if node['ISLEAF']:
                toAppend += f" -> {word + node['VALUE']}"
            self.tree.append(toAppend)
            if index != count - 1:
                prefix += PIPE_PREFIX
            else:
                prefix += SPACE_PREFIX
            self.tree_body(
                node,
                word + node["VALUE"],
                prefix=prefix,
            )
            self.tree.append(prefix.rstrip())

    r = requests.post(LINK + "dump")
    node = r.json()
    gen = TreeGenerator(node)
    tree = gen.build_tree()
    for line in tree:
        print(line)


if __name__ == '__main__':
    cli()
