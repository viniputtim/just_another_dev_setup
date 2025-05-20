#! /bin/bash

echo -n | xclip -selection clipboard
echo -n | xclip -selection primary
qdbus org.kde.klipper /klipper org.kde.klipper.klipper.clearClipboardHistory
