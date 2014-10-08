# ./bluesnap/schema/web_info.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:7707c01e299670773fa48a3eb29a9f4fcece2d24
# Generated 2014-10-08 16:54:28.061108 by PyXB version 1.2.3
# Namespace http://ws.plimus.com

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:62159f38-4f03-11e4-8769-3c15c2ea0f80')

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
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 17, 2)
    _Documentation = None
STD_ANON._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 22, 2)
    _Documentation = None
STD_ANON_._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 27, 2)
    _Documentation = None
STD_ANON_2._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 32, 2)
    _Documentation = None
STD_ANON_3._InitializeFacetMap()

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ws.plimus.com}ip uses Python identifier ip
    __ip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ip'), 'ip', '__httpws_plimus_com_CTD_ANON_httpws_plimus_comip', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 16, 1), )

    
    ip = property(__ip.value, __ip.set, None, None)

    
    # Element {http://ws.plimus.com}remote-host uses Python identifier remote_host
    __remote_host = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'remote-host'), 'remote_host', '__httpws_plimus_com_CTD_ANON_httpws_plimus_comremote_host', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 21, 1), )

    
    remote_host = property(__remote_host.value, __remote_host.set, None, None)

    
    # Element {http://ws.plimus.com}user-agent uses Python identifier user_agent
    __user_agent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'user-agent'), 'user_agent', '__httpws_plimus_com_CTD_ANON_httpws_plimus_comuser_agent', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 26, 1), )

    
    user_agent = property(__user_agent.value, __user_agent.set, None, None)

    
    # Element {http://ws.plimus.com}accept-language uses Python identifier accept_language
    __accept_language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'accept-language'), 'accept_language', '__httpws_plimus_com_CTD_ANON_httpws_plimus_comaccept_language', False, pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 31, 1), )

    
    accept_language = property(__accept_language.value, __accept_language.set, None, None)

    _ElementMap.update({
        __ip.name() : __ip,
        __remote_host.name() : __remote_host,
        __user_agent.name() : __user_agent,
        __accept_language.name() : __accept_language
    })
    _AttributeMap.update({
        
    })



web_info = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'web-info'), CTD_ANON, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 5, 1))
Namespace.addCategoryObject('elementBinding', web_info.name().localName(), web_info)

ip = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ip'), STD_ANON, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 16, 1))
Namespace.addCategoryObject('elementBinding', ip.name().localName(), ip)

remote_host = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'remote-host'), STD_ANON_, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 21, 1))
Namespace.addCategoryObject('elementBinding', remote_host.name().localName(), remote_host)

user_agent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'user-agent'), STD_ANON_2, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 26, 1))
Namespace.addCategoryObject('elementBinding', user_agent.name().localName(), user_agent)

accept_language = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accept-language'), STD_ANON_3, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 31, 1))
Namespace.addCategoryObject('elementBinding', accept_language.name().localName(), accept_language)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ip'), STD_ANON, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 16, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'remote-host'), STD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 21, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'user-agent'), STD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 26, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accept-language'), STD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 31, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 9, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 10, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 11, 4))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ip')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 8, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'remote-host')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 9, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'user-agent')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 10, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accept-language')), pyxb.utils.utility.Location('http://home.bluesnap.com/integrationguide/web-info.xsd', 11, 4))
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
CTD_ANON._Automaton = _BuildAutomaton()

