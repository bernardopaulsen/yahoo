# yahoo

yahoo is a Python library for downloading daily data for individual assets using Yahoo! Finance API.

It returns a pandas dataframe with the following columns: high, low, open, close, volume, and adjusted close.

It can also calculate the logarithmic return.

## Installation

At the library's folder, run

```python
pip install ../yahoo
```

## Usage

```python
import yahoo

ibov = yahoo.get("^BVSP", (2000,1,1), (2020,12,31))
```

## Support

Send me an email at [bernardopaulsen@gmail.com](bernardopaulsen@gmail.com)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)