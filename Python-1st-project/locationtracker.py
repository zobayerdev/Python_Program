import phonenumbers
from test import number

from phonenumbers import geocoder
oh_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(oh_nmber, "en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))


