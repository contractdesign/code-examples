#!/bin/bash

tmux -2 new-session -s devel -d
tmux split-window -h

tmux select-pane -t 1
tmux split-window -v


#tmux new-window
#tmux rename-window blog
#tmux 
#tmux select-pane -t 0
#tmux split-window -p 66
#tmux split-window -d
#tmux split-window -h
