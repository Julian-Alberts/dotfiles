set relativenumber
set number
set foldmethod=syntax
set foldlevel=10
set expandtab
set shiftwidth=4

call plug#begin('~/.vim/plugged')
let g:vimspector_enable_mappings = 'HUMAN'
let g:tex_flavor = 'latex'

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tomasiser/vim-code-dark'
Plug 'preservim/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'ryanoasis/vim-devicons'
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
Plug 'scrooloose/nerdtree-project-plugin'
Plug 'puremourning/vimspector'
Plug 'tyru/open-browser.vim'
Plug 'aklt/plantuml-syntax'
Plug 'weirongxu/plantuml-previewer.vim'
Plug 'luochen1990/rainbow'
Plug 'lervag/vimtex'


let g:rainbow_active = 1
call plug#end()
colorscheme codedark

nmap <F2> <Plug>(coc-rename)
nmap <F3> <Plug>(coc-definition)

" Use K to show documentation in preview window
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

