# ./bluesnap/schema/shopper.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:7707c01e299670773fa48a3eb29a9f4fcece2d24
# Generated 2014-10-08 16:42:01.765850 by PyXB version 1.2.3
# Namespace http://ws.plimus.com

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:a09ba2fd-4f01-11e4-8b75-3c15c2ea0f80')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://ws.plimus.com', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 6, 2)
    _Documentation = None
STD_ANON._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 11, 2)
    _Documentation = None
STD_ANON_._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 16, 2)
    _Documentation = None
STD_ANON_2._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 21, 2)
    _Documentation = None
STD_ANON_3._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 26, 2)
    _Documentation = None
STD_ANON_4._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 31, 2)
    _Documentation = None
STD_ANON_5._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 36, 2)
    _Documentation = None
STD_ANON_6._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 41, 2)
    _Documentation = None
STD_ANON_7._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 44, 2)
    _Documentation = None
STD_ANON_8._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 49, 2)
    _Documentation = None
STD_ANON_9._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 54, 2)
    _Documentation = None
STD_ANON_10._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 59, 2)
    _Documentation = None
STD_ANON_11._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 64, 2)
    _Documentation = None
STD_ANON_12._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 69, 2)
    _Documentation = None
STD_ANON_13._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 74, 2)
    _Documentation = None
STD_ANON_14._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 79, 2)
    _Documentation = None
STD_ANON_15._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 84, 2)
    _Documentation = None
STD_ANON_16._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 39, 2)
    _Documentation = None
STD_ANON_17._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 45, 2)
    _Documentation = None
STD_ANON_18._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_19 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 51, 2)
    _Documentation = None
STD_ANON_19._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_20 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 57, 2)
    _Documentation = None
STD_ANON_20._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_21 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 63, 2)
    _Documentation = None
STD_ANON_21._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_22 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 47, 2)
    _Documentation = None
STD_ANON_22._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_23 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 52, 2)
    _Documentation = None
STD_ANON_23._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_24 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 8, 2)
    _Documentation = None
STD_ANON_24._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_25 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 13, 2)
    _Documentation = None
STD_ANON_25._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_26 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 67, 2)
    _Documentation = None
STD_ANON_26._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_26, enum_prefix=None)
STD_ANON_26.initial = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value=u'initial', tag=u'initial')
STD_ANON_26.recurring = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value=u'recurring', tag=u'recurring')
STD_ANON_26._InitializeFacetMap(STD_ANON_26._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_27 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 14, 2)
    _Documentation = None
STD_ANON_27._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_28 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 19, 2)
    _Documentation = None
STD_ANON_28._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_29 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 24, 2)
    _Documentation = None
STD_ANON_29._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_30 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 29, 2)
    _Documentation = None
STD_ANON_30._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_31 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 34, 2)
    _Documentation = None
STD_ANON_31._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_32 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 39, 2)
    _Documentation = None
STD_ANON_32._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_33 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 52, 2)
    _Documentation = None
STD_ANON_33._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_34 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 132, 2)
    _Documentation = None
STD_ANON_34._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_35 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 137, 2)
    _Documentation = None
STD_ANON_35._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_36 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 142, 2)
    _Documentation = None
STD_ANON_36._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_37 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 147, 2)
    _Documentation = None
STD_ANON_37._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_38 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 152, 2)
    _Documentation = None
STD_ANON_38._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_39 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 172, 2)
    _Documentation = None
STD_ANON_39._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_40 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 177, 2)
    _Documentation = None
STD_ANON_40._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_41 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 182, 2)
    _Documentation = None
STD_ANON_41._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_42 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 187, 2)
    _Documentation = None
STD_ANON_42._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_43 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 192, 2)
    _Documentation = None
STD_ANON_43._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_44 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 220, 2)
    _Documentation = None
STD_ANON_44._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_45 (pyxb.binding.datatypes.int, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 226, 2)
    _Documentation = None
STD_ANON_45._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_45, enum_prefix=None)
STD_ANON_45._CF_enumeration.addEnumeration(unicode_value=u'1', tag=None)
STD_ANON_45._CF_enumeration.addEnumeration(unicode_value=u'2', tag=None)
STD_ANON_45._InitializeFacetMap(STD_ANON_45._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_46 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 234, 2)
    _Documentation = None
STD_ANON_46._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_47 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 264, 2)
    _Documentation = None
STD_ANON_47._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_48 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 269, 2)
    _Documentation = None
STD_ANON_48._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_49 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 274, 2)
    _Documentation = None
STD_ANON_49._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_50 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ordering-shopper.xsd', 6, 2)
    _Documentation = None
STD_ANON_50._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_51 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 26, 2)
    _Documentation = None
STD_ANON_51._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_52 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 39, 2)
    _Documentation = None
STD_ANON_52._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_53 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 44, 2)
    _Documentation = None
STD_ANON_53._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_54 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 6, 2)
    _Documentation = None
STD_ANON_54._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_55 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 11, 2)
    _Documentation = None
STD_ANON_55._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_56 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 25, 2)
    _Documentation = None
STD_ANON_56._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_57 (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 38, 2)
    _Documentation = None
STD_ANON_57._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_58 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 43, 2)
    _Documentation = None
STD_ANON_58._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_59 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 12, 2)
    _Documentation = None
STD_ANON_59._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_60 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 17, 2)
    _Documentation = None
STD_ANON_60._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_61 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 22, 2)
    _Documentation = None
STD_ANON_61._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_62 (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 27, 2)
    _Documentation = None
STD_ANON_62._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_63 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 32, 2)
    _Documentation = None
STD_ANON_63._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_64 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 37, 2)
    _Documentation = None
STD_ANON_64._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_65 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 42, 2)
    _Documentation = None
STD_ANON_65._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_66 (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 137, 2)
    _Documentation = None
STD_ANON_66._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_67 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 142, 2)
    _Documentation = None
STD_ANON_67._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_68 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 173, 2)
    _Documentation = None
STD_ANON_68._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_69 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 178, 2)
    _Documentation = None
STD_ANON_69._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_70 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 183, 2)
    _Documentation = None
STD_ANON_70._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_71 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 188, 2)
    _Documentation = None
STD_ANON_71._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_72 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 26, 2)
    _Documentation = None
STD_ANON_72._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_73 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 31, 2)
    _Documentation = None
STD_ANON_73._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_74 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 36, 2)
    _Documentation = None
STD_ANON_74._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_75 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 41, 2)
    _Documentation = None
STD_ANON_75._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_76 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 14, 2)
    _Documentation = None
STD_ANON_76._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_77 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 19, 2)
    _Documentation = None
STD_ANON_77._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_78 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 17, 2)
    _Documentation = None
STD_ANON_78._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_79 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 22, 2)
    _Documentation = None
STD_ANON_79._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_80 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 27, 2)
    _Documentation = None
STD_ANON_80._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_81 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 32, 2)
    _Documentation = None
