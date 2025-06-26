import logging
from pyad import adsearch

logger = logging.getLogger(__name__)


def search_user(query: str):
    """Search for a user by (partial) name and print details."""
    s = adsearch.ADSearch()
    s.execute_query(
        attributes=["distinguishedName", "memberOf", "displayName", "homeDirectory", "sAMAccountName", "objectSid", "userAccountControl"],
        where_clause=f"displayName LIKE '{query}*'"
    )
    results = s.get_results()
    for user in results:
        logger.info("Found user: %s", user.get("displayName"))
        print("Volledige naam:", user.get("displayName"))
        print("Lid van:", user.get("memberOf"))
        print("OU:", user.get("distinguishedName"))
        print("SID:", user.get("objectSid"))
        print("Home-directory:", user.get("homeDirectory"))
        uac = user.get("userAccountControl", 0)
        status = "inactief" if int(uac) & 2 else "actief"
        print("Status:", status)
        print()
    return results
