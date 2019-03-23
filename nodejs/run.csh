#!/bin/bash
rm -f *.log

node \
--logfile_per_isolate \
--log_api \
--log_function_events \
--log_code \
test.js

# --log_all
# can remove tick with internal_timer_events
#--log_timer_events \
#--log_internal_timer_events \

# too verbose
#--sodium \
