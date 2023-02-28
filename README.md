# checkm8_toolbox
a toolbox for checkm8 exploit
<h1 align="center">
   
    checkm8 toolbox
</h1>
<h3 align="center">This is a checkm8 toolbox (ios 12.x-16.x) form Laurin226</h3>
<p align="center">
    <strong><a href="CHANGELOG.md">Change Log</a></strong>
    •
    <strong><a href="https://twitter.com/palera1n">Twitter</a></strong>
    •
    <strong><a href="https://twitter.com/laurin2261">My Twitter</a></strong>
<h3 align="center">This gui was made with <strong><a href="https://github.com/bartektenDev/Python3MacApp-LearnerTemplate">Python3MacApp LearnerTemplate</a></strong> from @ios_euphoria </h3>
<h3 align="center">On ios 16.x you have to enable developer mode (before you can enable it, you must sideload an app)</h3>
<h3 align="center">On A11 and A10 devices you must disable passcode, on ios 16 you must never set a passcode, if you had a passcode you have to restore with itunes</h3>
<h3 align="center">Here you can download the Palera1n loader ipa: <strong><a href="https://nightly.link/palera1n/loader/workflows/build/main/palera1n.zip">Palera1n.ipa</a></strong></h3>
<h3 align="center">How does it work: It boots the device with multiple patches required. On first run, it'll boot a ramdisk which dumps your onboard blob, creates a fakefs (if using semi tethered), installs the loader app, and patches your kernel. </h3>

# Credits

Python3MacApp LearnerTemplate creator: 
<strong><a href="https://github.com/bartektenDev">ios_euphoria</a></strong>

