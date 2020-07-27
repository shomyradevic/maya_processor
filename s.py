from __future__ import print_function


def new(memory, new_line):
    return memory[1:] + [new_line]


if __name__ == '__main__':
    new_lines = ['sixth', 'seventh', 'eighth', 'nineth', 'tenth']
    history = ['first', 'second', 'third', 'fourth', 'fifth']
    for l in new_lines:
        history = history[1:] + [l]
        print(history)