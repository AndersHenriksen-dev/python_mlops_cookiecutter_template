# 🍪 A up-to-date Cookiecutter template for MLOps

Inspired by the original [cookiecutter-data-science](https://cookiecutter-data-science.drivendata.org/v1/) template and [Nicky Skafte's mlops_template](https://github.com/SkafteNicki/mlops_template).
This setup is made very specific to the needs of myself and data scientists with a lot of CI/CD work and time spent making packages. Where possible, the tooling from the [MLOps course](https://github.com/SkafteNicki/dtu_mlops) is used.

## ✋ Requirements to use the template:

* Python 3.11 or higher
* [cookiecutter](https://github.com/cookiecutter/cookiecutter) version 2.4.0 or higher

## 🆕 Start a new project

Start by creating a repository either using the GitHub GUI in the web browser or alternatively you can use the
[GitHub command line interface](https://cli.github.com/) if you have set it up:

```bash
gh repo create <repo_name> --public --confirm
```
Afterwards on your local machine run

```bash
cookiecutter https://github.com/AndersHenriksen-dev/python_mlops_cookiecutter_template
```

You will be prompted with the following questions:

```txt
    [1/9] repo_name (repo_name):
    [2/9] project_name (project_name):
    [3/9] Select deps_manager
        1 - pip
        2 - uv
        Choose from [1/2] (1):
    [4/9] Select use_aws
        1 - aws
        2 - none
        Choose from [1/2] (1):
    [5/9] Select use_logging
        1 - y
        2 - n
        Choose from [1/2] (1):
    [6/9] author_name (Your name (or your organization/company/team)):
    [7/9] description (A short description of the project.):
    [8/9] python_version (3.12):
    [9/9] Select open_source_license
        1 - No license file
        2 - MIT
        3 - BSD-3-Clause
        Choose from [1/2/3] (1):
```

Where you should input starting values for the project. A couple of notes regarding the different options:

1. When asked for the `repo_name` e.g. the repository name, this should be the same as when you created the Github
    repository in the beginning.

2. When asked for the `project_name` this should be a
    [valid Python package name](https://peps.python.org/pep-0008/#package-and-module-names). This means that the name
    should be all lowercase and only contain letters, numbers and underscores. The project name will be used as the name
    of the Python package. This will automatically be validated by the template.

3. The `author_name` and `description` fields are purely meant for the readme and other text fields. Besides this, they make no functional difference.

To commit to the remote repository afterwards execute the following series of commands:

```bash
cd <repo_name>
git init
git add .
git commit -m "init cookiecutter project"
git remote add origin https://github.com/<username>/<repo_name>
git push origin master
```

## 🗃️ Repository structure

Assuming you choose the `advance` structure and `uv` as the dependency manager, the repository will look like
something like this:

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

## 📚 The stack

🐍 Python projects using `pyproject.toml`

📦 Containerized using [Docker](https://www.docker.com/)

📄 Documentation with [Material Mkdocs](https://squidfunk.github.io/mkdocs-material/)

👕 Linting and formatting with [ruff](https://docs.astral.sh/ruff/)

✅ Checking using [pre-commit](https://pre-commit.com/)

🛠️ CI with [GitHub Actions](https://github.com/features/actions)

🤖 Automated dependency updates with [Dependabot](https://github.com/dependabot)

📝 Project tasks using [Invoke](https://www.pyinvoke.org/)

☁️ Cloud infrastructure with [AWS](https://aws.amazon.com/)

📜 Infrastructure as code with [Terraform](https://www.terraform.io/)

📝 Logging with standard Python logging or preferred libraries

and probably more that I have forgotten...

## ❕ License

If you enjoy using this template, please consider giving credit to myself and Nicki Skafte by citing this project and the original.
You can use the following BibTeX entries:

```bibtex
@misc{skafte_mlops_template,
    author       = {Anders Henriksen},
    title        = {Python MLOps Cookiecutter Template},
    howpublished = {\url{https://github.com/AndersHenriksen-dev/python_mlops_cookiecutter_template}},
    year         = {2025}
}
@misc{skafte_mlops_template,
    author       = {Nicki Skafte Detlefsen},
    title        = {MLOps template},
    howpublished = {\url{https://github.com/SkafteNicki/mlops_template}},
    year         = {2025}
}
```
