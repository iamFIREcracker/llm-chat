# llm-chat

A lightweight CLI wrapper for `llm chat` that enhances the chat experience with interactive model/template selection and improved readline support.

## Features

- Fuzzy-select LLM models and templates using `fzf`
- Enhanced readline support and persistent command history via `rlwrap`
- Supports piping input to prepopulate the message prompt

## Requirements

- `llm`
- `fzf`
- `rlwrap`

## Installation

```bash
curl https://raw.githubusercontent.com/iamFIREcracker/llm-chat/main/llm-chat > ~/bin/llm-chat
chmod +x ~/bin/llm-chat
```

## Usage

```bash
# Interactive model/template selection
llm-chat

# Preselect model/template
llm-chat gpt-4

# Prepopulate the message prompt
cat ./llm-chat | llm-chat explain-code
```
