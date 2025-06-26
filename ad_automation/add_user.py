import logging
import subprocess
from pathlib import Path
from pyad import aduser, adgroup, pyad

logger = logging.getLogger(__name__)


def add_user(username: str, fullname: str, group: str,
             home_root: str = r"\\server\home",
             servicedesk_phone: str = "123-456789"):
    """Add a user to Active Directory and create home directory."""
    try:
        container = pyad.adcontainer.ADContainer.from_dn("CN=Users")
        user = aduser.ADUser.create(
            username,
            container,
            password="Pa$$w0rd",
            optional_attributes={'displayName': fullname}
        )
        group_obj = adgroup.ADGroup.from_cn(group)
        group_obj.add_members([user])
    except Exception as exc:
        logger.error("Failed to create user or add to group: %s", exc)
        return False

    home_dir = Path(home_root) / username
    home_dir.mkdir(parents=True, exist_ok=True)

    try:
        subprocess.run([
            "icacls",
            str(home_dir),
            "/grant",
            f"{username}:(OI)(CI)F"
        ], check=True)
    except Exception as exc:
        logger.error("Failed to set NTFS rights: %s", exc)

    summary_path = Path(f"{username}_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as fh:
        fh.write(f"Gebruikersnaam: {username}\n")
        fh.write(f"Directory-pad: {home_dir}\n")
        fh.write(f"Groepsnaam: {group}\n")
        fh.write(f"Servicedesk-telefoonnummer: {servicedesk_phone}\n")
    logger.info("Nieuwe gebruiker %s aangemaakt met rechten.", username)
    return True
