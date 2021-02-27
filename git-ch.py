import sys
import os
import getch

CHOICE = '0123456789abcdefghijklmnprstuvwxyz'


def branch_choose():
    current_branch = os.popen('git branch --show-current').read().strip()
    branches = os.popen('git branch').read().split()
    branches = list(filter(lambda x: len(x) > 1, branches))
    branches = sorted(branches)[::-1]
    for i, br in enumerate(branches):
        if current_branch == br:
            print('\u001b[32m[{}] *{}\u001b[0m'.format(CHOICE[i], br))
        else:
            print('[{}]  {}'.format(CHOICE[i], br))
    ch = getch.getch()
    os.system('git checkout {}'.format(branches[CHOICE.index(ch)]))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        try:
            branch_choose()
        except:
            print('canceled')
            exit(1)
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg == '-':
            os.system('git checkout -')
        else:
            os.system(
                'sh -c "git branch | grep -v remotes | grep {} | head -n 1 | xargs git checkout"'.format(arg))
    else:
        os.system('git checkout {}'.format(' '.join(sys.argv[1:])))
