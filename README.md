# WaterSurfaceLevelSensing
CSE237A WI23 Project. Using Infineon BGT60TR13C and underwater speaker to communicate 0 and 1s

System:
Windows 10

Hardware:
- Infineon BGT60TR13C - USB to Laptop
- Under water bluetooth speaker - Bluetooth to laptop


How to use:
1. Start the radar to collect 20 seconds of data.
2. In between the 20 seconds, start playing a custom 100 hz audio file.
3. The speaker under water will generate waves on the water surface.

The radar's resulting amplitude will be higher in variance as shown in the given test.ipynb file using sample data data13.npz

## Encode Data
You can use the `encode_as_sound.py` script to encode binary data as pulses of sound and silence like so

    python encode_as_sound.py 1101 --freq 100 --duration 1
This will create `data.wav` file in the current working directory. The `freq` and `duration` arguments are optional. Use `python encode_as_sound.py --help` to see more details.