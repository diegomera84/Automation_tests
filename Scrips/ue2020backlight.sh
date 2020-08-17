#!/bin/bash

# This script sets the backlight level for the two kind of display (eDP and HDMI)
# It also persists the last setting, storing it in a file.
# After restarting it is possible to reapply the last setting with the -get
# parameter.
# New parameters are added for turn on and off the display without changing the 
# stored value.

 if [ ! $# -eq 2 ] && [ ! $# -eq 3 ]; then
	 echo "Usage: $0 edp|hdmi -get|-set <value>|on|off"
	 echo "where:"
	 echo "        edp Display connected on eDP port"
	 echo "        hdmi Display connected on HDMI port"
     echo "        -get Read the backlight value stored and apply to current settings"
	 echo "        -set <value> Store the backlight value and apply to current settings"
	 echo "        on Turn on display using the last stored setting"
	 echo "        off Turn off display without changing the last stored setting"
	 exit 1
 fi

 if [ ! "$1" == "edp" ] && [ ! "$1" == "hdmi" ]; then
    echo "Error: display \"$1\" is not valid"
	exit 1
 fi

 if [ "$1" == "edp" ]; then 
	 if [[ ${EUID} -ne 0 ]]; then
        echo "Root permission are required. Please run $0 using sudo"
        exit 1
     fi

	 MAXVAL=$(cat /sys/class/backlight/intel_backlight/max_brightness)
	 VALUEFILE=/var/backlight/value
 else
	 MAXVAL=100
	 VALUEFILE=/var/backlight/hdmivalue
 fi

 if [ -f $VALUEFILE ]; then
    VAL=$(cat $VALUEFILE)
    if [ "$2" == "-get" ]; then
		if [ "$1" == "edp" ]; then
			echo "$VAL" > /sys/class/backlight/intel_backlight/brightness
		else
			if [[ ${EUID} -eq 0 ]]; then
				cp $(ps auxxw |grep "Xorg" | sed -En "s%.*\-auth (/[^ ]*).*%\1%p") /root/.Xauthority
				XAUTHORITY=/root/.Xauthority DISPLAY=:0 xrandr --output HDMI-1 --brightness $(bc -l <<< "$VAL/100")
				rm /root/.Xauthority
			else
				xrandr --output HDMI-1 --brightness $(bc -l <<< "$VAL/100")
			fi
		fi
	    echo "Backlight set to $(( $VAL * 100 / $MAXVAL ))%"
        exit 0
   fi
   if [ "$2" == "-set" ]; then
		NEWVALP=$3
		if [ -z "$NEWVALP" ]; then
			echo "Error: No value informed to set the backlight"
			exit 1
		fi
		if [ $NEWVALP -lt 0 ] || [ $NEWVALP -gt 100 ]; then
			echo "Error: Value should be a percent (0-100)"
			exit 1
		fi

		NEWVAL=$(( $MAXVAL * $NEWVALP / 100 ))
   fi
   if [ "$2" == "on" ]; then
	NEWVAL=$VAL
	NO_PERSIST=1
   fi
   if [ "$2" == "off" ]; then
	NEWVAL=0
	NO_PERSIST=1
   fi

 else
   mkdir -p /var/backlight 2> /dev/null
   chmod a+rwx /var/backlight 2> /dev/null
   if [ "$2" == "-get" ]; then
	   echo "No previous Backlight level set"
       exit 0
   fi
   if [ "$2" == "-set" ]; then
		NEWVALP=$3
		if [ -z "$NEWVALP" ]; then
			echo "Error: No value informed to set the backlight"
			exit 1
		fi
		if [ $NEWVALP -lt 0 ] || [ $NEWVALP -gt 100 ]; then
			echo "Error: Value should be a percent (0-100)"
			exit 1
		fi
		NEWVAL=$(( $MAXVAL * $NEWVALP / 100 ))
   fi
   if [ "$2" == "on" ]; then
	NEWVAL=$MAXVAL
	NO_PERSIST=1
   fi
   if [ "$2" == "off" ]; then
	NEWVAL=0
	NO_PERSIST=1
   fi
 fi

 if [ "$1" == "edp" ]; then
   echo "$NEWVAL" > /sys/class/backlight/intel_backlight/brightness
 else
	 if [[ ${EUID} -eq 0 ]]; then
		 cp $(ps auxxw |grep "Xorg" | sed -En "s%.*\-auth (/[^ ]*).*%\1%p") /root/.Xauthority
		 XAUTHORITY=/root/.Xauthority DISPLAY=:0 xrandr --output HDMI-1 --brightness $(bc -l <<< "$NEWVAL/100")
		 rm /root/.Xauthority
	 else
		 xrandr --output HDMI-1 --brightness $(bc -l <<< "$NEWVAL/100")
	 fi
 fi

 if [ -z "$NO_PERSIST" ]; then
   echo "$NEWVAL" > $VALUEFILE
   chmod a+rw $VALUEFILE 2> /dev/null
 fi
