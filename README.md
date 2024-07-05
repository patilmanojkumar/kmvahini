# Download market data from Krishimaratavahini! 

<table border=1 cellpadding=10><tr><td>

#### \*\*\* IMPORTANT LEGAL DISCLAIMER \*\*\*

---

** Krishi Marata Vahini is the registered trademark of `The Karnataka State Agricultural Marketing Board(KSAMB)` and `Department of Agricultural Marketing, Govt. of Karnataka!.`**

kmvahini is **not** affiliated, endorsed, or vetted by KSAMB, GoK
It's an open-source tool that uses KSAMB's publicly available data, and is
intended for research and educational purposes.

**You should refer to KSAMB!'s terms of use**
([Terms of Use](https://krama.karnataka.gov.in/department.aspx?page=terms),
[Privacy Policy](https://krama.karnataka.gov.in/department.aspx?page=privacy), and
[Copyright Information](https://krama.karnataka.gov.in/department.aspx?page=copyright)) **for
details on your rights to use the actual data downloaded. Remember - the
KSAMB!'s data is intended for personal and Reserach use only.**

</td></tr></table>

---

**kmvahini** offers a threaded and Pythonic way to download market data from [Krishi Marata Vahini](https://krama.karnataka.gov.in/).

---

- [Installation](##installation)
- [Quick start](##quick-start)
---

## Installation

Install `kmvahini` using `pip`:

``` {.sourceCode .bash}
$ pip install kmvahini --upgrade --no-cache-dir
```
``` {.sourceCode .bash}
$ pip install "kmvahini[optional]"
```

[Required dependencies](./requirements.txt) , [all dependencies](./setup.py).

---

## Quick Start

```python
import kmvahini as kv
# Define parameters for scraping
months = ["JANUARY"]
years = ["2010"]
commodities = ["BENGALGRAM"]
markets = ["AllMarkets"]
df = kv.scraper.scrape_website(months,years,commodities,markets)
...
```

---

### Legal Stuff

**kmvahini** is distributed under the **MIT License**. See
the [LICENSE](./LICENSE) file in the release for details.


AGAIN - kmvahini is **not** affiliated, endorsed, or vetted by KSAMB, GoK
It's an open-source tool that uses KSAMB's publicly available data, and is
intended for research and educational purposes. You should refer to KSAMB!'s terms of use
([Terms of Use](https://krama.karnataka.gov.in/department.aspx?page=terms),
[Privacy Policy](https://krama.karnataka.gov.in/department.aspx?page=privacy), and
[Copyright Information](https://krama.karnataka.gov.in/department.aspx?page=copyright)). for
details on your rights to use the actual data downloaded.

---

### P.S.

Please drop me an note with any feedback you have.

**Manojkumar Patil**
