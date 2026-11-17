import platform
import shutil
from pathlib import Path
from functools import wraps
import time

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
      "zed"  : None,
      
      # list casks: brew list --casks
      # list leaves: brew leaves
      # path not required, for brew we only need get casks, leaves
      "brew" : None,
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


def copy_tool_config(tool: str, source_path: Path, destination_path: Path) -> None:
  if not source_path.exists():
    print(f"Skipping {tool_name}: source not found")
    return
  
  if source_path.is_dir():
    shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
    print(f"{tool} backup done !")
        
  elif source_path.is_file():
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, destination_path)
    print(f"{tool} backup done !")

  else: print(f"Skipping: {source} does not exist")


def time_it(func):
  GREEN = "\033[92m"
  RESET = "\033[0m"

  @wraps(func)
  def wrapper(*args, **kwargs):
    start_time = time.perf_counter_ns()
    result = func(*args, **kwargs)
    end_time = time.perf_counter_ns()

    time_taken =  (end_time - start_time) * 1e-6  # nanoseconds -> milli seconds
    print(f"{GREEN}\nFinished in {time_taken} ms{RESET}")
    return result
    
  return wrapper

if __name__ == "__main__":
  os_name = get_os()
  tools = targeted_tools_paths(get_paths=True)

  #print(os_name)
  print(tools)
