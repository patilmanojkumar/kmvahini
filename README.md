<table border=1 cellpadding=10><tr><td>
<h1 align="center"><b>Download market data from Krishimaratavahini! </b>
<!--  -->
<br>

<p align="center">
  <a href="https://github.com/DenverCoder1/readme-typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Time+New+Roman&color=cyan&size=30&center=true&vCenter=true&width=600&height=100&lines=One+Stop+Data+Source+For+Price+Data;kmvahini+1.0;"></a>
</p>

#### \*\*\* IMPORTANT LEGAL DISCLAIMER \*\*\*

---

** Krishi Marata Vahini is the registered trademark of `The Karnataka State Agricultural Marketing Board(KSAMB)` and `Department of Agricultural Marketing, Govt. of Karnataka!.`**

kmvahini is **not** affiliated, endorsed, or vetted by KSAMB, GoK. It's an open-source tool that uses KSAMB's publicly available data, and is intended for research and educational purposes.
**You should refer to KSAMB!'s terms of use**
([Terms of Use](https://krama.karnataka.gov.in/department.aspx?page=terms),
[Privacy Policy](https://krama.karnataka.gov.in/department.aspx?page=privacy), and
[Copyright Information](https://krama.karnataka.gov.in/department.aspx?page=copyright)) **for details on your rights to use the actual data downloaded. Remember - the KSAMB!'s data is intended for personal and Reserach use only.**
</td></tr></table>
---
**kmvahini** offers a threaded and Pythonic way to download market data from [Krishi Marata Vahini](https://krama.karnataka.gov.in/).
---
- [Installation](#installation)
- [Quick start](#quick-start)
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
import kmvahini.scraper as scrape_website
# Define parameters for scraping
months = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
years = ["2010"] # Data available from 2002 to till present
commodities = ["BENGALGRAM"] #264 commodities data is available
markets = ["AllMarkets"] # 164 markets
df = scrape_website(months,years,commodities,markets)
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
