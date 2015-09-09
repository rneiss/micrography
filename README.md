# Micrography #
A python script for converting an image and Judaic text source into a computer generated micrograph.

Uses the [Sefaria API](https://github.com/blockspeiser/Sefaria-Project) for finding texts.

### How to use ###
* Open `micrography.py` edit `sourceImage` & `sefariaRef` in the variable section at the top. Run script via command line.

### Examples ###

####Genesis 1: Earth####
![Genesis 1](http://www.russelneiss.com/micrography/genesis1.png)

####Psalm 137: Israeli Flag####
![Psalm 137](http://www.russelneiss.com/micrography/psalm137.png)

####Book of Jonah: Pieter Lastman Jonah and the Whale painting####
![Jonah 1-4](http://www.russelneiss.com/micrography/Jonah.png)

### Next steps ###
* Figure out if it's possible to speed up process. It's slower than I'd like at this juncture.
* Fix words at end of line, prevent words from being broken.
* Accept variables via command line using [argparse](https://docs.python.org/3/library/argparse.html)
* Build front end web interface allowing for file upload and easy text selection
* ????