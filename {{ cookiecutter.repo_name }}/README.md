# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project structure

The directory structure of the project looks like this:
```txt
├── .github/                  # Github actions and dependabot
│   ├── dependabot.yaml
│   └── workflows/
│       ├── linting.yaml
│       ├── pre-commit-update.yaml
│       ├── deploy.yaml       # if aws is chosen
│       └── tests.yaml

├── configs/                  # Configuration files
├── logs/                     # Log outputs, if logging is chosen
├── data/                     # Data directory
├── dockerfiles/              # Dockerfiles
│   ├── api.Dockerfile
│   └── train.Dockerfile
├── docs/                     # Documentation
│   ├── mkdocs.yml
│   └── source/
│       └── index.md
├── notebooks/                # Jupyter notebooks
├── infra/                    # deployment infrastrucure, if aws is chosen
│   ├── terraform
│       ├── main.tf
│       ├── outputs.tf
│       └── variables.tf
├── reports/                  # Reports
│   └── figures/
├── src/                      # Source code
│   ├── project_name/
│   │   ├── __init__.py
│   │   └── main.py
└── tests/                    # Tests
│   ├── __init__.py
│   ├── test_file.py
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── pyproject.toml            # Python project file
├── README.md                 # Project README
├── requirements.txt          # Project requirements
├── requirements_dev.txt      # Development requirements
└── tasks.py                  # Project tasks
```


## Setup

### Software
- Pip
- Git
- Python
- Docker and Docker Desktop
- Terraform (if you want terraform support)
- Minikube (if you need kubernetes)
- Kubectl (if you need kubernetes)

### Git setup
Some of these settings should always be on to get the best git experience. Others are highly controversial. To learn more, read [this blog](https://blog.gitbutler.com/how-git-core-devs-configure-git).

#### Always a good idea
```git config --global user.name "Your Name"```
```git config --global user.email "you@example.com"```
```git config --global core.editor "code --wait"```
<!-- ``git config --global column.ui auto`` -->
``git config --global branch.sort -committerdate``
``git config --global tag.sort version:refname``
``git config --global init.defaultBranch main``
``git config --global diff.algorithm histogram``
``git config --global diff.mnemonicPrefix true``
``git config --global diff.renames true``
``git config --global diff.colorMoved plain``
``git config --global push.autoSetupRemote true``
``git config --global push.default simple # (default since 2.0)``
``git config --global push.followTags true``
``git config --global fetch.prune true``
``git config --global fetch.pruneTags true``
``git config --global fetch.all true``


#### Sometimes a good idea
``git config --global help.autocorrect prompt``
``git config --global commit.verbose true``
``git config --global rerere.enabled true``
``git config --global rerere.autoupdate true``
``git config --global rebase.autoSquash true``
``git config --global rebase.autoStash true``
<!-- git config --global merge.conflictstyle zdiff3 -->
<!-- git config --global pull.rebase true -->
``git config --global core.fsmonitor true``
``git config --global core.untrackedCache true``

### Git Hooks
To setup git hooks (check commit message setup, only allow rebase to feature-branches and merge to main), use the following line:
```git config core.hooksPath hooks```

### GitHub Secrets

To keep your project secure, you must configure the following GitHub repository secrets:
- GITHUB_TOKEN
- TF_API_TOKEN
- DOCKER_USERNAME
- DOCKER_PASSWORD

You can add these in:

GitHub → Settings → Secrets and variables → Actions → New repository secret


### AWS (Optional)
If you want to use AWS, you will need to run:
```aws configure```


## Acknowledgements

Created using [python mlops template](https://github.com/AndersHenriksen-dev/python_mlops_cookiecutter_template),
a [cookiecutter template](https://github.com/cookiecutter/cookiecutter) for getting started with python and CI/CD.
