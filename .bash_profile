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
export PS1="\[\e[1;32m\]\W\[\e[0m\] \$ "
