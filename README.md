# bluesnap-python

A Python module to interact with Bluesnap API.

Travis status:

[![Build Status](https://magnum.travis-ci.com/justyoyo/bluesnap-python.svg?token=pHFjvPjQV7qD6qKKb1HD&branch=master)](https://magnum.travis-ci.com/justyoyo/bluesnap-ledger) 

## Contributing

Install with:
```sh
$ make
```
and run the tests with:
```sh
$ make test
```
or 
```sh
$ nosetests tests/
```

## Converting XSD (XML Schema Definition) to Python objects

[List of schemas](http://home.bluesnap.com/integrationguide/default.htm#WordManual/Schemas.htm)

```sh
$ pip install -r requirements.txt
$ pyxbgen -u http://home.bluesnap.com/integrationguide/credit-card-info.xsd -m bluesnap/schema/credit_card_info
$ pyxbgen -u http://home.bluesnap.com/integrationguide/messages.xsd -m bluesnap/schema/messages
$ pyxbgen -u http://home.bluesnap.com/integrationguide/order.xsd -m bluesnap/schema/order
$ pyxbgen -u http://home.bluesnap.com/integrationguide/shopper.xsd -m bluesnap/schema/shopper
$ pyxbgen -u http://home.bluesnap.com/integrationguide/web-info.xsd -m bluesnap/schema/web_info
```
