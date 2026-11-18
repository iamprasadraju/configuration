from pathlib import Path
from config.helpers import targeted_tools_paths, get_backup_path, copy_tool_config, time_it

@time_it
def backup_action(tools: str | list) -> None:
  # get the local backup path based on os
  backup_path = get_backup_path()
  tools_info = targeted_tools_paths(get_paths=True) # consists of tool name and paths

  def backup_single_tool(tool_name: str, paths: list) -> None:
    if paths is None:
      print(f"Skipping {tool_name}: configuration unavailable")
      return

    tool_src_path, backup_name = paths
    tool_src_path = Path(tool_src_path)

    tool_backup_path = backup_path / backup_name
    # print(tool_backup_path)

    try:       
     copy_tool_config(tool_name, tool_src_path, tool_backup_path)
    except OSError as e:
     print(f"Backup failed for {tool_name}: {e}")


  if tools == ["all"]:
    for tool, paths in tools_info.items():
      backup_single_tool(tool, paths)
    return

  if len(tools) == 1:
    tool = tools[0]
    if tool not in tools_info:
      print(f"Unknown tool: {tool}")
      return
    else:
      backup_single_tool(tool, tools_info[tool])
  
  elif len(tools) > 1:
    for tool in tools:
      backup_single_tool(tool, tools_info[tool])
    return


if __name__ == "__main__":
  backup_action("all")
