import platform
from pathlib import Path

def getos() -> str: return platform.system()

# structure {os: {tool: [system_config_path, save_config_path]}}
def targeted_tools_and_paths(get_tools = None, get_paths = None) -> dict | list:
  os = getos()
  sys_home_dirpath = Path().home()
  
  tools_paths = {
    "Darwin": {
      "git"   : [sys_home_dirpath / ".gitconfig",  ".gitconfig"],
      "helix" : [sys_home_dirpath / ".config/helix/", "/helix"], 
      "kitty" : [sys_home_dirpath / ".config/kitty", "/kitty"],
      "zsh"   : [sys_home_dirpath / ".zshrc", ".zshrc"],
      "vim"   : [sys_home_dirpath / ".vimrc", ".vimrc"], 
      "tmux"  : [sys_home_dirpath / ".tmux.conf", ".tmux.conf"],
      "zed"  : [],
      
      # list casks: brew list --casks
      # list leaves: brew leaves
      # path not required, for brew we only need get casks, leaves
      "brew" : [],
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

# create paths requires to save config into according dirs
def setup_config_save_paths() -> None:
  root_backup_path = Path(__file__).resolve().parents[2] # cd ../.. for cwd
  
  if get_os() == "Darwin":
    mac_backup_path = Path(root_backup_path / "mac")
    mac_backup_path.mkdir(parents=True, exist_ok=True)
         
  elif get_os() == "Windows":
    window_backup_path = Path(root_backup_path / "windows")
    window_backup_path.mkdir(parents=True, exist_ok=True)
    
  elif get_os() == "Linux":
    linux_backup_path = Path(root_save_path / "linux")
    linux_backup_path.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
  os_name = getos()
  tools = targeted_tools_and_paths(get_paths=True)

  print(os_name)
  print(tools)
