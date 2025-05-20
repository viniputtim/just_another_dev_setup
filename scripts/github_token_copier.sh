#! /bin/bash

7z x /home/vinicius/Desenvolvimento/.secrets/github_token.7z -p"$GITHUB_TOKEN_FILE_PASSWORD"
cat github_token.txt | tr -d '\n' | xclip -selection clipboard
rm -rf github_token.txt
