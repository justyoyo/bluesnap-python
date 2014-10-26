import datetime
import os

from lxml import etree


now = datetime.datetime.now()
future = now + datetime.timedelta(days=1)

__path__ = os.path.dirname(os.path.realpath(__file__))

NAMESPACE_PREFIX = '{http://ws.plimus.com}'

SANDBOX_CLIENT_CONFIG = {
    'env': 'sandbox',
    'username': 'API_14127729102161320867365',
    'password': 'JustYoyo1',
    'default_store_id': '13945',
    'seller_id': '397608',
    'default_currency': 'GBP'
}

TEST_PRODUCT_SKU_ID = '2152476'

# Dummy cards taken from
# http://home.bluesnap.com/integrationguide/default.htm#WordManual/Working_with_Sandbox_Testing.htm
# http://avners.info/api/constant-values/test-credit-card-numbers

DUMMY_CARD_VISA = {
    'card_type': 'VISA',
    'card_number': '4111111111111111',
    'expiration_month': future.month,
    'expiration_year': future.year,
    'security_code': '123',
    'encrypted_card_number': r'$bsjs_0_0_1$kfCO6GbacV0ZdjSmvtbAuMLLaV/wI6SVi58UtfPv pE8ISm GCfPG8trhh/DC0Zi7/S30L69P03KkD2SS2VA9StchpKdoxxfTKoEaP2nwp0QqowCul9ihy8H4XBCFe49u1Undjm3/feZ77/7TTsxG4jlWZUtNLBW88oHpZ280fZ872QG1LDw6MBdfZmF3dnQYt5K2QMFFTR8L/sTfUMeF/6XY33032ilwlIZX8Cg 436r8b2Ty9m9AkO2V97fltlpzjzkHqghdOi/K0gV5LnGtOAaIYxpdvRR5w  AvkIiOuXhuB5efOAQzBiGmpe3R1STNZHmxI13nKEdtgdldGgQ==$/lEM/65AZrbpE90lR80mySr0Nmmyc35w34JDie1SVymuqI S2PS8k/aZQ/KuAHzN$YiBjtDY/jy3RYrrWMaGRwHF1VWFIPcN/5DzcEFGIEDI=',
    'encrypted_security_code': r'$bsjs_0_0_1$RoHzysitb3cte6uCQ o1TTDTnFgxOZWICnSRUwttwLxyNBlMQ8L2FBS251rScLCmr A346yO16xEjOwaBC8vracsa//MT3MpiMt8/A279468Eh6s5KTDmLLE CN4DNENHIpy83SAMCvBGucZStkjYR5PL8XHKd7s LnkYbnKMovvwJ4/bH3t0OtL4YSx41jq2owZba8B5n8gRg2fxpJEDR6skqicrdeP8VqX11jUV5m1dkUQKVJEUkaLgboRgLcTTOZqSDHDBS7DBdM7nyYi7  NWjhGj/R/kjI9kHjANcJGlpuM/VTuJn1b9DysckoVIsp1i786C6RBLnXMnGpSYQ==$Fcy7ItIlPc pe3iQPiRyStUkDTWDPmSA3iBwusdJLgs=$CZxZts79RpIbvWMKwLhHDWcf0oCKRyq l/bueF/UjCs=',
}

