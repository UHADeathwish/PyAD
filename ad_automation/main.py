import argparse
from .connection import init_connection
from .add_user import add_user
from .offboard_user import offboard_user
from .add_group import add_group
from .search_user import search_user
from .migrate_folders import migrate_all
from .logger import setup_logger


def main():
    setup_logger()
    init_connection()

    parser = argparse.ArgumentParser(description="AD automatiseringstool")
    subparsers = parser.add_subparsers(dest="action")

    parser_add = subparsers.add_parser("adduser")
    parser_add.add_argument("--username", required=True)
    parser_add.add_argument("--fullname", required=True)
    parser_add.add_argument("--group", required=True)

    parser_group = subparsers.add_parser("addgroup")
    parser_group.add_argument("--groupname", required=True)

    parser_off = subparsers.add_parser("offboard")
    parser_off.add_argument("--username", required=True)

    parser_search = subparsers.add_parser("search")
    parser_search.add_argument("--query", required=True)

    parser_migrate = subparsers.add_parser("migrate")

    args = parser.parse_args()

    if args.action == "adduser":
        add_user(args.username, args.fullname, args.group)
    elif args.action == "offboard":
        offboard_user(args.username)
    elif args.action == "addgroup":
        add_group(args.groupname)
    elif args.action == "search":
        search_user(args.query)
    elif args.action == "migrate":
        migrate_all()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