STD_ANON_81._InitializeFacetMap()

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}billing-contact-info uses Python identifier billing_contact_info
    __billing_contact_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'billing-contact-info'), 'billing_contact_info', '__httpws_plimus_com_CTD_ANON_httpws_plimus_combilling_contact_info', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 14, 1), )

    
    billing_contact_info = property(__billing_contact_info.value, __billing_contact_info.set, None, None)

    
    # Element {http://ws.plimus.com}credit-card uses Python identifier credit_card
    __credit_card = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'credit-card'), 'credit_card', '__httpws_plimus_com_CTD_ANON_httpws_plimus_comcredit_card', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 28, 1), )

    
    credit_card = property(__credit_card.value, __credit_card.set, None, None)

    _ElementMap.update({
        __billing_contact_info.name() : __billing_contact_info,
        __credit_card.name() : __credit_card
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 15, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'zip'), 'zip', '__httpws_plimus_com_CTD_ANON__httpws_plimus_comzip', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 5, 1), )

    
    zip = property(__zip.value, __zip.set, None, None)

    
    # Element {http://ws.plimus.com}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'state'), 'state', '__httpws_plimus_com_CTD_ANON__httpws_plimus_comstate', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 10, 1), )

    
    state = property(__state.value, __state.set, None, None)

    
    # Element {http://ws.plimus.com}last-name uses Python identifier last_name
    __last_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'last-name'), 'last_name', '__httpws_plimus_com_CTD_ANON__httpws_plimus_comlast_name', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 15, 1), )

    
    last_name = property(__last_name.value, __last_name.set, None, None)

    
    # Element {http://ws.plimus.com}first-name uses Python identifier first_name
    __first_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'first-name'), 'first_name', '__httpws_plimus_com_CTD_ANON__httpws_plimus_comfirst_name', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 20, 1), )

    
    first_name = property(__first_name.value, __first_name.set, None, None)

    
    # Element {http://ws.plimus.com}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'country'), 'country', '__httpws_plimus_com_CTD_ANON__httpws_plimus_comcountry', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 25, 1), )

    
    country = property(__country.value, __country.set, None, None)

    
    # Element {http://ws.plimus.com}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httpws_plimus_com_CTD_ANON__httpws_plimus_comcity', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 30, 1), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://ws.plimus.com}address2 uses Python identifier address2
    __address2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'address2'), 'address2', '__httpws_plimus_com_CTD_ANON__httpws_plimus_comaddress2', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 35, 1), )

    
    address2 = property(__address2.value, __address2.set, None, None)

    
    # Element {http://ws.plimus.com}address1 uses Python identifier address1
    __address1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'address1'), 'address1', '__httpws_plimus_com_CTD_ANON__httpws_plimus_comaddress1', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 40, 1), )

    
    address1 = property(__address1.value, __address1.set, None, None)

    _ElementMap.update({
        __zip.name() : __zip,
        __state.name() : __state,
        __last_name.name() : __last_name,
        __first_name.name() : __first_name,
        __country.name() : __country,
        __city.name() : __city,
        __address2.name() : __address2,
        __address1.name() : __address1
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 29, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}card-type uses Python identifier card_type
    __card_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'card-type'), 'card_type', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comcard_type', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 43, 1), )

    
    card_type = property(__card_type.value, __card_type.set, None, None)

    
    # Element {http://ws.plimus.com}card-number uses Python identifier card_number
    __card_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'card-number'), 'card_number', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comcard_number', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 48, 1), )

    
    card_number = property(__card_number.value, __card_number.set, None, None)

    
    # Element {http://ws.plimus.com}card-last-four-digits uses Python identifier card_last_four_digits
    __card_last_four_digits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'card-last-four-digits'), 'card_last_four_digits', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comcard_last_four_digits', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 53, 1), )

    
    card_last_four_digits = property(__card_last_four_digits.value, __card_last_four_digits.set, None, None)

    
    # Element {http://ws.plimus.com}security-code uses Python identifier security_code
    __security_code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'security-code'), 'security_code', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comsecurity_code', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 58, 1), )

    
    security_code = property(__security_code.value, __security_code.set, None, None)

    
    # Element {http://ws.plimus.com}expiration-month uses Python identifier expiration_month
    __expiration_month = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'expiration-month'), 'expiration_month', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comexpiration_month', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 63, 1), )

    
    expiration_month = property(__expiration_month.value, __expiration_month.set, None, None)

    
    # Element {http://ws.plimus.com}expiration-year uses Python identifier expiration_year
    __expiration_year = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'expiration-year'), 'expiration_year', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comexpiration_year', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 68, 1), )

    
    expiration_year = property(__expiration_year.value, __expiration_year.set, None, None)

    
    # Element {http://ws.plimus.com}start-year uses Python identifier start_year
    __start_year = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'start-year'), 'start_year', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comstart_year', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 73, 1), )

    
    start_year = property(__start_year.value, __start_year.set, None, None)

    
    # Element {http://ws.plimus.com}start-month uses Python identifier start_month
    __start_month = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'start-month'), 'start_month', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comstart_month', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 78, 1), )

    
    start_month = property(__start_month.value, __start_month.set, None, None)

    
    # Element {http://ws.plimus.com}issue-number uses Python identifier issue_number
    __issue_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'issue-number'), 'issue_number', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comissue_number', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 83, 1), )

    
    issue_number = property(__issue_number.value, __issue_number.set, None, None)

    _ElementMap.update({
        __card_type.name() : __card_type,
        __card_number.name() : __card_number,
        __card_last_four_digits.name() : __card_last_four_digits,
        __security_code.name() : __security_code,
        __expiration_month.name() : __expiration_month,
        __expiration_year.name() : __expiration_year,
        __start_year.name() : __start_year,
        __start_month.name() : __start_month,
        __issue_number.name() : __issue_number
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 10, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}ecp-info uses Python identifier ecp_info
    __ecp_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ecp-info'), 'ecp_info', '__httpws_plimus_com_CTD_ANON_3_httpws_plimus_comecp_info', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 17, 1), )

    
    ecp_info = property(__ecp_info.value, __ecp_info.set, None, None)

    _ElementMap.update({
        __ecp_info.name() : __ecp_info
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 18, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}billing-contact-info uses Python identifier billing_contact_info
    __billing_contact_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'billing-contact-info'), 'billing_contact_info', '__httpws_plimus_com_CTD_ANON_4_httpws_plimus_combilling_contact_info', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 14, 1), )

    
    billing_contact_info = property(__billing_contact_info.value, __billing_contact_info.set, None, None)

    
    # Element {http://ws.plimus.com}ecp uses Python identifier ecp
    __ecp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ecp'), 'ecp', '__httpws_plimus_com_CTD_ANON_4_httpws_plimus_comecp', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 26, 1), )

    
    ecp = property(__ecp.value, __ecp.set, None, None)

    _ElementMap.update({
        __billing_contact_info.name() : __billing_contact_info,
        __ecp.name() : __ecp
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 27, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}account-number uses Python identifier account_number
    __account_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'account-number'), 'account_number', '__httpws_plimus_com_CTD_ANON_5_httpws_plimus_comaccount_number', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 38, 1), )

    
    account_number = property(__account_number.value, __account_number.set, None, None)

    
    # Element {http://ws.plimus.com}account-type uses Python identifier account_type
    __account_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'account-type'), 'account_type', '__httpws_plimus_com_CTD_ANON_5_httpws_plimus_comaccount_type', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 44, 1), )

    
    account_type = property(__account_type.value, __account_type.set, None, None)

    
    # Element {http://ws.plimus.com}routing-number uses Python identifier routing_number
    __routing_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'routing-number'), 'routing_number', '__httpws_plimus_com_CTD_ANON_5_httpws_plimus_comrouting_number', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 50, 1), )

    
    routing_number = property(__routing_number.value, __routing_number.set, None, None)

    
    # Element {http://ws.plimus.com}public-account-number uses Python identifier public_account_number
    __public_account_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'public-account-number'), 'public_account_number', '__httpws_plimus_com_CTD_ANON_5_httpws_plimus_compublic_account_number', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 56, 1), )

    
    public_account_number = property(__public_account_number.value, __public_account_number.set, None, None)

    
    # Element {http://ws.plimus.com}public-routing-number uses Python identifier public_routing_number
    __public_routing_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'public-routing-number'), 'public_routing_number', '__httpws_plimus_com_CTD_ANON_5_httpws_plimus_compublic_routing_number', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 62, 1), )

    
    public_routing_number = property(__public_routing_number.value, __public_routing_number.set, None, None)

    _ElementMap.update({
        __account_number.name() : __account_number,
        __account_type.name() : __account_type,
        __routing_number.name() : __routing_number,
        __public_account_number.name() : __public_account_number,
        __public_routing_number.name() : __public_routing_number
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}license-key uses Python identifier license_key
    __license_key = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'license-key'), 'license_key', '__httpws_plimus_com_CTD_ANON_6_httpws_plimus_comlicense_key', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 46, 1), )

    
    license_key = property(__license_key.value, __license_key.set, None, None)

    
    # Element {http://ws.plimus.com}sku-id uses Python identifier sku_id
    __sku_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sku-id'), 'sku_id', '__httpws_plimus_com_CTD_ANON_6_httpws_plimus_comsku_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 25, 1), )

    
    sku_id = property(__sku_id.value, __sku_id.set, None, None)

    
    # Element {http://ws.plimus.com}sku-name uses Python identifier sku_name
    __sku_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sku-name'), 'sku_name', '__httpws_plimus_com_CTD_ANON_6_httpws_plimus_comsku_name', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 30, 1), )

    
    sku_name = property(__sku_name.value, __sku_name.set, None, None)

    _ElementMap.update({
        __license_key.name() : __license_key,
        __sku_id.name() : __sku_id,
        __sku_name.name() : __sku_name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 16, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}download-link uses Python identifier download_link
    __download_link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'download-link'), 'download_link', '__httpws_plimus_com_CTD_ANON_7_httpws_plimus_comdownload_link', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 51, 1), )

    
    download_link = property(__download_link.value, __download_link.set, None, None)

    
    # Element {http://ws.plimus.com}sku-id uses Python identifier sku_id
    __sku_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sku-id'), 'sku_id', '__httpws_plimus_com_CTD_ANON_7_httpws_plimus_comsku_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 25, 1), )

    
    sku_id = property(__sku_id.value, __sku_id.set, None, None)

    
    # Element {http://ws.plimus.com}sku-name uses Python identifier sku_name
    __sku_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sku-name'), 'sku_name', '__httpws_plimus_com_CTD_ANON_7_httpws_plimus_comsku_name', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 30, 1), )

    
    sku_name = property(__sku_name.value, __sku_name.set, None, None)

    _ElementMap.update({
        __download_link.name() : __download_link,
        __sku_id.name() : __sku_id,
        __sku_name.name() : __sku_name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 25, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}sku-license uses Python identifier sku_license
    __sku_license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sku-license'), 'sku_license', '__httpws_plimus_com_CTD_ANON_8_httpws_plimus_comsku_license', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 6, 1), )

    
    sku_license = property(__sku_license.value, __sku_license.set, None, None)

    _ElementMap.update({
        __sku_license.name() : __sku_license
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 32, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}sku-download-link uses Python identifier sku_download_link
    __sku_download_link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sku-download-link'), 'sku_download_link', '__httpws_plimus_com_CTD_ANON_9_httpws_plimus_comsku_download_link', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 15, 1), )

    
    sku_download_link = property(__sku_download_link.value, __sku_download_link.set, None, None)

    _ElementMap.update({
        __sku_download_link.name() : __sku_download_link
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 39, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}license-keys uses Python identifier license_keys
    __license_keys = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'license-keys'), 'license_keys', '__httpws_plimus_com_CTD_ANON_10_httpws_plimus_comlicense_keys', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 24, 1), )

    
    license_keys = property(__license_keys.value, __license_keys.set, None, None)

    
    # Element {http://ws.plimus.com}download-links uses Python identifier download_links
    __download_links = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'download-links'), 'download_links', '__httpws_plimus_com_CTD_ANON_10_httpws_plimus_comdownload_links', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 31, 1), )

    
    download_links = property(__download_links.value, __download_links.set, None, None)

    _ElementMap.update({
        __license_keys.name() : __license_keys,
        __download_links.name() : __download_links
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 19, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'state'), 'state', '__httpws_plimus_com_CTD_ANON_11_httpws_plimus_comstate', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 10, 1), )

    
    state = property(__state.value, __state.set, None, None)

    
    # Element {http://ws.plimus.com}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'country'), 'country', '__httpws_plimus_com_CTD_ANON_11_httpws_plimus_comcountry', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 25, 1), )

    
    country = property(__country.value, __country.set, None, None)

    
    # Element {http://ws.plimus.com}store-id uses Python identifier store_id
    __store_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'store-id'), 'store_id', '__httpws_plimus_com_CTD_ANON_11_httpws_plimus_comstore_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 7, 1), )

    
    store_id = property(__store_id.value, __store_id.set, None, None)

    
    # Element {http://ws.plimus.com}quantity uses Python identifier quantity
    __quantity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'quantity'), 'quantity', '__httpws_plimus_com_CTD_ANON_11_httpws_plimus_comquantity', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 12, 1), )

    
    quantity = property(__quantity.value, __quantity.set, None, None)

    
    # Element {http://ws.plimus.com}unit-price uses Python identifier unit_price
    __unit_price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'unit-price'), 'unit_price', '__httpws_plimus_com_CTD_ANON_11_httpws_plimus_comunit_price', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 34, 1), )

    
    unit_price = property(__unit_price.value, __unit_price.set, None, None)

    
    # Element {http://ws.plimus.com}total-price uses Python identifier total_price
    __total_price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'total-price'), 'total_price', '__httpws_plimus_com_CTD_ANON_11_httpws_plimus_comtotal_price', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 41, 1), )

    
    total_price = property(__total_price.value, __total_price.set, None, None)

    
    # Element {http://ws.plimus.com}total-price-with-tax uses Python identifier total_price_with_tax
    __total_price_with_tax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'total-price-with-tax'), 'total_price_with_tax', '__httpws_plimus_com_CTD_ANON_11_httpws_plimus_comtotal_price_with_tax', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 48, 1), )

    
    total_price_with_tax = property(__total_price_with_tax.value, __total_price_with_tax.set, None, None)

    
    # Element {http://ws.plimus.com}tax uses Python identifier tax
    __tax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tax'), 'tax', '__httpws_plimus_com_CTD_ANON_11_httpws_plimus_comtax', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 23, 1), )

    
    tax = property(__tax.value, __tax.set, None, None)

    
    # Element {http://ws.plimus.com}tax-recurring uses Python identifier tax_recurring
    __tax_recurring = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tax-recurring'), 'tax_recurring', '__httpws_plimus_com_CTD_ANON_11_httpws_plimus_comtax_recurring', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 28, 1), )

    
    tax_recurring = property(__tax_recurring.value, __tax_recurring.set, None, None)

    
    # Element {http://ws.plimus.com}tax-rate uses Python identifier tax_rate
    __tax_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tax-rate'), 'tax_rate', '__httpws_plimus_com_CTD_ANON_11_httpws_plimus_comtax_rate', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 33, 1), )

    
    tax_rate = property(__tax_rate.value, __tax_rate.set, None, None)

    _ElementMap.update({
        __state.name() : __state,
        __country.name() : __country,
        __store_id.name() : __store_id,
        __quantity.name() : __quantity,
        __unit_price.name() : __unit_price,
        __total_price.name() : __total_price,
        __total_price_with_tax.name() : __total_price_with_tax,
        __tax.name() : __tax,
        __tax_recurring.name() : __tax_recurring,
        __tax_rate.name() : __tax_rate
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 35, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}charge-price uses Python identifier charge_price
    __charge_price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'charge-price'), 'charge_price', '__httpws_plimus_com_CTD_ANON_12_httpws_plimus_comcharge_price', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 55, 1), )

    
    charge_price = property(__charge_price.value, __charge_price.set, None, None)

    _ElementMap.update({
        __charge_price.name() : __charge_price
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 42, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}charge-price uses Python identifier charge_price
    __charge_price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'charge-price'), 'charge_price', '__httpws_plimus_com_CTD_ANON_13_httpws_plimus_comcharge_price', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 55, 1), )

    
    charge_price = property(__charge_price.value, __charge_price.set, None, None)

    _ElementMap.update({
        __charge_price.name() : __charge_price
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 49, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}charge-price uses Python identifier charge_price
    __charge_price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'charge-price'), 'charge_price', '__httpws_plimus_com_CTD_ANON_14_httpws_plimus_comcharge_price', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 55, 1), )

    
    charge_price = property(__charge_price.value, __charge_price.set, None, None)

    _ElementMap.update({
        __charge_price.name() : __charge_price
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 56, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}tax-included uses Python identifier tax_included
    __tax_included = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tax-included'), 'tax_included', '__httpws_plimus_com_CTD_ANON_15_httpws_plimus_comtax_included', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 17, 1), )

    
    tax_included = property(__tax_included.value, __tax_included.set, None, None)

    
    # Element {http://ws.plimus.com}charge-type uses Python identifier charge_type
    __charge_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'charge-type'), 'charge_type', '__httpws_plimus_com_CTD_ANON_15_httpws_plimus_comcharge_type', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 66, 1), )

    
    charge_type = property(__charge_type.value, __charge_type.set, None, None)

    
    # Element {http://ws.plimus.com}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'value'), 'value_', '__httpws_plimus_com_CTD_ANON_15_httpws_plimus_comvalue', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 5, 1), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element {http://ws.plimus.com}formatted-price uses Python identifier formatted_price
    __formatted_price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'formatted-price'), 'formatted_price', '__httpws_plimus_com_CTD_ANON_15_httpws_plimus_comformatted_price', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 29, 1), )

    
    formatted_price = property(__formatted_price.value, __formatted_price.set, None, None)

    
    # Element {http://ws.plimus.com}currency uses Python identifier currency
    __currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'currency'), 'currency', '__httpws_plimus_com_CTD_ANON_15_httpws_plimus_comcurrency', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1), )

    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        __tax_included.name() : __tax_included,
        __charge_type.name() : __charge_type,
        __value.name() : __value,
        __formatted_price.name() : __formatted_price,
        __currency.name() : __currency
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 44, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}param-value uses Python identifier param_value
    __param_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'param-value'), 'param_value', '__httpws_plimus_com_CTD_ANON_16_httpws_plimus_comparam_value', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 13, 1), )

    
    param_value = property(__param_value.value, __param_value.set, None, None)

    
    # Element {http://ws.plimus.com}param-name uses Python identifier param_name
    __param_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'param-name'), 'param_name', '__httpws_plimus_com_CTD_ANON_16_httpws_plimus_comparam_name', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 171, 1), )

    
    param_name = property(__param_name.value, __param_name.set, None, None)

    _ElementMap.update({
        __param_value.name() : __param_value,
        __param_name.name() : __param_name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 57, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}credit-card uses Python identifier credit_card
    __credit_card = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'credit-card'), 'credit_card', '__httpws_plimus_com_CTD_ANON_17_httpws_plimus_comcredit_card', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 28, 1), )

    
    credit_card = property(__credit_card.value, __credit_card.set, None, None)

    
    # Element {http://ws.plimus.com}ecp uses Python identifier ecp
    __ecp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ecp'), 'ecp', '__httpws_plimus_com_CTD_ANON_17_httpws_plimus_comecp', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 26, 1), )

    
    ecp = property(__ecp.value, __ecp.set, None, None)

    
    # Element {http://ws.plimus.com}shopper-id uses Python identifier shopper_id
    __shopper_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'shopper-id'), 'shopper_id', '__httpws_plimus_com_CTD_ANON_17_httpws_plimus_comshopper_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 51, 1), )

    
    shopper_id = property(__shopper_id.value, __shopper_id.set, None, None)

    
    # Element {http://ws.plimus.com}seller-shopper-id uses Python identifier seller_shopper_id
    __seller_shopper_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'seller-shopper-id'), 'seller_shopper_id', '__httpws_plimus_com_CTD_ANON_17_httpws_plimus_comseller_shopper_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ordering-shopper.xsd', 5, 1), )

    
    seller_shopper_id = property(__seller_shopper_id.value, __seller_shopper_id.set, None, None)

    
    # Element {http://ws.plimus.com}paypal uses Python identifier paypal
    __paypal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'paypal'), 'paypal', '__httpws_plimus_com_CTD_ANON_17_httpws_plimus_compaypal', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 13, 1), )

    
    paypal = property(__paypal.value, __paypal.set, None, None)

    
    # Element {http://ws.plimus.com}invoice-contact-info uses Python identifier invoice_contact_info
    __invoice_contact_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'invoice-contact-info'), 'invoice_contact_info', '__httpws_plimus_com_CTD_ANON_17_httpws_plimus_cominvoice_contact_info', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 114, 1), )

    
    invoice_contact_info = property(__invoice_contact_info.value, __invoice_contact_info.set, None, None)

    
    # Element {http://ws.plimus.com}three-d-authenticated-info uses Python identifier three_d_authenticated_info
    __three_d_authenticated_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'three-d-authenticated-info'), 'three_d_authenticated_info', '__httpws_plimus_com_CTD_ANON_17_httpws_plimus_comthree_d_authenticated_info', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 5, 1), )

    
    three_d_authenticated_info = property(__three_d_authenticated_info.value, __three_d_authenticated_info.set, None, None)

    
    # Element {http://ws.plimus.com}web-info uses Python identifier web_info
    __web_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'web-info'), 'web_info', '__httpws_plimus_com_CTD_ANON_17_httpws_plimus_comweb_info', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 5, 1), )

    
    web_info = property(__web_info.value, __web_info.set, None, None)

    _ElementMap.update({
        __credit_card.name() : __credit_card,
        __ecp.name() : __ecp,
        __shopper_id.name() : __shopper_id,
        __seller_shopper_id.name() : __seller_shopper_id,
        __paypal.name() : __paypal,
        __invoice_contact_info.name() : __invoice_contact_info,
        __three_d_authenticated_info.name() : __three_d_authenticated_info,
        __web_info.name() : __web_info
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 71, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}soft-descriptor uses Python identifier soft_descriptor
    __soft_descriptor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'soft-descriptor'), 'soft_descriptor', '__httpws_plimus_com_CTD_ANON_18_httpws_plimus_comsoft_descriptor', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 38, 1), )

    
    soft_descriptor = property(__soft_descriptor.value, __soft_descriptor.set, None, None)

    
    # Element {http://ws.plimus.com}invoices uses Python identifier invoices
    __invoices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'invoices'), 'invoices', '__httpws_plimus_com_CTD_ANON_18_httpws_plimus_cominvoices', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 80, 1), )

    
    invoices = property(__invoices.value, __invoices.set, None, None)

    
    # Element {http://ws.plimus.com}invoice-status uses Python identifier invoice_status
    __invoice_status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'invoice-status'), 'invoice_status', '__httpws_plimus_com_CTD_ANON_18_httpws_plimus_cominvoice_status', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 151, 1), )

    
    invoice_status = property(__invoice_status.value, __invoice_status.set, None, None)

    
    # Element {http://ws.plimus.com}invoice-id uses Python identifier invoice_id
    __invoice_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'invoice-id'), 'invoice_id', '__httpws_plimus_com_CTD_ANON_18_httpws_plimus_cominvoice_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 181, 1), )

    
    invoice_id = property(__invoice_id.value, __invoice_id.set, None, None)

    _ElementMap.update({
        __soft_descriptor.name() : __soft_descriptor,
        __invoices.name() : __invoices,
        __invoice_status.name() : __invoice_status,
        __invoice_id.name() : __invoice_id
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 81, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}invoice uses Python identifier invoice
    __invoice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'invoice'), 'invoice', '__httpws_plimus_com_CTD_ANON_19_httpws_plimus_cominvoice', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 87, 1), )

    
    invoice = property(__invoice.value, __invoice.set, None, None)

    _ElementMap.update({
        __invoice.name() : __invoice
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 88, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}financial-transactions uses Python identifier financial_transactions
    __financial_transactions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'financial-transactions'), 'financial_transactions', '__httpws_plimus_com_CTD_ANON_20_httpws_plimus_comfinancial_transactions', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 96, 1), )

    
    financial_transactions = property(__financial_transactions.value, __financial_transactions.set, None, None)

    
    # Element {http://ws.plimus.com}invoice-id uses Python identifier invoice_id
    __invoice_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'invoice-id'), 'invoice_id', '__httpws_plimus_com_CTD_ANON_20_httpws_plimus_cominvoice_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 181, 1), )

    
    invoice_id = property(__invoice_id.value, __invoice_id.set, None, None)

    
    # Element {http://ws.plimus.com}url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'url'), 'url', '__httpws_plimus_com_CTD_ANON_20_httpws_plimus_comurl', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 268, 1), )

    
    url = property(__url.value, __url.set, None, None)

    _ElementMap.update({
        __financial_transactions.name() : __financial_transactions,
        __invoice_id.name() : __invoice_id,
        __url.name() : __url
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 97, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}financial-transaction uses Python identifier financial_transaction
    __financial_transaction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'financial-transaction'), 'financial_transaction', '__httpws_plimus_com_CTD_ANON_21_httpws_plimus_comfinancial_transaction', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 103, 1), )

    
    financial_transaction = property(__financial_transaction.value, __financial_transaction.set, None, None)

    _ElementMap.update({
        __financial_transaction.name() : __financial_transaction
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 104, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}credit-card uses Python identifier credit_card
    __credit_card = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'credit-card'), 'credit_card', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_comcredit_card', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 28, 1), )

    
    credit_card = property(__credit_card.value, __credit_card.set, None, None)

    
    # Element {http://ws.plimus.com}ecp uses Python identifier ecp
    __ecp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ecp'), 'ecp', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_comecp', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 26, 1), )

    
    ecp = property(__ecp.value, __ecp.set, None, None)

    
    # Element {http://ws.plimus.com}tax uses Python identifier tax
    __tax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tax'), 'tax', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_comtax', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 23, 1), )

    
    tax = property(__tax.value, __tax.set, None, None)

    
    # Element {http://ws.plimus.com}tax-rate uses Python identifier tax_rate
    __tax_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tax-rate'), 'tax_rate', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_comtax_rate', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 33, 1), )

    
    tax_rate = property(__tax_rate.value, __tax_rate.set, None, None)

    
    # Element {http://ws.plimus.com}soft-descriptor uses Python identifier soft_descriptor
    __soft_descriptor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'soft-descriptor'), 'soft_descriptor', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_comsoft_descriptor', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 38, 1), )

    
    soft_descriptor = property(__soft_descriptor.value, __soft_descriptor.set, None, None)

    
    # Element {http://ws.plimus.com}skus uses Python identifier skus
    __skus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'skus'), 'skus', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_comskus', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 124, 1), )

    
    skus = property(__skus.value, __skus.set, None, None)

    
    # Element {http://ws.plimus.com}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'status'), 'status', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_comstatus', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 131, 1), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element {http://ws.plimus.com}date-due uses Python identifier date_due
    __date_due = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'date-due'), 'date_due', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_comdate_due', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 136, 1), )

    
    date_due = property(__date_due.value, __date_due.set, None, None)

    
    # Element {http://ws.plimus.com}date-created uses Python identifier date_created
    __date_created = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'date-created'), 'date_created', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_comdate_created', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 141, 1), )

    
    date_created = property(__date_created.value, __date_created.set, None, None)

    
    # Element {http://ws.plimus.com}payment-method uses Python identifier payment_method
    __payment_method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'payment-method'), 'payment_method', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_compayment_method', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 146, 1), )

    
    payment_method = property(__payment_method.value, __payment_method.set, None, None)

    
    # Element {http://ws.plimus.com}target-balance uses Python identifier target_balance
    __target_balance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'target-balance'), 'target_balance', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_comtarget_balance', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 273, 2), )

    
    target_balance = property(__target_balance.value, __target_balance.set, None, None)

    
    # Element {http://ws.plimus.com}paypal-transaction-data uses Python identifier paypal_transaction_data
    __paypal_transaction_data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'paypal-transaction-data'), 'paypal_transaction_data', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_compaypal_transaction_data', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 17, 1), )

    
    paypal_transaction_data = property(__paypal_transaction_data.value, __paypal_transaction_data.set, None, None)

    
    # Element {http://ws.plimus.com}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_comamount', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 37, 1), )

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://ws.plimus.com}currency uses Python identifier currency
    __currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'currency'), 'currency', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_comcurrency', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1), )

    
    currency = property(__currency.value, __currency.set, None, None)

    
    # Element {http://ws.plimus.com}invoice-contact-info uses Python identifier invoice_contact_info
    __invoice_contact_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'invoice-contact-info'), 'invoice_contact_info', '__httpws_plimus_com_CTD_ANON_22_httpws_plimus_cominvoice_contact_info', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 114, 1), )

    
    invoice_contact_info = property(__invoice_contact_info.value, __invoice_contact_info.set, None, None)

    _ElementMap.update({
        __credit_card.name() : __credit_card,
        __ecp.name() : __ecp,
        __tax.name() : __tax,
        __tax_rate.name() : __tax_rate,
        __soft_descriptor.name() : __soft_descriptor,
        __skus.name() : __skus,
        __status.name() : __status,
        __date_due.name() : __date_due,
        __date_created.name() : __date_created,
        __payment_method.name() : __payment_method,
        __target_balance.name() : __target_balance,
        __paypal_transaction_data.name() : __paypal_transaction_data,
        __amount.name() : __amount,
        __currency.name() : __currency,
        __invoice_contact_info.name() : __invoice_contact_info
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 125, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}sku uses Python identifier sku
    __sku = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sku'), 'sku', '__httpws_plimus_com_CTD_ANON_23_httpws_plimus_comsku', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 6, 1), )

    
    sku = property(__sku.value, __sku.set, None, None)

    _ElementMap.update({
        __sku.name() : __sku
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 157, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}fulfillment uses Python identifier fulfillment
    __fulfillment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fulfillment'), 'fulfillment', '__httpws_plimus_com_CTD_ANON_24_httpws_plimus_comfulfillment', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 38, 1), )

    
    fulfillment = property(__fulfillment.value, __fulfillment.set, None, None)

    
    # Element {http://ws.plimus.com}soft-descriptor uses Python identifier soft_descriptor
    __soft_descriptor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'soft-descriptor'), 'soft_descriptor', '__httpws_plimus_com_CTD_ANON_24_httpws_plimus_comsoft_descriptor', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 38, 1), )

    
    soft_descriptor = property(__soft_descriptor.value, __soft_descriptor.set, None, None)

    
    # Element {http://ws.plimus.com}ordering-shopper uses Python identifier ordering_shopper
    __ordering_shopper = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ordering-shopper'), 'ordering_shopper', '__httpws_plimus_com_CTD_ANON_24_httpws_plimus_comordering_shopper', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 56, 1), )

    
    ordering_shopper = property(__ordering_shopper.value, __ordering_shopper.set, None, None)

    
    # Element {http://ws.plimus.com}post-sale-info uses Python identifier post_sale_info
    __post_sale_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'post-sale-info'), 'post_sale_info', '__httpws_plimus_com_CTD_ANON_24_httpws_plimus_compost_sale_info', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 70, 1), )

    
    post_sale_info = property(__post_sale_info.value, __post_sale_info.set, None, None)

    
    # Element {http://ws.plimus.com}order-id uses Python identifier order_id
    __order_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'order-id'), 'order_id', '__httpws_plimus_com_CTD_ANON_24_httpws_plimus_comorder_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 186, 1), )

    
    order_id = property(__order_id.value, __order_id.set, None, None)

    
    # Element {http://ws.plimus.com}affiliate-id uses Python identifier affiliate_id
    __affiliate_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'affiliate-id'), 'affiliate_id', '__httpws_plimus_com_CTD_ANON_24_httpws_plimus_comaffiliate_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 191, 1), )

    
    affiliate_id = property(__affiliate_id.value, __affiliate_id.set, None, None)

    
    # Element {http://ws.plimus.com}expected-total-price uses Python identifier expected_total_price
    __expected_total_price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'expected-total-price'), 'expected_total_price', '__httpws_plimus_com_CTD_ANON_24_httpws_plimus_comexpected_total_price', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 196, 1), )

    
    expected_total_price = property(__expected_total_price.value, __expected_total_price.set, None, None)

    
    # Element {http://ws.plimus.com}transaction-payment-info uses Python identifier transaction_payment_info
    __transaction_payment_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'transaction-payment-info'), 'transaction_payment_info', '__httpws_plimus_com_CTD_ANON_24_httpws_plimus_comtransaction_payment_info', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 204, 1), )

    
    transaction_payment_info = property(__transaction_payment_info.value, __transaction_payment_info.set, None, None)

    
    # Element {http://ws.plimus.com}cart uses Python identifier cart
    __cart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cart'), 'cart', '__httpws_plimus_com_CTD_ANON_24_httpws_plimus_comcart', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 249, 1), )

    
    cart = property(__cart.value, __cart.set, None, None)

    _ElementMap.update({
        __fulfillment.name() : __fulfillment,
        __soft_descriptor.name() : __soft_descriptor,
        __ordering_shopper.name() : __ordering_shopper,
        __post_sale_info.name() : __post_sale_info,
        __order_id.name() : __order_id,
        __affiliate_id.name() : __affiliate_id,
        __expected_total_price.name() : __expected_total_price,
        __transaction_payment_info.name() : __transaction_payment_info,
        __cart.name() : __cart
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 197, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpws_plimus_com_CTD_ANON_25_httpws_plimus_comamount', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 37, 1), )

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://ws.plimus.com}currency uses Python identifier currency
    __currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'currency'), 'currency', '__httpws_plimus_com_CTD_ANON_25_httpws_plimus_comcurrency', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1), )

    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        __amount.name() : __amount,
        __currency.name() : __currency
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 205, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}paypal-info uses Python identifier paypal_info
    __paypal_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'paypal-info'), 'paypal_info', '__httpws_plimus_com_CTD_ANON_26_httpws_plimus_compaypal_info', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 6, 1), )

    
    paypal_info = property(__paypal_info.value, __paypal_info.set, None, None)

    _ElementMap.update({
        __paypal_info.name() : __paypal_info
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 212, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}coupon uses Python identifier coupon
    __coupon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'coupon'), 'coupon', '__httpws_plimus_com_CTD_ANON_27_httpws_plimus_comcoupon', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 219, 1), )

    
    coupon = property(__coupon.value, __coupon.set, None, None)

    
    # Element {http://ws.plimus.com}coupons-total uses Python identifier coupons_total
    __coupons_total = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'coupons-total'), 'coupons_total', '__httpws_plimus_com_CTD_ANON_27_httpws_plimus_comcoupons_total', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 263, 1), )

    
    coupons_total = property(__coupons_total.value, __coupons_total.set, None, None)

    _ElementMap.update({
        __coupon.name() : __coupon,
        __coupons_total.name() : __coupons_total
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 239, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}quantity uses Python identifier quantity
    __quantity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'quantity'), 'quantity', '__httpws_plimus_com_CTD_ANON_28_httpws_plimus_comquantity', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 12, 1), )

    
    quantity = property(__quantity.value, __quantity.set, None, None)

    
    # Element {http://ws.plimus.com}sku-parameter uses Python identifier sku_parameter
    __sku_parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sku-parameter'), 'sku_parameter', '__httpws_plimus_com_CTD_ANON_28_httpws_plimus_comsku_parameter', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 43, 1), )

    
    sku_parameter = property(__sku_parameter.value, __sku_parameter.set, None, None)

    
    # Element {http://ws.plimus.com}item-sub-total uses Python identifier item_sub_total
    __item_sub_total = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'item-sub-total'), 'item_sub_total', '__httpws_plimus_com_CTD_ANON_28_httpws_plimus_comitem_sub_total', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 176, 1), )

    
    item_sub_total = property(__item_sub_total.value, __item_sub_total.set, None, None)

    
    # Element {http://ws.plimus.com}url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'url'), 'url', '__httpws_plimus_com_CTD_ANON_28_httpws_plimus_comurl', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 268, 1), )

    
    url = property(__url.value, __url.set, None, None)

    
    # Element {http://ws.plimus.com}sku uses Python identifier sku
    __sku = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sku'), 'sku', '__httpws_plimus_com_CTD_ANON_28_httpws_plimus_comsku', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 6, 1), )

    
    sku = property(__sku.value, __sku.set, None, None)

    _ElementMap.update({
        __quantity.name() : __quantity,
        __sku_parameter.name() : __sku_parameter,
        __item_sub_total.name() : __item_sub_total,
        __url.name() : __url,
        __sku.name() : __sku
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 250, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}total-cart-cost uses Python identifier total_cart_cost
    __total_cart_cost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'total-cart-cost'), 'total_cart_cost', '__httpws_plimus_com_CTD_ANON_29_httpws_plimus_comtotal_cart_cost', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 18, 1), )

    
    total_cart_cost = property(__total_cart_cost.value, __total_cart_cost.set, None, None)

    
    # Element {http://ws.plimus.com}tax uses Python identifier tax
    __tax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tax'), 'tax', '__httpws_plimus_com_CTD_ANON_29_httpws_plimus_comtax', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 23, 1), )

    
    tax = property(__tax.value, __tax.set, None, None)

    
    # Element {http://ws.plimus.com}tax-rate uses Python identifier tax_rate
    __tax_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tax-rate'), 'tax_rate', '__httpws_plimus_com_CTD_ANON_29_httpws_plimus_comtax_rate', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 33, 1), )

    
    tax_rate = property(__tax_rate.value, __tax_rate.set, None, None)

    
    # Element {http://ws.plimus.com}coupons uses Python identifier coupons
    __coupons = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'coupons'), 'coupons', '__httpws_plimus_com_CTD_ANON_29_httpws_plimus_comcoupons', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 211, 1), )

    
    coupons = property(__coupons.value, __coupons.set, None, None)

    
    # Element {http://ws.plimus.com}cdod uses Python identifier cdod
    __cdod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cdod'), 'cdod', '__httpws_plimus_com_CTD_ANON_29_httpws_plimus_comcdod', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 224, 1), )

    
    cdod = property(__cdod.value, __cdod.set, None, None)

    
    # Element {http://ws.plimus.com}edw-duration uses Python identifier edw_duration
    __edw_duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'edw-duration'), 'edw_duration', '__httpws_plimus_com_CTD_ANON_29_httpws_plimus_comedw_duration', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 225, 1), )

    
    edw_duration = property(__edw_duration.value, __edw_duration.set, None, None)

    
    # Element {http://ws.plimus.com}charged-currency uses Python identifier charged_currency
    __charged_currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'charged-currency'), 'charged_currency', '__httpws_plimus_com_CTD_ANON_29_httpws_plimus_comcharged_currency', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 233, 1), )

    
    charged_currency = property(__charged_currency.value, __charged_currency.set, None, None)

    
    # Element {http://ws.plimus.com}cart-item uses Python identifier cart_item
    __cart_item = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cart-item'), 'cart_item', '__httpws_plimus_com_CTD_ANON_29_httpws_plimus_comcart_item', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 238, 1), )

    
    cart_item = property(__cart_item.value, __cart_item.set, None, None)

    _ElementMap.update({
        __total_cart_cost.name() : __total_cart_cost,
        __tax.name() : __tax,
        __tax_rate.name() : __tax_rate,
        __coupons.name() : __coupons,
        __cdod.name() : __cdod,
        __edw_duration.name() : __edw_duration,
        __charged_currency.name() : __charged_currency,
        __cart_item.name() : __cart_item
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'url'), 'url', '__httpws_plimus_com_CTD_ANON_30_httpws_plimus_comurl', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 268, 1), )

    
    url = property(__url.value, __url.set, None, None)

    _ElementMap.update({
        __url.name() : __url
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 14, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 18, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}pp-transaction-id uses Python identifier pp_transaction_id
    __pp_transaction_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pp-transaction-id'), 'pp_transaction_id', '__httpws_plimus_com_CTD_ANON_32_httpws_plimus_compp_transaction_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 25, 1), )

    
    pp_transaction_id = property(__pp_transaction_id.value, __pp_transaction_id.set, None, None)

    
    # Element {http://ws.plimus.com}pp-subscription-id uses Python identifier pp_subscription_id
    __pp_subscription_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pp-subscription-id'), 'pp_subscription_id', '__httpws_plimus_com_CTD_ANON_32_httpws_plimus_compp_subscription_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 38, 1), )

    
    pp_subscription_id = property(__pp_subscription_id.value, __pp_subscription_id.set, None, None)

    _ElementMap.update({
        __pp_transaction_id.name() : __pp_transaction_id,
        __pp_subscription_id.name() : __pp_subscription_id
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 31, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}pp-subscription-id uses Python identifier pp_subscription_id
    __pp_subscription_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pp-subscription-id'), 'pp_subscription_id', '__httpws_plimus_com_CTD_ANON_33_httpws_plimus_compp_subscription_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 38, 1), )

    
    pp_subscription_id = property(__pp_subscription_id.value, __pp_subscription_id.set, None, None)

    
    # Element {http://ws.plimus.com}pp-original-transaction-id uses Python identifier pp_original_transaction_id
    __pp_original_transaction_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pp-original-transaction-id'), 'pp_original_transaction_id', '__httpws_plimus_com_CTD_ANON_33_httpws_plimus_compp_original_transaction_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 43, 2), )

    
    pp_original_transaction_id = property(__pp_original_transaction_id.value, __pp_original_transaction_id.set, None, None)

    _ElementMap.update({
        __pp_subscription_id.name() : __pp_subscription_id,
        __pp_original_transaction_id.name() : __pp_original_transaction_id
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 16, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'value'), 'value_', '__httpws_plimus_com_CTD_ANON_34_httpws_plimus_comvalue', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 5, 1), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element {http://ws.plimus.com}formatted-price uses Python identifier formatted_price
    __formatted_price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'formatted-price'), 'formatted_price', '__httpws_plimus_com_CTD_ANON_34_httpws_plimus_comformatted_price', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 29, 1), )

    
    formatted_price = property(__formatted_price.value, __formatted_price.set, None, None)

    
    # Element {http://ws.plimus.com}currency uses Python identifier currency
    __currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'currency'), 'currency', '__httpws_plimus_com_CTD_ANON_34_httpws_plimus_comcurrency', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1), )

    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        __value.name() : __value,
        __formatted_price.name() : __formatted_price,
        __currency.name() : __currency
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 30, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}symbol uses Python identifier symbol
    __symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'symbol'), 'symbol', '__httpws_plimus_com_CTD_ANON_35_httpws_plimus_comsymbol', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 10, 1), )

    
    symbol = property(__symbol.value, __symbol.set, None, None)

    
    # Element {http://ws.plimus.com}iso uses Python identifier iso
    __iso = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iso'), 'iso', '__httpws_plimus_com_CTD_ANON_35_httpws_plimus_comiso', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 24, 1), )

    
    iso = property(__iso.value, __iso.set, None, None)

    _ElementMap.update({
        __symbol.name() : __symbol,
        __iso.name() : __iso
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 47, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}store-id uses Python identifier store_id
    __store_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'store-id'), 'store_id', '__httpws_plimus_com_CTD_ANON_36_httpws_plimus_comstore_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 7, 1), )

    
    store_id = property(__store_id.value, __store_id.set, None, None)

    
    # Element {http://ws.plimus.com}seller-shopper-id uses Python identifier seller_shopper_id
    __seller_shopper_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'seller-shopper-id'), 'seller_shopper_id', '__httpws_plimus_com_CTD_ANON_36_httpws_plimus_comseller_shopper_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ordering-shopper.xsd', 5, 1), )

    
    seller_shopper_id = property(__seller_shopper_id.value, __seller_shopper_id.set, None, None)

    
    # Element {http://ws.plimus.com}vat-code uses Python identifier vat_code
    __vat_code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'vat-code'), 'vat_code', '__httpws_plimus_com_CTD_ANON_36_httpws_plimus_comvat_code', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 11, 1), )

    
    vat_code = property(__vat_code.value, __vat_code.set, None, None)

    
    # Element {http://ws.plimus.com}shopper-currency uses Python identifier shopper_currency
    __shopper_currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'shopper-currency'), 'shopper_currency', '__httpws_plimus_com_CTD_ANON_36_httpws_plimus_comshopper_currency', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 16, 1), )

    
    shopper_currency = property(__shopper_currency.value, __shopper_currency.set, None, None)

    
    # Element {http://ws.plimus.com}locale uses Python identifier locale
    __locale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'locale'), 'locale', '__httpws_plimus_com_CTD_ANON_36_httpws_plimus_comlocale', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 21, 1), )

    
    locale = property(__locale.value, __locale.set, None, None)

    
    # Element {http://ws.plimus.com}permitted-future-charges uses Python identifier permitted_future_charges
    __permitted_future_charges = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'permitted-future-charges'), 'permitted_future_charges', '__httpws_plimus_com_CTD_ANON_36_httpws_plimus_compermitted_future_charges', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 26, 1), )

    
    permitted_future_charges = property(__permitted_future_charges.value, __permitted_future_charges.set, None, None)

    
    # Element {http://ws.plimus.com}username uses Python identifier username
    __username = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'username'), 'username', '__httpws_plimus_com_CTD_ANON_36_httpws_plimus_comusername', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 36, 1), )

    
    username = property(__username.value, __username.set, None, None)

    
    # Element {http://ws.plimus.com}password uses Python identifier password
    __password = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'password'), 'password', '__httpws_plimus_com_CTD_ANON_36_httpws_plimus_compassword', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 41, 1), )

    
    password = property(__password.value, __password.set, None, None)

    
    # Element {http://ws.plimus.com}shopper-contact-info uses Python identifier shopper_contact_info
    __shopper_contact_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'shopper-contact-info'), 'shopper_contact_info', '__httpws_plimus_com_CTD_ANON_36_httpws_plimus_comshopper_contact_info', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 64, 1), )

    
    shopper_contact_info = property(__shopper_contact_info.value, __shopper_contact_info.set, None, None)

    
    # Element {http://ws.plimus.com}shipping-contact-info uses Python identifier shipping_contact_info
    __shipping_contact_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'shipping-contact-info'), 'shipping_contact_info', '__httpws_plimus_com_CTD_ANON_36_httpws_plimus_comshipping_contact_info', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 93, 1), )

    
    shipping_contact_info = property(__shipping_contact_info.value, __shipping_contact_info.set, None, None)

    
    # Element {http://ws.plimus.com}invoice-contacts-info uses Python identifier invoice_contacts_info
    __invoice_contacts_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'invoice-contacts-info'), 'invoice_contacts_info', '__httpws_plimus_com_CTD_ANON_36_httpws_plimus_cominvoice_contacts_info', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 107, 1), )

    
    invoice_contacts_info = property(__invoice_contacts_info.value, __invoice_contacts_info.set, None, None)

    
    # Element {http://ws.plimus.com}payment-info uses Python identifier payment_info
    __payment_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'payment-info'), 'payment_info', '__httpws_plimus_com_CTD_ANON_36_httpws_plimus_compayment_info', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 146, 1), )

    
    payment_info = property(__payment_info.value, __payment_info.set, None, None)

    _ElementMap.update({
        __store_id.name() : __store_id,
        __seller_shopper_id.name() : __seller_shopper_id,
        __vat_code.name() : __vat_code,
        __shopper_currency.name() : __shopper_currency,
        __locale.name() : __locale,
        __permitted_future_charges.name() : __permitted_future_charges,
        __username.name() : __username,
        __password.name() : __password,
        __shopper_contact_info.name() : __shopper_contact_info,
        __shipping_contact_info.name() : __shipping_contact_info,
        __invoice_contacts_info.name() : __invoice_contacts_info,
        __payment_info.name() : __payment_info
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 65, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'zip'), 'zip', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comzip', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 5, 1), )

    
    zip = property(__zip.value, __zip.set, None, None)

    
    # Element {http://ws.plimus.com}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'state'), 'state', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comstate', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 10, 1), )

    
    state = property(__state.value, __state.set, None, None)

    
    # Element {http://ws.plimus.com}last-name uses Python identifier last_name
    __last_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'last-name'), 'last_name', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comlast_name', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 15, 1), )

    
    last_name = property(__last_name.value, __last_name.set, None, None)

    
    # Element {http://ws.plimus.com}first-name uses Python identifier first_name
    __first_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'first-name'), 'first_name', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comfirst_name', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 20, 1), )

    
    first_name = property(__first_name.value, __first_name.set, None, None)

    
    # Element {http://ws.plimus.com}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'country'), 'country', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comcountry', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 25, 1), )

    
    country = property(__country.value, __country.set, None, None)

    
    # Element {http://ws.plimus.com}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comcity', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 30, 1), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://ws.plimus.com}address2 uses Python identifier address2
    __address2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'address2'), 'address2', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comaddress2', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 35, 1), )

    
    address2 = property(__address2.value, __address2.set, None, None)

    
    # Element {http://ws.plimus.com}address1 uses Python identifier address1
    __address1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'address1'), 'address1', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comaddress1', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 40, 1), )

    
    address1 = property(__address1.value, __address1.set, None, None)

    
    # Element {http://ws.plimus.com}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comtitle', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 31, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://ws.plimus.com}phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'phone'), 'phone', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comphone', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 141, 1), )

    
    phone = property(__phone.value, __phone.set, None, None)

    
    # Element {http://ws.plimus.com}fax uses Python identifier fax
    __fax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fax'), 'fax', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comfax', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 177, 1), )

    
    fax = property(__fax.value, __fax.set, None, None)

    
    # Element {http://ws.plimus.com}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'email'), 'email', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comemail', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 182, 1), )

    
    email = property(__email.value, __email.set, None, None)

    
    # Element {http://ws.plimus.com}company-name uses Python identifier company_name
    __company_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'company-name'), 'company_name', '__httpws_plimus_com_CTD_ANON_37_httpws_plimus_comcompany_name', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 187, 1), )

    
    company_name = property(__company_name.value, __company_name.set, None, None)

    _ElementMap.update({
        __zip.name() : __zip,
        __state.name() : __state,
        __last_name.name() : __last_name,
        __first_name.name() : __first_name,
        __country.name() : __country,
        __city.name() : __city,
        __address2.name() : __address2,
        __address1.name() : __address1,
        __title.name() : __title,
        __phone.name() : __phone,
        __fax.name() : __fax,
        __email.name() : __email,
        __company_name.name() : __company_name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 84, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}shopper-info uses Python identifier shopper_info
    __shopper_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'shopper-info'), 'shopper_info', '__httpws_plimus_com_CTD_ANON_38_httpws_plimus_comshopper_info', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 46, 1), )

    
    shopper_info = property(__shopper_info.value, __shopper_info.set, None, None)

    
    # Element {http://ws.plimus.com}three-d-authenticated-info uses Python identifier three_d_authenticated_info
    __three_d_authenticated_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'three-d-authenticated-info'), 'three_d_authenticated_info', '__httpws_plimus_com_CTD_ANON_38_httpws_plimus_comthree_d_authenticated_info', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 5, 1), )

    
    three_d_authenticated_info = property(__three_d_authenticated_info.value, __three_d_authenticated_info.set, None, None)

    
    # Element {http://ws.plimus.com}web-info uses Python identifier web_info
    __web_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'web-info'), 'web_info', '__httpws_plimus_com_CTD_ANON_38_httpws_plimus_comweb_info', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 5, 1), )

    
    web_info = property(__web_info.value, __web_info.set, None, None)

    _ElementMap.update({
        __shopper_info.name() : __shopper_info,
        __three_d_authenticated_info.name() : __three_d_authenticated_info,
        __web_info.name() : __web_info
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_39 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 94, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'zip'), 'zip', '__httpws_plimus_com_CTD_ANON_39_httpws_plimus_comzip', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 5, 1), )

    
    zip = property(__zip.value, __zip.set, None, None)

    
    # Element {http://ws.plimus.com}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'state'), 'state', '__httpws_plimus_com_CTD_ANON_39_httpws_plimus_comstate', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 10, 1), )

    
    state = property(__state.value, __state.set, None, None)

    
    # Element {http://ws.plimus.com}last-name uses Python identifier last_name
    __last_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'last-name'), 'last_name', '__httpws_plimus_com_CTD_ANON_39_httpws_plimus_comlast_name', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 15, 1), )

    
    last_name = property(__last_name.value, __last_name.set, None, None)

    
    # Element {http://ws.plimus.com}first-name uses Python identifier first_name
    __first_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'first-name'), 'first_name', '__httpws_plimus_com_CTD_ANON_39_httpws_plimus_comfirst_name', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 20, 1), )

    
    first_name = property(__first_name.value, __first_name.set, None, None)

    
    # Element {http://ws.plimus.com}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'country'), 'country', '__httpws_plimus_com_CTD_ANON_39_httpws_plimus_comcountry', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 25, 1), )

    
    country = property(__country.value, __country.set, None, None)

    
    # Element {http://ws.plimus.com}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httpws_plimus_com_CTD_ANON_39_httpws_plimus_comcity', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 30, 1), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://ws.plimus.com}address2 uses Python identifier address2
    __address2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'address2'), 'address2', '__httpws_plimus_com_CTD_ANON_39_httpws_plimus_comaddress2', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 35, 1), )

    
    address2 = property(__address2.value, __address2.set, None, None)

    
    # Element {http://ws.plimus.com}address1 uses Python identifier address1
    __address1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'address1'), 'address1', '__httpws_plimus_com_CTD_ANON_39_httpws_plimus_comaddress1', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 40, 1), )

    
    address1 = property(__address1.value, __address1.set, None, None)

    _ElementMap.update({
        __zip.name() : __zip,
        __state.name() : __state,
        __last_name.name() : __last_name,
        __first_name.name() : __first_name,
        __country.name() : __country,
        __city.name() : __city,
        __address2.name() : __address2,
        __address1.name() : __address1
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_40 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 108, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}invoice-contact-info uses Python identifier invoice_contact_info
    __invoice_contact_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'invoice-contact-info'), 'invoice_contact_info', '__httpws_plimus_com_CTD_ANON_40_httpws_plimus_cominvoice_contact_info', True, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 114, 1), )

    
    invoice_contact_info = property(__invoice_contact_info.value, __invoice_contact_info.set, None, None)

    _ElementMap.update({
        __invoice_contact_info.name() : __invoice_contact_info
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_41 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 115, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'zip'), 'zip', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comzip', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 5, 1), )

    
    zip = property(__zip.value, __zip.set, None, None)

    
    # Element {http://ws.plimus.com}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'state'), 'state', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comstate', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 10, 1), )

    
    state = property(__state.value, __state.set, None, None)

    
    # Element {http://ws.plimus.com}last-name uses Python identifier last_name
    __last_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'last-name'), 'last_name', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comlast_name', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 15, 1), )

    
    last_name = property(__last_name.value, __last_name.set, None, None)

    
    # Element {http://ws.plimus.com}first-name uses Python identifier first_name
    __first_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'first-name'), 'first_name', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comfirst_name', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 20, 1), )

    
    first_name = property(__first_name.value, __first_name.set, None, None)

    
    # Element {http://ws.plimus.com}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'country'), 'country', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comcountry', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 25, 1), )

    
    country = property(__country.value, __country.set, None, None)

    
    # Element {http://ws.plimus.com}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comcity', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 30, 1), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://ws.plimus.com}address2 uses Python identifier address2
    __address2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'address2'), 'address2', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comaddress2', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 35, 1), )

    
    address2 = property(__address2.value, __address2.set, None, None)

    
    # Element {http://ws.plimus.com}address1 uses Python identifier address1
    __address1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'address1'), 'address1', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comaddress1', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 40, 1), )

    
    address1 = property(__address1.value, __address1.set, None, None)

    
    # Element {http://ws.plimus.com}vat-code uses Python identifier vat_code
    __vat_code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'vat-code'), 'vat_code', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comvat_code', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 11, 1), )

    
    vat_code = property(__vat_code.value, __vat_code.set, None, None)

    
    # Element {http://ws.plimus.com}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comtitle', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 31, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://ws.plimus.com}default uses Python identifier default
    __default = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'default'), 'default', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comdefault', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 136, 1), )

    
    default = property(__default.value, __default.set, None, None)

    
    # Element {http://ws.plimus.com}phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'phone'), 'phone', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comphone', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 141, 1), )

    
    phone = property(__phone.value, __phone.set, None, None)

    
    # Element {http://ws.plimus.com}fax uses Python identifier fax
    __fax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fax'), 'fax', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comfax', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 177, 1), )

    
    fax = property(__fax.value, __fax.set, None, None)

    
    # Element {http://ws.plimus.com}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'email'), 'email', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comemail', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 182, 1), )

    
    email = property(__email.value, __email.set, None, None)

    
    # Element {http://ws.plimus.com}company-name uses Python identifier company_name
    __company_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'company-name'), 'company_name', '__httpws_plimus_com_CTD_ANON_41_httpws_plimus_comcompany_name', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 187, 1), )

    
    company_name = property(__company_name.value, __company_name.set, None, None)

    _ElementMap.update({
        __zip.name() : __zip,
        __state.name() : __state,
        __last_name.name() : __last_name,
        __first_name.name() : __first_name,
        __country.name() : __country,
        __city.name() : __city,
        __address2.name() : __address2,
        __address1.name() : __address1,
        __vat_code.name() : __vat_code,
        __title.name() : __title,
        __default.name() : __default,
        __phone.name() : __phone,
        __fax.name() : __fax,
        __email.name() : __email,
        __company_name.name() : __company_name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_42 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 147, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}credit-card-info uses Python identifier credit_card_info
    __credit_card_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'credit-card-info'), 'credit_card_info', '__httpws_plimus_com_CTD_ANON_42_httpws_plimus_comcredit_card_info', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 6, 1), )

    
    credit_card_info = property(__credit_card_info.value, __credit_card_info.set, None, None)

    
    # Element {http://ws.plimus.com}ecps-info uses Python identifier ecps_info
    __ecps_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ecps-info'), 'ecps_info', '__httpws_plimus_com_CTD_ANON_42_httpws_plimus_comecps_info', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 9, 1), )

    
    ecps_info = property(__ecps_info.value, __ecps_info.set, None, None)

    
    # Element {http://ws.plimus.com}credit-cards-info uses Python identifier credit_cards_info
    __credit_cards_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'credit-cards-info'), 'credit_cards_info', '__httpws_plimus_com_CTD_ANON_42_httpws_plimus_comcredit_cards_info', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 156, 1), )

    
    credit_cards_info = property(__credit_cards_info.value, __credit_cards_info.set, None, None)

    
    # Element {http://ws.plimus.com}balance uses Python identifier balance
    __balance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'balance'), 'balance', '__httpws_plimus_com_CTD_ANON_42_httpws_plimus_combalance', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 164, 1), )

    
    balance = property(__balance.value, __balance.set, None, None)

    _ElementMap.update({
        __credit_card_info.name() : __credit_card_info,
        __ecps_info.name() : __ecps_info,
        __credit_cards_info.name() : __credit_cards_info,
        __balance.name() : __balance
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_43 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 157, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}credit-card-info uses Python identifier credit_card_info
    __credit_card_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'credit-card-info'), 'credit_card_info', '__httpws_plimus_com_CTD_ANON_43_httpws_plimus_comcredit_card_info', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 6, 1), )

    
    credit_card_info = property(__credit_card_info.value, __credit_card_info.set, None, None)

    _ElementMap.update({
        __credit_card_info.name() : __credit_card_info
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_44 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 165, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'value'), 'value_', '__httpws_plimus_com_CTD_ANON_44_httpws_plimus_comvalue', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 5, 1), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element {http://ws.plimus.com}currency uses Python identifier currency
    __currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'currency'), 'currency', '__httpws_plimus_com_CTD_ANON_44_httpws_plimus_comcurrency', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1), )

    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        __value.name() : __value,
        __currency.name() : __currency
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_45 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}sku-charge-price uses Python identifier sku_charge_price
    __sku_charge_price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sku-charge-price'), 'sku_charge_price', '__httpws_plimus_com_CTD_ANON_45_httpws_plimus_comsku_charge_price', True, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 16, 1), )

    
    sku_charge_price = property(__sku_charge_price.value, __sku_charge_price.set, None, None)

    
    # Element {http://ws.plimus.com}sku-id uses Python identifier sku_id
    __sku_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sku-id'), 'sku_id', '__httpws_plimus_com_CTD_ANON_45_httpws_plimus_comsku_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 25, 1), )

    
    sku_id = property(__sku_id.value, __sku_id.set, None, None)

    
    # Element {http://ws.plimus.com}sku-name uses Python identifier sku_name
    __sku_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sku-name'), 'sku_name', '__httpws_plimus_com_CTD_ANON_45_httpws_plimus_comsku_name', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 30, 1), )

    
    sku_name = property(__sku_name.value, __sku_name.set, None, None)

    _ElementMap.update({
        __sku_charge_price.name() : __sku_charge_price,
        __sku_id.name() : __sku_id,
        __sku_name.name() : __sku_name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_46 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 17, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}charge-type uses Python identifier charge_type
    __charge_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'charge-type'), 'charge_type', '__httpws_plimus_com_CTD_ANON_46_httpws_plimus_comcharge_type', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 66, 1), )

    
    charge_type = property(__charge_type.value, __charge_type.set, None, None)

    
    # Element {http://ws.plimus.com}amount uses Python identifier amount
    __amount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'amount'), 'amount', '__httpws_plimus_com_CTD_ANON_46_httpws_plimus_comamount', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 37, 1), )

    
    amount = property(__amount.value, __amount.set, None, None)

    
    # Element {http://ws.plimus.com}currency uses Python identifier currency
    __currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'currency'), 'currency', '__httpws_plimus_com_CTD_ANON_46_httpws_plimus_comcurrency', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1), )

    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        __charge_type.name() : __charge_type,
        __amount.name() : __amount,
        __currency.name() : __currency
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_47 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}transaction-id uses Python identifier transaction_id
    __transaction_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'transaction-id'), 'transaction_id', '__httpws_plimus_com_CTD_ANON_47_httpws_plimus_comtransaction_id', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 13, 1), )

    
    transaction_id = property(__transaction_id.value, __transaction_id.set, None, None)

    
    # Element {http://ws.plimus.com}payer-authentication-response uses Python identifier payer_authentication_response
    __payer_authentication_response = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'payer-authentication-response'), 'payer_authentication_response', '__httpws_plimus_com_CTD_ANON_47_httpws_plimus_compayer_authentication_response', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 18, 1), )

    
    payer_authentication_response = property(__payer_authentication_response.value, __payer_authentication_response.set, None, None)

    _ElementMap.update({
        __transaction_id.name() : __transaction_id,
        __payer_authentication_response.name() : __payer_authentication_response
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_48 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}ip uses Python identifier ip
    __ip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ip'), 'ip', '__httpws_plimus_com_CTD_ANON_48_httpws_plimus_comip', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 16, 1), )

    
    ip = property(__ip.value, __ip.set, None, None)

    
    # Element {http://ws.plimus.com}remote-host uses Python identifier remote_host
    __remote_host = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'remote-host'), 'remote_host', '__httpws_plimus_com_CTD_ANON_48_httpws_plimus_comremote_host', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 21, 1), )

    
    remote_host = property(__remote_host.value, __remote_host.set, None, None)

    
    # Element {http://ws.plimus.com}user-agent uses Python identifier user_agent
    __user_agent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'user-agent'), 'user_agent', '__httpws_plimus_com_CTD_ANON_48_httpws_plimus_comuser_agent', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 26, 1), )

    
    user_agent = property(__user_agent.value, __user_agent.set, None, None)

    
    # Element {http://ws.plimus.com}accept-language uses Python identifier accept_language
    __accept_language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'accept-language'), 'accept_language', '__httpws_plimus_com_CTD_ANON_48_httpws_plimus_comaccept_language', False, pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 31, 1), )

    
    accept_language = property(__accept_language.value, __accept_language.set, None, None)

    _ElementMap.update({
        __ip.name() : __ip,
        __remote_host.name() : __remote_host,
        __user_agent.name() : __user_agent,
        __accept_language.name() : __accept_language
    })
    _AttributeMap.update({
        
    })



