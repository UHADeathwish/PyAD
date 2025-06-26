import logging
import subprocess
from pathlib import Path
from pyad import adsearch

logger = logging.getLogger(__name__)


def migrate_all(home_root: str = r"\\server\home"):
    """Ensure all AD users have a home directory with correct rights."""
    search = adsearch.ADSearch()
    search.execute_query(
        attributes=["sAMAccountName", "homeDirectory"],
        where_clause="objectClass='user'"
    )
    results = search.get_results()
    summaries = []

    for user in results:
        username = user.get("sAMAccountName")
        if not username:
            continue
        home_dir_attr = user.get("homeDirectory")
        expected_dir = Path(home_root) / username
        if not home_dir_attr or not Path(str(home_dir_attr)).exists():
            expected_dir.mkdir(parents=True, exist_ok=True)
            try:
                subprocess.run([
                    "icacls",
                    str(expected_dir),
                    "/grant",
                    f"{username}:(OI)(CI)F"
                ], check=True)
            except Exception as exc:
                logger.error("Failed setting rights for %s: %s", username, exc)
            summary = f"{username}: {expected_dir} aangemaakt"
            summaries.append(summary)
            logger.info(summary)
    return summaries