DUMMY_CARD_DISCOVER = {
    'card_type': 'MASTERCARD',
    'card_number': '60115564485789458',
    'expiration_month': 12,
    'expiration_year': 2018,
    'security_code': '411',
    'encrypted_card_number': r'$bsjs_0_0_1$qKmNkMRc2YPL5O2JvFKCeGl hvvl0tATDMrFRc4R4cOb 48SeRhHLf LOvvTzD8pNV6U2pr3LESqJXMU9cJtnsNGkVmSWGR2JktCaeESMD2NfhLRt2UJGzHYW0suLTPNT74i8fV6Ccfm943t6UJJiIoYNWnHehbF0YbUyJjdIBJDTnJGJ7/MhCMXNAkl8V8CXBViCUuN2wywUoavCBce5BEiSnO/Yt2IiU5CRe82dp VLSu7ufmjrWjUifkeXu3poUIJDBk0ws8UDDKNeOEDYPM/ PQd5zTsb28y7CmW2JelngkDK NoKPPUIgaifP9g2mvUgeR2aUvUx1I07gyI8Q==$xIp98MF1M81yPWXPZtcnM n7Zi 8YYJRXtBcPPaWo4CsmteTLVT Ui 7nFKbeWN3$AtpgmpcV6Jaad3Hk55skVO/B6CC o8PBKDf/lATxSYc=',
    'encrypted_security_code': r'$bsjs_0_0_1$oJ W3C1S2NAQ6seuLUvsUuNVfr28Wx582bh6566Td2ADwjqM0uwCgeSNE6f6KHas5A91Rk7p GcMNI/s7aNmSUnKZ55oq/cobVbr53dtkUVf1 NLNmNbCqicqJT2wSrxUgpuY4Gwbbpy48XcZ00WKIP w40Cm5kGEuWwrj8AqNFDILYJlWv2W6e9oT9uusSsQntHA1BjsxALmHPUfUOUpUxqkLp3W2VNXOI5rRX8PJDSuDf43LHS3U/coesUSoOGW4xUwt/PXqGEwUf4pq/3hA3b4jmOHwXtuJDd8XuCivfWRC2FTMCPdTAOIck7MYaAOQW691Z9o9lhcIWv4Dp7jw==$GInf71tbwiTMPafBFANHBr5nZGZ1R7uHtT6dJPd0Vig=$YAoqR5tC5B/yDssf7ppYeCq2lZJW2NlFrE88K4E1ayo=',
}

DUMMY_CARD_VISA__EXPIRED = {
    'card_type': 'VISA',
    'card_number': '4917484589897107',
    'expiration_month': 4,
    'expiration_year': 2018,
    'security_code': '411',
    'encrypted_card_number': r'$bsjs_0_0_1$QLPSIni3utLbKGb9uSk2QxFaHfQwW3rhV93yPK0nqt/NpYBSQxQ4YDld594zUtr/Qn3J7mjVMqsePQlxS5jesPgI2wRbCRb3PkQY1h9gzIE7mqf1YqVThiOLV1/PFSO/ZXsPQz41vYAsokNllWqSoGa8SWPBBFIe22Vv25HW0nPCDnFx0yfImg7pT50GAOHjYEt20Ec13YGPxmcylrYlDmQL/OgMkijI4jQElkg03lhgBH5wcw5Hhq6t3I8pl91bA9Lljo4RdxYo4rMokbsnOIna0lsWRdgal/ggIYUTHU/UihvEPFbJdGnaRbKolHm4hY1qew0eIc3VIcq6CG94kg==$HgeWCfw2BN3wD2VdTmo1gp0jh8lpJZgHu29ifWjZ8aMHwVVxx5sJSmvKFQ7s1bub$xGsq3ICwGtZny lPE0h964OCHXo81hEH XpVr7mER1Y=',
    'encrypted_security_code': r'$bsjs_0_0_1$J I180PwR7DNuHQ939HJUendbwtRHlKSvisfz0W93/kk4fQi7s7uv2NmCWKaW9w9/UFk6UU/8hnTBu/2G67GqtESQw/jTjn8Pyx0cQ7K2b7nkN KwtgwByDusSeh8onqb4ML1zDP3oDM5WTp3Mu  BIzL31DQj477IV6VxPtugq2IEutmts05R45sGTEXzKhPCK/H4ESxQQwGxKPGI9JdTU/S3S/kv6Y7lQb5nX5KTgHfJbaPCDc2NrfwW6FgWmdKFlR9N6xau33f1aoLsYiZqdY7VRP6G4ce27QxFR21MN0evD qN6zcH355gd1IqehVIupuGkDY8hJ TIYf7iq6Q==$XaNCBn0xVVd7n4AzQAP5jC3Zvl2tUoXci4LxIjJQ4hI=$94Zlz7EUlLMpn1/9ZLk5BI4EjdAI7Be7uZJuYKspu1M='
}

