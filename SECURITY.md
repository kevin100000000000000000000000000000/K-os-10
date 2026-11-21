# KOS 1.0 Security

## Security model

- Normal accounts receive `sudo` access only when locally authorized.
- UFW starts with default-deny incoming and default-allow outgoing policies.
- Package installation uses APT and explicit Polkit authentication.
- Calamares retains Debian partition and account security behavior.
- KOS does not disable kernel security features or signed boot enforcement.

## Credentials

KOS AI stores provider URL and model in `~/.config/kos-ai/config.json` with
mode `0600`. API keys are stored through the system keyring when available;
otherwise they are stored in `~/.config/kos-ai/api-key` with mode `0600`.
API keys must never be committed to source control.

## Updates

Use KOS Update Center or `sudo apt-get update && sudo apt-get dist-upgrade`.
Debian stable security repositories are configured by Live Build. Automatic
security updates are optional and should be enabled through package selection
and unattended-upgrades policy if required by the organization.

## Safe package installation

KOS Store only submits package operations to APT for catalog entries and requires
normal privilege elevation. Removing or installing packages can affect system
dependencies, and the user must review the privilege prompt.
