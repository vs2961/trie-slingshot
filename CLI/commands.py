import click
import requests

# Change this to "http://127.0.0.1:5000/" if testing locally
LINK = "http://trie-slingshot-dev.us-west-2.elasticbeanstalk.com/"

@click.group()
def cli():
    pass


@cli.command()
@click.option('-f', '--file', is_flag=True, help="Use word file")
@click.argument('strings', nargs=-1)
def add(file, strings):
    """Adds the STRING/words in your file to the trie"""
    if file:
        for string in strings:
            x = open(string)
            words = []
            for i in x:
                words.append(i.strip())
            r = requests.post(LINK + "insert", json={'data': words})
            if r.text == "Done":
                print("Added all words from file")
            else:
                print("Something went wrong.\n" + r.text)
    else:
        data = [string.strip() for string in strings]
        r = requests.post(LINK + "insert", json={'data': data})
        if r.text == "Done":
            print(f"Added your keywords!")
        else:
            print("Something went wrong.\n" + r.text)


@cli.command()
@click.option('-f', '--file', is_flag=True, help="Use word file")
@click.argument('strings', nargs=-1)
def delete(file, strings):
    """Deletes the STRING/words in your file from the trie"""
    if file:
        for string in strings:
            x = open(string, "r")
            words = []
            for i in x:
                words.append(i.strip())
            r = requests.post(LINK + "delete", json={'data': words})
            if r.text == "Done":
                print("Deleted all words from file")
            else:
                print("Something went wrong.\n" + r.text)
    else:
        data = [string.strip() for string in strings]
        r = requests.post(LINK + "delete", json={'data': data})
        if r.text == "Done":
            print(f"Deleted all your keywords!")
        else:
            print("Something went wrong.\n" + r.text)


@cli.command()
@click.option('-v', '--verbose', is_flag=True, help="Give more details")
@click.argument('string')
def search(verbose, string):
    """Tells you whether or not the STRING is in the Trie"""
    r = requests.post(LINK + "search", json={'data': string})
    if verbose:
        if r.text == "True":
            print(f"{string} was found in the trie")
        else:
            print(f"{string} was not found.")
    else:
        print(r.text)


@cli.command()
@click.argument('string')
def autocomplete(string):
    """Returns a list of autocomplete suggestions based on your STRING"""
    r = requests.post(LINK + "autocomplete", json={'data': string})
    if r.text.strip() == "":
        print("No words detected.")
    else:
        print(r.text)


@cli.command()
def display():
    """Displays the Trie"""
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
            self.tree.append(PIPE_PREFIX.rstrip())
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

    r = requests.post(LINK + "dump")
    node = r.json()
    if len(node['CHILDREN']) == 0:
        print("No nodes in tree. Run Trie-CLI add test to add a few!")
    else:
        gen = TreeGenerator(node)
        tree = gen.build_tree()
        for line in tree:
            print(line)


@cli.command()
@click.confirmation_option(prompt='Are you sure you want to drop the db?')
def drop_db():
    """Deletes all nodes from the Trie"""
    r = requests.post(LINK + "dropdb")
    print(r.text)


if __name__ == '__main__':
    cli()