DUMMY_CARD_VISA__INSUFFICIENT_FUNDS = {
    'card_type': 'VISA',
    'card_number': '4917484589897107',
    'expiration_month': 5,
    'expiration_year': 2018,
    'security_code': '411',
    'encrypted_card_number': r'$bsjs_0_0_1$QLPSIni3utLbKGb9uSk2QxFaHfQwW3rhV93yPK0nqt/NpYBSQxQ4YDld594zUtr/Qn3J7mjVMqsePQlxS5jesPgI2wRbCRb3PkQY1h9gzIE7mqf1YqVThiOLV1/PFSO/ZXsPQz41vYAsokNllWqSoGa8SWPBBFIe22Vv25HW0nPCDnFx0yfImg7pT50GAOHjYEt20Ec13YGPxmcylrYlDmQL/OgMkijI4jQElkg03lhgBH5wcw5Hhq6t3I8pl91bA9Lljo4RdxYo4rMokbsnOIna0lsWRdgal/ggIYUTHU/UihvEPFbJdGnaRbKolHm4hY1qew0eIc3VIcq6CG94kg==$HgeWCfw2BN3wD2VdTmo1gp0jh8lpJZgHu29ifWjZ8aMHwVVxx5sJSmvKFQ7s1bub$xGsq3ICwGtZny lPE0h964OCHXo81hEH XpVr7mER1Y=',
    'encrypted_security_code': r'$bsjs_0_0_1$J I180PwR7DNuHQ939HJUendbwtRHlKSvisfz0W93/kk4fQi7s7uv2NmCWKaW9w9/UFk6UU/8hnTBu/2G67GqtESQw/jTjn8Pyx0cQ7K2b7nkN KwtgwByDusSeh8onqb4ML1zDP3oDM5WTp3Mu  BIzL31DQj477IV6VxPtugq2IEutmts05R45sGTEXzKhPCK/H4ESxQQwGxKPGI9JdTU/S3S/kv6Y7lQb5nX5KTgHfJbaPCDc2NrfwW6FgWmdKFlR9N6xau33f1aoLsYiZqdY7VRP6G4ce27QxFR21MN0evD qN6zcH355gd1IqehVIupuGkDY8hJ TIYf7iq6Q==$XaNCBn0xVVd7n4AzQAP5jC3Zvl2tUoXci4LxIjJQ4hI=$94Zlz7EUlLMpn1/9ZLk5BI4EjdAI7Be7uZJuYKspu1M='
}

