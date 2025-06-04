syntax on
set tabstop=2
set shiftwidth=2
set expandtab
set ai
set number
set hlsearch
set ruler
highlight Comment ctermfg=green

" Auto-save when losing focus or leaving insert mode
autocmd FocusLost,InsertLeave * silent! update