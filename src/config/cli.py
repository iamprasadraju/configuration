#!/usr/bin/env python3
import argparse

from helpers import targeted_tools


parser = argparse.ArgumentParser(description="")
subparsers = parser.add_subparsers(dest="command", required=True)

# subcommand: backup (device -> save config into config repo)
backup_parser = subparsers.add_parser("backup", help="Back up local configs")
backup_parser.add_argument(
    "targets", nargs="+", choices=targeted_tools(), help="tools to back up"
)


# subcommand: sync (saved config -> device)
sync_parser = subparsers.add_parser("sync", help="sync configs")
sync_parser.add_argument(
    "targets", nargs="+", choices=targeted_tools(), help="tools to sync"
)

args = parser.parse_args()
print(args)
