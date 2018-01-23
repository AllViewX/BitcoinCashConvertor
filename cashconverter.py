from cashaddress import convert
import sys


if len(sys.argv) != 2 :
  print("usage : bhcconvert <cashAddrss>")
else :
  addrss = sys.argv[1]
  addrss = addrss.replace('bitcoincash:' , '')
  if convert.is_valid('bitcoincash:' + addrss) :
    print( convert.to_legacy_address('bitcoincash:' + addrss))
  else :
    sys.stderr.write('Invalid address\n')