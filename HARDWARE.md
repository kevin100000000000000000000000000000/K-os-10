# KOS 1.0 Hardware Compatibility

## Target classes

- AMD64 desktop systems with AMD or Intel processors
- HP Pavilion desktop systems
- UEFI and legacy-BIOS firmware
- SATA and NVMe internal storage
- USB drives, keyboard, and pointer devices
- Ethernet and common Wi-Fi devices
- HDMI displays and common USB/Bluetooth audio devices

## Packages and drivers

The image includes Linux firmware, AMD and Intel microcode, AMD graphics firmware,
Mesa Vulkan, Intel firmware packages, and common Realtek and Intel Wi-Fi firmware.
NVIDIA hardware is not assumed compatible by the default build. Users should select
a Debian-supported proprietary or open NVIDIA driver appropriate to the exact GPU
and kernel. Steam/Proton, Lutris, Wine, and Winetricks provide compatibility tooling
for Windows games; they do not execute Windows games natively.

## Reporting support

Before declaring a device supported, document firmware mode, GPU model, Wi-Fi
chipset, audio device, storage controller, ISO checksum, exact BIOS/UEFI version,
boot method, and install success. A successful KOS Live boot does not prove a
successful physical installation or full hardware support.
