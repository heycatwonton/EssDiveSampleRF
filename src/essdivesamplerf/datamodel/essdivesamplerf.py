# Auto generated from essdivesamplerf.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-07-18T11:03:29
# Schema: EssDiveSampleRF
#
# id: https://w3id.org/heycatwonton/EssDiveSampleRF
# description: ESS-Dive Sample RF
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
ESSDIVESAMPLERF = CurieNamespace('essdivesamplerf', 'https://w3id.org/heycatwonton/EssDiveSampleRF/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = ESSDIVESAMPLERF


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class EssDiveSampleId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = ESSDIVESAMPLERF.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class EssDiveSample(NamedThing):
    """
    Represents a EssDiveSample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ESSDIVESAMPLERF["EssDiveSample"]
    class_class_curie: ClassVar[str] = "essdivesamplerf:EssDiveSample"
    class_name: ClassVar[str] = "EssDiveSample"
    class_model_uri: ClassVar[URIRef] = ESSDIVESAMPLERF.EssDiveSample

    id: Union[str, EssDiveSampleId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EssDiveSampleId):
            self.id = EssDiveSampleId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass
class EssDiveSampleCollection(YAMLRoot):
    """
    A holder for EssDiveSample objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ESSDIVESAMPLERF["EssDiveSampleCollection"]
    class_class_curie: ClassVar[str] = "essdivesamplerf:EssDiveSampleCollection"
    class_name: ClassVar[str] = "EssDiveSampleCollection"
    class_model_uri: ClassVar[URIRef] = ESSDIVESAMPLERF.EssDiveSampleCollection

    entries: Optional[Union[Dict[Union[str, EssDiveSampleId], Union[dict, EssDiveSample]], List[Union[dict, EssDiveSample]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=EssDiveSample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=ESSDIVESAMPLERF.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=ESSDIVESAMPLERF.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=ESSDIVESAMPLERF.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=ESSDIVESAMPLERF.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=ESSDIVESAMPLERF.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=ESSDIVESAMPLERF.age_in_years, name="age_in_years", curie=ESSDIVESAMPLERF.curie('age_in_years'),
                   model_uri=ESSDIVESAMPLERF.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=ESSDIVESAMPLERF.vital_status, name="vital_status", curie=ESSDIVESAMPLERF.curie('vital_status'),
                   model_uri=ESSDIVESAMPLERF.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.essDiveSampleCollection__entries = Slot(uri=ESSDIVESAMPLERF.entries, name="essDiveSampleCollection__entries", curie=ESSDIVESAMPLERF.curie('entries'),
                   model_uri=ESSDIVESAMPLERF.essDiveSampleCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, EssDiveSampleId], Union[dict, EssDiveSample]], List[Union[dict, EssDiveSample]]]])

slots.EssDiveSample_primary_email = Slot(uri=SCHEMA.email, name="EssDiveSample_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=ESSDIVESAMPLERF.EssDiveSample_primary_email, domain=EssDiveSample, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))