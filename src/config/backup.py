from pathlib import Path
from helpers import targeted_tools_paths, get_backup_path, copy_tool_config


def set_backup(tool: str) -> None:
  # get the local backup path based on os
  backup_path = get_backup_path()
  tools_info = targeted_tools_paths(get_paths=True) # consists of tool name and paths

  if tool == "all":
    for tool, (tool_src_path, backup_name) in tools_info.items():
      tool_src_path = Path(tool_src_path)

      # skip if paths not exists
      if not tool_src_path or not backup_name:
        print(f"Skipping {tool}: configuration unavailable")
        continue

      # checks whether we have tool config in system
      if not tool_src_path.exists():
        print(f"Skipping {tool}: source not found")
        continue
        
      # backup_name can be dir or file
      tool_backup_path = backup_path / backup_name

      try:
        copy_tool_config(tool, tool_src_path, tool_backup_path)
      except OSError as e:
                print(f"Backup failed for {tool}: {e}")
        
    return 
      
  if tool not in tools_info:
    print(f"Unknown tool: {tool}")
    return

  tool_src_path, backup_name = tools_info[tool]
  if not tool_src_path.exists():
    print(f"Source not found: {tool_src_path}")
    return
  
  tool_backup_path = backup_path / backup_name
  try:
    copy_tool_config(tool, tool_src_path, tool_backup_path)
  except OSError as e:
    print(f"Backup failed for {tool}: {e}")
  
if __name__ == "__main__":
  set_backup("all")
