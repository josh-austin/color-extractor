# ![](https://raw.githubusercontent.com/josh-austin/color-extractor/master/icon.png) color-extractor
Extracts distinct colors from CSS and makes them LESS variables.

## Usage
`$ python extract.py [files...]`

For each file, a corresponding pair of `.less` files will appear.  For example, if you call `python extract.py foo.css` against an existing `foo.css` file, you will get the following output files: 
- `foo.less`
- `foo_variables.less`

## Tests
`$ python tests.py`

## Todo
- Package properly for PyPI
- Support for `rgb()` colors
- Support for `@import`
   
Pull requests are welcome.
