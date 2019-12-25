# mag-dec-api

Helper functions to pull magnetic declination from the web

Wraps the Geoscience Australia Magnetic declination script into an API.

## Background

Inspired by Simon Murphy as a way to verify survex files had the righ magnetic declination. The original task description can be found below.

```
The command will search through all .svx files in a directory and check for magnetic declination declarations

It should take the tag number of the cave as an argument. This will be used as the location data for the search:

- search Northern_Limestone_Entrances.csv for the tag number, and extract the lat and long (in decimal deg) that precede it.
- search the .svx files for the command "fix ent", followed by that tag number, e.g. "* fix ent.J13" for Mammoth

It should give an error if it was not possible to extract a lat, lon and altitude for the file.
  
It should look for commands in the .svx file in the following order:
 *begin
 *date
 *calibrate declination

It should grab the number after 'magnetic declination' in the 'calibrate declination' command there for comparison.

It should query the geosciences site with the lat, lon, altitude and date.

It should write a warning, including the date from above, if the comparison not accurate to within 0.02 degrees
```

