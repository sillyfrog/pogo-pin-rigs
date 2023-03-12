# Pogo Pin Flashing Adaptors

Source code for a 3D printed pogo pin holder for flashing various chips:

- TYWE5P ESP based chip: https://www.thingiverse.com/thing:4889239
- CB2S: https://www.thingiverse.com/thing:5905447

# Using this code

This is written using the [SolidPython](https://github.com/SolidCode/SolidPython), so you will need to install the Python module to use it with the command:

```
pip install solidpython
```

Depending on your setup, you may need to just install it for your user account:

```
pip install --user solidpython
```

Once installed, generate the .scad files with:

```
python TYWE5P-pogopins.py
```

This will create a `TYWE5P-pogopins.scad` file you can then use to generate a .STL in OpenSCAD.

## Development Notes

Most of the dimensions and variables are at the top of the file. Run the file to build the OpenSCAD file, you can then open up in OpenSCAD.

Enjoy!
