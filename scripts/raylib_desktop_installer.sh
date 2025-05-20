#! /bin/bash

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
BLUE='\e[34m'
MAGENTA='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
RESET='\e[0m'


echo -e "installing ${GREEN}build-essential${RESET}, ${GREEN}cmake${RESET}, ${GREEN}pkg-config${RESET} and ${GREEN}git${RESET}"
sudo apt install -y build-essential cmake pkg-config git

echo -e "installing ${YELLOW}required libraries${RESET}"
sudo apt install -y libasound2-dev libx11-dev libxrandr-dev libxi-dev libgl1-mesa-dev libglu1-mesa-dev libxcursor-dev libxinerama-dev libwayland-dev libxkbcommon-dev

echo -e "cloning ${GREEN}raylib repository${RESET}"
git clone https://github.com/raysan5/raylib.git raylib

echo -e "entering ${CYAN}raylib directory${RESET}"
cd raylib

echo -e "creating and entering ${CYAN}build directory${RESET}"
mkdir build && cd build

echo -e "running ${YELLOW}cmake${RESET}"
cmake ..
# cmake -DBUILD_SHARED_LIBS=ON ..

echo -e "running ${GREEN}make${RESET}"
make

echo -e "making ${GREEN}installation${RESET}"
sudo make install

echo -e "updating ${YELLOW}dynamic linker cache${RESET}"
sudo ldconfig

echo -e "${GREEN}"
cat << "EOF"


                  _ _ _                                 
                 | (_) |                                
  _ __ __ _ _   _| |_| |__                              
 | '__/ _` | | | | | | '_ \                             
 | | | (_| | |_| | | | |_) |                            
 |_|  \__,_|\__, |_|_|_.__/                             
             __/ |                                      
  _         |___/      _ _          _                   
 (_)         | |      | | |        | |                  
  _ _ __  ___| |_ __ _| | | ___  __| |                  
 | | '_ \/ __| __/ _` | | |/ _ \/ _` |                  
 | | | | \__ \ || (_| | | |  __/ (_| |                  
 |_|_| |_|___/\__\__,_|_|_|\___|\__,_|                  
                                   __       _ _       _ 
                                  / _|     | | |     | |
  ___ _   _  ___ ___ ___  ___ ___| |_ _   _| | |_   _| |
 / __| | | |/ __/ __/ _ \/ __/ __|  _| | | | | | | | | |
 \__ \ |_| | (_| (_|  __/\__ \__ \ | | |_| | | | |_| |_|
 |___/\__,_|\___\___\___||___/___/_|  \__,_|_|_|\__, (_)
                                                 __/ |  
                                                |___/   


EOF
echo -e "${RESET}"
