export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="avit"

plugins=(
  git 
)

source $ZSH/oh-my-zsh.sh

aider:base() {
    aider \
        --pretty \
        --stream \
        --map-tokens 2048 \
        --editor nvim \
        --notifications \
        --dark-mode \
        --no-show-model-warnings \
        --no-auto-commits \
        --no-dirty-commits \
        --edit-format diff \
        "$@"
}


a(){
  aider:base \
        --model "openai/DeepSeek-V3.2-Exp" \ 
        "$@"

}

aider:ollama() {
    local selected_model=$(ollama list | awk 'NR>1 {print $1}' | fzf --prompt="Select a model: ")

    [[ -n "$selected_model" ]] && \
        aider:base \
            --model "ollama_chat/$selected_model" \
            "$@"
}


export OPENAI_API_BASE=https://agent.api.url
export OPENAI_API_KEY=key

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
alias lt='eza --tree --level=1 --color=always --group-directories-first --icons'
alias l.="eza -a | grep -E '^\.'"


alias p='pnpm'
alias px='pnpx'

alias py='python'

alias tor="sudo systemctl restart tor"
alias tor:q="sudo systemctl stop tor"
alias tor:s="sudo systemctl status tor"

alias doce="sudo systemctl start docker.service"
alias doce:q="sudo systemctl stop docker.service"

alias hypr="cd ~/.config/hypr/ && nv"
alias ray="sudo systemctl start xray"

alias dpi="sudo systemctl start zapret"
alias dpi:q="sudo systemctl stop zapret"

alias kycn="cd ~/Desktop/anivite/ && nv"
alias chad="cd ~/.config/nvim/ && nv"
