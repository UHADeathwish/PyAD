# PyAD Automation

This project contains a set of helper scripts for automating basic Active Directory
tasks such as onboarding and offboarding users. The code relies on the `pyad`
package and interacts with Windows commands like `icacls` for NTFS permissions.

## Structure

```
ad_automation/
├── add_group.py        # create groups and folders
├── add_user.py         # create users and home folders
├── connection.py       # initialise pyad connection
├── logger.py           # logging configuration
├── main.py             # command line interface
├── migrate_folders.py  # create missing home folders
├── offboard_user.py    # disable users and archive data
├── search_user.py      # query user information
├── utils.py            # helper utilities
└── logs/
    └── script.log      # log file (created at runtime)
```

Run `python -m ad_automation.main --help` for available commands.
