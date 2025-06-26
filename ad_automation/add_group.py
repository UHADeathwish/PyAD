import logging
import subprocess
from pathlib import Path
from pyad import adgroup, pyad

logger = logging.getLogger(__name__)


def add_group(groupname: str, groups_root: str = r"\\server\groups"):
    """Create AD group and directory with permissions."""
    try:
        container = pyad.adcontainer.ADContainer.from_dn("CN=Users")
        group = adgroup.ADGroup.create(groupname, container)
    except Exception as exc:
        logger.error("Failed to create group: %s", exc)
        return False

    group_dir = Path(groups_root) / groupname
    group_dir.mkdir(parents=True, exist_ok=True)

    try:
        subprocess.run([
            "icacls",
            str(group_dir),
            "/grant",
            f"{groupname}:(OI)(CI)F"
        ], check=True)
    except Exception as exc:
        logger.error("Failed to set directory permissions: %s", exc)

    logger.info("Groep %s aangemaakt met map en rechten.", groupname)
    return True
