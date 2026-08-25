#!/bin/bash


# zsh
cp ~/.zshrc .zshrc

# tmux
cp ~/.tmux.conf .tmux.conf

# helix
mkdir -p helix/themes
cp ~/.config/helix/config.toml ~/.config/helix/languages.toml helix/
cp -r ~/.config/helix/themes/* helix/themes/

# kitty
mkdir -p kitty
cp ~/.config/kitty/diff.conf ~/.config/kitty/kitty.conf ~/.config/kitty/open-actions.conf kitty/

# brew
#bash brew/dump.sh

# git
cp ~/.gitconfig ~/repos/configuration/.gitconfig

echo "Dump complete"
