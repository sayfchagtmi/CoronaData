# CoronaData
Download the latest updated data about coronavirus pandemic by country (Total Cases, New Cases, Total Deaths, New Deaths, Total Recovered, Active Cases, Serious Critical, Total cases/ 1M pop, Deaths/ 1M pop, Total Tests, Tests/ 1M pop).

* Source: https://www.worldometers.info/coronavirus/


# Install package
  ### Requires python 3.x  version.
```
pip install git+git://github.com/sayfchagtmi/CoronaData.git
```

# Use it directly from command line!
* Example: Download the latest data from https://www.worldometers.info/coronavirus/ into current directory and display the update date 
```
CoronaData
```
* Example: Download the into my_data_path without showing update date
```
CoronaData --fpath my_data_path --date False
```
* Display Help page 
```
CoronaData --help
```
  * output:
  ```
  Usage: CoronaData [OPTIONS]

  Download the latest updated data about coronavirus pandemic by country
  (Total Cases, New Cases, Total Deaths, New Deaths, Total Recovered, Active
  Cases, Serious Critical, Total cases/ 1M pop, Deaths/ 1M pop, Total Tests,
  Tests/ 1M pop). Source: https://www.worldometers.info/coronavirus/

Options:
  --fpath TEXT    The file path (By default current directory)
  --date BOOLEAN  Set it True to show the update date (By default True)
  --help
  ```

