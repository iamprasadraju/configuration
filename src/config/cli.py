#!/usr/bin/env python3
import argparse
from config.helpers import targeted_tools_paths, user_confirm
from config.backup import backup_action

parser = argparse.ArgumentParser(description="")
subparsers = parser.add_subparsers(dest="command", required=True)


def backup_main():
  tools = targeted_tools_paths(get_tools=True)
  # subcommand: backup (device -> save config into config repo)
  parser = argparse.ArgumentParser(description="Backup config")
  parser.add_argument(
    "targets", nargs="+", choices = tools + ["all"], help="tools to back up"
  )
  
  args = parser.parse_args()
  tools = args.targets
  user_input = user_confirm("backup").strip()
  if user_input in ["y", "yes"]:  
    backup_action(tools)
  elif user_input in ["n", "no"]:
    exit()

def sync_main():
  tools = targeted_tools_paths(get_tools=True)
  # subcommand: sync (saved config -> device)
  parser = argparse.ArgumentParser(description="Sync config")
  parser.add_argument(
    "targets", nargs="+", choices = tools + ["all"], help="tools to sync"
  )

  args = parser.parse_args()
  print(args)

