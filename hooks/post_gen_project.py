import subprocess


def add_to_vcs():
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])
    subprocess.call(['git', 'branch', '-M', 'main'])


if __name__ == "__main__":
    add_to_vcs()
