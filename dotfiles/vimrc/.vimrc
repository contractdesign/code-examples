" set color scheme
colo elflord

" show statusbar
set laststatus=2

" automatically recognize markdown files
au BufNewFile,BufRead *.md setf markdown

" options for Python
" see https://stackoverflow.com/questions/65076/how-to-setup-vim-autoindentation-properly-for-editing-python-files-py
syntax on
set showmatch
set ts=4
set sts=4
set sw=4
set autoindent
set smartindent
set smarttab
set expandtab
