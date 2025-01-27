export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="avit"

plugins=(
  git 
)

source $ZSH/oh-my-zsh.sh

alias nv="nvim"
alias cls="clear"
alias :q="exit"
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
alias kycn="cd ~/Desktop/kycn/ && nv"
alias chad="cd ~/.config/nvim/ && nv"

alias cat="bat"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# pnpm
export PNPM_HOME="/home/csw/.local/share/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end
