#!/bin/sh

export PIRACYSHIELD_CONFIG_PATH="/config"
export PIRACYSHIELD_DATA_PATH="/data"
export PIRACYSHIELD_CACHE_PATH="/cache"
export PIRACYSHIELD_VERSION="ZERO"

exec "$@"
