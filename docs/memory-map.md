# Memory map notes

Offsets live in `src/memory_adapter/offsets.py` and are tied to client
build `2026.01-r4`. On patch days run `scripts/dump_offsets.py` and
update the table. Ball array uses stride `0x40`, 16 slots.