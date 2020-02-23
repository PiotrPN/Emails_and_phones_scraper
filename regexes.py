import re

landlineNumberRegex = re.compile(r"""
\(?     #optional bracelet
\d\d    #two regional numbers
\)?     #optional bracelet
[\s|-]  #separator
\d\d\d  #first three digits
[\s|-]? #separator
\d\d    # next two digits
[\s|-]? #separator
\d\d    #last two digits
""", re.VERBOSE)


cellphoneNumberRegex = re.compile(r"""
\(?         #optional bracelet
\+?         #plus before code
\d?\d?      #areacode
\)?         #optional bracelet
[\s|-]?     #separator
\d\d\d      #first three digits
[\s|-]?     #separator
\d\d\d      # next three digits
[\s|-]?     #separator
\d\d\d      #last three digits
"""
, re.VERBOSE)


emailRegex = re.compile(r"""
[ab-z]     #start with letter
\S+        #adres name
@          #at
\S+        #domain adress
.          #dot
[ab-z]+    #country domain
"""
, re.VERBOSE | re.IGNORECASE)