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
max_version = "3.13"
if not (ge(python_version, min_version) and le(python_version, max_version)):
    raise ValueError(
        f"Python version must be between {min_version} and {max_version}."
        " These are the versions that still receive support."
        " You can read more about Python versioning here: https://devguide.python.org/versions/",
    )

logger.info("Setting the correct python version in .github/workflows.")
project_dir = Path.cwd()  # This is the generated project root

workflow_dir = Path(project_dir / ".github" / "workflows")

placeholders = {
    "PLACEHOLDER_FOR_PYTHON_VERSION": "{{ cookiecutter.python_version }}",
}

for file_path in workflow_dir.glob("*.yaml"):
    text = file_path.read_text()
    for key, val in placeholders.items():
        text = text.replace(key, val)
    file_path.write_text(text)


def replace_in_file(path, replacements) -> None:
    with open(path, "r") as f:
        content = f.read()

    for k, v in replacements.items():
        content = content.replace(k, v)

    with open(path, "w") as f:
        f.write(content)

use_aws = "{{cookiecutter.use_aws}}"
aws_region = "{{cookiecutter.aws_region}}"

aws_profile = "default"
aws_bucket_for_tf_state = f"{project_name}-tf-state"
aws_dynamodb_lock_table = f"{project_name}-tf-locks"

terraform_dir = "infra/terraform"

# Terraform setup
if not use_aws:
    sys.exit()

for root, _, files in os.walk(terraform_dir):
    for file in files:
        if file.endswith(".tf"):
            full_path = Path(root/file)
            replace_in_file(
                full_path,
                {
                    "{{ cookiecutter.aws_bucket_for_tf_state }}": aws_bucket_for_tf_state,
                    "{{ cookiecutter.aws_dynamodb_lock_table }}": aws_dynamodb_lock_table,
                    "{{ cookiecutter.aws_profile }}": aws_profile,
                    "{{ cookiecutter.aws_region }}": aws_region,
                },
            )
