# ./bluesnap/schema/credit_card_info.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:7707c01e299670773fa48a3eb29a9f4fcece2d24
# Generated 2014-10-08 16:45:40.679446 by PyXB version 1.2.3
# Namespace http://ws.plimus.com

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:2668108c-4f02-11e4-be90-3c15c2ea0f80')

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
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 44, 2)
    _Documentation = None
STD_ANON_8._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 49, 2)
    _Documentation = None
STD_ANON_9._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 54, 2)
    _Documentation = None
STD_ANON_10._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 59, 2)
    _Documentation = None
STD_ANON_11._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 64, 2)
    _Documentation = None
STD_ANON_12._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 69, 2)
    _Documentation = None
STD_ANON_13._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 74, 2)
    _Documentation = None
STD_ANON_14._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 79, 2)
    _Documentation = None
STD_ANON_15._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 84, 2)
    _Documentation = None
STD_ANON_16._InitializeFacetMap()

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}billing-contact-info uses Python identifier billing_contact_info
    __billing_contact_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'billing-contact-info'), 'billing_contact_info', '__httpws_plimus_com_CTD_ANON_httpws_plimus_combilling_contact_info', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 14, 1), )

    
    billing_contact_info = property(__billing_contact_info.value, __billing_contact_info.set, None, None)

    
    # Element {http://ws.plimus.com}credit-card uses Python identifier credit_card
    __credit_card = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'credit-card'), 'credit_card', '__httpws_plimus_com_CTD_ANON_httpws_plimus_comcredit_card', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 28, 1), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 15, 2)
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
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 29, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}card-type uses Python identifier card_type
    __card_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'card-type'), 'card_type', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comcard_type', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 43, 1), )

    
    card_type = property(__card_type.value, __card_type.set, None, None)

    
    # Element {http://ws.plimus.com}card-number uses Python identifier card_number
    __card_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'card-number'), 'card_number', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comcard_number', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 48, 1), )

    
    card_number = property(__card_number.value, __card_number.set, None, None)

    
    # Element {http://ws.plimus.com}card-last-four-digits uses Python identifier card_last_four_digits
    __card_last_four_digits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'card-last-four-digits'), 'card_last_four_digits', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comcard_last_four_digits', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 53, 1), )

    
    card_last_four_digits = property(__card_last_four_digits.value, __card_last_four_digits.set, None, None)

    
    # Element {http://ws.plimus.com}security-code uses Python identifier security_code
    __security_code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'security-code'), 'security_code', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comsecurity_code', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 58, 1), )

    
    security_code = property(__security_code.value, __security_code.set, None, None)

    
    # Element {http://ws.plimus.com}expiration-month uses Python identifier expiration_month
    __expiration_month = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'expiration-month'), 'expiration_month', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comexpiration_month', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 63, 1), )

    
    expiration_month = property(__expiration_month.value, __expiration_month.set, None, None)

    
    # Element {http://ws.plimus.com}expiration-year uses Python identifier expiration_year
    __expiration_year = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'expiration-year'), 'expiration_year', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comexpiration_year', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 68, 1), )

    
    expiration_year = property(__expiration_year.value, __expiration_year.set, None, None)

    
    # Element {http://ws.plimus.com}start-year uses Python identifier start_year
    __start_year = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'start-year'), 'start_year', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comstart_year', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 73, 1), )

    
    start_year = property(__start_year.value, __start_year.set, None, None)

    
    # Element {http://ws.plimus.com}start-month uses Python identifier start_month
    __start_month = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'start-month'), 'start_month', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comstart_month', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 78, 1), )

    
    start_month = property(__start_month.value, __start_month.set, None, None)

    
    # Element {http://ws.plimus.com}issue-number uses Python identifier issue_number
    __issue_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'issue-number'), 'issue_number', '__httpws_plimus_com_CTD_ANON_2_httpws_plimus_comissue_number', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 83, 1), )

    
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

credit_card_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit-card-info'), CTD_ANON, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 6, 1))
Namespace.addCategoryObject('elementBinding', credit_card_info.name().localName(), credit_card_info)

billing_contact_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billing-contact-info'), CTD_ANON_, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 14, 1))
Namespace.addCategoryObject('elementBinding', billing_contact_info.name().localName(), billing_contact_info)

credit_card = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit-card'), CTD_ANON_2, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 28, 1))
Namespace.addCategoryObject('elementBinding', credit_card.name().localName(), credit_card)

card_type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card-type'), STD_ANON_8, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 43, 1))
Namespace.addCategoryObject('elementBinding', card_type.name().localName(), card_type)

card_number = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card-number'), STD_ANON_9, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 48, 1))
Namespace.addCategoryObject('elementBinding', card_number.name().localName(), card_number)

card_last_four_digits = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card-last-four-digits'), STD_ANON_10, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 53, 1))
Namespace.addCategoryObject('elementBinding', card_last_four_digits.name().localName(), card_last_four_digits)

security_code = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'security-code'), STD_ANON_11, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 58, 1))
Namespace.addCategoryObject('elementBinding', security_code.name().localName(), security_code)

expiration_month = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expiration-month'), STD_ANON_12, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 63, 1))
Namespace.addCategoryObject('elementBinding', expiration_month.name().localName(), expiration_month)

expiration_year = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expiration-year'), STD_ANON_13, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 68, 1))
Namespace.addCategoryObject('elementBinding', expiration_year.name().localName(), expiration_year)

start_year = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'start-year'), STD_ANON_14, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 73, 1))
Namespace.addCategoryObject('elementBinding', start_year.name().localName(), start_year)

start_month = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'start-month'), STD_ANON_15, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 78, 1))
Namespace.addCategoryObject('elementBinding', start_month.name().localName(), start_month)

issue_number = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'issue-number'), STD_ANON_16, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 83, 1))
Namespace.addCategoryObject('elementBinding', issue_number.name().localName(), issue_number)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'billing-contact-info'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 14, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credit-card'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 28, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 9, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'billing-contact-info')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 9, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'credit-card')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 10, 4))
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
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 17, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 18, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 19, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 20, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 21, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 22, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 23, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 24, 4))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'first-name')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 17, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'last-name')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 18, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address1')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 19, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address2')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 20, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 21, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'state')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 22, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zip')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 23, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'country')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 24, 4))
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




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card-type'), STD_ANON_8, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 43, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card-number'), STD_ANON_9, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 48, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'card-last-four-digits'), STD_ANON_10, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 53, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'security-code'), STD_ANON_11, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 58, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expiration-month'), STD_ANON_12, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 63, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expiration-year'), STD_ANON_13, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 68, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'start-year'), STD_ANON_14, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 73, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'start-month'), STD_ANON_15, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 78, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'issue-number'), STD_ANON_16, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 83, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 31, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 32, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 34, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 35, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 36, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 37, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 38, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 39, 4))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card-number')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 31, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card-last-four-digits')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 32, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'card-type')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 33, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expiration-month')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 34, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expiration-year')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 35, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'security-code')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 36, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'start-month')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 37, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'start-year')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 38, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'issue-number')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/credit-card-info.xsd', 39, 4))
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

