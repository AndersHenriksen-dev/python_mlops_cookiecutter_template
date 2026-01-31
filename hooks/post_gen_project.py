from keyword import iskeyword
from operator import ge, le
from pathlib import Path
import os
import sys

try:
    from loguru import logger
except ImportError:
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)

project_name = "{{cookiecutter.project_name}}"
python_version = "{{cookiecutter.python_version}}"

logger.info(f"Project name: {project_name}")
logger.info(f"Python version: {python_version}")

if not project_name.isidentifier() or not project_name.islower():
    raise ValueError(
        "\n"
        "Project name must be a valid project name, meaning that it must be a valid Python name and also be lowercase."
        " This means that it must not contain spaces or special characters, and must not start with a number."
        " In general it is best to use only lowercase letters and underscores."
        " You can read more about Python naming conventions for packages here:"
        " https://peps.python.org/pep-0008/#package-and-module-names"
        "\n",
    )
if iskeyword(project_name):
    raise ValueError(
        "Project name must not be a built-in keyword, as it will cause syntax errors.",
    )

min_version = "3.10"
max_version = "3.14"
if not (ge(python_version, min_version) and le(python_version, max_version)):
    raise ValueError(
        f"Python version must be between {min_version} and {max_version}."
        " These are the versions that still receive support."
        " You can read more about Python versioning here: https://devguide.python.org/versions/",
    )

logger.info("Setting the correct python version in .github/workflows.")

# 1. Use the current working directory (the new project)
project_dir = Path.cwd()

# 2. Safely handle workflows (only if the directory exists)
workflow_dir = project_dir / ".github" / "workflows"
if workflow_dir.exists():
    for file_path in workflow_dir.glob("*.yaml"):
        text = file_path.read_text()
        text = text.replace("PLACEHOLDER_FOR_PYTHON_VERSION", python_version)
        file_path.write_text(text)

# 3. Fix the Git Hooks Pathing
# Hooks should be inside your generated project, e.g., in a 'hooks' folder
hooks_dir = project_dir / "hooks" 
if hooks_dir.exists():
    git_hooks = [
        hooks_dir / "commit-msg.sh",
        hooks_dir / "pre-merge-commit.sh",
        hooks_dir / "pre-push.sh",
    ]
    for git_hook in git_hooks:
        if git_hook.exists():
            git_hook.chmod(0o755)
