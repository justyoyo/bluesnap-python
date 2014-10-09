import datetime

now = datetime.datetime.now()
future = now + datetime.timedelta(days=1)

SANDBOX_CLIENT_CONFIG = {
    'env': 'sandbox',
    'username': 'API_14127729102161320867365',
    'password': 'JustYoyo1',
    'default_store_id': '13945'
}

# Dummy cards taken from
# http://home.bluesnap.com/integrationguide/default.htm#WordManual/Working_with_Sandbox_Testing.htm

DUMMY_CARD_VISA = {
    'number': '4111111111111111',
    'expire_month': future.month,
    'expire_year': future.year,
    'cvv': '111',
    'encrypted_number': r'$bsjs_0_0_1$fcFSIszGd/zeff2ykDptFvIVK5fsLxZpVmH1bujSYBfRwqRGvHbt/ig4BiSaCdnhqvFge/eMDcn6HMrzot4jNDxij70eEDUpoNI/ynhwlE7YEKfUPaax8OayU6SrAh1j5XlLAqHOXi9e0dfouy684uJP8l/nnnSAb6YsBFE+wTiSUJkuTCEbLdIxVPon7pfmPCiWFbq5ApTg2OoyBnHCEazAwNwFYb5rDi2clGZOrZ9t2aTiLMt8lI9eOxGK56B4VbMLEPFx9cC1k28mhl9ngEP8krM1hsmr60PtjbChBl76YGiIIkpO4oB4/B60mJ3yH9m7TCNVf6o+hAuhGPUPFA==$s9Gt7eXUdG3wnsCYXuylw8GEbPuHHtoc82wuDLlawiYj9Cz97C7X6VJ8Lr9SpPcX$0lkNKEuDWG6d9GVf3TWykyEePSfgAdqPPLgCV2JW7bQ=',
    'encrypted_cvv': r'$bsjs_0_0_1$WIZtg12e6eDuZ9lVIypJ5KZ0l81pHaSuIHvsavNowrcnvhmPzVGasjWMi9MxEAUPjoA+t/PKLTu1zuclcQQU9Qrrd/inOyb4JQdzu8V0f6bnl3b6r8n20c8hTY/SxDc2VTQUnprD4ue9xanHX+EeTDxBMAr7+EI9DvF6v/wGpJUzxi9EbxIA1I9yPtbXP+CnXlRCwOkIUxA2G4u178lSkEIN+2RO190be1imguBVuPh5V29/CeOjujk+3Wf6XcFjIbt5yN7WFYsrrY7XVWyTu9LXTto3HWihUAJXSt6y9Q3WuZ6cL+cYsqs6OmupmyPFsiStn7cWYJxcrst9/XsE1A==$J6AeBXHNoDQ84rq/1yNtZX5iPbbXlXBz0LxK3Vx8JZA=$lBpanoq9MuGmI7N/cpiVoO/ueF4JZm5ofrDVCj9Wvw0='
}

