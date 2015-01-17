# bluesnap-python

A Python module to interact with Bluesnap API.

## Running tests


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