DUMMY_CARD_VISA__INVALID_CARD_NUMBER = {
    'card_type': 'VISA',
    'card_number': '4917484589897107',
    'expiration_month': 8,
    'expiration_year': 2018,
    'security_code': '411',
    'encrypted_card_number': r'$bsjs_0_0_1$QLPSIni3utLbKGb9uSk2QxFaHfQwW3rhV93yPK0nqt/NpYBSQxQ4YDld594zUtr/Qn3J7mjVMqsePQlxS5jesPgI2wRbCRb3PkQY1h9gzIE7mqf1YqVThiOLV1/PFSO/ZXsPQz41vYAsokNllWqSoGa8SWPBBFIe22Vv25HW0nPCDnFx0yfImg7pT50GAOHjYEt20Ec13YGPxmcylrYlDmQL/OgMkijI4jQElkg03lhgBH5wcw5Hhq6t3I8pl91bA9Lljo4RdxYo4rMokbsnOIna0lsWRdgal/ggIYUTHU/UihvEPFbJdGnaRbKolHm4hY1qew0eIc3VIcq6CG94kg==$HgeWCfw2BN3wD2VdTmo1gp0jh8lpJZgHu29ifWjZ8aMHwVVxx5sJSmvKFQ7s1bub$xGsq3ICwGtZny lPE0h964OCHXo81hEH XpVr7mER1Y=',
    'encrypted_security_code': r'$bsjs_0_0_1$J I180PwR7DNuHQ939HJUendbwtRHlKSvisfz0W93/kk4fQi7s7uv2NmCWKaW9w9/UFk6UU/8hnTBu/2G67GqtESQw/jTjn8Pyx0cQ7K2b7nkN KwtgwByDusSeh8onqb4ML1zDP3oDM5WTp3Mu  BIzL31DQj477IV6VxPtugq2IEutmts05R45sGTEXzKhPCK/H4ESxQQwGxKPGI9JdTU/S3S/kv6Y7lQb5nX5KTgHfJbaPCDc2NrfwW6FgWmdKFlR9N6xau33f1aoLsYiZqdY7VRP6G4ce27QxFR21MN0evD qN6zcH355gd1IqehVIupuGkDY8hJ TIYf7iq6Q==$XaNCBn0xVVd7n4AzQAP5jC3Zvl2tUoXci4LxIjJQ4hI=$94Zlz7EUlLMpn1/9ZLk5BI4EjdAI7Be7uZJuYKspu1M='
}

DUMMY_CARD_MASTERCARD = {
    'card_type': 'MASTERCARD',
    'card_number': '5105105105105100',
    'expiration_month': future.month,
    'expiration_year': future.year,
    'security_code': '123',
    'encrypted_card_number': r'$bsjs_0_0_1$VCqQiniRC5Fm82Q cnbdIjEj5/ryp7MOgnZEVWlHUW YzolRZZA4jsj JffP6PL2wMw0TiUgOCVjuocksCks5Dax2oLLVKE5bqngOXJ2tfhol 204RhcEPyGwqMyUsKQ6rYQ/rRrLqQCm0Bjp6G8XS12qt5FYQLTd9qtwsIfd30D2V2h3JIhBXRTbPzxkJG4LJdG e3iat0lOSj0fgHSzBc/PMg3WMklGGBK i4pYzjDEie3hNnymooUizu2j3ixnevoXuRlKwHVwtTjx3Rinht2iIehhyZ0SFGYl581QGC3uAZiI1D0K42RVRpgTUdUv0GLQWe1UDrM5ue5DpFZUQ==$rOfki3saXgafeKoLZ0aQV3JF4EHHgdYxQok/rOpCN3yfu84XAAXtLfv8hAAXGASi$SHlEQ19qxnAQAMD04DMmWoldoF41deCc69aou4aKv E=',
    'encrypted_security_code': r'$bsjs_0_0_1$Lfz84IA1YXKLlpm7ko3 ANr/cItAq1j34GuyUqYddeu9RHzR/ttXVwXWdZOQ1eTVTzjmue dlkAVGsSTY/uB4sVVrcxIGO4kpGElBw3d2CzKTumitNmLgjaHUUWpoAWEqoOfJlsmIYg9hwJ4FGsq3ofLlfcOipEGaEWM777AXTPdqJlPyD8njaEwOSWvPcuxkteJB/aDU8jCs9gV0h2qio36AJme6rnCjexdgbDrQCOj0nMXKBjVbMdmDV05Xh0D Xhrx9km09jSDn3Ax2JiRkRMRDF5Mny9d0lkanYAeRNykptl78ZNV0RVrpvcEPHGfA2xbLSpWmv ayg4ydvaYA==$g7A6vrSnq8FW soCGC94RD3eIiqJfcLODxz7LV5LIo0=$4ten/DM01yfVJxPaOHwQ/GfReHowd4phHiL7JcPCe9k='
}