DUMMY_CARD_MASTERCARD = {
    'number': '5105105105105100',
    'expire_month': future.month,
    'expire_year': future.year,
    'cvv': '111',
    'encrypted_number': r'$bsjs_0_0_1$c/la9cXLZSMWgoiOwzoAdb4JditIL7DtrJT5MeS805vGMftQEf+rkBGLYgHyR2VrV4hIJJR5GdJ2P/dwqMgqbESMuA6lBStfSyMUw3fxduSuzqldLkCxEebOfXPSnIYLAAS0vG3aV17/JTu//SyTQDgCjcPOEhndk5RCf/r7MV1r67/IrgwC4ifedi8F2FXRJUH3Szyt3ABhQDaxP3hmzJup7XQYuZ1Sg+bdRz7201xhZsgi9Cqx1fCQ4lHLwuP91kFlXQx1haRJpRv90O1xrl1olFoZp5VBgORfsf516oNqUeP4LRhSFND8FtgMy24yNzQ4GZFw+dJULLLEiO2cpA==$WvP+Y15Bz6ltYB95PQHBd4lrGMEh5qgPfy2OLRKdwIuDmYjr6735naNijGhNnD8U$krCAINGJTTKJcvMjD5MXr/kji/7tG5/hTji+mYKBVds=',
    'encrypted_cvv': r'$bsjs_0_0_1$GC9mh85Q9Ri4XiZblGLTq8SwA9gXOh5pglpNgFDePLYgtn6GKjysjElJev2ckP6+wTWUEL82gp5Tu/JQMBrwO5mO7AZLN6Ejjbt58QtcDUm8H+ygEZidHFP13kGHBuJDDb+G6913d+6DSyBh+93Dnw6SxT7xh4lArmbkFA8EIMyWFxJNuQQwPZkGduS/6WzzKgaWHGY+om4CYhFYnRK34fKNaxt5cIgxJGtqxSrd+NamJGGudCZHqQ769RXoU6D4zBjZO8wBnQ6/+fzut8/Z0AlL5M2rF7LLxdpjmPsTR5q4ND1xl8Eg3qd4fgN6fTpQi8JVZymAQLlvqd5WU5So$UEJXlv36m27EVIrd2EpWfADlMnycs2M0XvvcUqojB9w=$Vn4m/JnIZG+/ihNeclTA66aEqLXgI927QjfXny4Kh+o='
}

DUMMY_CARD_AMEX = {
    'number': '378282246310005',
    'expire_month': future.month,
    'expire_year': future.year,
    'cvv': '111',
    'encrypted_number': r'$bsjs_0_0_1$D3VXNx7EVZtCzjcphi5HRMo8u//A3S5P1DTAu+Djb59KfkQCnOTB+U2XD+tU8Hc/aK8JJnaauLoNXdXjr5K/Em5yEdkE4JQjdsR/uDWiQHeox1A4pYvr69w4kYdyk/O/Xho/F+j4XWDflfakG9kgv+uQzWTuhQQNZ56tClV4SywTdAyvjgr5HncA/z5Uo0ujbU97PXA7FCEFR7/sAfLPVHfHH2NvTQeOfEzKIAGc80vwPUEwc48hW3DL7yl/eN5HSt6CknWB3/7MaK2SqhlU2UOb6qgtycqwhT4QLiJiP1cBF9Z8mnqW7j7O+Y3jqRF1chFLrRjDBpT/7uA8OJkEQA==$yi8X6VXOHAwwry0c6FWgnwNYq75jT2fyuuLVQ95YLE4=$a4kl/ph9Oi9Xi+ylU2g9rOTAqpQFjUpIrxpJxN4ut7c=',
    'encrypted_cvv': r'$bsjs_0_0_1$ITN4WbMDJZ3sqOmIRlMBTkuJaWyPl1ssM/tMHCyaC+gj8YqfOsNRNk52rgbxN4YAt9c2N50tir2xCYSARpjgGUgXAgyWkFcVvkTdDGtUugTuyC6pzhO0SYomdwlC98jKcl3dRi81HnETvLewn8vSHe7QLGNB5oOTvQespDpEpP0zDuOqaIJRZnItpmfcBPBr0pTb8H3S0ERkdbVL06xc0KhnSZKa/C24pJD4aHYvO3Mh9F3C4ZRcqf6tf6cpVYDVHQMoVqtDmKlmUlg2GdRdnxRhf0GGMEeHhlwPXKkMWExfIlr6KFrEg0BDVOIZXu7679O/VSP2G8nOmVfMJbd3eQ==$J1msedUPZjS9h5p/vRmk8ye30//eEU3hwJZR/WkOC/g=$Q6VO06LY8KIrqM6c9lPLNSBPFQcWpuCWpEO/jojvsG0='
}

DUMMY_CARDS = (
    ('Visa', DUMMY_CARD_VISA),
    ('MasterCard', DUMMY_CARD_MASTERCARD),
    ('American Express', DUMMY_CARD_AMEX)
)

