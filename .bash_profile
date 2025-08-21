# Make __git_ps1 faster (only show branch name)
GIT_PS1_SHOWDIRTYSTATE=
GIT_PS1_SHOWSTASHSTATE=
GIT_PS1_SHOWUPSTREAM=


# Start SSH Agent if not already running
if [ -z "$SSH_AUTH_SOCK" ]; then
    eval "$(ssh-agent -s)" &>/dev/null
    ssh-add ~/.ssh/Github_Avenger &>/dev/null
fi

# Save/restore last directory
LAST_DIR="$HOME/.last_dir"
if [ -f "$LAST_DIR" ] && [ -d "$(cat "$LAST_DIR")" ]; then
    cd "$(cat "$LAST_DIR")"
fi

# Override 'cd' to auto-save dir
cd() {
    builtin cd "$@" && pwd > "$LAST_DIR"
}

# Set custom prompt

# entire pwd
# export PS1="\[\e[1;32m\]\w\[\e[0m\] \$ "

# lastdir
# export PS1="\[\e[1;32m\]\W\[\e[0m\] \$ "
export PS1="\[\e[1;37m\]iamprasadraju:~\[\e[1;32m\]\$(basename \$(dirname \"\$PWD\"))/\W\[\e[0m\] \$ "

PROMPT_COMMAND='echo -ne "\033]0;JARVIS\007"'

# --- Fast Git branch detection ---
parse_git_branch() {
  if [ -d .git ]; then
    ref=$(<.git/HEAD)
    if [[ $ref == ref:\ refs/heads/* ]]; then
      echo " (${ref#*heads/})"
    fi
  fi
}


# --- Custom prompt with Git branch in brackets ---
export PS1="\[\e[1;37m\]iamprasadraju:~\[\e[1;32m\]\$(basename \$(dirname \"$PWD\"))/\W\[\e[0;33m\]\$(parse_git_branch)\[\e[0m\] \$ "

