#!/bin/bash

END_HOUR=17
END_MINUTE=0

now_h=$(date +%H)
now_m=$(date +%M)

now_total=$((10#$now_h * 60 + 10#$now_m))
end_total=$((END_HOUR * 60 + END_MINUTE))

echo "Current time: $(date +%H:%M)"

if [ "$now_total" -ge "$end_total" ]; then
  echo "Work day already ended."
else
  remaining=$((end_total - now_total))
  echo "Work day ends after $((remaining/60)) hours and $((remaining%60)) minutes."
fi
