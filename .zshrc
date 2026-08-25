# Enable CLI colors
export CLICOLOR=1

#export LSCOLORS=GxFxCxDxBxegedabagaced   # customize ls colors (optional)

# Prompt
export PROMPT='Jarvis:%F{green}%~%f $ '

# Default editor
export EDITOR='vim'

# PATH additions
export PATH="$HOME/bin:$PATH"
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
export PATH="/opt/homebrew/opt/llvm/bin:$PATH"

# micropython
alias mp='mpremote'

alias notebook="jupyter notebook"
alias rstudio='open -a RStudio'
alias activate='source .venv/bin/activate'

alias code='codium'
alias hgrep="kitten hyperlinked_grep"
alias icat="kitten icat"

