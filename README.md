# Log Puzzle

A Python program designed to scan log files for lines containing urls to puzzle pieces. Supplying a directory to download those images to also creates and html file that when opened in the browser shows the full image.

## Getting Started

Clone down the repo

```bash
git clone git@github.com:vitollom/Log-Puzzle.git
```

### Printing the urls

```bash
python logpuzzle.py animal_code.google.com
```

OR

```bash
python logpuzzle.py place_code.google.com
```

### Compling images into HTML file

```bash
python logpuzzle.py --todir <name-of-dir> animal_code.google.com
```

OR

```bash
python logpuzzle.py --todir <name-of-dir> place_code.google.com
```

Where `<name-of-dir>` is the name of the directory you'd like to save the image files and HTML document, nested in this project folder.
  
Open the HTML file in your chosen browser and it should display a coeherent image.

## Credits
This project was an assessment during my time at Kenzie Academy.
  
Creative Commons (CC) Attribution: The images used in this puzzle were made available by their owners under the [Creative Commons Attribution 2.5](http://creativecommons.org/licenses/by/2.5/) license, which generously encourages remixes of the content such as this one. The animal image is from the Flickr user `zappowbang` and the place image is from the Flickr user `booleansplit`.

 ---
