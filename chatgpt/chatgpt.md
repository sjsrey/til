# Enabling chatGPT at the cli

> tgpt is a cross-platform command-line interface (CLI) tool that allows you to use ChatGPT 3.5 in your Terminal without requiring API keys.

## Installing

```
curl -sSL https://raw.githubusercontent.com/aandrew-me/tgpt/main/install | bash
-s /usr/local/bin
```

## Using

```
Usage: tgpt [Flag] [Prompt]

Flags:
-s, --shell                                        Generate and Execute shell
commands. (Experimental) 
-c, --code                                         Generate Code. (Experimental)
-q, --quiet                                        Gives response back without
loading animation
-w, --whole                                        Gives response back as a
whole text

Options:
-f, --forget                                       Forget Chat ID 
-v, --version                                      Print version 
-h, --help                                         Print help message 
-i, --interactive                                  Start normal interactive mode 
-m, --multiline                                    Start multi-line interactive
mode 
-cl, --changelog                                   See changelog of versions 
-u, --update                                       Update program 

Examples:
tgpt "What is internet?"
tgpt -f
tgpt -m
tgpt -s "How to update my system?"

```

[Source](https://github.com/aandrew-me/tgpt)