DUMMY_CARD_AMEX = {
    'card_type': 'AMEX',
    'card_number': '378282246310005',
    'expiration_month': future.month,
    'expiration_year': future.year,
    'security_code': '4111',
    'encrypted_card_number': r'$bsjs_0_0_1$RI6mtf6iY1aArfeDULVnil3BYjSh7JywPbq6zpAWc/KSo3qK0jzhhfFtvYPUm2bMW9OL9bILFHOoJE/B/RmmEV59EUcNajnFHg7MeHMiNw36r4iehvQL4XqGo8ZAb0bojz7QYrV5Ry1DKB Af Cp73IlavhwZ0HuSExmyygRaAruPh8sJeUwKVgVO nyyP5eg4wjYL1tngxjzPYRDd/JIZdDiGHgTa 6fhy4s7VSGE31GcESufQIh38FKhbwFkCi0 stkb1fe3gwqFkG6BOsbyJuOE1xYKbPGqQJJfDumsOQHIIrYYLnrnlN2nbFa1//1htL9U3Fos1FsJ7WxH0gAQ==$xKrfie2CcCbFfkYA DxrrIM9R7SHlPc4CPE1EUWVHHo=$cK0F21MsUKyEqBV5wbmdoEIiqRzQvEkouZ3nyMqzqAA=',
    'encrypted_security_code': r'$bsjs_0_0_1$DqroDnh3 /s8jNR8AGMrcw3KPSXXX2RwhOIqGS6uyTXukFA1VePn1Trwp6/wuUxBbu7ltyOYO5b0WyVLAa 4DeNRBuIp5BbwlTdaU7yxj7qsFfOavsRN5v7u2LO5rUZM5YkdqLh7Bs00mjLf8/xT8GrSB2WZ9fuO6F0rnaZZBJRTrDd6oJIig/hm6/y N2ABcCw6GaPY1ozi3fC5xCizsMWLo4eMhswbBlgnsiCDx5Dn8/BGDhlqpht03/on3kKHT49XreibyR03OLoYsQrQmwPyKWbgvYklL3z0peTZfvzZBFXjX5LZEKzGFV2K2nqZhj99r8u05SRXmmmyhZRk/w==$nQ5EtsK6auumxELv/xPsfOX2CzphO9Xf/Ac8 S10i4Q=$Z/tz5NY2dNfLreUQs3smMgXQRXByExPs6iaFEWQAQLY='
}

DUMMY_CARD_AMEX__AUTH_FAIL = {
    'card_type': 'AMEX',
    'card_number': '378282246310005',
    'expiration_month': 5,
    'expiration_year': 2018,
    'security_code': '4111',
    'encrypted_card_number': r'$bsjs_0_0_1$RI6mtf6iY1aArfeDULVnil3BYjSh7JywPbq6zpAWc/KSo3qK0jzhhfFtvYPUm2bMW9OL9bILFHOoJE/B/RmmEV59EUcNajnFHg7MeHMiNw36r4iehvQL4XqGo8ZAb0bojz7QYrV5Ry1DKB Af Cp73IlavhwZ0HuSExmyygRaAruPh8sJeUwKVgVO nyyP5eg4wjYL1tngxjzPYRDd/JIZdDiGHgTa 6fhy4s7VSGE31GcESufQIh38FKhbwFkCi0 stkb1fe3gwqFkG6BOsbyJuOE1xYKbPGqQJJfDumsOQHIIrYYLnrnlN2nbFa1//1htL9U3Fos1FsJ7WxH0gAQ==$xKrfie2CcCbFfkYA DxrrIM9R7SHlPc4CPE1EUWVHHo=$cK0F21MsUKyEqBV5wbmdoEIiqRzQvEkouZ3nyMqzqAA=',
    'encrypted_security_code': r'$bsjs_0_0_1$DqroDnh3 /s8jNR8AGMrcw3KPSXXX2RwhOIqGS6uyTXukFA1VePn1Trwp6/wuUxBbu7ltyOYO5b0WyVLAa 4DeNRBuIp5BbwlTdaU7yxj7qsFfOavsRN5v7u2LO5rUZM5YkdqLh7Bs00mjLf8/xT8GrSB2WZ9fuO6F0rnaZZBJRTrDd6oJIig/hm6/y N2ABcCw6GaPY1ozi3fC5xCizsMWLo4eMhswbBlgnsiCDx5Dn8/BGDhlqpht03/on3kKHT49XreibyR03OLoYsQrQmwPyKWbgvYklL3z0peTZfvzZBFXjX5LZEKzGFV2K2nqZhj99r8u05SRXmmmyhZRk/w==$nQ5EtsK6auumxELv/xPsfOX2CzphO9Xf/Ac8 S10i4Q=$Z/tz5NY2dNfLreUQs3smMgXQRXByExPs6iaFEWQAQLY='
}

