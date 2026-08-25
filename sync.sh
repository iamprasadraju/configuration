#!/bin/bash

# zsh
cp .zshrc ~/.zshrc

# tmux
cp .tmux.conf ~/.tmux.conf

# helix
cp helix/config.toml helix/languages.toml ~/.config/helix/
cp -r helix/themes/* ~/.config/helix/themes/

# kitty
cp kitty/diff.conf kitty/kitty.conf kitty/open-actions.conf ~/.config/kitty/

# brew
#xargs brew install < brew/leaves
#xargs brew install --cask < brew/casks

# git
cp .gitconfig ~/.gitconfig

echo "Sync complete"
