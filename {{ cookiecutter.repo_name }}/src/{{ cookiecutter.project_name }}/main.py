

if __name__ == "__main__":
{% if cookiecutter.use_logging == 'y' %}
    from utils.logger import get_logger

    log = get_logger(__name__)

    log.info("Server started.")
    log.debug("Debugging connection issue...")
    log.warning("Low disk space.")
    log.error("Failed to save file!")
{% endif %}