import subprocess


def add(to_add, is_file=False):
    if type(to_add) == str:
        to_add = [to_add]
    if is_file:
        return subprocess.run(["Trie-CLI", "add", "-f"] + to_add,
                              stdout=subprocess.PIPE, text=True)
    return subprocess.run(["Trie-CLI", "add"] + to_add,
                          stdout=subprocess.PIPE, text=True)


def delete(to_delete, is_file=False):
    if type(to_delete) == str:
        to_delete = [to_delete]
    if is_file:
        return subprocess.run(["Trie-CLI", "delete", "-f"] + to_delete,
                              stdout=subprocess.PIPE, text=True)
    return subprocess.run(["Trie-CLI", "delete"] + to_delete,
                          stdout=subprocess.PIPE, text=True)


def search(to_search):
    return subprocess.run(["Trie-CLI", "search", to_search],
                          stdout=subprocess.PIPE, text=True).stdout.strip()


def autocomplete(to_autocomplete):
    return subprocess.run(["Trie-CLI", "autocomplete", to_autocomplete],
                          stdout=subprocess.PIPE, text=True).stdout.strip()


def display():
    return subprocess.run(["Trie-CLI", "display"],
                          stdout=subprocess.PIPE, text=True).stdout


"""
You may run this file on different devices to test the Global Trie state.

Past this point, you may add your own testing. I've provided some sample
testing to help you get started. To provide ease of access, I've also provided
a few functions for you to use:

Time Complexity: k = # of letters that you give in total
                 n = # of nodes in the Trie

add([args]) or add(arg) - Adds to the trie - O(k) time
- Optional is_file param: ex: add([words.txt, more_words.txt], is_file=True)

delete([args]) or delete(arg) - Deletes from the trie - O(k) time
- Optional is_file param: ex: delete([words.txt, more_words.txt], is_file=True)

search(arg) - Returns whether a keyword is in the trie - O(k) time

autocomplete(arg) - Returns autocomplete possibilites for keyword - O(n) time

display() - Displays the trie - O(n) time
"""

DEVICE_NUMBER = 1

if DEVICE_NUMBER == 1:
    # On one device
    add(["Hello", "World"])
    print(search("Hello"))
    display()

    # After running on device 2
    display()

elif DEVICE_NUMBER == 2:
    # On anohter device
    display()
    delete(["Hello", "World"])
    display()