tax_included = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tax-included'), pyxb.binding.datatypes.boolean, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 17, 1))
Namespace.addCategoryObject('elementBinding', tax_included.name().localName(), tax_included)

cdod = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cdod'), pyxb.binding.datatypes.boolean, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 224, 1))
Namespace.addCategoryObject('elementBinding', cdod.name().localName(), cdod)

zip = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zip'), STD_ANON, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 5, 1))
Namespace.addCategoryObject('elementBinding', zip.name().localName(), zip)

state = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'state'), STD_ANON_, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 10, 1))
Namespace.addCategoryObject('elementBinding', state.name().localName(), state)

last_name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'last-name'), STD_ANON_2, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 15, 1))
Namespace.addCategoryObject('elementBinding', last_name.name().localName(), last_name)

first_name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'first-name'), STD_ANON_3, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 20, 1))
Namespace.addCategoryObject('elementBinding', first_name.name().localName(), first_name)

country = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'country'), STD_ANON_4, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', country.name().localName(), country)

city = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), STD_ANON_5, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 30, 1))
Namespace.addCategoryObject('elementBinding', city.name().localName(), city)

address2 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address2'), STD_ANON_6, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 35, 1))
Namespace.addCategoryObject('elementBinding', address2.name().localName(), address2)

address1 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address1'), STD_ANON_7, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 40, 1))
Namespace.addCategoryObject('elementBinding', address1.name().localName(), address1)