DUMMY_CARD_MASTERCARD_2 = {
    'card_type': 'MASTERCARD',
    'card_number': '5425233430109903',
    'expiration_month': 4,
    'expiration_year': 2018,
    'security_code': '411',
    'encrypted_card_number': r'$bsjs_0_0_1$ZO0ANjUrKgwEqX1fx668reSO0fAxsEJGgKPbf8ah59l3r04VMC1UDm9jFDUpB0sv67ysm4nmJBNH/hTD3SrqlgNnEvMuTStuNPP1GUK8GZK7ZoCa95h5VGFsmwLeZYJlVlOlPJ7oNSwtN3on/OwVrux37sr yf6z//BN xgx0G5HmT43qlX61kKgjY92a5czQEQ21CteW3C0RGY NkQ3qTKMrOnAUmzUx Jnh 9bcviVpMa5xHyKffaql9uEEgd8UnoONXX0kciB26lsVDkXeZ0Vv3PQojUxkqx255 R W4wW7TIYgsEnvtBzzgIJXk2J5xhRB7E6Uhzb1Do1x5Atg==$5Sq2Y5 hmRKbSysMRHwfZ9Qtr12Xal6WIyw3ez2LtkDVEVkhZhYpDm5eJn8ASynV$cm0313ZBTuAsfZLCQfhPsIOFNrHzZNEVlhdAya2 X3I=',
    'encrypted_security_code': r'$bsjs_0_0_1$jAqRwJXC8P KTAImBG52vvHtOMzFkUM5iH9lrz3n6N/aXuPTb7uLj6nRf/CfRvrQ9FPoiEDuslldcsOVNkwtqRyV7Q2xsfS4qNtvTsp/LrpdbjbTTonUH0nuBJFGEcY0MgUJTRd5dKqz8U02jjfc0BbyAzOz94VagUssYtod/S8FIjmnspdaAXohpe/0y5GxW1GQr1buDrfHkG/BOw xeCakE8cpfeXda3G7YJnUYvxrFeKXOZI3VYiwCoZcWL8MdgLwCMq1evKlwWhZLReh16AS8UpYTQ0mjOKAz0gplByynqcdYfxFlkzNylNSOBZNhgDa yPuK3VpJ fTZ/YgEg==$YNFPYs3nA20BmpEsmCUPy0u bUCUkj7P7hO6MOhmWaA=$SONVMPRc8JpU0qQ/uzH5FH66weM/tAqUQRgRLBrrvNE='
}

DUMMY_CARDS = (
    ('Visa', DUMMY_CARD_VISA),
    ('MasterCard', DUMMY_CARD_MASTERCARD),
    ('MasterCard 2', DUMMY_CARD_MASTERCARD_2),
    ('American Express', DUMMY_CARD_AMEX)
    ('Discover', DUMMY_CARD_DISCOVER)
)


def configure_client():
    from bluesnap import client
    client.configure(**SANDBOX_CLIENT_CONFIG)


def get_xml_schema(file_name):
    return etree.XMLSchema(etree.parse(os.path.join(__path__, 'schemas', file_name)))
