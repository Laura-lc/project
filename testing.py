import re  
p1 = '[A-Z][a-z1-9]+([A-Z][a-z1-9]+)+'  # CLASS NAME
p2 = '[[][A-Z]{3}[-][0-9]{4}[]]'  # '[ASD-0522]' etc
p3 = '[a-z]+([-][a-z]+)+' # jekyll-relative-links etc