credit_card_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit-card-info'), CTD_ANON, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 6, 1))
Namespace.addCategoryObject('elementBinding', credit_card_info.name().localName(), credit_card_info)

billing_contact_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billing-contact-info'), CTD_ANON_, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 14, 1))
Namespace.addCategoryObject('elementBinding', billing_contact_info.name().localName(), billing_contact_info)

credit_card = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit-card'), CTD_ANON_2, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 28, 1))
Namespace.addCategoryObject('elementBinding', credit_card.name().localName(), credit_card)

card_type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card-type'), STD_ANON_8, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 43, 1))
Namespace.addCategoryObject('elementBinding', card_type.name().localName(), card_type)

card_number = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card-number'), STD_ANON_9, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 48, 1))
Namespace.addCategoryObject('elementBinding', card_number.name().localName(), card_number)

card_last_four_digits = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card-last-four-digits'), STD_ANON_10, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 53, 1))
Namespace.addCategoryObject('elementBinding', card_last_four_digits.name().localName(), card_last_four_digits)

security_code = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'security-code'), STD_ANON_11, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 58, 1))
Namespace.addCategoryObject('elementBinding', security_code.name().localName(), security_code)

expiration_month = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expiration-month'), STD_ANON_12, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 63, 1))
Namespace.addCategoryObject('elementBinding', expiration_month.name().localName(), expiration_month)

