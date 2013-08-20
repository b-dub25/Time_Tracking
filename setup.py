import os
from subprocess import call
from git import Repo
import json

def is_empty(path):
    if os.path.exists(path):
        if not os.path.isfile(path):
            return True
    else:
        print('No file or directory ' + path)
    return False

def git_install_repos(repos, path):
    # Make sure gitpython is installed
    call(['pip', 'install', 'gitpython'])
    errors = []
    for repo in repos:
        for i in range(1):
            print('\n')
        print('Installing ' + repo['name'])
        loc = repo['urls']['ssh'] if not None else repo['urls']['https']
        repo_path = path + repo['name']
        try:
            Repo.clone_from(repo['urls']['ssh'], repo_path) 
            reqs = repo_path + '/requirements.txt' 
            if os.path.exists(reqs):
                if os.path.isfile(reqs):
                    call(['pip', 'install', '-r', repo_path + '/requirements.txt'])
                else:
                    print(reqs + ' is a directory')
            else:
                print(reqs + ' does not exist')

        except:
            errors.append(repo)
    print('Errors installing:\n')
    for error in errors:
        print(json.dumps(error, indent=2))
    print('Done installing repos')

    
if __name__ == '__main__':
    pwd = os.getcwd()

    # Install pip packages
    reqs = pwd + '/requirements.txt'
    if os.path.exists(reqs):
        if os.path.isfile(reqs):
            call(['pip', 'install', '-r', 'requirements.txt'])
        else:
            print(reqs + ' is a directory')
    else:
        print(reqs + ' does not exist')

    # Install git repos
    apps_dir = pwd + '/apps/'
    if not os.path.exists(apps_dir):
        os.makedirs(apps_dir)

    ## List of git repos and options
    ## Pass in name of repo, https and ssh urls, and if repo has requirements.txt
    repos = [
        {
            'name': 'django-simple-token-auth', 
            'urls': {
                'https': 'https://github.com/jenterkin/django-simple-token-auth.git',
                'ssh': 'git@github.com:jenterkin/django-simple-token-auth.git',
            },
         },
    ]
    git_install_repos(repos, apps_dir)
