from pyad import pyad


def init_connection(domain_controller="dc01", username="admin", password="Pa$$w0rd"):
    """Initialize connection to Active Directory using pyad defaults."""
    pyad.set_defaults(ldap_server=domain_controller, username=username, password=password)
    return True