expiration_year = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expiration-year'), STD_ANON_13, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 68, 1))
Namespace.addCategoryObject('elementBinding', expiration_year.name().localName(), expiration_year)

start_year = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'start-year'), STD_ANON_14, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 73, 1))
Namespace.addCategoryObject('elementBinding', start_year.name().localName(), start_year)

start_month = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'start-month'), STD_ANON_15, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 78, 1))
Namespace.addCategoryObject('elementBinding', start_month.name().localName(), start_month)

issue_number = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'issue-number'), STD_ANON_16, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 83, 1))
Namespace.addCategoryObject('elementBinding', issue_number.name().localName(), issue_number)

ecps_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ecps-info'), CTD_ANON_3, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 9, 1))
Namespace.addCategoryObject('elementBinding', ecps_info.name().localName(), ecps_info)

ecp_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ecp-info'), CTD_ANON_4, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 17, 1))
Namespace.addCategoryObject('elementBinding', ecp_info.name().localName(), ecp_info)

ecp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ecp'), CTD_ANON_5, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 26, 1))
Namespace.addCategoryObject('elementBinding', ecp.name().localName(), ecp)

account_number = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'account-number'), STD_ANON_17, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 38, 1))
Namespace.addCategoryObject('elementBinding', account_number.name().localName(), account_number)

