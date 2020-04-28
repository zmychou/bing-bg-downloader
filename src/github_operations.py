import os


def run_cmd(cmd):
    pass
    
def git_add(files):
    for f in files:
        os.system('git add {}'.format(f))

def git_commit(desc):
    cmd = 'git commit -m "{}"'.format(desc)
    os.system(cmd)
        

def git_push(remote, branch):
    cmd = 'git push {} {}'.format(remote, branch)
    os.system(cmd)


