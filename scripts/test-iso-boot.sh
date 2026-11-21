#!/bin/bash
set -eu

ISO="${1:?Usage: test-iso-boot.sh /path/to/KOS.iso}"
OUT="${2:-/tmp/kos-qemu.log}"

command -v qemu-system-x86_64 >/dev/null
test -f "$ISO"

timeout 150s qemu-system-x86_64 \
  -machine accel=tcg \
  -m 2048 \
  -smp 2 \
  -nographic \
  -serial stdio \
  -monitor none \
  -no-reboot \
  -cdrom "$ISO" >"$OUT" 2>&1 || status=$?
status=${status:-0}

if grep -Eq "Reached target (Graphical Interface|Multi-User System)|KOS 1\.0|Debian GNU/Linux" "$OUT"; then
  echo "PASS: QEMU reached a KOS/Debian boot stage"
  exit 0
fi

echo "FAIL: QEMU did not reach a recognized boot stage (exit=$status)"
tail -n 80 "$OUT"
exit 1
