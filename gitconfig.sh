#!/bin/bash

git config --global user.name "iamprasadraju"
git config --global user.email "gls.prasadraju@gmail.com"
git config --global gpg.format "ssh"
git config --global user.signingkey "/Users/jarvis/.ssh/github.pub"

git config --global commit.gpgsign true

# aliases
git config --global alias.st "status"
git config --global alias.br "branch"

# cat
git config --global --list