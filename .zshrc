export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="avit"

plugins=(
  git 
)

source $ZSH/oh-my-zsh.sh

export OPENAI_API_KEY=CHANGE_ME

alias nv="nvim"
alias cls="clear"
alias :q="exit"
alias :qa="tmux kill-server"
alias yy="yazi"
alias ls='eza --color=always --group-directories-first --icons --tree --level=1'
alias ll='eza -la --icons --octal-permissions --group-directories-first'
alias l='eza -bGF --header --git --color=always --group-directories-first --icons'
alias llm='eza -lbGd --header --git --sort=modified --color=always --group-directories-first --icons' 
alias la='eza --long --all --group --group-directories-first'
alias lx='eza -lbhHigUmuSa@ --time-style=long-iso --git --color-scale --color=always --group-directories-first --icons'

alias lS='eza -1 --color=always --group-directories-first --icons'
alias lt='eza --tree --level=2 --color=always --group-directories-first --icons'
alias l.="eza -a | grep -E '^\.'"

alias p='pnpm'
alias px='pnpx'
alias doce="sudo systemctl start docker.service"

alias hypr="cd ~/.config/hypr/ && nv"
alias ray="sudo systemctl start xray"
alias dpi="sudo systemctl start zapret"
alias kycn="cd ~/Desktop/anivite/ && nv"
alias chad="cd ~/.config/nvim/ && nv"
