#!/bin/bash

sh -c "echo powersave > /sys/devices/system/cpu/cpu2/cpufreq/scaling_governor"
sh -c "echo 1 > /sys/devices/system/cpu/intel_pstate/no_turbo"
sh -c "echo 10 > /sys/devices/system/cpu/intel_pstate/min_perf_pct"
sh -c "echo 10 > /sys/devices/system/cpu/intel_pstate/max_perf_pct"
