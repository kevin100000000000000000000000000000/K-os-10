# Installing KOS 1.0

## Before installation

- Back up all data. KOS Calamares shows the selected disk and will warn before
  formatting or erasing it.
- The installer may use an entire selected disk or guided partitioning.
- Confirm that UEFI is enabled for a UEFI installation. Legacy BIOS is supported
  by the ISO hybrid bootloader where firmware permits.
- Minimum tested target: AMD64, 12 GB storage, and 2 GB RAM.

## Boot the Live ISO

1. Write the ISO to USB with Rufus, GNOME Disks, or `dd`.
2. Set the firmware to boot the USB device.
3. Choose **KOS 1.0 Live** from the boot menu.
4. Use **Install KOS** from the desktop.

## Installation

Calamares asks for locale, keyboard layout, disk selection, partition layout,
account details, timezone, network, and bootloader location. Review the summary
before clicking Install. Internet access is used for package operations only
where requested.

To install onto USB storage, select that USB disk explicitly. The host BIOS must
then support booting the external device. External installs consume the selected
disk and should not be used as data-only drives.

## Recovery

Boot the Live ISO and use GParted, TestDisk, firmware boot menus, or a rescue
shell. KOS does not replace a separate backup policy. UEFI boot entries can be
regenerated with GRUB and the EFI System Partition by a repair shell.
