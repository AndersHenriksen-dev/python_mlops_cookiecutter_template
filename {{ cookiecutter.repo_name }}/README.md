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
│       └── tests.yaml

├── configs/                  # Configuration files
├── logs/                     # Log outputs, if logging is chosen
├── data/                     # Data directory
├── docs/                     # Documentation
│   ├── mkdocs.yml
│   └── source/
│       └── index.md
├── notebooks/                # Jupyter notebooks
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

You can add these in:

GitHub → Settings → Secrets and variables → Actions → New repository secret


## Installation
Getting started running code in this project is easy.

1. First, clone the repository:
    ```bash
    git clone <<repository_url>>
    cd {{cookiecutter.repo_name}}
    ```

{% if cookiecutter.deps_manager == 'uv' %}
2. This project uses `uv` as dependency manager, make sure you have `uv` installed. You can find installation instructions [here](https://uv.dev/).

3. Then, install the dependencies:
    ```bash
    uv sync
    ```
{% endif %}

{% if cookiecutter.deps_manager == 'pip' %}
2. This project uses `pip` as dependency manager with conda. Make sure you have pip installed:
    ```bash
    python -m ensurepip --upgrade
    ```
3. Also make sure you have [conda](https://docs.conda.io/en/latest/) installed. You can use either [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution).
1. Create a conda environment with the specified python version and activate it:
    ```bash
    conda create -n {{cookiecutter.project_name}} python={{cookiecutter.python_version}} -y
    conda activate {{cookiecutter.project_name}}
    ```
2. install the dependencies in the created conda environment:
    ```bash
    pip install -r requirements.txt
    ```
{% endif %}
You are now ready to run code in this project!

## Acknowledgements

Created using [python mlops template](https://github.com/AndersHenriksen-dev/python_mlops_cookiecutter_template),
a [cookiecutter template](https://github.com/cookiecutter/cookiecutter) for getting started with python and CI/CD.
