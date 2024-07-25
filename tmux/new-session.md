# Creating and switching to a new tmux-session

Add this to `~/.tmux.conf`

```

# new session
# Bind a key to create a new session with a prompt for the name
bind-key C-n command-prompt -p "New session name:" "new-session -s '%%'; switch-client -t '%%'"

```

Now, when I'm in a session and need a clean new session, `C-a C-n` prompts me for the name, and once I enter that, I've added a new session that I'm now in
