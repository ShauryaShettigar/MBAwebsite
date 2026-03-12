#!/bin/bash
export PATH="$HOME/.local/node-v22.14.0-darwin-x64/bin:$PATH"
cd "$(dirname "$0")"
exec npx vite --host
