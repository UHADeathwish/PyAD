import logging
import shutil
from datetime import datetime
from pathlib import Path
from pyad import aduser

logger = logging.getLogger(__name__)


def offboard_user(username: str, backup_root: str = r"\\server\backup"):
    """Disable a user and archive home directory."""
    try:
        user = aduser.ADUser.from_cn(username)
        user.update_attribute("description", "Uit dienst")
        user.disable()
        home_dir = Path(user.get_attribute("homeDirectory")[0])
    except Exception as exc:
        logger.error("Failed to modify user: %s", exc)
        return False

    dest = Path(backup_root) / f"{username}_{datetime.now():%Y%m%d}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        shutil.move(str(home_dir), dest)
    except Exception as exc:
        logger.error("Failed to move home directory: %s", exc)
        return False
    logger.info("Gebruiker %s gearchiveerd naar %s", username, dest)
    return True
