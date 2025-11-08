from invoke import Context, task


@task
def template(ctx: Context) -> None:
    """Create a new project from the template."""
    ctx.run("cookiecutter -f --config-file configs/advance_config.yaml --no-input --verbose .")

@task
def requirements(ctx: Context) -> None:
    """Install project requirements."""
    ctx.run("python -m pip install --upgrade pip")
    ctx.run("pip install -r requirements.txt")


@task
def clean(ctx: Context) -> None:
    """Clean up the project."""
    ctx.run("rm -rf repo_name")
    ctx.run("rm -rf .pytest_cache")
    ctx.run("rm -rf .ruff_cache")


@task
def actions(ctx: Context) -> None:
    """Run Github actions."""
    ctx.run("act --list")
    ctx.run("act --artifact-server-path /tmp/artifacts")
