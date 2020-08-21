# Phantasy Star Online Mag timer 
Is a basic program coded with Nano in the git bash terminal to increase the quality of life while feeding PSO Mags.
The timer is personalised to run for 3 minutes and 15 seconds.  
- Plays a sound at the start of the timer  
- Produces a visual 30 second warning  
- Plays an alarm for 25 seconds giving enough time to feed the Mag  
- Clears screen inbetween resets  
- Resets automatically

## Usage:
Feel free to clone the program and use / modify it.

To use the program on Mac / Linux Operating systems, users have to:

- pip install pyobjc
- pip install playsound


Within the mag program, modify the sound files paths to:
- './sounds/AlpineCheckPoint.wav'
- './sounds/rose_confession.mp3'


**Run the program** with ./mag from the directory it is installed.


## Key Files:
sounds: directory storing all sound files for alarms and jingles used in the timer program
mag: program file which runs when added to a path directory 

## Methodology:
- Create a basic print hello Python program 
- Add shebang line for Python interpreter
- Allow executable permissions to all users
- Create first iteration of simple timer using Python time library
- Implement all below features step by step.

### Features list for Timer program
- [x]  Run for 3 minutes and 15 seconds
- [x]  Notify me when 30 seconds left
- [x]  Notify me when timer reaches 1 second remaining - preferably by sound
- [x]  Buffer some time so that I can feed mag (20 seconds)
- [x]  Restart on it's own
- [x]  Add starting sound to know when timer  begins.
- [x]  30 seconds to go... notification going to be eye sore, clear screen between warning prints? ASCII Art?
- [x]  Add in global location executability (adding program to home/bin directory and make sure that home/bin is in environment $PATH )

## Key Findings
Python playsound() event blocks successive events until the playsound event is finished. 
Absolute paths to sounds will not be transferrable.

## Conclusion
Relying on the playsound() event to naturally create a buffer period for feeding time was a happy accident.

## Recommendations
Refactor code into function 
Function can take arguments for long and short alarm ringtones?
