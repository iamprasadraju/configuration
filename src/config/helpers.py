import platform
import shutil
from pathlib import Path

def get_os() -> str: return platform.system()

# structure {os: {tool: [system_config_path, save_config_path]}}
def targeted_tools_paths(get_tools = None, get_paths = None) -> dict | list:
  os = get_os()
  sys_home_dirpath = Path().home()
  
  tools_paths = {
    "Darwin": {
      "git"   : [sys_home_dirpath / ".gitconfig",  ".gitconfig"],
      "helix" : [sys_home_dirpath / ".config/helix/", "helix"], 
      "kitty" : [sys_home_dirpath / ".config/kitty", "kitty"],
      "zsh"   : [sys_home_dirpath / ".zshrc", ".zshrc"],
      "vim"   : [sys_home_dirpath / ".vimrc", ".vimrc"], 
      "tmux"  : [sys_home_dirpath / ".tmux.conf", ".tmux.conf"],
      "zed"  : ["", ""],
      
      # list casks: brew list --casks
      # list leaves: brew leaves
      # path not required, for brew we only need get casks, leaves
      "brew" : ["", ""],
    },
    
    "Windows": {"": []},
    "Linux": {"": []}
  }

  if os not in tools_paths:
    raise ValueError(f"{os} is not supported!")

  if get_tools:
    return tools_paths[os].keys()
  if get_paths:
    return tools_paths[os]


def get_backup_path():
  os_name = get_os()

  root_backup_path = Path(__file__).resolve().parents[2] # cd ../.. for cwd
  if os_name == "Darwin":
    return root_backup_path / "mac"

  elif os_name == "Linux":
    return root_backup_path / "linux"

  elif os_name == "Windows":
    return root_backup_path / "windows"


def copy_tool_config(tool: str, source: Path, destination: Path) -> None:
  if source.is_dir():
    shutil.copytree(source, destination, dirs_exist_ok=True)
    print(f"{tool} backup done !")
        
  elif source.is_file():
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    print(f"{tool} backup done !")

  else: print(f"Skipping: {source} does not exist")

     

if __name__ == "__main__":
  os_name = get_os()
  tools = targeted_tools_paths(get_paths=True)

  #print(os_name)
  print(tools)
