# Deprecated

See [eve2clab](https://github.com/kaelemc/eve2clab)

# eve-ng-config-extractor

Extract device configs from EVE-NG `.unl` files. Meant for Cisco configs only, may work with other vendors with some modification.

> Device configs MUST have a hostname. The hostname from the config is used to name the exported config file.

## Usage

- Place config next to `parse.py` (in same directory).
- edit `filename` variable in `parse.py` to the exact name of the unl file you want to extract configs from.
- Execute `python parse.py`.
- Export directory will be created and exported configs can be found.