Original palera1n credits:
- [Nathan](https://github.com/verygenericname)
    - The ramdisk that dumps blobs, installs pogo to tips app, and duplicates rootfs is a slimmed down version of [SSHRD_Script](https://github.com/verygenericname/SSHRD_Script)
    - For modified [restored_external](https://github.com/verygenericname/sshrd_SSHRD_Script)
    - Also helped Mineek getting the kernel up and running and with the patches
    - Helping with adding multiple device support
    - Fixing issues relating to camera.. etc by switching to fsboot
    - [iBoot64Patcher fork](https://github.com/verygenericname/iBoot64Patcher)
- [Mineek](https://github.com/mineek)
    - For the patching and booting commands
    - Adding tweak support
    - For patchfinders for RELEASE kernels
    - [Kernel15Patcher](https://github.com/mineek/PongoOS/tree/iOS15/checkra1n/Kernel15Patcher)
    - [Kernel64Patcher](https://github.com/mineek/Kernel64Patcher)
- [Amy](https://github.com/elihwyma) for the [Pogo](https://github.com/elihwyma/Pogo) app
- [checkra1n](https://github.com/checkra1n) for the base of the kpf
- [nyuszika7h](https://github.com/nyuszika7h) for the script to help get into DFU
- [the Procursus Team](https://github.com/ProcursusTeam) for the amazing [bootstrap](https://github.com/ProcursusTeam/Procursus)
- [F121](https://github.com/F121Live) for helping test
- [m1sta](https://github.com/m1stadev) for [pyimg4](https://github.com/m1stadev/PyIMG4)
- [tihmstar](https://github.com/tihmstar) for [pzb](https://github.com/tihmstar/partialZipBrowser)/original [iBoot64Patcher](https://github.com/tihmstar/iBoot64Patcher)/original [liboffsetfinder64](https://github.com/tihmstar/liboffsetfinder64)/[img4tool](https://github.com/tihmstar/img4tool)
- [xerub](https://github.com/xerub) for [img4lib](https://github.com/xerub/img4lib) and [restored_external](https://github.com/xerub/sshrd) in the ramdisk
- [Cryptic](https://github.com/Cryptiiiic) for [iBoot64Patcher](https://github.com/Cryptiiiic/iBoot64Patcher) fork, and [liboffsetfinder64](https://github.com/Cryptiiiic/liboffsetfinder64) fork
- [libimobiledevice](https://github.com/libimobiledevice) for several tools used in this project (irecovery, ideviceenterrecovery etc), and [nikias](https://github.com/nikias) for keeping it up to date
- [Nick Chan](https://github.com/asdfugil) general help with patches.
- [Sam Bingner](https://github.com/sbingner) for [Substitute](https://github.com/sbingner/substitute)
- [Serena](https://github.com/SerenaKit) for helping with boot ramdisk.

<div class="section">
        <h2>Credits</h2>

        <div><h3>Made by</h3>
            <div class="credits-section"><a href="https://twitter.com/intent/follow?screen_name=_argp" target="_blank"><img src="/img/credits/_argp.png" referrerpolicy="no-referrer" /> <span>argp</span></a><a href="https://twitter.com/intent/follow?screen_name=aunali1" target="_blank"><img src="/img/credits/aunali1.png" referrerpolicy="no-referrer" /> <span>aunali1</span></a><a href="https://twitter.com/intent/follow?screen_name=axi0mX" target="_blank"><img src="/img/credits/axi0mX.png" referrerpolicy="no-referrer" /> <span>axi0mX</span></a><a href="https://twitter.com/intent/follow?screen_name=DanyL931" target="_blank"><img src="/img/credits/DanyL931.png" referrerpolicy="no-referrer" /> <span>Dany Lisiansky</span></a><a href="https://twitter.com/intent/follow?screen_name=Jaywalker" target="_blank"><img src="/img/credits/Jaywalker.png" referrerpolicy="no-referrer" /> <span>Jaywalker</span></a><a href="https://twitter.com/intent/follow?screen_name=hbkirb" target="_blank"><img src="/img/credits/hbkirb.png" referrerpolicy="no-referrer" /> <span>Adam Demasi</span></a><a href="https://twitter.com/intent/follow?screen_name=h0m3us3r" target="_blank"><img src="/img/credits/h0m3us3r.png" referrerpolicy="no-referrer" /> <span>h0m3us3r</span></a><a href="https://twitter.com/intent/follow?screen_name=littlelailo" target="_blank"><img src="/img/credits/littlelailo.png" referrerpolicy="no-referrer" /> <span>littlelailo</span></a><a href="https://twitter.com/intent/follow?screen_name=MCMrARM" target="_blank"><img src="/img/credits/MCMrARM.png" referrerpolicy="no-referrer" /> <span>MrARM</span></a><a href="https://twitter.com/intent/follow?screen_name=never_released" target="_blank"><img src="/img/credits/never_released.png" referrerpolicy="no-referrer" /> <span>Longhorn</span></a><a href="https://twitter.com/intent/follow?screen_name=nitoTV" target="_blank"><img src="/img/credits/nitoTV.png" referrerpolicy="no-referrer" /> <span>nitoTV</span></a><a href="https://twitter.com/intent/follow?screen_name=jamiebishop123" target="_blank"><img src="/img/credits/jamiebishop123.png" referrerpolicy="no-referrer" /> <span>Jamie Bishop</span></a><a href="https://twitter.com/intent/follow?screen_name=pimskeks" target="_blank"><img src="/img/credits/pimskeks.png" referrerpolicy="no-referrer" /> <span>pimskeks</span></a><a href="https://twitter.com/intent/follow?screen_name=qwertyoruiopz" target="_blank"><img src="/img/credits/qwertyoruiopz.png" referrerpolicy="no-referrer" /> <span>qwertyoruiopz</span></a><a href="https://twitter.com/intent/follow?screen_name=sbingner" target="_blank"><img src="/img/credits/sbingner.png" referrerpolicy="no-referrer" /> <span>Sam Bingner</span></a><a href="https://twitter.com/intent/follow?screen_name=su_rickmark" target="_blank"><img src="/img/credits/su_rickmark.png" referrerpolicy="no-referrer" /> <span>Rick Mark</span></a><a href="https://twitter.com/intent/follow?screen_name=s1guza" target="_blank"><img src="/img/credits/s1guza.png" referrerpolicy="no-referrer" /> <span>Siguza</span></a></div><h3>Thanks to</h3>
            <div class="credits-section"><a href="https://twitter.com/intent/follow?screen_name=kjchaifisch" target="_blank"><img src="/img/credits/kjchaifisch.png" referrerpolicy="no-referrer" /> <span>Dylan Laws</span></a><a href="https://twitter.com/intent/follow?screen_name=jndok" target="_blank"><img src="/img/credits/jndok.png" referrerpolicy="no-referrer" /> <span>jndok</span></a><a href="https://twitter.com/intent/follow?screen_name=JonathanSeals" target="_blank"><img src="/img/credits/JonathanSeals.png" referrerpolicy="no-referrer" /> <span>Jonathan Seals</span></a><a href="https://twitter.com/intent/follow?screen_name=xerub" target="_blank"><img src="/img/credits/xerub.png" referrerpolicy="no-referrer" /> <span>xerub</span></a><a href="https://twitter.com/intent/follow?screen_name=littlesteve" target="_blank"><img src="/img/credits/littlesteve.png" referrerpolicy="no-referrer" /> <span>Steve</span></a><a href="https://twitter.com/intent/follow?screen_name=iBSparkes" target="_blank"><img src="/img/credits/iBSparkes.png" referrerpolicy="no-referrer" /> <span>PsychoTea</span></a><a href="https://twitter.com/intent/follow?screen_name=Simone_Ferrini" target="_blank"><img src="/img/credits/Simone_Ferrini.png" referrerpolicy="no-referrer" /> <span>Simone Ferrini</span></a><a href="https://twitter.com/intent/follow?screen_name=ihackbanme" target="_blank"><img src="/img/credits/ihackbanme.png" referrerpolicy="no-referrer" /> <span>ihackbanme</span></a><a href="https://twitter.com/intent/follow?screen_name=iH8sn0w" target="_blank"><img src="/img/credits/iH8sn0w.png" referrerpolicy="no-referrer" /> <span>iH8sn0w</span></a><a href="https://twitter.com/intent/follow?screen_name=cjori" target="_blank"><img src="/img/credits/cjori.png" referrerpolicy="no-referrer" /> <span>Ori Kadosh</span></a><a href="https://twitter.com/intent/follow?screen_name=r0nyrus" target="_blank"><img src="/img/credits/r0nyrus.png" referrerpolicy="no-referrer" /> <span>Rony Kelner</span></a></div><h3>Website by</h3>
            <div class="credits-section"><a href="https://twitter.com/intent/follow?screen_name=aydenpanhuyzen" target="_blank"><img src="/img/credits/aydenpanhuyzen.png" referrerpolicy="no-referrer" /> <span>Ayden Panhuyzen</span></a></div></div>
    </div>
</p>
