# Start SSH Agent if not already running
if [ -z "$SSH_AUTH_SOCK" ]; then
    eval "$(ssh-agent -s)" &>/dev/null
    ssh-add ~/.ssh/Github_Avenger &>/dev/null
fi

# Set custom prompt
export PS1="\[\e[1;32m\]\W\[\e[0m\] \$ "