account_type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'account-type'), STD_ANON_18, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 44, 1))
Namespace.addCategoryObject('elementBinding', account_type.name().localName(), account_type)

routing_number = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'routing-number'), STD_ANON_19, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 50, 1))
Namespace.addCategoryObject('elementBinding', routing_number.name().localName(), routing_number)

public_account_number = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'public-account-number'), STD_ANON_20, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 56, 1))
Namespace.addCategoryObject('elementBinding', public_account_number.name().localName(), public_account_number)

public_routing_number = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'public-routing-number'), STD_ANON_21, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 62, 1))
Namespace.addCategoryObject('elementBinding', public_routing_number.name().localName(), public_routing_number)

sku_license = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-license'), CTD_ANON_6, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 6, 1))
Namespace.addCategoryObject('elementBinding', sku_license.name().localName(), sku_license)

sku_download_link = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-download-link'), CTD_ANON_7, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 15, 1))
Namespace.addCategoryObject('elementBinding', sku_download_link.name().localName(), sku_download_link)

license_keys = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'license-keys'), CTD_ANON_8, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', license_keys.name().localName(), license_keys)

download_links = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'download-links'), CTD_ANON_9, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 31, 1))
Namespace.addCategoryObject('elementBinding', download_links.name().localName(), download_links)

fulfillment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fulfillment'), CTD_ANON_10, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 38, 1))
Namespace.addCategoryObject('elementBinding', fulfillment.name().localName(), fulfillment)

license_key = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'license-key'), STD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 46, 1))
Namespace.addCategoryObject('elementBinding', license_key.name().localName(), license_key)

download_link = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'download-link'), STD_ANON_23, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 51, 1))
Namespace.addCategoryObject('elementBinding', download_link.name().localName(), download_link)

store_id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'store-id'), STD_ANON_24, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', store_id.name().localName(), store_id)

quantity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'quantity'), STD_ANON_25, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 12, 1))
Namespace.addCategoryObject('elementBinding', quantity.name().localName(), quantity)

item_price = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'item-price'), CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 18, 1))
Namespace.addCategoryObject('elementBinding', item_price.name().localName(), item_price)

unit_price = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unit-price'), CTD_ANON_12, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 34, 1))
Namespace.addCategoryObject('elementBinding', unit_price.name().localName(), unit_price)

total_price = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'total-price'), CTD_ANON_13, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 41, 1))
Namespace.addCategoryObject('elementBinding', total_price.name().localName(), total_price)

total_price_with_tax = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'total-price-with-tax'), CTD_ANON_14, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 48, 1))
Namespace.addCategoryObject('elementBinding', total_price_with_tax.name().localName(), total_price_with_tax)

charge_price = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'charge-price'), CTD_ANON_15, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 55, 1))
Namespace.addCategoryObject('elementBinding', charge_price.name().localName(), charge_price)

charge_type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'charge-type'), STD_ANON_26, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 66, 1))
Namespace.addCategoryObject('elementBinding', charge_type.name().localName(), charge_type)

param_value = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param-value'), STD_ANON_27, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 13, 1))
Namespace.addCategoryObject('elementBinding', param_value.name().localName(), param_value)

total_cart_cost = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'total-cart-cost'), STD_ANON_28, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 18, 1))
Namespace.addCategoryObject('elementBinding', total_cart_cost.name().localName(), total_cart_cost)

tax = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tax'), STD_ANON_29, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 23, 1))
Namespace.addCategoryObject('elementBinding', tax.name().localName(), tax)

tax_recurring = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tax-recurring'), STD_ANON_30, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 28, 1))
Namespace.addCategoryObject('elementBinding', tax_recurring.name().localName(), tax_recurring)

tax_rate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tax-rate'), STD_ANON_31, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 33, 1))
Namespace.addCategoryObject('elementBinding', tax_rate.name().localName(), tax_rate)

soft_descriptor = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'soft-descriptor'), STD_ANON_32, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 38, 1))
Namespace.addCategoryObject('elementBinding', soft_descriptor.name().localName(), soft_descriptor)

sku_parameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-parameter'), CTD_ANON_16, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 43, 1))
Namespace.addCategoryObject('elementBinding', sku_parameter.name().localName(), sku_parameter)

shopper_id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shopper-id'), STD_ANON_33, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 51, 1))
Namespace.addCategoryObject('elementBinding', shopper_id.name().localName(), shopper_id)

ordering_shopper = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ordering-shopper'), CTD_ANON_17, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 56, 1))
Namespace.addCategoryObject('elementBinding', ordering_shopper.name().localName(), ordering_shopper)

post_sale_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'post-sale-info'), CTD_ANON_18, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 70, 1))
Namespace.addCategoryObject('elementBinding', post_sale_info.name().localName(), post_sale_info)

invoices = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoices'), CTD_ANON_19, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 80, 1))
Namespace.addCategoryObject('elementBinding', invoices.name().localName(), invoices)

invoice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice'), CTD_ANON_20, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 87, 1))
Namespace.addCategoryObject('elementBinding', invoice.name().localName(), invoice)

financial_transactions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'financial-transactions'), CTD_ANON_21, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 96, 1))
Namespace.addCategoryObject('elementBinding', financial_transactions.name().localName(), financial_transactions)

financial_transaction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'financial-transaction'), CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 103, 1))
Namespace.addCategoryObject('elementBinding', financial_transaction.name().localName(), financial_transaction)

skus = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'skus'), CTD_ANON_23, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 124, 1))
Namespace.addCategoryObject('elementBinding', skus.name().localName(), skus)

status = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'status'), STD_ANON_34, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 131, 1))
Namespace.addCategoryObject('elementBinding', status.name().localName(), status)

date_due = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'date-due'), STD_ANON_35, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 136, 1))
Namespace.addCategoryObject('elementBinding', date_due.name().localName(), date_due)

date_created = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'date-created'), STD_ANON_36, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 141, 1))
Namespace.addCategoryObject('elementBinding', date_created.name().localName(), date_created)

payment_method = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payment-method'), STD_ANON_37, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 146, 1))
Namespace.addCategoryObject('elementBinding', payment_method.name().localName(), payment_method)

invoice_status = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice-status'), STD_ANON_38, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 151, 1))
Namespace.addCategoryObject('elementBinding', invoice_status.name().localName(), invoice_status)

order = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order'), CTD_ANON_24, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 156, 1))
Namespace.addCategoryObject('elementBinding', order.name().localName(), order)

param_name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param-name'), STD_ANON_39, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 171, 1))
Namespace.addCategoryObject('elementBinding', param_name.name().localName(), param_name)

item_sub_total = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'item-sub-total'), STD_ANON_40, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 176, 1))
Namespace.addCategoryObject('elementBinding', item_sub_total.name().localName(), item_sub_total)

invoice_id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice-id'), STD_ANON_41, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 181, 1))
Namespace.addCategoryObject('elementBinding', invoice_id.name().localName(), invoice_id)

order_id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order-id'), STD_ANON_42, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 186, 1))
Namespace.addCategoryObject('elementBinding', order_id.name().localName(), order_id)

affiliate_id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'affiliate-id'), STD_ANON_43, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 191, 1))
Namespace.addCategoryObject('elementBinding', affiliate_id.name().localName(), affiliate_id)

expected_total_price = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expected-total-price'), CTD_ANON_25, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 196, 1))
Namespace.addCategoryObject('elementBinding', expected_total_price.name().localName(), expected_total_price)

transaction_payment_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transaction-payment-info'), CTD_ANON_26, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 204, 1))
Namespace.addCategoryObject('elementBinding', transaction_payment_info.name().localName(), transaction_payment_info)

coupons = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'coupons'), CTD_ANON_27, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 211, 1))
Namespace.addCategoryObject('elementBinding', coupons.name().localName(), coupons)

coupon = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'coupon'), STD_ANON_44, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 219, 1))
Namespace.addCategoryObject('elementBinding', coupon.name().localName(), coupon)

edw_duration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'edw-duration'), STD_ANON_45, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 225, 1))
Namespace.addCategoryObject('elementBinding', edw_duration.name().localName(), edw_duration)

charged_currency = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'charged-currency'), STD_ANON_46, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 233, 1))
Namespace.addCategoryObject('elementBinding', charged_currency.name().localName(), charged_currency)

cart_item = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cart-item'), CTD_ANON_28, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 238, 1))
Namespace.addCategoryObject('elementBinding', cart_item.name().localName(), cart_item)

cart = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cart'), CTD_ANON_29, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 249, 1))
Namespace.addCategoryObject('elementBinding', cart.name().localName(), cart)

coupons_total = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'coupons-total'), STD_ANON_47, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 263, 1))
Namespace.addCategoryObject('elementBinding', coupons_total.name().localName(), coupons_total)

url = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'url'), STD_ANON_48, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 268, 1))
Namespace.addCategoryObject('elementBinding', url.name().localName(), url)

target_balance = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'target-balance'), STD_ANON_49, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 273, 2))
Namespace.addCategoryObject('elementBinding', target_balance.name().localName(), target_balance)

seller_shopper_id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'seller-shopper-id'), STD_ANON_50, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ordering-shopper.xsd', 5, 1))
Namespace.addCategoryObject('elementBinding', seller_shopper_id.name().localName(), seller_shopper_id)

paypal_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal-info'), CTD_ANON_30, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 6, 1))
Namespace.addCategoryObject('elementBinding', paypal_info.name().localName(), paypal_info)

paypal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal'), CTD_ANON_31, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 13, 1))
Namespace.addCategoryObject('elementBinding', paypal.name().localName(), paypal)

paypal_transaction_data = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal-transaction-data'), CTD_ANON_32, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 17, 1))
Namespace.addCategoryObject('elementBinding', paypal_transaction_data.name().localName(), paypal_transaction_data)

pp_transaction_id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pp-transaction-id'), STD_ANON_51, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', pp_transaction_id.name().localName(), pp_transaction_id)

paypal_subscription = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal-subscription'), CTD_ANON_33, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 30, 2))
Namespace.addCategoryObject('elementBinding', paypal_subscription.name().localName(), paypal_subscription)

pp_subscription_id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pp-subscription-id'), STD_ANON_52, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 38, 1))
Namespace.addCategoryObject('elementBinding', pp_subscription_id.name().localName(), pp_subscription_id)

pp_original_transaction_id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pp-original-transaction-id'), STD_ANON_53, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 43, 2))
Namespace.addCategoryObject('elementBinding', pp_original_transaction_id.name().localName(), pp_original_transaction_id)

value = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'value'), STD_ANON_54, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 5, 1))
Namespace.addCategoryObject('elementBinding', value.name().localName(), value)

symbol = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'symbol'), STD_ANON_55, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 10, 1))
Namespace.addCategoryObject('elementBinding', symbol.name().localName(), symbol)

price = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'price'), CTD_ANON_34, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 15, 1))
Namespace.addCategoryObject('elementBinding', price.name().localName(), price)

iso = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iso'), STD_ANON_56, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', iso.name().localName(), iso)

formatted_price = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'formatted-price'), CTD_ANON_35, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 29, 1))
Namespace.addCategoryObject('elementBinding', formatted_price.name().localName(), formatted_price)

amount = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), STD_ANON_57, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 37, 1))
Namespace.addCategoryObject('elementBinding', amount.name().localName(), amount)

currency = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'currency'), STD_ANON_58, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1))
Namespace.addCategoryObject('elementBinding', currency.name().localName(), currency)

