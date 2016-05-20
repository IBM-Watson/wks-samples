
# Watson Explorer Content Analytics (WEXCA) to Watson Knowledge Studio (WKS) Dictionary Converter

Developers that come to WKS with legacy content analytics solutions that were
built using the WEXCA product will have existing dictionary data this is
formatted for use in a WEXCA project and not for WKS. This sample code will
provide a method of converting existing dictionary resources from a WEXCA
Studio project to the format required to import those dictionaries into a WKS
project.

# Prerequisites

The sample code is written in Python and requires a working installation of
Python 2.7 or newer. 

# Installing

No installation is necessary. Simply download the script to whatever directory
is appropriate for your system. If you are on a Linux system, it is recommended
to set the file permissions to executable for ease of use.

```
chmod u+x wexca-to-wks-dict.py
```

# Usage

```
python wexca-to-wks-dict.py  # OR// ./wexca-to-wks-dict.py
usage: lw_to_wks_dict.py [-h] inputFile outputFile
```

The inputFile is the path to a DATA.csv file in your WEXCA Studio project and
the outputFile is the path to the WKS formatted data file that will be created
by the conversion logic. For example, if you created a default WEXCA Studio
project named "Example" and inside that project you created a dictionary called
"Foo," you could convert the contents of Foo to WKS format with the following
command:

```
python wexca-to-wks-dict.py myworkspace/Example/Resources/Dictionaries/Foo/DATA.csv foo-wks.csv
```

WKS-formatted dictionaries should contain lowercase terms for the best possible
matching of words in mixed uppercase, lowercase, and proper case forms. However,
it is generally desirable to match acronyms in only the specifically stated word
case (e.g. uppercase) so the converter tool makes a reasonable attempt to
determine if the source dictionary entry is an acronym or not and to preserve
the word case if it is determined to be an acronym. All other terms are
converted to lowercase.

The WKS BETA does not use the part-of-speech (POS) code associated with a
dictionary entry and no attempt was made to preserve that value during
conversion. All output entries are coded as nouns (aka POS=3). If you are
interested in setting the POS code correctly, see the WKS documentation for a
complete list of possible POS code values.


# License
This project is Copyright IBM Corporation 2016,2017 and is licensed under the
Apache License 2.0 (Apache-2.0). See license.txt for details.


