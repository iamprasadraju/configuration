#!/usr/bin/env python3
from config.helpers import targeted_tools_paths
import argparse

parser = argparse.ArgumentParser(description="")
subparsers = parser.add_subparsers(dest="command", required=True)

tools = targeted_tools_paths(get_tools=True)

def backup_main():
  # subcommand: backup (device -> save config into config repo)
  parser = argparse.ArgumentParser(description="Backup config")
  parser.add_argument(
    "targets", nargs="+", choices=tools, help="tools to back up"
  )
  args = parser.parse_args()
  print(args)

def sync_main():
  # subcommand: sync (saved config -> device)
  parser = argparse.ArgumentParser(description="Sync config")
  parser.add_argument(
    "targets", nargs="+", choices=tools, help="tools to sync"
  )

  args = parser.parse_args()
  print(args)