vat_code = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'vat-code'), STD_ANON_59, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 11, 1))
Namespace.addCategoryObject('elementBinding', vat_code.name().localName(), vat_code)

shopper_currency = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shopper-currency'), STD_ANON_60, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 16, 1))
Namespace.addCategoryObject('elementBinding', shopper_currency.name().localName(), shopper_currency)

locale = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'locale'), STD_ANON_61, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 21, 1))
Namespace.addCategoryObject('elementBinding', locale.name().localName(), locale)

permitted_future_charges = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'permitted-future-charges'), STD_ANON_62, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 26, 1))
Namespace.addCategoryObject('elementBinding', permitted_future_charges.name().localName(), permitted_future_charges)

title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), STD_ANON_63, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 31, 1))
Namespace.addCategoryObject('elementBinding', title.name().localName(), title)

username = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'username'), STD_ANON_64, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 36, 1))
Namespace.addCategoryObject('elementBinding', username.name().localName(), username)

password = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'password'), STD_ANON_65, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 41, 1))
Namespace.addCategoryObject('elementBinding', password.name().localName(), password)

shopper_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shopper-info'), CTD_ANON_36, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 46, 1))
Namespace.addCategoryObject('elementBinding', shopper_info.name().localName(), shopper_info)

shopper_contact_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shopper-contact-info'), CTD_ANON_37, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 64, 1))
Namespace.addCategoryObject('elementBinding', shopper_contact_info.name().localName(), shopper_contact_info)

shopper = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shopper'), CTD_ANON_38, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 83, 1))
Namespace.addCategoryObject('elementBinding', shopper.name().localName(), shopper)

shipping_contact_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shipping-contact-info'), CTD_ANON_39, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 93, 1))
Namespace.addCategoryObject('elementBinding', shipping_contact_info.name().localName(), shipping_contact_info)

invoice_contacts_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice-contacts-info'), CTD_ANON_40, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 107, 1))
Namespace.addCategoryObject('elementBinding', invoice_contacts_info.name().localName(), invoice_contacts_info)

invoice_contact_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice-contact-info'), CTD_ANON_41, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 114, 1))
Namespace.addCategoryObject('elementBinding', invoice_contact_info.name().localName(), invoice_contact_info)

default = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'default'), STD_ANON_66, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 136, 1))
Namespace.addCategoryObject('elementBinding', default.name().localName(), default)

phone = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phone'), STD_ANON_67, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 141, 1))
Namespace.addCategoryObject('elementBinding', phone.name().localName(), phone)

payment_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payment-info'), CTD_ANON_42, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 146, 1))
Namespace.addCategoryObject('elementBinding', payment_info.name().localName(), payment_info)

credit_cards_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit-cards-info'), CTD_ANON_43, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 156, 1))
Namespace.addCategoryObject('elementBinding', credit_cards_info.name().localName(), credit_cards_info)

balance = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'balance'), CTD_ANON_44, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 164, 1))
Namespace.addCategoryObject('elementBinding', balance.name().localName(), balance)

id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'id'), STD_ANON_68, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 172, 1))
Namespace.addCategoryObject('elementBinding', id.name().localName(), id)

fax = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fax'), STD_ANON_69, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 177, 1))
Namespace.addCategoryObject('elementBinding', fax.name().localName(), fax)

email = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'email'), STD_ANON_70, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 182, 1))
Namespace.addCategoryObject('elementBinding', email.name().localName(), email)

company_name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'company-name'), STD_ANON_71, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 187, 1))
Namespace.addCategoryObject('elementBinding', company_name.name().localName(), company_name)

sku = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku'), CTD_ANON_45, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 6, 1))
Namespace.addCategoryObject('elementBinding', sku.name().localName(), sku)

sku_charge_price = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-charge-price'), CTD_ANON_46, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 16, 1))
Namespace.addCategoryObject('elementBinding', sku_charge_price.name().localName(), sku_charge_price)

sku_id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-id'), STD_ANON_72, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', sku_id.name().localName(), sku_id)

sku_name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-name'), STD_ANON_73, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 30, 1))
Namespace.addCategoryObject('elementBinding', sku_name.name().localName(), sku_name)

contract_name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contract-name'), STD_ANON_74, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 35, 1))
Namespace.addCategoryObject('elementBinding', contract_name.name().localName(), contract_name)

sku_status = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-status'), STD_ANON_75, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 40, 1))
Namespace.addCategoryObject('elementBinding', sku_status.name().localName(), sku_status)

three_d_authenticated_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'three-d-authenticated-info'), CTD_ANON_47, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 5, 1))
Namespace.addCategoryObject('elementBinding', three_d_authenticated_info.name().localName(), three_d_authenticated_info)

transaction_id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transaction-id'), STD_ANON_76, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 13, 1))
Namespace.addCategoryObject('elementBinding', transaction_id.name().localName(), transaction_id)

payer_authentication_response = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payer-authentication-response'), STD_ANON_77, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 18, 1))
Namespace.addCategoryObject('elementBinding', payer_authentication_response.name().localName(), payer_authentication_response)

web_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'web-info'), CTD_ANON_48, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 5, 1))
Namespace.addCategoryObject('elementBinding', web_info.name().localName(), web_info)

ip = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ip'), STD_ANON_78, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 16, 1))
Namespace.addCategoryObject('elementBinding', ip.name().localName(), ip)

remote_host = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'remote-host'), STD_ANON_79, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 21, 1))
Namespace.addCategoryObject('elementBinding', remote_host.name().localName(), remote_host)

user_agent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'user-agent'), STD_ANON_80, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 26, 1))
Namespace.addCategoryObject('elementBinding', user_agent.name().localName(), user_agent)

accept_language = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accept-language'), STD_ANON_81, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 31, 1))
Namespace.addCategoryObject('elementBinding', accept_language.name().localName(), accept_language)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billing-contact-info'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 14, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit-card'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 28, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 9, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billing-contact-info')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 9, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'credit-card')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 10, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zip'), STD_ANON, scope=CTD_ANON_, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 5, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'state'), STD_ANON_, scope=CTD_ANON_, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 10, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'last-name'), STD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 15, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'first-name'), STD_ANON_3, scope=CTD_ANON_, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 20, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'country'), STD_ANON_4, scope=CTD_ANON_, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 25, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), STD_ANON_5, scope=CTD_ANON_, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 30, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address2'), STD_ANON_6, scope=CTD_ANON_, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 35, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address1'), STD_ANON_7, scope=CTD_ANON_, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 40, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 17, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 18, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 19, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 20, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 21, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 22, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 23, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 24, 4))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'first-name')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 17, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'last-name')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 18, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address1')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 19, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address2')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 20, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 21, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'state')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 22, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zip')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 23, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'country')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 24, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card-type'), STD_ANON_8, scope=CTD_ANON_2, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 43, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card-number'), STD_ANON_9, scope=CTD_ANON_2, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 48, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card-last-four-digits'), STD_ANON_10, scope=CTD_ANON_2, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 53, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'security-code'), STD_ANON_11, scope=CTD_ANON_2, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 58, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expiration-month'), STD_ANON_12, scope=CTD_ANON_2, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 63, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expiration-year'), STD_ANON_13, scope=CTD_ANON_2, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 68, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'start-year'), STD_ANON_14, scope=CTD_ANON_2, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 73, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'start-month'), STD_ANON_15, scope=CTD_ANON_2, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 78, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'issue-number'), STD_ANON_16, scope=CTD_ANON_2, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 83, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 31, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 32, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 34, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 35, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 36, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 37, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 38, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 39, 4))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card-number')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 31, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card-last-four-digits')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 32, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card-type')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 33, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expiration-month')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 34, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expiration-year')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 35, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'security-code')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 36, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'start-month')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 37, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'start-year')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 38, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'issue-number')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 39, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ecp-info'), CTD_ANON_4, scope=CTD_ANON_3, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 17, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 12, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ecp-info')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 12, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billing-contact-info'), CTD_ANON_, scope=CTD_ANON_4, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 14, 1)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ecp'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 26, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billing-contact-info')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 20, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ecp')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 21, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'account-number'), STD_ANON_17, scope=CTD_ANON_5, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 38, 1)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'account-type'), STD_ANON_18, scope=CTD_ANON_5, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 44, 1)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'routing-number'), STD_ANON_19, scope=CTD_ANON_5, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 50, 1)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'public-account-number'), STD_ANON_20, scope=CTD_ANON_5, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 56, 1)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'public-routing-number'), STD_ANON_21, scope=CTD_ANON_5, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 62, 1)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'account-number')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 29, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'routing-number')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 30, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'account-type')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 31, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'public-account-number')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 32, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'public-routing-number')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 33, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'license-key'), STD_ANON_22, scope=CTD_ANON_6, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 46, 1)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-id'), STD_ANON_72, scope=CTD_ANON_6, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 25, 1)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-name'), STD_ANON_73, scope=CTD_ANON_6, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 30, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sku-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 9, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sku-name')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 10, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'license-key')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 11, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'download-link'), STD_ANON_23, scope=CTD_ANON_7, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 51, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-id'), STD_ANON_72, scope=CTD_ANON_7, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 25, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-name'), STD_ANON_73, scope=CTD_ANON_7, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 30, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sku-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 18, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sku-name')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 19, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'download-link')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 20, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-license'), CTD_ANON_6, scope=CTD_ANON_8, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 6, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 27, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sku-license')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 27, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-download-link'), CTD_ANON_7, scope=CTD_ANON_9, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 15, 1)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 34, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sku-download-link')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 34, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'license-keys'), CTD_ANON_8, scope=CTD_ANON_10, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 24, 1)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'download-links'), CTD_ANON_9, scope=CTD_ANON_10, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 31, 1)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 41, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 42, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'license-keys')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 41, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'download-links')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 42, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_10()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'state'), STD_ANON_, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 10, 1)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'country'), STD_ANON_4, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 25, 1)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'store-id'), STD_ANON_24, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 7, 1)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'quantity'), STD_ANON_25, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 12, 1)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unit-price'), CTD_ANON_12, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 34, 1)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'total-price'), CTD_ANON_13, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 41, 1)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'total-price-with-tax'), CTD_ANON_14, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 48, 1)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tax'), STD_ANON_29, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 23, 1)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tax-recurring'), STD_ANON_30, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 28, 1)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tax-rate'), STD_ANON_31, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 33, 1)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 27, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'store-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 21, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'quantity')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 22, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'unit-price')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 23, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'total-price')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 24, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'total-price-with-tax')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 25, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tax')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 26, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tax-recurring')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 27, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tax-rate')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 28, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'country')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 29, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'state')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 30, 4))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_11()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'charge-price'), CTD_ANON_15, scope=CTD_ANON_12, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 55, 1)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 37, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'charge-price')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 37, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_12()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'charge-price'), CTD_ANON_15, scope=CTD_ANON_13, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 55, 1)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 44, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'charge-price')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 44, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_13()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'charge-price'), CTD_ANON_15, scope=CTD_ANON_14, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 55, 1)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 51, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'charge-price')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 51, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_14()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tax-included'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_15, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 17, 1)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'charge-type'), STD_ANON_26, scope=CTD_ANON_15, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 66, 1)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'value'), STD_ANON_54, scope=CTD_ANON_15, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 5, 1)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'formatted-price'), CTD_ANON_35, scope=CTD_ANON_15, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 29, 1)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'currency'), STD_ANON_58, scope=CTD_ANON_15, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'charge-type')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 58, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'value')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 59, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'currency')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 60, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'formatted-price')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 61, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tax-included')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 62, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_15()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param-value'), STD_ANON_27, scope=CTD_ANON_16, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 13, 1)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'param-name'), STD_ANON_39, scope=CTD_ANON_16, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 171, 1)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'param-name')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 46, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'param-value')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 47, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_16()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit-card'), CTD_ANON_2, scope=CTD_ANON_17, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 28, 1)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ecp'), CTD_ANON_5, scope=CTD_ANON_17, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 26, 1)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shopper-id'), STD_ANON_33, scope=CTD_ANON_17, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 51, 1)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'seller-shopper-id'), STD_ANON_50, scope=CTD_ANON_17, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ordering-shopper.xsd', 5, 1)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal'), CTD_ANON_31, scope=CTD_ANON_17, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 13, 1)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice-contact-info'), CTD_ANON_41, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 114, 1)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'three-d-authenticated-info'), CTD_ANON_47, scope=CTD_ANON_17, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 5, 1)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'web-info'), CTD_ANON_48, scope=CTD_ANON_17, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 5, 1)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 59, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 60, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 61, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 62, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 63, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 64, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 66, 4))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shopper-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 59, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'seller-shopper-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 60, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'credit-card')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 61, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ecp')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 62, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invoice-contact-info')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 63, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypal')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 64, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'web-info')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 65, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'three-d-authenticated-info')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 66, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_17()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'soft-descriptor'), STD_ANON_32, scope=CTD_ANON_18, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 38, 1)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoices'), CTD_ANON_19, scope=CTD_ANON_18, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 80, 1)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice-status'), STD_ANON_38, scope=CTD_ANON_18, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 151, 1)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice-id'), STD_ANON_41, scope=CTD_ANON_18, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 181, 1)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 73, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 75, 4))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invoice-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 73, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invoice-status')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 74, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'soft-descriptor')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 75, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invoices')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 76, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_18()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice'), CTD_ANON_20, scope=CTD_ANON_19, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 87, 1)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invoice')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 83, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_19()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'financial-transactions'), CTD_ANON_21, scope=CTD_ANON_20, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 96, 1)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice-id'), STD_ANON_41, scope=CTD_ANON_20, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 181, 1)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'url'), STD_ANON_48, scope=CTD_ANON_20, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 268, 1)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invoice-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 90, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'url')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 91, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'financial-transactions')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 92, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_20()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'financial-transaction'), CTD_ANON_22, scope=CTD_ANON_21, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 103, 1)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'financial-transaction')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 99, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_21()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit-card'), CTD_ANON_2, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 28, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ecp'), CTD_ANON_5, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 26, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tax'), STD_ANON_29, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 23, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tax-rate'), STD_ANON_31, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 33, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'soft-descriptor'), STD_ANON_32, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 38, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'skus'), CTD_ANON_23, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 124, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'status'), STD_ANON_34, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 131, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'date-due'), STD_ANON_35, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 136, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'date-created'), STD_ANON_36, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 141, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payment-method'), STD_ANON_37, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 146, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'target-balance'), STD_ANON_49, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 273, 2)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal-transaction-data'), CTD_ANON_32, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 17, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), STD_ANON_57, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 37, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'currency'), STD_ANON_58, scope=CTD_ANON_22, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice-contact-info'), CTD_ANON_41, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 114, 1)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 117, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'status')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 106, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'date-due')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 107, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'date-created')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 108, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 109, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tax')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 110, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tax-rate')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 111, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'currency')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 112, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'soft-descriptor')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 113, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'payment-method')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 114, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'target-balance')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 115, 4))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'credit-card')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 116, 4))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypal-transaction-data')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 117, 4))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ecp')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 118, 4))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invoice-contact-info')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 119, 4))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'skus')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 120, 4))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_22()




CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku'), CTD_ANON_45, scope=CTD_ANON_23, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 6, 1)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sku')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 127, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_23()




CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fulfillment'), CTD_ANON_10, scope=CTD_ANON_24, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/fulfillment.xsd', 38, 1)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'soft-descriptor'), STD_ANON_32, scope=CTD_ANON_24, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 38, 1)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ordering-shopper'), CTD_ANON_17, scope=CTD_ANON_24, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 56, 1)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'post-sale-info'), CTD_ANON_18, scope=CTD_ANON_24, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 70, 1)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order-id'), STD_ANON_42, scope=CTD_ANON_24, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 186, 1)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'affiliate-id'), STD_ANON_43, scope=CTD_ANON_24, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 191, 1)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expected-total-price'), CTD_ANON_25, scope=CTD_ANON_24, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 196, 1)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transaction-payment-info'), CTD_ANON_26, scope=CTD_ANON_24, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 204, 1)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cart'), CTD_ANON_29, scope=CTD_ANON_24, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 249, 1)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 160, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 162, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 164, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 165, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 166, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 167, 4))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'order-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 159, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'soft-descriptor')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 160, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ordering-shopper')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 161, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transaction-payment-info')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 162, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cart')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 163, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expected-total-price')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 164, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'affiliate-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 165, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'post-sale-info')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 166, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fulfillment')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 167, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_24()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), STD_ANON_57, scope=CTD_ANON_25, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 37, 1)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'currency'), STD_ANON_58, scope=CTD_ANON_25, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 199, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'currency')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 200, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_25()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypal-info'), CTD_ANON_30, scope=CTD_ANON_26, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 6, 1)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 207, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypal-info')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 207, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_26()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'coupon'), STD_ANON_44, scope=CTD_ANON_27, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 219, 1)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'coupons-total'), STD_ANON_47, scope=CTD_ANON_27, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 263, 1)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 215, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'coupon')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 214, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'coupons-total')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 215, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_27()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'quantity'), STD_ANON_25, scope=CTD_ANON_28, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 12, 1)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-parameter'), CTD_ANON_16, scope=CTD_ANON_28, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 43, 1)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'item-sub-total'), STD_ANON_40, scope=CTD_ANON_28, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 176, 1)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'url'), STD_ANON_48, scope=CTD_ANON_28, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 268, 1)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku'), CTD_ANON_45, scope=CTD_ANON_28, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 6, 1)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 243, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 244, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 245, 4))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sku')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 241, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'quantity')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 242, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sku-parameter')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 243, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'url')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 244, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'item-sub-total')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 245, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_28()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'total-cart-cost'), STD_ANON_28, scope=CTD_ANON_29, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 18, 1)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tax'), STD_ANON_29, scope=CTD_ANON_29, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 23, 1)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tax-rate'), STD_ANON_31, scope=CTD_ANON_29, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 33, 1)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'coupons'), CTD_ANON_27, scope=CTD_ANON_29, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 211, 1)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cdod'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_29, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 224, 1)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'edw-duration'), STD_ANON_45, scope=CTD_ANON_29, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 225, 1)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'charged-currency'), STD_ANON_46, scope=CTD_ANON_29, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 233, 1)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cart-item'), CTD_ANON_28, scope=CTD_ANON_29, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 238, 1)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 252, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 254, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 255, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 256, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 257, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 258, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 259, 4))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'charged-currency')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 252, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cart-item')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 253, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'coupons')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 254, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'edw-duration')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 255, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cdod')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 256, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tax')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 257, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tax-rate')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 258, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'total-cart-cost')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 259, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_29()




CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'url'), STD_ANON_48, scope=CTD_ANON_30, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/order.xsd', 268, 1)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'url')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 9, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_30()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pp-transaction-id'), STD_ANON_51, scope=CTD_ANON_32, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 25, 1)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pp-subscription-id'), STD_ANON_52, scope=CTD_ANON_32, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 38, 1)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pp-transaction-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 20, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pp-subscription-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 21, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_32._Automaton = _BuildAutomaton_31()




CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pp-subscription-id'), STD_ANON_52, scope=CTD_ANON_33, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 38, 1)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pp-original-transaction-id'), STD_ANON_53, scope=CTD_ANON_33, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 43, 2)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pp-subscription-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 33, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pp-original-transaction-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/paypal-info.xsd', 34, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_33._Automaton = _BuildAutomaton_32()




CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'value'), STD_ANON_54, scope=CTD_ANON_34, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 5, 1)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'formatted-price'), CTD_ANON_35, scope=CTD_ANON_34, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 29, 1)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'currency'), STD_ANON_58, scope=CTD_ANON_34, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 20, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'value')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 18, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'currency')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 19, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'formatted-price')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 20, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_34._Automaton = _BuildAutomaton_33()




CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'symbol'), STD_ANON_55, scope=CTD_ANON_35, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 10, 1)))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iso'), STD_ANON_56, scope=CTD_ANON_35, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 24, 1)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iso')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 32, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'symbol')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 33, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_35._Automaton = _BuildAutomaton_34()




CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'store-id'), STD_ANON_24, scope=CTD_ANON_36, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 7, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'seller-shopper-id'), STD_ANON_50, scope=CTD_ANON_36, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ordering-shopper.xsd', 5, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'vat-code'), STD_ANON_59, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 11, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shopper-currency'), STD_ANON_60, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 16, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'locale'), STD_ANON_61, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 21, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'permitted-future-charges'), STD_ANON_62, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 26, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'username'), STD_ANON_64, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 36, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'password'), STD_ANON_65, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 41, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shopper-contact-info'), CTD_ANON_37, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 64, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shipping-contact-info'), CTD_ANON_39, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 93, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice-contacts-info'), CTD_ANON_40, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 107, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payment-info'), CTD_ANON_42, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 146, 1)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 49, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 50, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 51, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 52, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 53, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 54, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 55, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 56, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 57, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 58, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 59, 4))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 60, 4))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'seller-shopper-id')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 49, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'username')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 50, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'password')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 51, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shopper-contact-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 52, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shipping-contact-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 53, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invoice-contacts-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 54, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'payment-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 55, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'store-id')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 56, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'vat-code')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 57, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shopper-currency')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 58, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'locale')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 59, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'permitted-future-charges')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 60, 4))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_36._Automaton = _BuildAutomaton_35()




CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zip'), STD_ANON, scope=CTD_ANON_37, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 5, 1)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'state'), STD_ANON_, scope=CTD_ANON_37, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 10, 1)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'last-name'), STD_ANON_2, scope=CTD_ANON_37, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 15, 1)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'first-name'), STD_ANON_3, scope=CTD_ANON_37, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 20, 1)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'country'), STD_ANON_4, scope=CTD_ANON_37, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 25, 1)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), STD_ANON_5, scope=CTD_ANON_37, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 30, 1)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address2'), STD_ANON_6, scope=CTD_ANON_37, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 35, 1)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address1'), STD_ANON_7, scope=CTD_ANON_37, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 40, 1)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), STD_ANON_63, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 31, 1)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phone'), STD_ANON_67, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 141, 1)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fax'), STD_ANON_69, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 177, 1)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'email'), STD_ANON_70, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 182, 1)))

CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'company-name'), STD_ANON_71, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 187, 1)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 67, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 68, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 69, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 70, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 71, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 72, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 73, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 74, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 75, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 76, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 77, 4))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 78, 4))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 79, 4))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 67, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'first-name')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 68, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'last-name')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 69, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'email')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 70, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'company-name')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 71, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address1')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 72, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address2')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 73, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 74, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'state')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 75, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zip')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 76, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'country')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 77, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'phone')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 78, 4))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fax')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 79, 4))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_37._Automaton = _BuildAutomaton_36()




CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shopper-info'), CTD_ANON_36, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 46, 1)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'three-d-authenticated-info'), CTD_ANON_47, scope=CTD_ANON_38, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 5, 1)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'web-info'), CTD_ANON_48, scope=CTD_ANON_38, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 5, 1)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 87, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 88, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shopper-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 86, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'web-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 87, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'three-d-authenticated-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 88, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_37()




CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zip'), STD_ANON, scope=CTD_ANON_39, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 5, 1)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'state'), STD_ANON_, scope=CTD_ANON_39, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 10, 1)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'last-name'), STD_ANON_2, scope=CTD_ANON_39, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 15, 1)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'first-name'), STD_ANON_3, scope=CTD_ANON_39, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 20, 1)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'country'), STD_ANON_4, scope=CTD_ANON_39, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 25, 1)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), STD_ANON_5, scope=CTD_ANON_39, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 30, 1)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address2'), STD_ANON_6, scope=CTD_ANON_39, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 35, 1)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address1'), STD_ANON_7, scope=CTD_ANON_39, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 40, 1)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 96, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 97, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 98, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 99, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 100, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 101, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 102, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 103, 4))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'first-name')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 96, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'last-name')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 97, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address1')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 98, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address2')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 99, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 100, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'state')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 101, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zip')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 102, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'country')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 103, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_39._Automaton = _BuildAutomaton_38()




CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invoice-contact-info'), CTD_ANON_41, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 114, 1)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 110, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invoice-contact-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 110, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_40._Automaton = _BuildAutomaton_39()




CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zip'), STD_ANON, scope=CTD_ANON_41, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 5, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'state'), STD_ANON_, scope=CTD_ANON_41, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 10, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'last-name'), STD_ANON_2, scope=CTD_ANON_41, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 15, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'first-name'), STD_ANON_3, scope=CTD_ANON_41, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 20, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'country'), STD_ANON_4, scope=CTD_ANON_41, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 25, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), STD_ANON_5, scope=CTD_ANON_41, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 30, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address2'), STD_ANON_6, scope=CTD_ANON_41, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 35, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address1'), STD_ANON_7, scope=CTD_ANON_41, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/contract-info.xsd', 40, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'vat-code'), STD_ANON_59, scope=CTD_ANON_41, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 11, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), STD_ANON_63, scope=CTD_ANON_41, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 31, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'default'), STD_ANON_66, scope=CTD_ANON_41, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 136, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phone'), STD_ANON_67, scope=CTD_ANON_41, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 141, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fax'), STD_ANON_69, scope=CTD_ANON_41, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 177, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'email'), STD_ANON_70, scope=CTD_ANON_41, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 182, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'company-name'), STD_ANON_71, scope=CTD_ANON_41, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 187, 1)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 117, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 118, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 119, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 120, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 121, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 122, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 123, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 124, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 125, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 126, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 127, 4))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 128, 4))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 129, 4))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 130, 4))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 131, 4))
    counters.add(cc_14)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'default')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 117, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'vat-code')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 118, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 119, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'first-name')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 120, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'last-name')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 121, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'email')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 122, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'company-name')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 123, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address1')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 124, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address2')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 125, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 126, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'state')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 127, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zip')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 128, 4))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'country')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 129, 4))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'phone')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 130, 4))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fax')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 131, 4))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_41._Automaton = _BuildAutomaton_40()




CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit-card-info'), CTD_ANON, scope=CTD_ANON_42, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 6, 1)))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ecps-info'), CTD_ANON_3, scope=CTD_ANON_42, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/ecp-info.xsd', 9, 1)))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit-cards-info'), CTD_ANON_43, scope=CTD_ANON_42, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 156, 1)))

CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'balance'), CTD_ANON_44, scope=CTD_ANON_42, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 164, 1)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 149, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 150, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 151, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 152, 4))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'credit-card-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 149, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'credit-cards-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 150, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ecps-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 151, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'balance')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 152, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_42._Automaton = _BuildAutomaton_41()




CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit-card-info'), CTD_ANON, scope=CTD_ANON_43, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 6, 1)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 159, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'credit-card-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 159, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_43._Automaton = _BuildAutomaton_42()




CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'value'), STD_ANON_54, scope=CTD_ANON_44, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 5, 1)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'currency'), STD_ANON_58, scope=CTD_ANON_44, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'currency')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 167, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'value')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/shopper.xsd', 168, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_44._Automaton = _BuildAutomaton_43()




CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-charge-price'), CTD_ANON_46, scope=CTD_ANON_45, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 16, 1)))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-id'), STD_ANON_72, scope=CTD_ANON_45, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 25, 1)))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sku-name'), STD_ANON_73, scope=CTD_ANON_45, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 30, 1)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=2L, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 11, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sku-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 9, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sku-name')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 10, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sku-charge-price')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 11, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_45._Automaton = _BuildAutomaton_44()




CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'charge-type'), STD_ANON_26, scope=CTD_ANON_46, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/item-price.xsd', 66, 1)))

CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amount'), STD_ANON_57, scope=CTD_ANON_46, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 37, 1)))

CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'currency'), STD_ANON_58, scope=CTD_ANON_46, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/price.xsd', 42, 1)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'charge-type')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 19, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amount')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 20, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'currency')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/sku.xsd', 21, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_46._Automaton = _BuildAutomaton_45()




CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transaction-id'), STD_ANON_76, scope=CTD_ANON_47, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 13, 1)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'payer-authentication-response'), STD_ANON_77, scope=CTD_ANON_47, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 18, 1)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transaction-id')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 8, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'payer-authentication-response')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/three-d-info.xsd', 9, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_47._Automaton = _BuildAutomaton_46()




CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ip'), STD_ANON_78, scope=CTD_ANON_48, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 16, 1)))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'remote-host'), STD_ANON_79, scope=CTD_ANON_48, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 21, 1)))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'user-agent'), STD_ANON_80, scope=CTD_ANON_48, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 26, 1)))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accept-language'), STD_ANON_81, scope=CTD_ANON_48, location=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 31, 1)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 9, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 10, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 11, 4))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ip')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 8, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'remote-host')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 9, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'user-agent')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 10, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accept-language')), pyxb.utils.utility.Location(u'http://home.bluesnap.com/integrationguide/web-info.xsd', 11, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_48._Automaton = _BuildAutomaton_47()

