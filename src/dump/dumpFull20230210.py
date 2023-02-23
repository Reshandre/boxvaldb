#!/usr/bin/env python


# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones intact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# ./manage.py dumpscript partners assets locations profiles boxes
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper:

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
    from dateutil.tz import tzoffset
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports
    from django.contrib.auth.models import User

    # Processing model: partners.models.BusinessPartner

    from partners.models import BusinessPartner

    partners_businesspartner_1 = BusinessPartner()
    partners_businesspartner_1.BusinessPartnerId = 'aaa6782f-4033-4e53-8c62-fe84642558dd'
    partners_businesspartner_1.BusinessPartnerclass = 'IndividualPerson'
    partners_businesspartner_1.ConsumerStatus = 'Open'
    partners_businesspartner_1 = importer.save_or_locate(partners_businesspartner_1)

    partners_businesspartner_2 = BusinessPartner()
    partners_businesspartner_2.BusinessPartnerId = '5cb0a39b-9460-44a0-9bde-d55bf1d6fa4f'
    partners_businesspartner_2.BusinessPartnerclass = 'Organization'
    partners_businesspartner_2.ConsumerStatus = 'Open'
    partners_businesspartner_2 = importer.save_or_locate(partners_businesspartner_2)

    # Processing model: assets.models.Asset

    from assets.models import Asset


    # Processing model: locations.models.GeographicalUnit

    from locations.models import GeographicalUnit

    locations_geographicalunit_1 = GeographicalUnit()
    locations_geographicalunit_1.GeographicalUnitId = 'Country_FR'
    locations_geographicalunit_1.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_1.GeographicalUnitName = 'France'
    locations_geographicalunit_1.GeographicalUnitShortName = 'France'
    locations_geographicalunit_1.HierarchyLevel = 30
    locations_geographicalunit_1 = importer.save_or_locate(locations_geographicalunit_1)

    locations_geographicalunit_2 = GeographicalUnit()
    locations_geographicalunit_2.GeographicalUnitId = 'Continent_EU'
    locations_geographicalunit_2.GeographicalUnitCategory = 'Continent'
    locations_geographicalunit_2.GeographicalUnitName = 'Europe'
    locations_geographicalunit_2.GeographicalUnitShortName = 'Europe'
    locations_geographicalunit_2.HierarchyLevel = 20
    locations_geographicalunit_2.IsPartOf = None
    locations_geographicalunit_2 = importer.save_or_locate(locations_geographicalunit_2)

    locations_geographicalunit_3 = GeographicalUnit()
    locations_geographicalunit_3.GeographicalUnitId = 'Continent_AF'
    locations_geographicalunit_3.GeographicalUnitCategory = 'Continent'
    locations_geographicalunit_3.GeographicalUnitName = 'Africa'
    locations_geographicalunit_3.GeographicalUnitShortName = 'Africa'
    locations_geographicalunit_3.HierarchyLevel = 20
    locations_geographicalunit_3.IsPartOf = None
    locations_geographicalunit_3 = importer.save_or_locate(locations_geographicalunit_3)

    locations_geographicalunit_4 = GeographicalUnit()
    locations_geographicalunit_4.GeographicalUnitId = 'Continent_AN'
    locations_geographicalunit_4.GeographicalUnitCategory = 'Continent'
    locations_geographicalunit_4.GeographicalUnitName = 'Antartica'
    locations_geographicalunit_4.GeographicalUnitShortName = 'Antartica'
    locations_geographicalunit_4.HierarchyLevel = 20
    locations_geographicalunit_4.IsPartOf = None
    locations_geographicalunit_4 = importer.save_or_locate(locations_geographicalunit_4)

    locations_geographicalunit_5 = GeographicalUnit()
    locations_geographicalunit_5.GeographicalUnitId = 'Continent_AS'
    locations_geographicalunit_5.GeographicalUnitCategory = 'Continent'
    locations_geographicalunit_5.GeographicalUnitName = 'Asia'
    locations_geographicalunit_5.GeographicalUnitShortName = 'Asia'
    locations_geographicalunit_5.HierarchyLevel = 20
    locations_geographicalunit_5.IsPartOf = None
    locations_geographicalunit_5 = importer.save_or_locate(locations_geographicalunit_5)

    locations_geographicalunit_6 = GeographicalUnit()
    locations_geographicalunit_6.GeographicalUnitId = 'Continent_OC'
    locations_geographicalunit_6.GeographicalUnitCategory = 'Continent'
    locations_geographicalunit_6.GeographicalUnitName = 'Oceania'
    locations_geographicalunit_6.GeographicalUnitShortName = 'Oceania'
    locations_geographicalunit_6.HierarchyLevel = 20
    locations_geographicalunit_6.IsPartOf = None
    locations_geographicalunit_6 = importer.save_or_locate(locations_geographicalunit_6)

    locations_geographicalunit_7 = GeographicalUnit()
    locations_geographicalunit_7.GeographicalUnitId = 'Continent_NA'
    locations_geographicalunit_7.GeographicalUnitCategory = 'Continent'
    locations_geographicalunit_7.GeographicalUnitName = 'North America'
    locations_geographicalunit_7.GeographicalUnitShortName = 'North America'
    locations_geographicalunit_7.HierarchyLevel = 20
    locations_geographicalunit_7.IsPartOf = None
    locations_geographicalunit_7 = importer.save_or_locate(locations_geographicalunit_7)

    locations_geographicalunit_8 = GeographicalUnit()
    locations_geographicalunit_8.GeographicalUnitId = 'Continent_SA'
    locations_geographicalunit_8.GeographicalUnitCategory = 'Continent'
    locations_geographicalunit_8.GeographicalUnitName = 'South America'
    locations_geographicalunit_8.GeographicalUnitShortName = 'South America'
    locations_geographicalunit_8.HierarchyLevel = 20
    locations_geographicalunit_8.IsPartOf = None
    locations_geographicalunit_8 = importer.save_or_locate(locations_geographicalunit_8)

    locations_geographicalunit_9 = GeographicalUnit()
    locations_geographicalunit_9.GeographicalUnitId = 'Country_BE'
    locations_geographicalunit_9.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_9.GeographicalUnitName = 'Belgium'
    locations_geographicalunit_9.GeographicalUnitShortName = 'Belgium'
    locations_geographicalunit_9.HierarchyLevel = 30
    locations_geographicalunit_9.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_9 = importer.save_or_locate(locations_geographicalunit_9)

    locations_geographicalunit_10 = GeographicalUnit()
    locations_geographicalunit_10.GeographicalUnitId = 'City_PARIS'
    locations_geographicalunit_10.GeographicalUnitCategory = 'City'
    locations_geographicalunit_10.GeographicalUnitName = 'Paris'
    locations_geographicalunit_10.GeographicalUnitShortName = 'Paris'
    locations_geographicalunit_10.HierarchyLevel = 40
    locations_geographicalunit_10.IsPartOf = locations_geographicalunit_1
    locations_geographicalunit_10 = importer.save_or_locate(locations_geographicalunit_10)

    locations_geographicalunit_11 = GeographicalUnit()
    locations_geographicalunit_11.GeographicalUnitId = 'City_MONTARGIS'
    locations_geographicalunit_11.GeographicalUnitCategory = 'City'
    locations_geographicalunit_11.GeographicalUnitName = 'Montargis'
    locations_geographicalunit_11.GeographicalUnitShortName = 'Montargis'
    locations_geographicalunit_11.HierarchyLevel = 40
    locations_geographicalunit_11.IsPartOf = locations_geographicalunit_1
    locations_geographicalunit_11 = importer.save_or_locate(locations_geographicalunit_11)

    locations_geographicalunit_12 = GeographicalUnit()
    locations_geographicalunit_12.GeographicalUnitId = 'Country_AX'
    locations_geographicalunit_12.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_12.GeographicalUnitName = 'Åland Islands'
    locations_geographicalunit_12.GeographicalUnitShortName = 'Åland Islands'
    locations_geographicalunit_12.HierarchyLevel = 30
    locations_geographicalunit_12.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_12 = importer.save_or_locate(locations_geographicalunit_12)

    locations_geographicalunit_13 = GeographicalUnit()
    locations_geographicalunit_13.GeographicalUnitId = 'Country_ZM'
    locations_geographicalunit_13.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_13.GeographicalUnitName = 'Zambia'
    locations_geographicalunit_13.GeographicalUnitShortName = 'Zambia'
    locations_geographicalunit_13.HierarchyLevel = 30
    locations_geographicalunit_13.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_13 = importer.save_or_locate(locations_geographicalunit_13)

    locations_geographicalunit_14 = GeographicalUnit()
    locations_geographicalunit_14.GeographicalUnitId = 'Country_YE'
    locations_geographicalunit_14.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_14.GeographicalUnitName = 'Yemen'
    locations_geographicalunit_14.GeographicalUnitShortName = 'Yemen'
    locations_geographicalunit_14.HierarchyLevel = 30
    locations_geographicalunit_14.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_14 = importer.save_or_locate(locations_geographicalunit_14)

    locations_geographicalunit_15 = GeographicalUnit()
    locations_geographicalunit_15.GeographicalUnitId = 'Country_EH'
    locations_geographicalunit_15.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_15.GeographicalUnitName = 'Western Sahara'
    locations_geographicalunit_15.GeographicalUnitShortName = 'Western Sahara'
    locations_geographicalunit_15.HierarchyLevel = 30
    locations_geographicalunit_15.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_15 = importer.save_or_locate(locations_geographicalunit_15)

    locations_geographicalunit_16 = GeographicalUnit()
    locations_geographicalunit_16.GeographicalUnitId = 'Country_WF'
    locations_geographicalunit_16.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_16.GeographicalUnitName = 'Wallis and Futuna'
    locations_geographicalunit_16.GeographicalUnitShortName = 'Wallis and Futuna'
    locations_geographicalunit_16.HierarchyLevel = 30
    locations_geographicalunit_16.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_16 = importer.save_or_locate(locations_geographicalunit_16)

    locations_geographicalunit_17 = GeographicalUnit()
    locations_geographicalunit_17.GeographicalUnitId = 'Country_VI'
    locations_geographicalunit_17.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_17.GeographicalUnitName = 'Virgin Islands (U.S.)'
    locations_geographicalunit_17.GeographicalUnitShortName = 'Virgin Islands '
    locations_geographicalunit_17.HierarchyLevel = 30
    locations_geographicalunit_17.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_17 = importer.save_or_locate(locations_geographicalunit_17)

    locations_geographicalunit_18 = GeographicalUnit()
    locations_geographicalunit_18.GeographicalUnitId = 'Country_VG'
    locations_geographicalunit_18.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_18.GeographicalUnitName = 'Virgin Islands (British)'
    locations_geographicalunit_18.GeographicalUnitShortName = 'Virgin Islands'
    locations_geographicalunit_18.HierarchyLevel = 30
    locations_geographicalunit_18.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_18 = importer.save_or_locate(locations_geographicalunit_18)

    locations_geographicalunit_19 = GeographicalUnit()
    locations_geographicalunit_19.GeographicalUnitId = 'Country_VN'
    locations_geographicalunit_19.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_19.GeographicalUnitName = 'Vietnam'
    locations_geographicalunit_19.GeographicalUnitShortName = 'Vietnam'
    locations_geographicalunit_19.HierarchyLevel = 30
    locations_geographicalunit_19.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_19 = importer.save_or_locate(locations_geographicalunit_19)

    locations_geographicalunit_20 = GeographicalUnit()
    locations_geographicalunit_20.GeographicalUnitId = 'Country_VE'
    locations_geographicalunit_20.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_20.GeographicalUnitName = 'Venezuela (Bolivarian Republic of)'
    locations_geographicalunit_20.GeographicalUnitShortName = 'Venezuela'
    locations_geographicalunit_20.HierarchyLevel = 30
    locations_geographicalunit_20.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_20 = importer.save_or_locate(locations_geographicalunit_20)

    locations_geographicalunit_21 = GeographicalUnit()
    locations_geographicalunit_21.GeographicalUnitId = 'Country_VU'
    locations_geographicalunit_21.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_21.GeographicalUnitName = 'Vanuatu'
    locations_geographicalunit_21.GeographicalUnitShortName = 'Vanuatu'
    locations_geographicalunit_21.HierarchyLevel = 30
    locations_geographicalunit_21.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_21 = importer.save_or_locate(locations_geographicalunit_21)

    locations_geographicalunit_22 = GeographicalUnit()
    locations_geographicalunit_22.GeographicalUnitId = 'Country_UZ'
    locations_geographicalunit_22.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_22.GeographicalUnitName = 'Uzbekistan'
    locations_geographicalunit_22.GeographicalUnitShortName = 'Uzbekistan'
    locations_geographicalunit_22.HierarchyLevel = 30
    locations_geographicalunit_22.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_22 = importer.save_or_locate(locations_geographicalunit_22)

    locations_geographicalunit_23 = GeographicalUnit()
    locations_geographicalunit_23.GeographicalUnitId = 'Country_UY'
    locations_geographicalunit_23.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_23.GeographicalUnitName = 'Uruguay'
    locations_geographicalunit_23.GeographicalUnitShortName = 'Uruguay'
    locations_geographicalunit_23.HierarchyLevel = 30
    locations_geographicalunit_23.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_23 = importer.save_or_locate(locations_geographicalunit_23)

    locations_geographicalunit_24 = GeographicalUnit()
    locations_geographicalunit_24.GeographicalUnitId = 'Country_US'
    locations_geographicalunit_24.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_24.GeographicalUnitName = 'United States of America (the)'
    locations_geographicalunit_24.GeographicalUnitShortName = 'USA'
    locations_geographicalunit_24.HierarchyLevel = 30
    locations_geographicalunit_24.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_24 = importer.save_or_locate(locations_geographicalunit_24)

    locations_geographicalunit_25 = GeographicalUnit()
    locations_geographicalunit_25.GeographicalUnitId = 'Country_UM'
    locations_geographicalunit_25.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_25.GeographicalUnitName = 'United States Minor Outlying Islands (the)'
    locations_geographicalunit_25.GeographicalUnitShortName = 'United States Minor Outlying Islands '
    locations_geographicalunit_25.HierarchyLevel = 30
    locations_geographicalunit_25.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_25 = importer.save_or_locate(locations_geographicalunit_25)

    locations_geographicalunit_26 = GeographicalUnit()
    locations_geographicalunit_26.GeographicalUnitId = 'Country_GB'
    locations_geographicalunit_26.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_26.GeographicalUnitName = 'United Kingdom of Great Britain and Northern Ireland (the)'
    locations_geographicalunit_26.GeographicalUnitShortName = 'UK'
    locations_geographicalunit_26.HierarchyLevel = 30
    locations_geographicalunit_26.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_26 = importer.save_or_locate(locations_geographicalunit_26)

    locations_geographicalunit_27 = GeographicalUnit()
    locations_geographicalunit_27.GeographicalUnitId = 'Country_AE'
    locations_geographicalunit_27.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_27.GeographicalUnitName = 'United Arab Emirates (the)'
    locations_geographicalunit_27.GeographicalUnitShortName = 'UAE'
    locations_geographicalunit_27.HierarchyLevel = 30
    locations_geographicalunit_27.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_27 = importer.save_or_locate(locations_geographicalunit_27)

    locations_geographicalunit_28 = GeographicalUnit()
    locations_geographicalunit_28.GeographicalUnitId = 'Country_UA'
    locations_geographicalunit_28.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_28.GeographicalUnitName = 'Ukraine'
    locations_geographicalunit_28.GeographicalUnitShortName = 'Ukraine'
    locations_geographicalunit_28.HierarchyLevel = 30
    locations_geographicalunit_28.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_28 = importer.save_or_locate(locations_geographicalunit_28)

    locations_geographicalunit_29 = GeographicalUnit()
    locations_geographicalunit_29.GeographicalUnitId = 'Country_UG'
    locations_geographicalunit_29.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_29.GeographicalUnitName = 'Uganda'
    locations_geographicalunit_29.GeographicalUnitShortName = 'Uganda'
    locations_geographicalunit_29.HierarchyLevel = 30
    locations_geographicalunit_29.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_29 = importer.save_or_locate(locations_geographicalunit_29)

    locations_geographicalunit_30 = GeographicalUnit()
    locations_geographicalunit_30.GeographicalUnitId = 'Country_TV'
    locations_geographicalunit_30.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_30.GeographicalUnitName = 'Tuvalu'
    locations_geographicalunit_30.GeographicalUnitShortName = 'Tuvalu'
    locations_geographicalunit_30.HierarchyLevel = 30
    locations_geographicalunit_30.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_30 = importer.save_or_locate(locations_geographicalunit_30)

    locations_geographicalunit_31 = GeographicalUnit()
    locations_geographicalunit_31.GeographicalUnitId = 'Country_TC'
    locations_geographicalunit_31.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_31.GeographicalUnitName = 'Turks and Caicos Islands (the)'
    locations_geographicalunit_31.GeographicalUnitShortName = 'Turks and Caicos Islands '
    locations_geographicalunit_31.HierarchyLevel = 30
    locations_geographicalunit_31.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_31 = importer.save_or_locate(locations_geographicalunit_31)

    locations_geographicalunit_32 = GeographicalUnit()
    locations_geographicalunit_32.GeographicalUnitId = 'Country_TM'
    locations_geographicalunit_32.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_32.GeographicalUnitName = 'Turkmenistan'
    locations_geographicalunit_32.GeographicalUnitShortName = 'Turkmenistan'
    locations_geographicalunit_32.HierarchyLevel = 30
    locations_geographicalunit_32.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_32 = importer.save_or_locate(locations_geographicalunit_32)

    locations_geographicalunit_33 = GeographicalUnit()
    locations_geographicalunit_33.GeographicalUnitId = 'Country_TR'
    locations_geographicalunit_33.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_33.GeographicalUnitName = 'Turkey'
    locations_geographicalunit_33.GeographicalUnitShortName = 'Turkey'
    locations_geographicalunit_33.HierarchyLevel = 30
    locations_geographicalunit_33.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_33 = importer.save_or_locate(locations_geographicalunit_33)

    locations_geographicalunit_34 = GeographicalUnit()
    locations_geographicalunit_34.GeographicalUnitId = 'Country_TN'
    locations_geographicalunit_34.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_34.GeographicalUnitName = 'Tunisia'
    locations_geographicalunit_34.GeographicalUnitShortName = 'Tunisia'
    locations_geographicalunit_34.HierarchyLevel = 30
    locations_geographicalunit_34.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_34 = importer.save_or_locate(locations_geographicalunit_34)

    locations_geographicalunit_35 = GeographicalUnit()
    locations_geographicalunit_35.GeographicalUnitId = 'Country_TT'
    locations_geographicalunit_35.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_35.GeographicalUnitName = 'Trinidad and Tobago'
    locations_geographicalunit_35.GeographicalUnitShortName = 'Trinidad'
    locations_geographicalunit_35.HierarchyLevel = 30
    locations_geographicalunit_35.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_35 = importer.save_or_locate(locations_geographicalunit_35)

    locations_geographicalunit_36 = GeographicalUnit()
    locations_geographicalunit_36.GeographicalUnitId = 'Country_TO'
    locations_geographicalunit_36.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_36.GeographicalUnitName = 'Tonga'
    locations_geographicalunit_36.GeographicalUnitShortName = 'Tonga'
    locations_geographicalunit_36.HierarchyLevel = 30
    locations_geographicalunit_36.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_36 = importer.save_or_locate(locations_geographicalunit_36)

    locations_geographicalunit_37 = GeographicalUnit()
    locations_geographicalunit_37.GeographicalUnitId = 'Country_TK'
    locations_geographicalunit_37.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_37.GeographicalUnitName = 'Tokelau'
    locations_geographicalunit_37.GeographicalUnitShortName = 'Tokelau'
    locations_geographicalunit_37.HierarchyLevel = 30
    locations_geographicalunit_37.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_37 = importer.save_or_locate(locations_geographicalunit_37)

    locations_geographicalunit_38 = GeographicalUnit()
    locations_geographicalunit_38.GeographicalUnitId = 'Country_TG'
    locations_geographicalunit_38.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_38.GeographicalUnitName = 'Togo'
    locations_geographicalunit_38.GeographicalUnitShortName = 'Togo'
    locations_geographicalunit_38.HierarchyLevel = 30
    locations_geographicalunit_38.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_38 = importer.save_or_locate(locations_geographicalunit_38)

    locations_geographicalunit_39 = GeographicalUnit()
    locations_geographicalunit_39.GeographicalUnitId = 'Country_TL'
    locations_geographicalunit_39.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_39.GeographicalUnitName = 'Timor-Leste'
    locations_geographicalunit_39.GeographicalUnitShortName = 'East Timor'
    locations_geographicalunit_39.HierarchyLevel = 30
    locations_geographicalunit_39.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_39 = importer.save_or_locate(locations_geographicalunit_39)

    locations_geographicalunit_40 = GeographicalUnit()
    locations_geographicalunit_40.GeographicalUnitId = 'Country_TH'
    locations_geographicalunit_40.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_40.GeographicalUnitName = 'Thailand'
    locations_geographicalunit_40.GeographicalUnitShortName = 'Thailand'
    locations_geographicalunit_40.HierarchyLevel = 30
    locations_geographicalunit_40.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_40 = importer.save_or_locate(locations_geographicalunit_40)

    locations_geographicalunit_41 = GeographicalUnit()
    locations_geographicalunit_41.GeographicalUnitId = 'Country_TZ'
    locations_geographicalunit_41.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_41.GeographicalUnitName = 'Tanzania, United Republic of'
    locations_geographicalunit_41.GeographicalUnitShortName = 'Tanzania'
    locations_geographicalunit_41.HierarchyLevel = 30
    locations_geographicalunit_41.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_41 = importer.save_or_locate(locations_geographicalunit_41)

    locations_geographicalunit_42 = GeographicalUnit()
    locations_geographicalunit_42.GeographicalUnitId = 'Country_TJ'
    locations_geographicalunit_42.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_42.GeographicalUnitName = 'Tajikistan'
    locations_geographicalunit_42.GeographicalUnitShortName = 'Tajikistan'
    locations_geographicalunit_42.HierarchyLevel = 30
    locations_geographicalunit_42.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_42 = importer.save_or_locate(locations_geographicalunit_42)

    locations_geographicalunit_43 = GeographicalUnit()
    locations_geographicalunit_43.GeographicalUnitId = 'Country_TW'
    locations_geographicalunit_43.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_43.GeographicalUnitName = 'Taiwan (Province of China)'
    locations_geographicalunit_43.GeographicalUnitShortName = 'Taiwan'
    locations_geographicalunit_43.HierarchyLevel = 30
    locations_geographicalunit_43.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_43 = importer.save_or_locate(locations_geographicalunit_43)

    locations_geographicalunit_44 = GeographicalUnit()
    locations_geographicalunit_44.GeographicalUnitId = 'Country_SY'
    locations_geographicalunit_44.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_44.GeographicalUnitName = 'Syrian Arab Republic'
    locations_geographicalunit_44.GeographicalUnitShortName = 'Syrian Arab Republic'
    locations_geographicalunit_44.HierarchyLevel = 30
    locations_geographicalunit_44.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_44 = importer.save_or_locate(locations_geographicalunit_44)

    locations_geographicalunit_45 = GeographicalUnit()
    locations_geographicalunit_45.GeographicalUnitId = 'Country_CH'
    locations_geographicalunit_45.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_45.GeographicalUnitName = 'Switzerland'
    locations_geographicalunit_45.GeographicalUnitShortName = 'Switzerland'
    locations_geographicalunit_45.HierarchyLevel = 30
    locations_geographicalunit_45.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_45 = importer.save_or_locate(locations_geographicalunit_45)

    locations_geographicalunit_46 = GeographicalUnit()
    locations_geographicalunit_46.GeographicalUnitId = 'Country_SE'
    locations_geographicalunit_46.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_46.GeographicalUnitName = 'Sweden'
    locations_geographicalunit_46.GeographicalUnitShortName = 'Sweden'
    locations_geographicalunit_46.HierarchyLevel = 30
    locations_geographicalunit_46.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_46 = importer.save_or_locate(locations_geographicalunit_46)

    locations_geographicalunit_47 = GeographicalUnit()
    locations_geographicalunit_47.GeographicalUnitId = 'Country_SJ'
    locations_geographicalunit_47.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_47.GeographicalUnitName = 'Svalbard and Jan Mayen'
    locations_geographicalunit_47.GeographicalUnitShortName = 'Svalbard and Jan Mayen'
    locations_geographicalunit_47.HierarchyLevel = 30
    locations_geographicalunit_47.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_47 = importer.save_or_locate(locations_geographicalunit_47)

    locations_geographicalunit_48 = GeographicalUnit()
    locations_geographicalunit_48.GeographicalUnitId = 'Country_SR'
    locations_geographicalunit_48.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_48.GeographicalUnitName = 'Suriname'
    locations_geographicalunit_48.GeographicalUnitShortName = 'Suriname'
    locations_geographicalunit_48.HierarchyLevel = 30
    locations_geographicalunit_48.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_48 = importer.save_or_locate(locations_geographicalunit_48)

    locations_geographicalunit_49 = GeographicalUnit()
    locations_geographicalunit_49.GeographicalUnitId = 'Country_SD'
    locations_geographicalunit_49.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_49.GeographicalUnitName = 'Sudan (the)'
    locations_geographicalunit_49.GeographicalUnitShortName = 'Sudan'
    locations_geographicalunit_49.HierarchyLevel = 30
    locations_geographicalunit_49.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_49 = importer.save_or_locate(locations_geographicalunit_49)

    locations_geographicalunit_50 = GeographicalUnit()
    locations_geographicalunit_50.GeographicalUnitId = 'Country_LK'
    locations_geographicalunit_50.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_50.GeographicalUnitName = 'Sri Lanka'
    locations_geographicalunit_50.GeographicalUnitShortName = 'Sri Lanka'
    locations_geographicalunit_50.HierarchyLevel = 30
    locations_geographicalunit_50.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_50 = importer.save_or_locate(locations_geographicalunit_50)

    locations_geographicalunit_51 = GeographicalUnit()
    locations_geographicalunit_51.GeographicalUnitId = 'Country_ES'
    locations_geographicalunit_51.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_51.GeographicalUnitName = 'Spain'
    locations_geographicalunit_51.GeographicalUnitShortName = 'Spain'
    locations_geographicalunit_51.HierarchyLevel = 30
    locations_geographicalunit_51.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_51 = importer.save_or_locate(locations_geographicalunit_51)

    locations_geographicalunit_52 = GeographicalUnit()
    locations_geographicalunit_52.GeographicalUnitId = 'Country_SS'
    locations_geographicalunit_52.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_52.GeographicalUnitName = 'South Sudan'
    locations_geographicalunit_52.GeographicalUnitShortName = 'South Sudan'
    locations_geographicalunit_52.HierarchyLevel = 30
    locations_geographicalunit_52.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_52 = importer.save_or_locate(locations_geographicalunit_52)

    locations_geographicalunit_53 = GeographicalUnit()
    locations_geographicalunit_53.GeographicalUnitId = 'Country_GS'
    locations_geographicalunit_53.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_53.GeographicalUnitName = 'South Georgia and the South Sandwich Islands'
    locations_geographicalunit_53.GeographicalUnitShortName = 'South Georgia and the South Sandwich Islands'
    locations_geographicalunit_53.HierarchyLevel = 30
    locations_geographicalunit_53.IsPartOf = locations_geographicalunit_4
    locations_geographicalunit_53 = importer.save_or_locate(locations_geographicalunit_53)

    locations_geographicalunit_54 = GeographicalUnit()
    locations_geographicalunit_54.GeographicalUnitId = 'Country_ZA'
    locations_geographicalunit_54.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_54.GeographicalUnitName = 'South Africa'
    locations_geographicalunit_54.GeographicalUnitShortName = 'South Africa'
    locations_geographicalunit_54.HierarchyLevel = 30
    locations_geographicalunit_54.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_54 = importer.save_or_locate(locations_geographicalunit_54)

    locations_geographicalunit_55 = GeographicalUnit()
    locations_geographicalunit_55.GeographicalUnitId = 'Country_SO'
    locations_geographicalunit_55.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_55.GeographicalUnitName = 'Somalia'
    locations_geographicalunit_55.GeographicalUnitShortName = 'Somalia'
    locations_geographicalunit_55.HierarchyLevel = 30
    locations_geographicalunit_55.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_55 = importer.save_or_locate(locations_geographicalunit_55)

    locations_geographicalunit_56 = GeographicalUnit()
    locations_geographicalunit_56.GeographicalUnitId = 'Country_SB'
    locations_geographicalunit_56.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_56.GeographicalUnitName = 'Solomon Islands'
    locations_geographicalunit_56.GeographicalUnitShortName = 'Solomon Islands'
    locations_geographicalunit_56.HierarchyLevel = 30
    locations_geographicalunit_56.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_56 = importer.save_or_locate(locations_geographicalunit_56)

    locations_geographicalunit_57 = GeographicalUnit()
    locations_geographicalunit_57.GeographicalUnitId = 'Country_SI'
    locations_geographicalunit_57.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_57.GeographicalUnitName = 'Slovenia'
    locations_geographicalunit_57.GeographicalUnitShortName = 'Slovenia'
    locations_geographicalunit_57.HierarchyLevel = 30
    locations_geographicalunit_57.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_57 = importer.save_or_locate(locations_geographicalunit_57)

    locations_geographicalunit_58 = GeographicalUnit()
    locations_geographicalunit_58.GeographicalUnitId = 'Country_SK'
    locations_geographicalunit_58.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_58.GeographicalUnitName = 'Slovakia'
    locations_geographicalunit_58.GeographicalUnitShortName = 'Slovakia'
    locations_geographicalunit_58.HierarchyLevel = 30
    locations_geographicalunit_58.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_58 = importer.save_or_locate(locations_geographicalunit_58)

    locations_geographicalunit_59 = GeographicalUnit()
    locations_geographicalunit_59.GeographicalUnitId = 'Country_SX'
    locations_geographicalunit_59.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_59.GeographicalUnitName = 'Sint Maarten (Dutch part)'
    locations_geographicalunit_59.GeographicalUnitShortName = 'Sint Maarten'
    locations_geographicalunit_59.HierarchyLevel = 30
    locations_geographicalunit_59.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_59 = importer.save_or_locate(locations_geographicalunit_59)

    locations_geographicalunit_60 = GeographicalUnit()
    locations_geographicalunit_60.GeographicalUnitId = 'Country_SG'
    locations_geographicalunit_60.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_60.GeographicalUnitName = 'Singapore'
    locations_geographicalunit_60.GeographicalUnitShortName = 'Singapore'
    locations_geographicalunit_60.HierarchyLevel = 30
    locations_geographicalunit_60.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_60 = importer.save_or_locate(locations_geographicalunit_60)

    locations_geographicalunit_61 = GeographicalUnit()
    locations_geographicalunit_61.GeographicalUnitId = 'Country_SL'
    locations_geographicalunit_61.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_61.GeographicalUnitName = 'Sierra Leone'
    locations_geographicalunit_61.GeographicalUnitShortName = 'Sierra Leone'
    locations_geographicalunit_61.HierarchyLevel = 30
    locations_geographicalunit_61.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_61 = importer.save_or_locate(locations_geographicalunit_61)

    locations_geographicalunit_62 = GeographicalUnit()
    locations_geographicalunit_62.GeographicalUnitId = 'Country_SC'
    locations_geographicalunit_62.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_62.GeographicalUnitName = 'Seychelles'
    locations_geographicalunit_62.GeographicalUnitShortName = 'Seychelles'
    locations_geographicalunit_62.HierarchyLevel = 30
    locations_geographicalunit_62.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_62 = importer.save_or_locate(locations_geographicalunit_62)

    locations_geographicalunit_63 = GeographicalUnit()
    locations_geographicalunit_63.GeographicalUnitId = 'Country_RS'
    locations_geographicalunit_63.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_63.GeographicalUnitName = 'Serbia'
    locations_geographicalunit_63.GeographicalUnitShortName = 'Serbia'
    locations_geographicalunit_63.HierarchyLevel = 30
    locations_geographicalunit_63.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_63 = importer.save_or_locate(locations_geographicalunit_63)

    locations_geographicalunit_64 = GeographicalUnit()
    locations_geographicalunit_64.GeographicalUnitId = 'Country_SN'
    locations_geographicalunit_64.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_64.GeographicalUnitName = 'Senegal'
    locations_geographicalunit_64.GeographicalUnitShortName = 'Senegal'
    locations_geographicalunit_64.HierarchyLevel = 30
    locations_geographicalunit_64.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_64 = importer.save_or_locate(locations_geographicalunit_64)

    locations_geographicalunit_65 = GeographicalUnit()
    locations_geographicalunit_65.GeographicalUnitId = 'Country_SA'
    locations_geographicalunit_65.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_65.GeographicalUnitName = 'Saudi Arabia'
    locations_geographicalunit_65.GeographicalUnitShortName = 'Saudi Arabia'
    locations_geographicalunit_65.HierarchyLevel = 30
    locations_geographicalunit_65.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_65 = importer.save_or_locate(locations_geographicalunit_65)

    locations_geographicalunit_66 = GeographicalUnit()
    locations_geographicalunit_66.GeographicalUnitId = 'Country_ST'
    locations_geographicalunit_66.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_66.GeographicalUnitName = 'Sao Tome and Principe'
    locations_geographicalunit_66.GeographicalUnitShortName = 'Sao Tome and Principe'
    locations_geographicalunit_66.HierarchyLevel = 30
    locations_geographicalunit_66.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_66 = importer.save_or_locate(locations_geographicalunit_66)

    locations_geographicalunit_67 = GeographicalUnit()
    locations_geographicalunit_67.GeographicalUnitId = 'Country_SM'
    locations_geographicalunit_67.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_67.GeographicalUnitName = 'San Marino'
    locations_geographicalunit_67.GeographicalUnitShortName = 'San Marino'
    locations_geographicalunit_67.HierarchyLevel = 30
    locations_geographicalunit_67.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_67 = importer.save_or_locate(locations_geographicalunit_67)

    locations_geographicalunit_68 = GeographicalUnit()
    locations_geographicalunit_68.GeographicalUnitId = 'Country_WS'
    locations_geographicalunit_68.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_68.GeographicalUnitName = 'Samoa'
    locations_geographicalunit_68.GeographicalUnitShortName = 'Samoa'
    locations_geographicalunit_68.HierarchyLevel = 30
    locations_geographicalunit_68.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_68 = importer.save_or_locate(locations_geographicalunit_68)

    locations_geographicalunit_69 = GeographicalUnit()
    locations_geographicalunit_69.GeographicalUnitId = 'Country_VC'
    locations_geographicalunit_69.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_69.GeographicalUnitName = 'Saint Vincent and the Grenadines'
    locations_geographicalunit_69.GeographicalUnitShortName = 'Saint Vincent and the Grenadines'
    locations_geographicalunit_69.HierarchyLevel = 30
    locations_geographicalunit_69.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_69 = importer.save_or_locate(locations_geographicalunit_69)

    locations_geographicalunit_70 = GeographicalUnit()
    locations_geographicalunit_70.GeographicalUnitId = 'Country_PM'
    locations_geographicalunit_70.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_70.GeographicalUnitName = 'Saint Pierre and Miquelon'
    locations_geographicalunit_70.GeographicalUnitShortName = 'Saint Pierre and Miquelon'
    locations_geographicalunit_70.HierarchyLevel = 30
    locations_geographicalunit_70.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_70 = importer.save_or_locate(locations_geographicalunit_70)

    locations_geographicalunit_71 = GeographicalUnit()
    locations_geographicalunit_71.GeographicalUnitId = 'Country_MF'
    locations_geographicalunit_71.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_71.GeographicalUnitName = 'Saint Martin (French part)'
    locations_geographicalunit_71.GeographicalUnitShortName = 'Saint Martin'
    locations_geographicalunit_71.HierarchyLevel = 30
    locations_geographicalunit_71.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_71 = importer.save_or_locate(locations_geographicalunit_71)

    locations_geographicalunit_72 = GeographicalUnit()
    locations_geographicalunit_72.GeographicalUnitId = 'Country_LC'
    locations_geographicalunit_72.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_72.GeographicalUnitName = 'Saint Lucia'
    locations_geographicalunit_72.GeographicalUnitShortName = 'Saint Lucia'
    locations_geographicalunit_72.HierarchyLevel = 30
    locations_geographicalunit_72.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_72 = importer.save_or_locate(locations_geographicalunit_72)

    locations_geographicalunit_73 = GeographicalUnit()
    locations_geographicalunit_73.GeographicalUnitId = 'Country_KN'
    locations_geographicalunit_73.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_73.GeographicalUnitName = 'Saint Kitts and Nevis'
    locations_geographicalunit_73.GeographicalUnitShortName = 'Saint Kitts and Nevis'
    locations_geographicalunit_73.HierarchyLevel = 30
    locations_geographicalunit_73.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_73 = importer.save_or_locate(locations_geographicalunit_73)

    locations_geographicalunit_74 = GeographicalUnit()
    locations_geographicalunit_74.GeographicalUnitId = 'Country_SH'
    locations_geographicalunit_74.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_74.GeographicalUnitName = 'Saint Helena, Ascension and Tristan da Cunha'
    locations_geographicalunit_74.GeographicalUnitShortName = 'Saint Helena, Ascension and Tristan da Cunha'
    locations_geographicalunit_74.HierarchyLevel = 30
    locations_geographicalunit_74.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_74 = importer.save_or_locate(locations_geographicalunit_74)

    locations_geographicalunit_75 = GeographicalUnit()
    locations_geographicalunit_75.GeographicalUnitId = 'Country_BL'
    locations_geographicalunit_75.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_75.GeographicalUnitName = 'Saint Barthélemy'
    locations_geographicalunit_75.GeographicalUnitShortName = 'Saint Barthélemy'
    locations_geographicalunit_75.HierarchyLevel = 30
    locations_geographicalunit_75.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_75 = importer.save_or_locate(locations_geographicalunit_75)

    locations_geographicalunit_76 = GeographicalUnit()
    locations_geographicalunit_76.GeographicalUnitId = 'Country_RE'
    locations_geographicalunit_76.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_76.GeographicalUnitName = 'Réunion'
    locations_geographicalunit_76.GeographicalUnitShortName = 'Réunion'
    locations_geographicalunit_76.HierarchyLevel = 30
    locations_geographicalunit_76.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_76 = importer.save_or_locate(locations_geographicalunit_76)

    locations_geographicalunit_77 = GeographicalUnit()
    locations_geographicalunit_77.GeographicalUnitId = 'Country_RW'
    locations_geographicalunit_77.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_77.GeographicalUnitName = 'Rwanda'
    locations_geographicalunit_77.GeographicalUnitShortName = 'Rwanda'
    locations_geographicalunit_77.HierarchyLevel = 30
    locations_geographicalunit_77.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_77 = importer.save_or_locate(locations_geographicalunit_77)

    locations_geographicalunit_78 = GeographicalUnit()
    locations_geographicalunit_78.GeographicalUnitId = 'Country_RU'
    locations_geographicalunit_78.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_78.GeographicalUnitName = 'Russian Federation (the)'
    locations_geographicalunit_78.GeographicalUnitShortName = 'Russia'
    locations_geographicalunit_78.HierarchyLevel = 30
    locations_geographicalunit_78.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_78 = importer.save_or_locate(locations_geographicalunit_78)

    locations_geographicalunit_79 = GeographicalUnit()
    locations_geographicalunit_79.GeographicalUnitId = 'Country_RO'
    locations_geographicalunit_79.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_79.GeographicalUnitName = 'Romania'
    locations_geographicalunit_79.GeographicalUnitShortName = 'Romania'
    locations_geographicalunit_79.HierarchyLevel = 30
    locations_geographicalunit_79.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_79 = importer.save_or_locate(locations_geographicalunit_79)

    locations_geographicalunit_80 = GeographicalUnit()
    locations_geographicalunit_80.GeographicalUnitId = 'Country_MK'
    locations_geographicalunit_80.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_80.GeographicalUnitName = 'Republic of North Macedonia'
    locations_geographicalunit_80.GeographicalUnitShortName = 'North Macedonia'
    locations_geographicalunit_80.HierarchyLevel = 30
    locations_geographicalunit_80.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_80 = importer.save_or_locate(locations_geographicalunit_80)

    locations_geographicalunit_81 = GeographicalUnit()
    locations_geographicalunit_81.GeographicalUnitId = 'Country_QA'
    locations_geographicalunit_81.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_81.GeographicalUnitName = 'Qatar'
    locations_geographicalunit_81.GeographicalUnitShortName = 'Qatar'
    locations_geographicalunit_81.HierarchyLevel = 30
    locations_geographicalunit_81.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_81 = importer.save_or_locate(locations_geographicalunit_81)

    locations_geographicalunit_82 = GeographicalUnit()
    locations_geographicalunit_82.GeographicalUnitId = 'Country_PR'
    locations_geographicalunit_82.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_82.GeographicalUnitName = 'Puerto Rico'
    locations_geographicalunit_82.GeographicalUnitShortName = 'Puerto Rico'
    locations_geographicalunit_82.HierarchyLevel = 30
    locations_geographicalunit_82.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_82 = importer.save_or_locate(locations_geographicalunit_82)

    locations_geographicalunit_83 = GeographicalUnit()
    locations_geographicalunit_83.GeographicalUnitId = 'Country_PT'
    locations_geographicalunit_83.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_83.GeographicalUnitName = 'Portugal'
    locations_geographicalunit_83.GeographicalUnitShortName = 'Portugal'
    locations_geographicalunit_83.HierarchyLevel = 30
    locations_geographicalunit_83.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_83 = importer.save_or_locate(locations_geographicalunit_83)

    locations_geographicalunit_84 = GeographicalUnit()
    locations_geographicalunit_84.GeographicalUnitId = 'Country_PL'
    locations_geographicalunit_84.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_84.GeographicalUnitName = 'Poland'
    locations_geographicalunit_84.GeographicalUnitShortName = 'Poland'
    locations_geographicalunit_84.HierarchyLevel = 30
    locations_geographicalunit_84.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_84 = importer.save_or_locate(locations_geographicalunit_84)

    locations_geographicalunit_85 = GeographicalUnit()
    locations_geographicalunit_85.GeographicalUnitId = 'Country_PN'
    locations_geographicalunit_85.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_85.GeographicalUnitName = 'Pitcairn'
    locations_geographicalunit_85.GeographicalUnitShortName = 'Pitcairn'
    locations_geographicalunit_85.HierarchyLevel = 30
    locations_geographicalunit_85.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_85 = importer.save_or_locate(locations_geographicalunit_85)

    locations_geographicalunit_86 = GeographicalUnit()
    locations_geographicalunit_86.GeographicalUnitId = 'Country_PH'
    locations_geographicalunit_86.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_86.GeographicalUnitName = 'Philippines (the)'
    locations_geographicalunit_86.GeographicalUnitShortName = 'Philippines'
    locations_geographicalunit_86.HierarchyLevel = 30
    locations_geographicalunit_86.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_86 = importer.save_or_locate(locations_geographicalunit_86)

    locations_geographicalunit_87 = GeographicalUnit()
    locations_geographicalunit_87.GeographicalUnitId = 'Country_PE'
    locations_geographicalunit_87.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_87.GeographicalUnitName = 'Peru'
    locations_geographicalunit_87.GeographicalUnitShortName = 'Peru'
    locations_geographicalunit_87.HierarchyLevel = 30
    locations_geographicalunit_87.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_87 = importer.save_or_locate(locations_geographicalunit_87)

    locations_geographicalunit_88 = GeographicalUnit()
    locations_geographicalunit_88.GeographicalUnitId = 'Country_PY'
    locations_geographicalunit_88.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_88.GeographicalUnitName = 'Paraguay'
    locations_geographicalunit_88.GeographicalUnitShortName = 'Paraguay'
    locations_geographicalunit_88.HierarchyLevel = 30
    locations_geographicalunit_88.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_88 = importer.save_or_locate(locations_geographicalunit_88)

    locations_geographicalunit_89 = GeographicalUnit()
    locations_geographicalunit_89.GeographicalUnitId = 'Country_PG'
    locations_geographicalunit_89.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_89.GeographicalUnitName = 'Papua New Guinea'
    locations_geographicalunit_89.GeographicalUnitShortName = 'Papua New Guinea'
    locations_geographicalunit_89.HierarchyLevel = 30
    locations_geographicalunit_89.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_89 = importer.save_or_locate(locations_geographicalunit_89)

    locations_geographicalunit_90 = GeographicalUnit()
    locations_geographicalunit_90.GeographicalUnitId = 'Country_PA'
    locations_geographicalunit_90.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_90.GeographicalUnitName = 'Panama'
    locations_geographicalunit_90.GeographicalUnitShortName = 'Panama'
    locations_geographicalunit_90.HierarchyLevel = 30
    locations_geographicalunit_90.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_90 = importer.save_or_locate(locations_geographicalunit_90)

    locations_geographicalunit_91 = GeographicalUnit()
    locations_geographicalunit_91.GeographicalUnitId = 'Country_PS'
    locations_geographicalunit_91.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_91.GeographicalUnitName = 'Palestine, State of'
    locations_geographicalunit_91.GeographicalUnitShortName = 'Palestine'
    locations_geographicalunit_91.HierarchyLevel = 30
    locations_geographicalunit_91.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_91 = importer.save_or_locate(locations_geographicalunit_91)

    locations_geographicalunit_92 = GeographicalUnit()
    locations_geographicalunit_92.GeographicalUnitId = 'Country_PW'
    locations_geographicalunit_92.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_92.GeographicalUnitName = 'Palau'
    locations_geographicalunit_92.GeographicalUnitShortName = 'Palau'
    locations_geographicalunit_92.HierarchyLevel = 30
    locations_geographicalunit_92.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_92 = importer.save_or_locate(locations_geographicalunit_92)

    locations_geographicalunit_93 = GeographicalUnit()
    locations_geographicalunit_93.GeographicalUnitId = 'Country_PK'
    locations_geographicalunit_93.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_93.GeographicalUnitName = 'Pakistan'
    locations_geographicalunit_93.GeographicalUnitShortName = 'Pakistan'
    locations_geographicalunit_93.HierarchyLevel = 30
    locations_geographicalunit_93.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_93 = importer.save_or_locate(locations_geographicalunit_93)

    locations_geographicalunit_94 = GeographicalUnit()
    locations_geographicalunit_94.GeographicalUnitId = 'Country_OM'
    locations_geographicalunit_94.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_94.GeographicalUnitName = 'Oman'
    locations_geographicalunit_94.GeographicalUnitShortName = 'Oman'
    locations_geographicalunit_94.HierarchyLevel = 30
    locations_geographicalunit_94.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_94 = importer.save_or_locate(locations_geographicalunit_94)

    locations_geographicalunit_95 = GeographicalUnit()
    locations_geographicalunit_95.GeographicalUnitId = 'Country_NO'
    locations_geographicalunit_95.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_95.GeographicalUnitName = 'Norway'
    locations_geographicalunit_95.GeographicalUnitShortName = 'Norway'
    locations_geographicalunit_95.HierarchyLevel = 30
    locations_geographicalunit_95.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_95 = importer.save_or_locate(locations_geographicalunit_95)

    locations_geographicalunit_96 = GeographicalUnit()
    locations_geographicalunit_96.GeographicalUnitId = 'Country_MP'
    locations_geographicalunit_96.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_96.GeographicalUnitName = 'Northern Mariana Islands (the)'
    locations_geographicalunit_96.GeographicalUnitShortName = 'Northern Mariana Islands'
    locations_geographicalunit_96.HierarchyLevel = 30
    locations_geographicalunit_96.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_96 = importer.save_or_locate(locations_geographicalunit_96)

    locations_geographicalunit_97 = GeographicalUnit()
    locations_geographicalunit_97.GeographicalUnitId = 'Country_NF'
    locations_geographicalunit_97.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_97.GeographicalUnitName = 'Norfolk Island'
    locations_geographicalunit_97.GeographicalUnitShortName = 'Norfolk Island'
    locations_geographicalunit_97.HierarchyLevel = 30
    locations_geographicalunit_97.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_97 = importer.save_or_locate(locations_geographicalunit_97)

    locations_geographicalunit_98 = GeographicalUnit()
    locations_geographicalunit_98.GeographicalUnitId = 'Country_NU'
    locations_geographicalunit_98.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_98.GeographicalUnitName = 'Niue'
    locations_geographicalunit_98.GeographicalUnitShortName = 'Niue'
    locations_geographicalunit_98.HierarchyLevel = 30
    locations_geographicalunit_98.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_98 = importer.save_or_locate(locations_geographicalunit_98)

    locations_geographicalunit_99 = GeographicalUnit()
    locations_geographicalunit_99.GeographicalUnitId = 'Country_NG'
    locations_geographicalunit_99.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_99.GeographicalUnitName = 'Nigeria'
    locations_geographicalunit_99.GeographicalUnitShortName = 'Nigeria'
    locations_geographicalunit_99.HierarchyLevel = 30
    locations_geographicalunit_99.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_99 = importer.save_or_locate(locations_geographicalunit_99)

    locations_geographicalunit_100 = GeographicalUnit()
    locations_geographicalunit_100.GeographicalUnitId = 'Country_NE'
    locations_geographicalunit_100.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_100.GeographicalUnitName = 'Niger (the)'
    locations_geographicalunit_100.GeographicalUnitShortName = 'Niger (the)'
    locations_geographicalunit_100.HierarchyLevel = 30
    locations_geographicalunit_100.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_100 = importer.save_or_locate(locations_geographicalunit_100)

    locations_geographicalunit_101 = GeographicalUnit()
    locations_geographicalunit_101.GeographicalUnitId = 'Country_NI'
    locations_geographicalunit_101.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_101.GeographicalUnitName = 'Nicaragua'
    locations_geographicalunit_101.GeographicalUnitShortName = 'Nicaragua'
    locations_geographicalunit_101.HierarchyLevel = 30
    locations_geographicalunit_101.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_101 = importer.save_or_locate(locations_geographicalunit_101)

    locations_geographicalunit_102 = GeographicalUnit()
    locations_geographicalunit_102.GeographicalUnitId = 'Country_NZ'
    locations_geographicalunit_102.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_102.GeographicalUnitName = 'New Zealand'
    locations_geographicalunit_102.GeographicalUnitShortName = 'New Zealand'
    locations_geographicalunit_102.HierarchyLevel = 30
    locations_geographicalunit_102.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_102 = importer.save_or_locate(locations_geographicalunit_102)

    locations_geographicalunit_103 = GeographicalUnit()
    locations_geographicalunit_103.GeographicalUnitId = 'Country_NC'
    locations_geographicalunit_103.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_103.GeographicalUnitName = 'New Caledonia'
    locations_geographicalunit_103.GeographicalUnitShortName = 'New Caledonia'
    locations_geographicalunit_103.HierarchyLevel = 30
    locations_geographicalunit_103.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_103 = importer.save_or_locate(locations_geographicalunit_103)

    locations_geographicalunit_104 = GeographicalUnit()
    locations_geographicalunit_104.GeographicalUnitId = 'Country_NL'
    locations_geographicalunit_104.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_104.GeographicalUnitName = 'Netherlands (the)'
    locations_geographicalunit_104.GeographicalUnitShortName = 'Netherlands'
    locations_geographicalunit_104.HierarchyLevel = 30
    locations_geographicalunit_104.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_104 = importer.save_or_locate(locations_geographicalunit_104)

    locations_geographicalunit_105 = GeographicalUnit()
    locations_geographicalunit_105.GeographicalUnitId = 'Country_NP'
    locations_geographicalunit_105.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_105.GeographicalUnitName = 'Nepal'
    locations_geographicalunit_105.GeographicalUnitShortName = 'Nepal'
    locations_geographicalunit_105.HierarchyLevel = 30
    locations_geographicalunit_105.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_105 = importer.save_or_locate(locations_geographicalunit_105)

    locations_geographicalunit_106 = GeographicalUnit()
    locations_geographicalunit_106.GeographicalUnitId = 'Country_NR'
    locations_geographicalunit_106.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_106.GeographicalUnitName = 'Nauru'
    locations_geographicalunit_106.GeographicalUnitShortName = 'Nauru'
    locations_geographicalunit_106.HierarchyLevel = 30
    locations_geographicalunit_106.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_106 = importer.save_or_locate(locations_geographicalunit_106)

    locations_geographicalunit_107 = GeographicalUnit()
    locations_geographicalunit_107.GeographicalUnitId = 'Country_NA'
    locations_geographicalunit_107.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_107.GeographicalUnitName = 'Namibia'
    locations_geographicalunit_107.GeographicalUnitShortName = 'Namibia'
    locations_geographicalunit_107.HierarchyLevel = 30
    locations_geographicalunit_107.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_107 = importer.save_or_locate(locations_geographicalunit_107)

    locations_geographicalunit_108 = GeographicalUnit()
    locations_geographicalunit_108.GeographicalUnitId = 'Country_MM'
    locations_geographicalunit_108.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_108.GeographicalUnitName = 'Myanmar'
    locations_geographicalunit_108.GeographicalUnitShortName = 'Myanmar'
    locations_geographicalunit_108.HierarchyLevel = 30
    locations_geographicalunit_108.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_108 = importer.save_or_locate(locations_geographicalunit_108)

    locations_geographicalunit_109 = GeographicalUnit()
    locations_geographicalunit_109.GeographicalUnitId = 'Country_MZ'
    locations_geographicalunit_109.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_109.GeographicalUnitName = 'Mozambique'
    locations_geographicalunit_109.GeographicalUnitShortName = 'Mozambique'
    locations_geographicalunit_109.HierarchyLevel = 30
    locations_geographicalunit_109.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_109 = importer.save_or_locate(locations_geographicalunit_109)

    locations_geographicalunit_110 = GeographicalUnit()
    locations_geographicalunit_110.GeographicalUnitId = 'Country_MA'
    locations_geographicalunit_110.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_110.GeographicalUnitName = 'Morocco'
    locations_geographicalunit_110.GeographicalUnitShortName = 'Morocco'
    locations_geographicalunit_110.HierarchyLevel = 30
    locations_geographicalunit_110.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_110 = importer.save_or_locate(locations_geographicalunit_110)

    locations_geographicalunit_111 = GeographicalUnit()
    locations_geographicalunit_111.GeographicalUnitId = 'Country_MS'
    locations_geographicalunit_111.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_111.GeographicalUnitName = 'Montserrat'
    locations_geographicalunit_111.GeographicalUnitShortName = 'Montserrat'
    locations_geographicalunit_111.HierarchyLevel = 30
    locations_geographicalunit_111.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_111 = importer.save_or_locate(locations_geographicalunit_111)

    locations_geographicalunit_112 = GeographicalUnit()
    locations_geographicalunit_112.GeographicalUnitId = 'Country_ME'
    locations_geographicalunit_112.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_112.GeographicalUnitName = 'Montenegro'
    locations_geographicalunit_112.GeographicalUnitShortName = 'Montenegro'
    locations_geographicalunit_112.HierarchyLevel = 30
    locations_geographicalunit_112.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_112 = importer.save_or_locate(locations_geographicalunit_112)

    locations_geographicalunit_113 = GeographicalUnit()
    locations_geographicalunit_113.GeographicalUnitId = 'Country_MN'
    locations_geographicalunit_113.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_113.GeographicalUnitName = 'Mongolia'
    locations_geographicalunit_113.GeographicalUnitShortName = 'Mongolia'
    locations_geographicalunit_113.HierarchyLevel = 30
    locations_geographicalunit_113.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_113 = importer.save_or_locate(locations_geographicalunit_113)

    locations_geographicalunit_114 = GeographicalUnit()
    locations_geographicalunit_114.GeographicalUnitId = 'Country_MC'
    locations_geographicalunit_114.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_114.GeographicalUnitName = 'Monaco'
    locations_geographicalunit_114.GeographicalUnitShortName = 'Monaco'
    locations_geographicalunit_114.HierarchyLevel = 30
    locations_geographicalunit_114.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_114 = importer.save_or_locate(locations_geographicalunit_114)

    locations_geographicalunit_115 = GeographicalUnit()
    locations_geographicalunit_115.GeographicalUnitId = 'Country_MD'
    locations_geographicalunit_115.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_115.GeographicalUnitName = 'Moldova (the Republic of)'
    locations_geographicalunit_115.GeographicalUnitShortName = 'Moldova'
    locations_geographicalunit_115.HierarchyLevel = 30
    locations_geographicalunit_115.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_115 = importer.save_or_locate(locations_geographicalunit_115)

    locations_geographicalunit_116 = GeographicalUnit()
    locations_geographicalunit_116.GeographicalUnitId = 'Country_FM'
    locations_geographicalunit_116.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_116.GeographicalUnitName = 'Micronesia (Federated States of)'
    locations_geographicalunit_116.GeographicalUnitShortName = 'Micronesia'
    locations_geographicalunit_116.HierarchyLevel = 30
    locations_geographicalunit_116.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_116 = importer.save_or_locate(locations_geographicalunit_116)

    locations_geographicalunit_117 = GeographicalUnit()
    locations_geographicalunit_117.GeographicalUnitId = 'Country_MX'
    locations_geographicalunit_117.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_117.GeographicalUnitName = 'Mexico'
    locations_geographicalunit_117.GeographicalUnitShortName = 'Mexico'
    locations_geographicalunit_117.HierarchyLevel = 30
    locations_geographicalunit_117.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_117 = importer.save_or_locate(locations_geographicalunit_117)

    locations_geographicalunit_118 = GeographicalUnit()
    locations_geographicalunit_118.GeographicalUnitId = 'Country_YT'
    locations_geographicalunit_118.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_118.GeographicalUnitName = 'Mayotte'
    locations_geographicalunit_118.GeographicalUnitShortName = 'Mayotte'
    locations_geographicalunit_118.HierarchyLevel = 30
    locations_geographicalunit_118.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_118 = importer.save_or_locate(locations_geographicalunit_118)

    locations_geographicalunit_119 = GeographicalUnit()
    locations_geographicalunit_119.GeographicalUnitId = 'Country_MU'
    locations_geographicalunit_119.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_119.GeographicalUnitName = 'Mauritius'
    locations_geographicalunit_119.GeographicalUnitShortName = 'Mauritius'
    locations_geographicalunit_119.HierarchyLevel = 30
    locations_geographicalunit_119.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_119 = importer.save_or_locate(locations_geographicalunit_119)

    locations_geographicalunit_120 = GeographicalUnit()
    locations_geographicalunit_120.GeographicalUnitId = 'Country_MR'
    locations_geographicalunit_120.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_120.GeographicalUnitName = 'Mauritania'
    locations_geographicalunit_120.GeographicalUnitShortName = 'Mauritania'
    locations_geographicalunit_120.HierarchyLevel = 30
    locations_geographicalunit_120.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_120 = importer.save_or_locate(locations_geographicalunit_120)

    locations_geographicalunit_121 = GeographicalUnit()
    locations_geographicalunit_121.GeographicalUnitId = 'Country_MQ'
    locations_geographicalunit_121.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_121.GeographicalUnitName = 'Martinique'
    locations_geographicalunit_121.GeographicalUnitShortName = 'Martinique'
    locations_geographicalunit_121.HierarchyLevel = 30
    locations_geographicalunit_121.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_121 = importer.save_or_locate(locations_geographicalunit_121)

    locations_geographicalunit_122 = GeographicalUnit()
    locations_geographicalunit_122.GeographicalUnitId = 'Country_MH'
    locations_geographicalunit_122.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_122.GeographicalUnitName = 'Marshall Islands (the)'
    locations_geographicalunit_122.GeographicalUnitShortName = 'Marshall Islands'
    locations_geographicalunit_122.HierarchyLevel = 30
    locations_geographicalunit_122.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_122 = importer.save_or_locate(locations_geographicalunit_122)

    locations_geographicalunit_123 = GeographicalUnit()
    locations_geographicalunit_123.GeographicalUnitId = 'Country_MT'
    locations_geographicalunit_123.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_123.GeographicalUnitName = 'Malta'
    locations_geographicalunit_123.GeographicalUnitShortName = 'Malta'
    locations_geographicalunit_123.HierarchyLevel = 30
    locations_geographicalunit_123.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_123 = importer.save_or_locate(locations_geographicalunit_123)

    locations_geographicalunit_124 = GeographicalUnit()
    locations_geographicalunit_124.GeographicalUnitId = 'Country_ML'
    locations_geographicalunit_124.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_124.GeographicalUnitName = 'Mali'
    locations_geographicalunit_124.GeographicalUnitShortName = 'Mali'
    locations_geographicalunit_124.HierarchyLevel = 30
    locations_geographicalunit_124.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_124 = importer.save_or_locate(locations_geographicalunit_124)

    locations_geographicalunit_125 = GeographicalUnit()
    locations_geographicalunit_125.GeographicalUnitId = 'Country_MV'
    locations_geographicalunit_125.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_125.GeographicalUnitName = 'Maldives'
    locations_geographicalunit_125.GeographicalUnitShortName = 'Maldives'
    locations_geographicalunit_125.HierarchyLevel = 30
    locations_geographicalunit_125.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_125 = importer.save_or_locate(locations_geographicalunit_125)

    locations_geographicalunit_126 = GeographicalUnit()
    locations_geographicalunit_126.GeographicalUnitId = 'Country_MY'
    locations_geographicalunit_126.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_126.GeographicalUnitName = 'Malaysia'
    locations_geographicalunit_126.GeographicalUnitShortName = 'Malaysia'
    locations_geographicalunit_126.HierarchyLevel = 30
    locations_geographicalunit_126.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_126 = importer.save_or_locate(locations_geographicalunit_126)

    locations_geographicalunit_127 = GeographicalUnit()
    locations_geographicalunit_127.GeographicalUnitId = 'Country_MW'
    locations_geographicalunit_127.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_127.GeographicalUnitName = 'Malawi'
    locations_geographicalunit_127.GeographicalUnitShortName = 'Malawi'
    locations_geographicalunit_127.HierarchyLevel = 30
    locations_geographicalunit_127.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_127 = importer.save_or_locate(locations_geographicalunit_127)

    locations_geographicalunit_128 = GeographicalUnit()
    locations_geographicalunit_128.GeographicalUnitId = 'Country_MG'
    locations_geographicalunit_128.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_128.GeographicalUnitName = 'Madagascar'
    locations_geographicalunit_128.GeographicalUnitShortName = 'Madagascar'
    locations_geographicalunit_128.HierarchyLevel = 30
    locations_geographicalunit_128.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_128 = importer.save_or_locate(locations_geographicalunit_128)

    locations_geographicalunit_129 = GeographicalUnit()
    locations_geographicalunit_129.GeographicalUnitId = 'Country_MO'
    locations_geographicalunit_129.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_129.GeographicalUnitName = 'Macao'
    locations_geographicalunit_129.GeographicalUnitShortName = 'Macao'
    locations_geographicalunit_129.HierarchyLevel = 30
    locations_geographicalunit_129.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_129 = importer.save_or_locate(locations_geographicalunit_129)

    locations_geographicalunit_130 = GeographicalUnit()
    locations_geographicalunit_130.GeographicalUnitId = 'Country_LU'
    locations_geographicalunit_130.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_130.GeographicalUnitName = 'Luxembourg'
    locations_geographicalunit_130.GeographicalUnitShortName = 'Luxembourg'
    locations_geographicalunit_130.HierarchyLevel = 30
    locations_geographicalunit_130.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_130 = importer.save_or_locate(locations_geographicalunit_130)

    locations_geographicalunit_131 = GeographicalUnit()
    locations_geographicalunit_131.GeographicalUnitId = 'Country_LT'
    locations_geographicalunit_131.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_131.GeographicalUnitName = 'Lithuania'
    locations_geographicalunit_131.GeographicalUnitShortName = 'Lithuania'
    locations_geographicalunit_131.HierarchyLevel = 30
    locations_geographicalunit_131.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_131 = importer.save_or_locate(locations_geographicalunit_131)

    locations_geographicalunit_132 = GeographicalUnit()
    locations_geographicalunit_132.GeographicalUnitId = 'Country_LI'
    locations_geographicalunit_132.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_132.GeographicalUnitName = 'Liechtenstein'
    locations_geographicalunit_132.GeographicalUnitShortName = 'Liechtenstein'
    locations_geographicalunit_132.HierarchyLevel = 30
    locations_geographicalunit_132.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_132 = importer.save_or_locate(locations_geographicalunit_132)

    locations_geographicalunit_133 = GeographicalUnit()
    locations_geographicalunit_133.GeographicalUnitId = 'Country_LY'
    locations_geographicalunit_133.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_133.GeographicalUnitName = 'Libya'
    locations_geographicalunit_133.GeographicalUnitShortName = 'Libya'
    locations_geographicalunit_133.HierarchyLevel = 30
    locations_geographicalunit_133.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_133 = importer.save_or_locate(locations_geographicalunit_133)

    locations_geographicalunit_134 = GeographicalUnit()
    locations_geographicalunit_134.GeographicalUnitId = 'Country_LR'
    locations_geographicalunit_134.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_134.GeographicalUnitName = 'Liberia'
    locations_geographicalunit_134.GeographicalUnitShortName = 'Liberia'
    locations_geographicalunit_134.HierarchyLevel = 30
    locations_geographicalunit_134.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_134 = importer.save_or_locate(locations_geographicalunit_134)

    locations_geographicalunit_135 = GeographicalUnit()
    locations_geographicalunit_135.GeographicalUnitId = 'Country_LS'
    locations_geographicalunit_135.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_135.GeographicalUnitName = 'Lesotho'
    locations_geographicalunit_135.GeographicalUnitShortName = 'Lesotho'
    locations_geographicalunit_135.HierarchyLevel = 30
    locations_geographicalunit_135.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_135 = importer.save_or_locate(locations_geographicalunit_135)

    locations_geographicalunit_136 = GeographicalUnit()
    locations_geographicalunit_136.GeographicalUnitId = 'Country_LB'
    locations_geographicalunit_136.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_136.GeographicalUnitName = 'Lebanon'
    locations_geographicalunit_136.GeographicalUnitShortName = 'Lebanon'
    locations_geographicalunit_136.HierarchyLevel = 30
    locations_geographicalunit_136.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_136 = importer.save_or_locate(locations_geographicalunit_136)

    locations_geographicalunit_137 = GeographicalUnit()
    locations_geographicalunit_137.GeographicalUnitId = 'Country_LV'
    locations_geographicalunit_137.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_137.GeographicalUnitName = 'Latvia'
    locations_geographicalunit_137.GeographicalUnitShortName = 'Latvia'
    locations_geographicalunit_137.HierarchyLevel = 30
    locations_geographicalunit_137.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_137 = importer.save_or_locate(locations_geographicalunit_137)

    locations_geographicalunit_138 = GeographicalUnit()
    locations_geographicalunit_138.GeographicalUnitId = 'Country_LA'
    locations_geographicalunit_138.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_138.GeographicalUnitName = "Lao People's Democratic Republic (the)"
    locations_geographicalunit_138.GeographicalUnitShortName = 'Lao'
    locations_geographicalunit_138.HierarchyLevel = 30
    locations_geographicalunit_138.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_138 = importer.save_or_locate(locations_geographicalunit_138)

    locations_geographicalunit_139 = GeographicalUnit()
    locations_geographicalunit_139.GeographicalUnitId = 'Country_KG'
    locations_geographicalunit_139.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_139.GeographicalUnitName = 'Kyrgyzstan'
    locations_geographicalunit_139.GeographicalUnitShortName = 'Kyrgyzstan'
    locations_geographicalunit_139.HierarchyLevel = 30
    locations_geographicalunit_139.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_139 = importer.save_or_locate(locations_geographicalunit_139)

    locations_geographicalunit_140 = GeographicalUnit()
    locations_geographicalunit_140.GeographicalUnitId = 'Country_KW'
    locations_geographicalunit_140.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_140.GeographicalUnitName = 'Kuwait'
    locations_geographicalunit_140.GeographicalUnitShortName = 'Kuwait'
    locations_geographicalunit_140.HierarchyLevel = 30
    locations_geographicalunit_140.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_140 = importer.save_or_locate(locations_geographicalunit_140)

    locations_geographicalunit_141 = GeographicalUnit()
    locations_geographicalunit_141.GeographicalUnitId = 'Country_KR'
    locations_geographicalunit_141.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_141.GeographicalUnitName = 'Korea (the Republic of)'
    locations_geographicalunit_141.GeographicalUnitShortName = 'South Korea'
    locations_geographicalunit_141.HierarchyLevel = 30
    locations_geographicalunit_141.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_141 = importer.save_or_locate(locations_geographicalunit_141)

    locations_geographicalunit_142 = GeographicalUnit()
    locations_geographicalunit_142.GeographicalUnitId = 'Country_KP'
    locations_geographicalunit_142.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_142.GeographicalUnitName = "Korea (the Democratic People's Republic of)"
    locations_geographicalunit_142.GeographicalUnitShortName = 'North Korea'
    locations_geographicalunit_142.HierarchyLevel = 30
    locations_geographicalunit_142.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_142 = importer.save_or_locate(locations_geographicalunit_142)

    locations_geographicalunit_143 = GeographicalUnit()
    locations_geographicalunit_143.GeographicalUnitId = 'Country_KI'
    locations_geographicalunit_143.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_143.GeographicalUnitName = 'Kiribati'
    locations_geographicalunit_143.GeographicalUnitShortName = 'Kiribati'
    locations_geographicalunit_143.HierarchyLevel = 30
    locations_geographicalunit_143.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_143 = importer.save_or_locate(locations_geographicalunit_143)

    locations_geographicalunit_144 = GeographicalUnit()
    locations_geographicalunit_144.GeographicalUnitId = 'Country_KE'
    locations_geographicalunit_144.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_144.GeographicalUnitName = 'Kenya'
    locations_geographicalunit_144.GeographicalUnitShortName = 'Kenya'
    locations_geographicalunit_144.HierarchyLevel = 30
    locations_geographicalunit_144.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_144 = importer.save_or_locate(locations_geographicalunit_144)

    locations_geographicalunit_145 = GeographicalUnit()
    locations_geographicalunit_145.GeographicalUnitId = 'Country_KZ'
    locations_geographicalunit_145.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_145.GeographicalUnitName = 'Kazakhstan'
    locations_geographicalunit_145.GeographicalUnitShortName = 'Kazakhstan'
    locations_geographicalunit_145.HierarchyLevel = 30
    locations_geographicalunit_145.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_145 = importer.save_or_locate(locations_geographicalunit_145)

    locations_geographicalunit_146 = GeographicalUnit()
    locations_geographicalunit_146.GeographicalUnitId = 'Country_JO'
    locations_geographicalunit_146.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_146.GeographicalUnitName = 'Jordan'
    locations_geographicalunit_146.GeographicalUnitShortName = 'Jordan'
    locations_geographicalunit_146.HierarchyLevel = 30
    locations_geographicalunit_146.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_146 = importer.save_or_locate(locations_geographicalunit_146)

    locations_geographicalunit_147 = GeographicalUnit()
    locations_geographicalunit_147.GeographicalUnitId = 'Country_JE'
    locations_geographicalunit_147.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_147.GeographicalUnitName = 'Jersey'
    locations_geographicalunit_147.GeographicalUnitShortName = 'Jersey'
    locations_geographicalunit_147.HierarchyLevel = 30
    locations_geographicalunit_147.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_147 = importer.save_or_locate(locations_geographicalunit_147)

    locations_geographicalunit_148 = GeographicalUnit()
    locations_geographicalunit_148.GeographicalUnitId = 'Country_JP'
    locations_geographicalunit_148.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_148.GeographicalUnitName = 'Japan'
    locations_geographicalunit_148.GeographicalUnitShortName = 'Japan'
    locations_geographicalunit_148.HierarchyLevel = 30
    locations_geographicalunit_148.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_148 = importer.save_or_locate(locations_geographicalunit_148)

    locations_geographicalunit_149 = GeographicalUnit()
    locations_geographicalunit_149.GeographicalUnitId = 'Country_JM'
    locations_geographicalunit_149.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_149.GeographicalUnitName = 'Jamaica'
    locations_geographicalunit_149.GeographicalUnitShortName = 'Jamaica'
    locations_geographicalunit_149.HierarchyLevel = 30
    locations_geographicalunit_149.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_149 = importer.save_or_locate(locations_geographicalunit_149)

    locations_geographicalunit_150 = GeographicalUnit()
    locations_geographicalunit_150.GeographicalUnitId = 'Country_IT'
    locations_geographicalunit_150.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_150.GeographicalUnitName = 'Italy'
    locations_geographicalunit_150.GeographicalUnitShortName = 'Italy'
    locations_geographicalunit_150.HierarchyLevel = 30
    locations_geographicalunit_150.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_150 = importer.save_or_locate(locations_geographicalunit_150)

    locations_geographicalunit_151 = GeographicalUnit()
    locations_geographicalunit_151.GeographicalUnitId = 'Country_IL'
    locations_geographicalunit_151.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_151.GeographicalUnitName = 'Israel'
    locations_geographicalunit_151.GeographicalUnitShortName = 'Israel'
    locations_geographicalunit_151.HierarchyLevel = 30
    locations_geographicalunit_151.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_151 = importer.save_or_locate(locations_geographicalunit_151)

    locations_geographicalunit_152 = GeographicalUnit()
    locations_geographicalunit_152.GeographicalUnitId = 'Country_IM'
    locations_geographicalunit_152.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_152.GeographicalUnitName = 'Isle of Man'
    locations_geographicalunit_152.GeographicalUnitShortName = 'Isle of Man'
    locations_geographicalunit_152.HierarchyLevel = 30
    locations_geographicalunit_152.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_152 = importer.save_or_locate(locations_geographicalunit_152)

    locations_geographicalunit_153 = GeographicalUnit()
    locations_geographicalunit_153.GeographicalUnitId = 'Country_IE'
    locations_geographicalunit_153.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_153.GeographicalUnitName = 'Ireland'
    locations_geographicalunit_153.GeographicalUnitShortName = 'Ireland'
    locations_geographicalunit_153.HierarchyLevel = 30
    locations_geographicalunit_153.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_153 = importer.save_or_locate(locations_geographicalunit_153)

    locations_geographicalunit_154 = GeographicalUnit()
    locations_geographicalunit_154.GeographicalUnitId = 'Country_IQ'
    locations_geographicalunit_154.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_154.GeographicalUnitName = 'Iraq'
    locations_geographicalunit_154.GeographicalUnitShortName = 'Iraq'
    locations_geographicalunit_154.HierarchyLevel = 30
    locations_geographicalunit_154.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_154 = importer.save_or_locate(locations_geographicalunit_154)

    locations_geographicalunit_155 = GeographicalUnit()
    locations_geographicalunit_155.GeographicalUnitId = 'Country_IR'
    locations_geographicalunit_155.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_155.GeographicalUnitName = 'Iran (Islamic Republic of)'
    locations_geographicalunit_155.GeographicalUnitShortName = 'Iran (Islamic Republic of)'
    locations_geographicalunit_155.HierarchyLevel = 30
    locations_geographicalunit_155.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_155 = importer.save_or_locate(locations_geographicalunit_155)

    locations_geographicalunit_156 = GeographicalUnit()
    locations_geographicalunit_156.GeographicalUnitId = 'Country_ID'
    locations_geographicalunit_156.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_156.GeographicalUnitName = 'Indonesia'
    locations_geographicalunit_156.GeographicalUnitShortName = 'Indonesia'
    locations_geographicalunit_156.HierarchyLevel = 30
    locations_geographicalunit_156.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_156 = importer.save_or_locate(locations_geographicalunit_156)

    locations_geographicalunit_157 = GeographicalUnit()
    locations_geographicalunit_157.GeographicalUnitId = 'Country_IN'
    locations_geographicalunit_157.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_157.GeographicalUnitName = 'India'
    locations_geographicalunit_157.GeographicalUnitShortName = 'India'
    locations_geographicalunit_157.HierarchyLevel = 30
    locations_geographicalunit_157.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_157 = importer.save_or_locate(locations_geographicalunit_157)

    locations_geographicalunit_158 = GeographicalUnit()
    locations_geographicalunit_158.GeographicalUnitId = 'Country_IS'
    locations_geographicalunit_158.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_158.GeographicalUnitName = 'Iceland'
    locations_geographicalunit_158.GeographicalUnitShortName = 'Iceland'
    locations_geographicalunit_158.HierarchyLevel = 30
    locations_geographicalunit_158.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_158 = importer.save_or_locate(locations_geographicalunit_158)

    locations_geographicalunit_159 = GeographicalUnit()
    locations_geographicalunit_159.GeographicalUnitId = 'Country_HU'
    locations_geographicalunit_159.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_159.GeographicalUnitName = 'Hungary'
    locations_geographicalunit_159.GeographicalUnitShortName = 'Hungary'
    locations_geographicalunit_159.HierarchyLevel = 30
    locations_geographicalunit_159.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_159 = importer.save_or_locate(locations_geographicalunit_159)

    locations_geographicalunit_160 = GeographicalUnit()
    locations_geographicalunit_160.GeographicalUnitId = 'Country_HK'
    locations_geographicalunit_160.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_160.GeographicalUnitName = 'Hong Kong'
    locations_geographicalunit_160.GeographicalUnitShortName = 'Hong Kong'
    locations_geographicalunit_160.HierarchyLevel = 30
    locations_geographicalunit_160.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_160 = importer.save_or_locate(locations_geographicalunit_160)

    locations_geographicalunit_161 = GeographicalUnit()
    locations_geographicalunit_161.GeographicalUnitId = 'Country_HN'
    locations_geographicalunit_161.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_161.GeographicalUnitName = 'Honduras'
    locations_geographicalunit_161.GeographicalUnitShortName = 'Honduras'
    locations_geographicalunit_161.HierarchyLevel = 30
    locations_geographicalunit_161.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_161 = importer.save_or_locate(locations_geographicalunit_161)

    locations_geographicalunit_162 = GeographicalUnit()
    locations_geographicalunit_162.GeographicalUnitId = 'Country_VA'
    locations_geographicalunit_162.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_162.GeographicalUnitName = 'Holy See (the)'
    locations_geographicalunit_162.GeographicalUnitShortName = 'Holy See (the)'
    locations_geographicalunit_162.HierarchyLevel = 30
    locations_geographicalunit_162.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_162 = importer.save_or_locate(locations_geographicalunit_162)

    locations_geographicalunit_163 = GeographicalUnit()
    locations_geographicalunit_163.GeographicalUnitId = 'Country_HM'
    locations_geographicalunit_163.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_163.GeographicalUnitName = 'Heard Island and McDonald Islands'
    locations_geographicalunit_163.GeographicalUnitShortName = 'Heard Island and McDonald Islands'
    locations_geographicalunit_163.HierarchyLevel = 30
    locations_geographicalunit_163.IsPartOf = locations_geographicalunit_4
    locations_geographicalunit_163 = importer.save_or_locate(locations_geographicalunit_163)

    locations_geographicalunit_164 = GeographicalUnit()
    locations_geographicalunit_164.GeographicalUnitId = 'Country_HT'
    locations_geographicalunit_164.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_164.GeographicalUnitName = 'Haiti'
    locations_geographicalunit_164.GeographicalUnitShortName = 'Haiti'
    locations_geographicalunit_164.HierarchyLevel = 30
    locations_geographicalunit_164.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_164 = importer.save_or_locate(locations_geographicalunit_164)

    locations_geographicalunit_165 = GeographicalUnit()
    locations_geographicalunit_165.GeographicalUnitId = 'Country_GY'
    locations_geographicalunit_165.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_165.GeographicalUnitName = 'Guyana'
    locations_geographicalunit_165.GeographicalUnitShortName = 'Guyana'
    locations_geographicalunit_165.HierarchyLevel = 30
    locations_geographicalunit_165.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_165 = importer.save_or_locate(locations_geographicalunit_165)

    locations_geographicalunit_166 = GeographicalUnit()
    locations_geographicalunit_166.GeographicalUnitId = 'Country_GW'
    locations_geographicalunit_166.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_166.GeographicalUnitName = 'Guinea-Bissau'
    locations_geographicalunit_166.GeographicalUnitShortName = 'Guinea-Bissau'
    locations_geographicalunit_166.HierarchyLevel = 30
    locations_geographicalunit_166.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_166 = importer.save_or_locate(locations_geographicalunit_166)

    locations_geographicalunit_167 = GeographicalUnit()
    locations_geographicalunit_167.GeographicalUnitId = 'Country_GN'
    locations_geographicalunit_167.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_167.GeographicalUnitName = 'Guinea'
    locations_geographicalunit_167.GeographicalUnitShortName = 'Guinea'
    locations_geographicalunit_167.HierarchyLevel = 30
    locations_geographicalunit_167.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_167 = importer.save_or_locate(locations_geographicalunit_167)

    locations_geographicalunit_168 = GeographicalUnit()
    locations_geographicalunit_168.GeographicalUnitId = 'Country_GG'
    locations_geographicalunit_168.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_168.GeographicalUnitName = 'Guernsey'
    locations_geographicalunit_168.GeographicalUnitShortName = 'Guernsey'
    locations_geographicalunit_168.HierarchyLevel = 30
    locations_geographicalunit_168.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_168 = importer.save_or_locate(locations_geographicalunit_168)

    locations_geographicalunit_169 = GeographicalUnit()
    locations_geographicalunit_169.GeographicalUnitId = 'Country_GT'
    locations_geographicalunit_169.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_169.GeographicalUnitName = 'Guatemala'
    locations_geographicalunit_169.GeographicalUnitShortName = 'Guatemala'
    locations_geographicalunit_169.HierarchyLevel = 30
    locations_geographicalunit_169.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_169 = importer.save_or_locate(locations_geographicalunit_169)

    locations_geographicalunit_170 = GeographicalUnit()
    locations_geographicalunit_170.GeographicalUnitId = 'Country_GU'
    locations_geographicalunit_170.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_170.GeographicalUnitName = 'Guam'
    locations_geographicalunit_170.GeographicalUnitShortName = 'Guam'
    locations_geographicalunit_170.HierarchyLevel = 30
    locations_geographicalunit_170.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_170 = importer.save_or_locate(locations_geographicalunit_170)

    locations_geographicalunit_171 = GeographicalUnit()
    locations_geographicalunit_171.GeographicalUnitId = 'Country_GP'
    locations_geographicalunit_171.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_171.GeographicalUnitName = 'Guadeloupe'
    locations_geographicalunit_171.GeographicalUnitShortName = 'Guadeloupe'
    locations_geographicalunit_171.HierarchyLevel = 30
    locations_geographicalunit_171.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_171 = importer.save_or_locate(locations_geographicalunit_171)

    locations_geographicalunit_172 = GeographicalUnit()
    locations_geographicalunit_172.GeographicalUnitId = 'Country_GD'
    locations_geographicalunit_172.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_172.GeographicalUnitName = 'Grenada'
    locations_geographicalunit_172.GeographicalUnitShortName = 'Grenada'
    locations_geographicalunit_172.HierarchyLevel = 30
    locations_geographicalunit_172.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_172 = importer.save_or_locate(locations_geographicalunit_172)

    locations_geographicalunit_173 = GeographicalUnit()
    locations_geographicalunit_173.GeographicalUnitId = 'Country_GL'
    locations_geographicalunit_173.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_173.GeographicalUnitName = 'Greenland'
    locations_geographicalunit_173.GeographicalUnitShortName = 'Greenland'
    locations_geographicalunit_173.HierarchyLevel = 30
    locations_geographicalunit_173.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_173 = importer.save_or_locate(locations_geographicalunit_173)

    locations_geographicalunit_174 = GeographicalUnit()
    locations_geographicalunit_174.GeographicalUnitId = 'Country_GR'
    locations_geographicalunit_174.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_174.GeographicalUnitName = 'Greece'
    locations_geographicalunit_174.GeographicalUnitShortName = 'Greece'
    locations_geographicalunit_174.HierarchyLevel = 30
    locations_geographicalunit_174.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_174 = importer.save_or_locate(locations_geographicalunit_174)

    locations_geographicalunit_175 = GeographicalUnit()
    locations_geographicalunit_175.GeographicalUnitId = 'Country_GI'
    locations_geographicalunit_175.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_175.GeographicalUnitName = 'Gibraltar'
    locations_geographicalunit_175.GeographicalUnitShortName = 'Gibraltar'
    locations_geographicalunit_175.HierarchyLevel = 30
    locations_geographicalunit_175.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_175 = importer.save_or_locate(locations_geographicalunit_175)

    locations_geographicalunit_176 = GeographicalUnit()
    locations_geographicalunit_176.GeographicalUnitId = 'Country_GH'
    locations_geographicalunit_176.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_176.GeographicalUnitName = 'Ghana'
    locations_geographicalunit_176.GeographicalUnitShortName = 'Ghana'
    locations_geographicalunit_176.HierarchyLevel = 30
    locations_geographicalunit_176.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_176 = importer.save_or_locate(locations_geographicalunit_176)

    locations_geographicalunit_177 = GeographicalUnit()
    locations_geographicalunit_177.GeographicalUnitId = 'Country_DE'
    locations_geographicalunit_177.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_177.GeographicalUnitName = 'Germany'
    locations_geographicalunit_177.GeographicalUnitShortName = 'Germany'
    locations_geographicalunit_177.HierarchyLevel = 30
    locations_geographicalunit_177.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_177 = importer.save_or_locate(locations_geographicalunit_177)

    locations_geographicalunit_178 = GeographicalUnit()
    locations_geographicalunit_178.GeographicalUnitId = 'Country_GE'
    locations_geographicalunit_178.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_178.GeographicalUnitName = 'Georgia'
    locations_geographicalunit_178.GeographicalUnitShortName = 'Georgia'
    locations_geographicalunit_178.HierarchyLevel = 30
    locations_geographicalunit_178.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_178 = importer.save_or_locate(locations_geographicalunit_178)

    locations_geographicalunit_179 = GeographicalUnit()
    locations_geographicalunit_179.GeographicalUnitId = 'Country_GM'
    locations_geographicalunit_179.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_179.GeographicalUnitName = 'Gambia (the)'
    locations_geographicalunit_179.GeographicalUnitShortName = 'Gambia'
    locations_geographicalunit_179.HierarchyLevel = 30
    locations_geographicalunit_179.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_179 = importer.save_or_locate(locations_geographicalunit_179)

    locations_geographicalunit_180 = GeographicalUnit()
    locations_geographicalunit_180.GeographicalUnitId = 'Country_GA'
    locations_geographicalunit_180.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_180.GeographicalUnitName = 'Gabon'
    locations_geographicalunit_180.GeographicalUnitShortName = 'Gabon'
    locations_geographicalunit_180.HierarchyLevel = 30
    locations_geographicalunit_180.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_180 = importer.save_or_locate(locations_geographicalunit_180)

    locations_geographicalunit_181 = GeographicalUnit()
    locations_geographicalunit_181.GeographicalUnitId = 'Country_TF'
    locations_geographicalunit_181.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_181.GeographicalUnitName = 'French Southern Territories (the)'
    locations_geographicalunit_181.GeographicalUnitShortName = 'French Southern Territories'
    locations_geographicalunit_181.HierarchyLevel = 30
    locations_geographicalunit_181.IsPartOf = locations_geographicalunit_4
    locations_geographicalunit_181 = importer.save_or_locate(locations_geographicalunit_181)

    locations_geographicalunit_182 = GeographicalUnit()
    locations_geographicalunit_182.GeographicalUnitId = 'Country_PF'
    locations_geographicalunit_182.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_182.GeographicalUnitName = 'French Polynesia'
    locations_geographicalunit_182.GeographicalUnitShortName = 'French Polynesia'
    locations_geographicalunit_182.HierarchyLevel = 30
    locations_geographicalunit_182.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_182 = importer.save_or_locate(locations_geographicalunit_182)

    locations_geographicalunit_183 = GeographicalUnit()
    locations_geographicalunit_183.GeographicalUnitId = 'Country_GF'
    locations_geographicalunit_183.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_183.GeographicalUnitName = 'French Guiana'
    locations_geographicalunit_183.GeographicalUnitShortName = 'French Guiana'
    locations_geographicalunit_183.HierarchyLevel = 30
    locations_geographicalunit_183.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_183 = importer.save_or_locate(locations_geographicalunit_183)

    locations_geographicalunit_184 = GeographicalUnit()
    locations_geographicalunit_184.GeographicalUnitId = 'Country_FI'
    locations_geographicalunit_184.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_184.GeographicalUnitName = 'Finland'
    locations_geographicalunit_184.GeographicalUnitShortName = 'Finland'
    locations_geographicalunit_184.HierarchyLevel = 30
    locations_geographicalunit_184.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_184 = importer.save_or_locate(locations_geographicalunit_184)

    locations_geographicalunit_185 = GeographicalUnit()
    locations_geographicalunit_185.GeographicalUnitId = 'Country_FJ'
    locations_geographicalunit_185.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_185.GeographicalUnitName = 'Fiji'
    locations_geographicalunit_185.GeographicalUnitShortName = 'Fiji'
    locations_geographicalunit_185.HierarchyLevel = 30
    locations_geographicalunit_185.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_185 = importer.save_or_locate(locations_geographicalunit_185)

    locations_geographicalunit_186 = GeographicalUnit()
    locations_geographicalunit_186.GeographicalUnitId = 'Country_FO'
    locations_geographicalunit_186.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_186.GeographicalUnitName = 'Faroe Islands (the)'
    locations_geographicalunit_186.GeographicalUnitShortName = 'Faroe Islands'
    locations_geographicalunit_186.HierarchyLevel = 30
    locations_geographicalunit_186.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_186 = importer.save_or_locate(locations_geographicalunit_186)

    locations_geographicalunit_187 = GeographicalUnit()
    locations_geographicalunit_187.GeographicalUnitId = 'Country_FK'
    locations_geographicalunit_187.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_187.GeographicalUnitName = 'Falkland Islands (the) [Malvinas]'
    locations_geographicalunit_187.GeographicalUnitShortName = 'Falkland Islands'
    locations_geographicalunit_187.HierarchyLevel = 30
    locations_geographicalunit_187.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_187 = importer.save_or_locate(locations_geographicalunit_187)

    locations_geographicalunit_188 = GeographicalUnit()
    locations_geographicalunit_188.GeographicalUnitId = 'Country_ET'
    locations_geographicalunit_188.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_188.GeographicalUnitName = 'Ethiopia'
    locations_geographicalunit_188.GeographicalUnitShortName = 'Ethiopia'
    locations_geographicalunit_188.HierarchyLevel = 30
    locations_geographicalunit_188.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_188 = importer.save_or_locate(locations_geographicalunit_188)

    locations_geographicalunit_189 = GeographicalUnit()
    locations_geographicalunit_189.GeographicalUnitId = 'Country_SZ'
    locations_geographicalunit_189.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_189.GeographicalUnitName = 'Eswatini'
    locations_geographicalunit_189.GeographicalUnitShortName = 'Eswatini'
    locations_geographicalunit_189.HierarchyLevel = 30
    locations_geographicalunit_189.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_189 = importer.save_or_locate(locations_geographicalunit_189)

    locations_geographicalunit_190 = GeographicalUnit()
    locations_geographicalunit_190.GeographicalUnitId = 'Country_EE'
    locations_geographicalunit_190.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_190.GeographicalUnitName = 'Estonia'
    locations_geographicalunit_190.GeographicalUnitShortName = 'Estonia'
    locations_geographicalunit_190.HierarchyLevel = 30
    locations_geographicalunit_190.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_190 = importer.save_or_locate(locations_geographicalunit_190)

    locations_geographicalunit_191 = GeographicalUnit()
    locations_geographicalunit_191.GeographicalUnitId = 'Country_ER'
    locations_geographicalunit_191.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_191.GeographicalUnitName = 'Eritrea'
    locations_geographicalunit_191.GeographicalUnitShortName = 'Eritrea'
    locations_geographicalunit_191.HierarchyLevel = 30
    locations_geographicalunit_191.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_191 = importer.save_or_locate(locations_geographicalunit_191)

    locations_geographicalunit_192 = GeographicalUnit()
    locations_geographicalunit_192.GeographicalUnitId = 'Country_GQ'
    locations_geographicalunit_192.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_192.GeographicalUnitName = 'Equatorial Guinea'
    locations_geographicalunit_192.GeographicalUnitShortName = 'Equatorial Guinea'
    locations_geographicalunit_192.HierarchyLevel = 30
    locations_geographicalunit_192.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_192 = importer.save_or_locate(locations_geographicalunit_192)

    locations_geographicalunit_193 = GeographicalUnit()
    locations_geographicalunit_193.GeographicalUnitId = 'Country_SV'
    locations_geographicalunit_193.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_193.GeographicalUnitName = 'El Salvador'
    locations_geographicalunit_193.GeographicalUnitShortName = 'El Salvador'
    locations_geographicalunit_193.HierarchyLevel = 30
    locations_geographicalunit_193.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_193 = importer.save_or_locate(locations_geographicalunit_193)

    locations_geographicalunit_194 = GeographicalUnit()
    locations_geographicalunit_194.GeographicalUnitId = 'Country_EG'
    locations_geographicalunit_194.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_194.GeographicalUnitName = 'Egypt'
    locations_geographicalunit_194.GeographicalUnitShortName = 'Egypt'
    locations_geographicalunit_194.HierarchyLevel = 30
    locations_geographicalunit_194.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_194 = importer.save_or_locate(locations_geographicalunit_194)

    locations_geographicalunit_195 = GeographicalUnit()
    locations_geographicalunit_195.GeographicalUnitId = 'Country_EC'
    locations_geographicalunit_195.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_195.GeographicalUnitName = 'Ecuador'
    locations_geographicalunit_195.GeographicalUnitShortName = 'Ecuador'
    locations_geographicalunit_195.HierarchyLevel = 30
    locations_geographicalunit_195.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_195 = importer.save_or_locate(locations_geographicalunit_195)

    locations_geographicalunit_196 = GeographicalUnit()
    locations_geographicalunit_196.GeographicalUnitId = 'Country_DO'
    locations_geographicalunit_196.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_196.GeographicalUnitName = 'Dominican Republic (the)'
    locations_geographicalunit_196.GeographicalUnitShortName = 'Dominican Republic'
    locations_geographicalunit_196.HierarchyLevel = 30
    locations_geographicalunit_196.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_196 = importer.save_or_locate(locations_geographicalunit_196)

    locations_geographicalunit_197 = GeographicalUnit()
    locations_geographicalunit_197.GeographicalUnitId = 'Country_DM'
    locations_geographicalunit_197.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_197.GeographicalUnitName = 'Dominica'
    locations_geographicalunit_197.GeographicalUnitShortName = 'Dominica'
    locations_geographicalunit_197.HierarchyLevel = 30
    locations_geographicalunit_197.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_197 = importer.save_or_locate(locations_geographicalunit_197)

    locations_geographicalunit_198 = GeographicalUnit()
    locations_geographicalunit_198.GeographicalUnitId = 'Country_DJ'
    locations_geographicalunit_198.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_198.GeographicalUnitName = 'Djibouti'
    locations_geographicalunit_198.GeographicalUnitShortName = 'Djibouti'
    locations_geographicalunit_198.HierarchyLevel = 30
    locations_geographicalunit_198.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_198 = importer.save_or_locate(locations_geographicalunit_198)

    locations_geographicalunit_199 = GeographicalUnit()
    locations_geographicalunit_199.GeographicalUnitId = 'Country_DK'
    locations_geographicalunit_199.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_199.GeographicalUnitName = 'Denmark'
    locations_geographicalunit_199.GeographicalUnitShortName = 'Denmark'
    locations_geographicalunit_199.HierarchyLevel = 30
    locations_geographicalunit_199.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_199 = importer.save_or_locate(locations_geographicalunit_199)

    locations_geographicalunit_200 = GeographicalUnit()
    locations_geographicalunit_200.GeographicalUnitId = 'Country_CI'
    locations_geographicalunit_200.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_200.GeographicalUnitName = "Côte d'Ivoire"
    locations_geographicalunit_200.GeographicalUnitShortName = "Côte d'Ivoire"
    locations_geographicalunit_200.HierarchyLevel = 30
    locations_geographicalunit_200.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_200 = importer.save_or_locate(locations_geographicalunit_200)

    locations_geographicalunit_201 = GeographicalUnit()
    locations_geographicalunit_201.GeographicalUnitId = 'Country_CZ'
    locations_geographicalunit_201.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_201.GeographicalUnitName = 'Czechia'
    locations_geographicalunit_201.GeographicalUnitShortName = 'Czechia'
    locations_geographicalunit_201.HierarchyLevel = 30
    locations_geographicalunit_201.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_201 = importer.save_or_locate(locations_geographicalunit_201)

    locations_geographicalunit_202 = GeographicalUnit()
    locations_geographicalunit_202.GeographicalUnitId = 'Country_CY'
    locations_geographicalunit_202.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_202.GeographicalUnitName = 'Cyprus'
    locations_geographicalunit_202.GeographicalUnitShortName = 'Cyprus'
    locations_geographicalunit_202.HierarchyLevel = 30
    locations_geographicalunit_202.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_202 = importer.save_or_locate(locations_geographicalunit_202)

    locations_geographicalunit_203 = GeographicalUnit()
    locations_geographicalunit_203.GeographicalUnitId = 'Country_CW'
    locations_geographicalunit_203.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_203.GeographicalUnitName = 'Curacao'
    locations_geographicalunit_203.GeographicalUnitShortName = 'Curacao'
    locations_geographicalunit_203.HierarchyLevel = 30
    locations_geographicalunit_203.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_203 = importer.save_or_locate(locations_geographicalunit_203)

    locations_geographicalunit_204 = GeographicalUnit()
    locations_geographicalunit_204.GeographicalUnitId = 'Country_CU'
    locations_geographicalunit_204.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_204.GeographicalUnitName = 'Cuba'
    locations_geographicalunit_204.GeographicalUnitShortName = 'Cuba'
    locations_geographicalunit_204.HierarchyLevel = 30
    locations_geographicalunit_204.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_204 = importer.save_or_locate(locations_geographicalunit_204)

    locations_geographicalunit_205 = GeographicalUnit()
    locations_geographicalunit_205.GeographicalUnitId = 'Country_HR'
    locations_geographicalunit_205.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_205.GeographicalUnitName = 'Croatia'
    locations_geographicalunit_205.GeographicalUnitShortName = 'Croatia'
    locations_geographicalunit_205.HierarchyLevel = 30
    locations_geographicalunit_205.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_205 = importer.save_or_locate(locations_geographicalunit_205)

    locations_geographicalunit_206 = GeographicalUnit()
    locations_geographicalunit_206.GeographicalUnitId = 'Country_CR'
    locations_geographicalunit_206.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_206.GeographicalUnitName = 'Costa Rica'
    locations_geographicalunit_206.GeographicalUnitShortName = 'Costa Rica'
    locations_geographicalunit_206.HierarchyLevel = 30
    locations_geographicalunit_206.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_206 = importer.save_or_locate(locations_geographicalunit_206)

    locations_geographicalunit_207 = GeographicalUnit()
    locations_geographicalunit_207.GeographicalUnitId = 'Country_CK'
    locations_geographicalunit_207.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_207.GeographicalUnitName = 'Cook Islands (the)'
    locations_geographicalunit_207.GeographicalUnitShortName = 'Cook Islands'
    locations_geographicalunit_207.HierarchyLevel = 30
    locations_geographicalunit_207.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_207 = importer.save_or_locate(locations_geographicalunit_207)

    locations_geographicalunit_208 = GeographicalUnit()
    locations_geographicalunit_208.GeographicalUnitId = 'Country_CG'
    locations_geographicalunit_208.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_208.GeographicalUnitName = 'Congo, Republic of the'
    locations_geographicalunit_208.GeographicalUnitShortName = 'Congo Brazzaville'
    locations_geographicalunit_208.HierarchyLevel = 30
    locations_geographicalunit_208.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_208 = importer.save_or_locate(locations_geographicalunit_208)

    locations_geographicalunit_209 = GeographicalUnit()
    locations_geographicalunit_209.GeographicalUnitId = 'Country_CD'
    locations_geographicalunit_209.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_209.GeographicalUnitName = 'Congo, Democratic Republic of the'
    locations_geographicalunit_209.GeographicalUnitShortName = 'Congo, Democratic Republic of the'
    locations_geographicalunit_209.HierarchyLevel = 30
    locations_geographicalunit_209.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_209 = importer.save_or_locate(locations_geographicalunit_209)

    locations_geographicalunit_210 = GeographicalUnit()
    locations_geographicalunit_210.GeographicalUnitId = 'Country_KM'
    locations_geographicalunit_210.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_210.GeographicalUnitName = 'Comoros (the)'
    locations_geographicalunit_210.GeographicalUnitShortName = 'Comoros '
    locations_geographicalunit_210.HierarchyLevel = 30
    locations_geographicalunit_210.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_210 = importer.save_or_locate(locations_geographicalunit_210)

    locations_geographicalunit_211 = GeographicalUnit()
    locations_geographicalunit_211.GeographicalUnitId = 'Country_CO'
    locations_geographicalunit_211.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_211.GeographicalUnitName = 'Colombia'
    locations_geographicalunit_211.GeographicalUnitShortName = 'Colombia'
    locations_geographicalunit_211.HierarchyLevel = 30
    locations_geographicalunit_211.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_211 = importer.save_or_locate(locations_geographicalunit_211)

    locations_geographicalunit_212 = GeographicalUnit()
    locations_geographicalunit_212.GeographicalUnitId = 'Country_CC'
    locations_geographicalunit_212.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_212.GeographicalUnitName = 'Cocos (Keeling) Islands (the)'
    locations_geographicalunit_212.GeographicalUnitShortName = 'Cocos Islands '
    locations_geographicalunit_212.HierarchyLevel = 30
    locations_geographicalunit_212.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_212 = importer.save_or_locate(locations_geographicalunit_212)

    locations_geographicalunit_213 = GeographicalUnit()
    locations_geographicalunit_213.GeographicalUnitId = 'Country_CX'
    locations_geographicalunit_213.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_213.GeographicalUnitName = 'Christmas Island'
    locations_geographicalunit_213.GeographicalUnitShortName = 'Christmas Island'
    locations_geographicalunit_213.HierarchyLevel = 30
    locations_geographicalunit_213.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_213 = importer.save_or_locate(locations_geographicalunit_213)

    locations_geographicalunit_214 = GeographicalUnit()
    locations_geographicalunit_214.GeographicalUnitId = 'Country_CN'
    locations_geographicalunit_214.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_214.GeographicalUnitName = 'China'
    locations_geographicalunit_214.GeographicalUnitShortName = 'China'
    locations_geographicalunit_214.HierarchyLevel = 30
    locations_geographicalunit_214.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_214 = importer.save_or_locate(locations_geographicalunit_214)

    locations_geographicalunit_215 = GeographicalUnit()
    locations_geographicalunit_215.GeographicalUnitId = 'Country_CL'
    locations_geographicalunit_215.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_215.GeographicalUnitName = 'Chile'
    locations_geographicalunit_215.GeographicalUnitShortName = 'Chile'
    locations_geographicalunit_215.HierarchyLevel = 30
    locations_geographicalunit_215.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_215 = importer.save_or_locate(locations_geographicalunit_215)

    locations_geographicalunit_216 = GeographicalUnit()
    locations_geographicalunit_216.GeographicalUnitId = 'Country_TD'
    locations_geographicalunit_216.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_216.GeographicalUnitName = 'Chad'
    locations_geographicalunit_216.GeographicalUnitShortName = 'Chad'
    locations_geographicalunit_216.HierarchyLevel = 30
    locations_geographicalunit_216.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_216 = importer.save_or_locate(locations_geographicalunit_216)

    locations_geographicalunit_217 = GeographicalUnit()
    locations_geographicalunit_217.GeographicalUnitId = 'Country_CF'
    locations_geographicalunit_217.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_217.GeographicalUnitName = 'Central African Republic (the)'
    locations_geographicalunit_217.GeographicalUnitShortName = 'Central African Republic'
    locations_geographicalunit_217.HierarchyLevel = 30
    locations_geographicalunit_217.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_217 = importer.save_or_locate(locations_geographicalunit_217)

    locations_geographicalunit_218 = GeographicalUnit()
    locations_geographicalunit_218.GeographicalUnitId = 'Country_KY'
    locations_geographicalunit_218.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_218.GeographicalUnitName = 'Cayman Islands (the)'
    locations_geographicalunit_218.GeographicalUnitShortName = 'Cayman Islands'
    locations_geographicalunit_218.HierarchyLevel = 30
    locations_geographicalunit_218.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_218 = importer.save_or_locate(locations_geographicalunit_218)

    locations_geographicalunit_219 = GeographicalUnit()
    locations_geographicalunit_219.GeographicalUnitId = 'Country_CA'
    locations_geographicalunit_219.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_219.GeographicalUnitName = 'Canada'
    locations_geographicalunit_219.GeographicalUnitShortName = 'Canada'
    locations_geographicalunit_219.HierarchyLevel = 30
    locations_geographicalunit_219.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_219 = importer.save_or_locate(locations_geographicalunit_219)

    locations_geographicalunit_220 = GeographicalUnit()
    locations_geographicalunit_220.GeographicalUnitId = 'Country_CM'
    locations_geographicalunit_220.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_220.GeographicalUnitName = 'Cameroon'
    locations_geographicalunit_220.GeographicalUnitShortName = 'Cameroon'
    locations_geographicalunit_220.HierarchyLevel = 30
    locations_geographicalunit_220.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_220 = importer.save_or_locate(locations_geographicalunit_220)

    locations_geographicalunit_221 = GeographicalUnit()
    locations_geographicalunit_221.GeographicalUnitId = 'Country_KH'
    locations_geographicalunit_221.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_221.GeographicalUnitName = 'Cambodia'
    locations_geographicalunit_221.GeographicalUnitShortName = 'Cambodia'
    locations_geographicalunit_221.HierarchyLevel = 30
    locations_geographicalunit_221.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_221 = importer.save_or_locate(locations_geographicalunit_221)

    locations_geographicalunit_222 = GeographicalUnit()
    locations_geographicalunit_222.GeographicalUnitId = 'Country_CV'
    locations_geographicalunit_222.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_222.GeographicalUnitName = 'Cabo Verde'
    locations_geographicalunit_222.GeographicalUnitShortName = 'Cabo Verde'
    locations_geographicalunit_222.HierarchyLevel = 30
    locations_geographicalunit_222.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_222 = importer.save_or_locate(locations_geographicalunit_222)

    locations_geographicalunit_223 = GeographicalUnit()
    locations_geographicalunit_223.GeographicalUnitId = 'Country_BI'
    locations_geographicalunit_223.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_223.GeographicalUnitName = 'Burundi'
    locations_geographicalunit_223.GeographicalUnitShortName = 'Burundi'
    locations_geographicalunit_223.HierarchyLevel = 30
    locations_geographicalunit_223.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_223 = importer.save_or_locate(locations_geographicalunit_223)

    locations_geographicalunit_224 = GeographicalUnit()
    locations_geographicalunit_224.GeographicalUnitId = 'Country_BF'
    locations_geographicalunit_224.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_224.GeographicalUnitName = 'Burkina Faso'
    locations_geographicalunit_224.GeographicalUnitShortName = 'Burkina Faso'
    locations_geographicalunit_224.HierarchyLevel = 30
    locations_geographicalunit_224.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_224 = importer.save_or_locate(locations_geographicalunit_224)

    locations_geographicalunit_225 = GeographicalUnit()
    locations_geographicalunit_225.GeographicalUnitId = 'Country_BG'
    locations_geographicalunit_225.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_225.GeographicalUnitName = 'Bulgaria'
    locations_geographicalunit_225.GeographicalUnitShortName = 'Bulgaria'
    locations_geographicalunit_225.HierarchyLevel = 30
    locations_geographicalunit_225.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_225 = importer.save_or_locate(locations_geographicalunit_225)

    locations_geographicalunit_226 = GeographicalUnit()
    locations_geographicalunit_226.GeographicalUnitId = 'Country_BN'
    locations_geographicalunit_226.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_226.GeographicalUnitName = 'Brunei Darussalam'
    locations_geographicalunit_226.GeographicalUnitShortName = 'Brunei Darussalam'
    locations_geographicalunit_226.HierarchyLevel = 30
    locations_geographicalunit_226.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_226 = importer.save_or_locate(locations_geographicalunit_226)

    locations_geographicalunit_227 = GeographicalUnit()
    locations_geographicalunit_227.GeographicalUnitId = 'Country_IO'
    locations_geographicalunit_227.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_227.GeographicalUnitName = 'British Indian Ocean Territory (the)'
    locations_geographicalunit_227.GeographicalUnitShortName = 'British Indian Ocean Territory'
    locations_geographicalunit_227.HierarchyLevel = 30
    locations_geographicalunit_227.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_227 = importer.save_or_locate(locations_geographicalunit_227)

    locations_geographicalunit_228 = GeographicalUnit()
    locations_geographicalunit_228.GeographicalUnitId = 'Country_BR'
    locations_geographicalunit_228.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_228.GeographicalUnitName = 'Brazil'
    locations_geographicalunit_228.GeographicalUnitShortName = 'Brazil'
    locations_geographicalunit_228.HierarchyLevel = 30
    locations_geographicalunit_228.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_228 = importer.save_or_locate(locations_geographicalunit_228)

    locations_geographicalunit_229 = GeographicalUnit()
    locations_geographicalunit_229.GeographicalUnitId = 'Country_BV'
    locations_geographicalunit_229.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_229.GeographicalUnitName = 'Bouvet Island'
    locations_geographicalunit_229.GeographicalUnitShortName = 'Bouvet Island'
    locations_geographicalunit_229.HierarchyLevel = 30
    locations_geographicalunit_229.IsPartOf = locations_geographicalunit_4
    locations_geographicalunit_229 = importer.save_or_locate(locations_geographicalunit_229)

    locations_geographicalunit_230 = GeographicalUnit()
    locations_geographicalunit_230.GeographicalUnitId = 'Country_BW'
    locations_geographicalunit_230.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_230.GeographicalUnitName = 'Botswana'
    locations_geographicalunit_230.GeographicalUnitShortName = 'Botswana'
    locations_geographicalunit_230.HierarchyLevel = 30
    locations_geographicalunit_230.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_230 = importer.save_or_locate(locations_geographicalunit_230)

    locations_geographicalunit_231 = GeographicalUnit()
    locations_geographicalunit_231.GeographicalUnitId = 'Country_BA'
    locations_geographicalunit_231.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_231.GeographicalUnitName = 'Bosnia and Herzegovina'
    locations_geographicalunit_231.GeographicalUnitShortName = 'Bosnia and Herzegovina'
    locations_geographicalunit_231.HierarchyLevel = 30
    locations_geographicalunit_231.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_231 = importer.save_or_locate(locations_geographicalunit_231)

    locations_geographicalunit_232 = GeographicalUnit()
    locations_geographicalunit_232.GeographicalUnitId = 'Country_BQ'
    locations_geographicalunit_232.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_232.GeographicalUnitName = 'Bonaire, Sint Eustatius and Saba'
    locations_geographicalunit_232.GeographicalUnitShortName = 'Bonaire, Sint Eustatius and Saba'
    locations_geographicalunit_232.HierarchyLevel = 30
    locations_geographicalunit_232.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_232 = importer.save_or_locate(locations_geographicalunit_232)

    locations_geographicalunit_233 = GeographicalUnit()
    locations_geographicalunit_233.GeographicalUnitId = 'Country_BO'
    locations_geographicalunit_233.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_233.GeographicalUnitName = 'Bolivia (Plurinational State of)'
    locations_geographicalunit_233.GeographicalUnitShortName = 'Bolivia'
    locations_geographicalunit_233.HierarchyLevel = 30
    locations_geographicalunit_233.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_233 = importer.save_or_locate(locations_geographicalunit_233)

    locations_geographicalunit_234 = GeographicalUnit()
    locations_geographicalunit_234.GeographicalUnitId = 'Country_BT'
    locations_geographicalunit_234.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_234.GeographicalUnitName = 'Bhutan'
    locations_geographicalunit_234.GeographicalUnitShortName = 'Bhutan'
    locations_geographicalunit_234.HierarchyLevel = 30
    locations_geographicalunit_234.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_234 = importer.save_or_locate(locations_geographicalunit_234)

    locations_geographicalunit_235 = GeographicalUnit()
    locations_geographicalunit_235.GeographicalUnitId = 'Country_BM'
    locations_geographicalunit_235.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_235.GeographicalUnitName = 'Bermuda'
    locations_geographicalunit_235.GeographicalUnitShortName = 'Bermuda'
    locations_geographicalunit_235.HierarchyLevel = 30
    locations_geographicalunit_235.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_235 = importer.save_or_locate(locations_geographicalunit_235)

    locations_geographicalunit_236 = GeographicalUnit()
    locations_geographicalunit_236.GeographicalUnitId = 'Country_BJ'
    locations_geographicalunit_236.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_236.GeographicalUnitName = 'Benin'
    locations_geographicalunit_236.GeographicalUnitShortName = 'Benin'
    locations_geographicalunit_236.HierarchyLevel = 30
    locations_geographicalunit_236.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_236 = importer.save_or_locate(locations_geographicalunit_236)

    locations_geographicalunit_237 = GeographicalUnit()
    locations_geographicalunit_237.GeographicalUnitId = 'Country_BZ'
    locations_geographicalunit_237.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_237.GeographicalUnitName = 'Belize'
    locations_geographicalunit_237.GeographicalUnitShortName = 'Belize'
    locations_geographicalunit_237.HierarchyLevel = 30
    locations_geographicalunit_237.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_237 = importer.save_or_locate(locations_geographicalunit_237)

    locations_geographicalunit_238 = GeographicalUnit()
    locations_geographicalunit_238.GeographicalUnitId = 'Country_BY'
    locations_geographicalunit_238.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_238.GeographicalUnitName = 'Belarus'
    locations_geographicalunit_238.GeographicalUnitShortName = 'Belarus'
    locations_geographicalunit_238.HierarchyLevel = 30
    locations_geographicalunit_238.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_238 = importer.save_or_locate(locations_geographicalunit_238)

    locations_geographicalunit_239 = GeographicalUnit()
    locations_geographicalunit_239.GeographicalUnitId = 'Country_BB'
    locations_geographicalunit_239.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_239.GeographicalUnitName = 'Barbados'
    locations_geographicalunit_239.GeographicalUnitShortName = 'Barbados'
    locations_geographicalunit_239.HierarchyLevel = 30
    locations_geographicalunit_239.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_239 = importer.save_or_locate(locations_geographicalunit_239)

    locations_geographicalunit_240 = GeographicalUnit()
    locations_geographicalunit_240.GeographicalUnitId = 'Country_BD'
    locations_geographicalunit_240.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_240.GeographicalUnitName = 'Bangladesh'
    locations_geographicalunit_240.GeographicalUnitShortName = 'Bangladesh'
    locations_geographicalunit_240.HierarchyLevel = 30
    locations_geographicalunit_240.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_240 = importer.save_or_locate(locations_geographicalunit_240)

    locations_geographicalunit_241 = GeographicalUnit()
    locations_geographicalunit_241.GeographicalUnitId = 'Country_BH'
    locations_geographicalunit_241.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_241.GeographicalUnitName = 'Bahrain'
    locations_geographicalunit_241.GeographicalUnitShortName = 'Bahrain'
    locations_geographicalunit_241.HierarchyLevel = 30
    locations_geographicalunit_241.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_241 = importer.save_or_locate(locations_geographicalunit_241)

    locations_geographicalunit_242 = GeographicalUnit()
    locations_geographicalunit_242.GeographicalUnitId = 'Country_BS'
    locations_geographicalunit_242.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_242.GeographicalUnitName = 'Bahamas (the)'
    locations_geographicalunit_242.GeographicalUnitShortName = 'Bahamas'
    locations_geographicalunit_242.HierarchyLevel = 30
    locations_geographicalunit_242.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_242 = importer.save_or_locate(locations_geographicalunit_242)

    locations_geographicalunit_243 = GeographicalUnit()
    locations_geographicalunit_243.GeographicalUnitId = 'Country_AZ'
    locations_geographicalunit_243.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_243.GeographicalUnitName = 'Azerbaijan'
    locations_geographicalunit_243.GeographicalUnitShortName = 'Azerbaijan'
    locations_geographicalunit_243.HierarchyLevel = 30
    locations_geographicalunit_243.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_243 = importer.save_or_locate(locations_geographicalunit_243)

    locations_geographicalunit_244 = GeographicalUnit()
    locations_geographicalunit_244.GeographicalUnitId = 'Country_AT'
    locations_geographicalunit_244.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_244.GeographicalUnitName = 'Austria'
    locations_geographicalunit_244.GeographicalUnitShortName = 'Austria'
    locations_geographicalunit_244.HierarchyLevel = 30
    locations_geographicalunit_244.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_244 = importer.save_or_locate(locations_geographicalunit_244)

    locations_geographicalunit_245 = GeographicalUnit()
    locations_geographicalunit_245.GeographicalUnitId = 'Country_AU'
    locations_geographicalunit_245.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_245.GeographicalUnitName = 'Australia'
    locations_geographicalunit_245.GeographicalUnitShortName = 'Australia'
    locations_geographicalunit_245.HierarchyLevel = 30
    locations_geographicalunit_245.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_245 = importer.save_or_locate(locations_geographicalunit_245)

    locations_geographicalunit_246 = GeographicalUnit()
    locations_geographicalunit_246.GeographicalUnitId = 'Country_AW'
    locations_geographicalunit_246.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_246.GeographicalUnitName = 'Aruba'
    locations_geographicalunit_246.GeographicalUnitShortName = 'Aruba'
    locations_geographicalunit_246.HierarchyLevel = 30
    locations_geographicalunit_246.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_246 = importer.save_or_locate(locations_geographicalunit_246)

    locations_geographicalunit_247 = GeographicalUnit()
    locations_geographicalunit_247.GeographicalUnitId = 'Country_AM'
    locations_geographicalunit_247.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_247.GeographicalUnitName = 'Armenia'
    locations_geographicalunit_247.GeographicalUnitShortName = 'Armenia'
    locations_geographicalunit_247.HierarchyLevel = 30
    locations_geographicalunit_247.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_247 = importer.save_or_locate(locations_geographicalunit_247)

    locations_geographicalunit_248 = GeographicalUnit()
    locations_geographicalunit_248.GeographicalUnitId = 'Country_AR'
    locations_geographicalunit_248.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_248.GeographicalUnitName = 'Argentina'
    locations_geographicalunit_248.GeographicalUnitShortName = 'Argentina'
    locations_geographicalunit_248.HierarchyLevel = 30
    locations_geographicalunit_248.IsPartOf = locations_geographicalunit_8
    locations_geographicalunit_248 = importer.save_or_locate(locations_geographicalunit_248)

    locations_geographicalunit_249 = GeographicalUnit()
    locations_geographicalunit_249.GeographicalUnitId = 'Country_AG'
    locations_geographicalunit_249.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_249.GeographicalUnitName = 'Antigua and Barbuda'
    locations_geographicalunit_249.GeographicalUnitShortName = 'Antigua and Barbuda'
    locations_geographicalunit_249.HierarchyLevel = 30
    locations_geographicalunit_249.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_249 = importer.save_or_locate(locations_geographicalunit_249)

    locations_geographicalunit_250 = GeographicalUnit()
    locations_geographicalunit_250.GeographicalUnitId = 'Country_AQ'
    locations_geographicalunit_250.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_250.GeographicalUnitName = 'Antarctica'
    locations_geographicalunit_250.GeographicalUnitShortName = 'Antarctica'
    locations_geographicalunit_250.HierarchyLevel = 30
    locations_geographicalunit_250.IsPartOf = locations_geographicalunit_4
    locations_geographicalunit_250 = importer.save_or_locate(locations_geographicalunit_250)

    locations_geographicalunit_251 = GeographicalUnit()
    locations_geographicalunit_251.GeographicalUnitId = 'Country_AI'
    locations_geographicalunit_251.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_251.GeographicalUnitName = 'Anguilla'
    locations_geographicalunit_251.GeographicalUnitShortName = 'Anguilla'
    locations_geographicalunit_251.HierarchyLevel = 30
    locations_geographicalunit_251.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_251 = importer.save_or_locate(locations_geographicalunit_251)

    locations_geographicalunit_252 = GeographicalUnit()
    locations_geographicalunit_252.GeographicalUnitId = 'Country_AO'
    locations_geographicalunit_252.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_252.GeographicalUnitName = 'Angola'
    locations_geographicalunit_252.GeographicalUnitShortName = 'Angola'
    locations_geographicalunit_252.HierarchyLevel = 30
    locations_geographicalunit_252.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_252 = importer.save_or_locate(locations_geographicalunit_252)

    locations_geographicalunit_253 = GeographicalUnit()
    locations_geographicalunit_253.GeographicalUnitId = 'Country_AD'
    locations_geographicalunit_253.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_253.GeographicalUnitName = 'Andorra'
    locations_geographicalunit_253.GeographicalUnitShortName = 'Andorra'
    locations_geographicalunit_253.HierarchyLevel = 30
    locations_geographicalunit_253.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_253 = importer.save_or_locate(locations_geographicalunit_253)

    locations_geographicalunit_254 = GeographicalUnit()
    locations_geographicalunit_254.GeographicalUnitId = 'Country_AS'
    locations_geographicalunit_254.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_254.GeographicalUnitName = 'American Samoa'
    locations_geographicalunit_254.GeographicalUnitShortName = 'American Samoa'
    locations_geographicalunit_254.HierarchyLevel = 30
    locations_geographicalunit_254.IsPartOf = locations_geographicalunit_6
    locations_geographicalunit_254 = importer.save_or_locate(locations_geographicalunit_254)

    locations_geographicalunit_255 = GeographicalUnit()
    locations_geographicalunit_255.GeographicalUnitId = 'Country_DZ'
    locations_geographicalunit_255.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_255.GeographicalUnitName = 'Algeria'
    locations_geographicalunit_255.GeographicalUnitShortName = 'Algeria'
    locations_geographicalunit_255.HierarchyLevel = 30
    locations_geographicalunit_255.IsPartOf = locations_geographicalunit_3
    locations_geographicalunit_255 = importer.save_or_locate(locations_geographicalunit_255)

    locations_geographicalunit_256 = GeographicalUnit()
    locations_geographicalunit_256.GeographicalUnitId = 'Country_AL'
    locations_geographicalunit_256.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_256.GeographicalUnitName = 'Albania'
    locations_geographicalunit_256.GeographicalUnitShortName = 'Albania'
    locations_geographicalunit_256.HierarchyLevel = 30
    locations_geographicalunit_256.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_256 = importer.save_or_locate(locations_geographicalunit_256)

    locations_geographicalunit_257 = GeographicalUnit()
    locations_geographicalunit_257.GeographicalUnitId = 'Country_AF'
    locations_geographicalunit_257.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_257.GeographicalUnitName = 'Afghanistan'
    locations_geographicalunit_257.GeographicalUnitShortName = 'Afghanistan'
    locations_geographicalunit_257.HierarchyLevel = 30
    locations_geographicalunit_257.IsPartOf = locations_geographicalunit_5
    locations_geographicalunit_257 = importer.save_or_locate(locations_geographicalunit_257)

    locations_geographicalunit_258 = GeographicalUnit()
    locations_geographicalunit_258.GeographicalUnitId = 'Country_AN'
    locations_geographicalunit_258.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_258.GeographicalUnitName = 'Antilles Neerlandaises'
    locations_geographicalunit_258.GeographicalUnitShortName = 'Antilles Neerlandaises'
    locations_geographicalunit_258.HierarchyLevel = 30
    locations_geographicalunit_258.IsPartOf = locations_geographicalunit_7
    locations_geographicalunit_258 = importer.save_or_locate(locations_geographicalunit_258)

    locations_geographicalunit_1.IsPartOf = locations_geographicalunit_2
    locations_geographicalunit_1 = importer.save_or_locate(locations_geographicalunit_1)

    # Processing model: locations.models.Continent

    from locations.models import Continent

    locations_continent_1 = Continent()
    locations_continent_1.GeographicalUnitId = 'Continent_AF'
    locations_continent_1.GeographicalUnitCategory = 'Continent'
    locations_continent_1.GeographicalUnitName = 'Africa'
    locations_continent_1.GeographicalUnitShortName = 'Africa'
    locations_continent_1.HierarchyLevel = 20
    locations_continent_1.IsPartOf = None
    locations_continent_1.geographicalunit_ptr = locations_geographicalunit_3
    locations_continent_1.ContinentCode = 'AF'
    locations_continent_1 = importer.save_or_locate(locations_continent_1)

    locations_continent_2 = Continent()
    locations_continent_2.GeographicalUnitId = 'Continent_AN'
    locations_continent_2.GeographicalUnitCategory = 'Continent'
    locations_continent_2.GeographicalUnitName = 'Antartica'
    locations_continent_2.GeographicalUnitShortName = 'Antartica'
    locations_continent_2.HierarchyLevel = 20
    locations_continent_2.IsPartOf = None
    locations_continent_2.geographicalunit_ptr = locations_geographicalunit_4
    locations_continent_2.ContinentCode = 'AN'
    locations_continent_2 = importer.save_or_locate(locations_continent_2)

    locations_continent_3 = Continent()
    locations_continent_3.GeographicalUnitId = 'Continent_AS'
    locations_continent_3.GeographicalUnitCategory = 'Continent'
    locations_continent_3.GeographicalUnitName = 'Asia'
    locations_continent_3.GeographicalUnitShortName = 'Asia'
    locations_continent_3.HierarchyLevel = 20
    locations_continent_3.IsPartOf = None
    locations_continent_3.geographicalunit_ptr = locations_geographicalunit_5
    locations_continent_3.ContinentCode = 'AS'
    locations_continent_3 = importer.save_or_locate(locations_continent_3)

    locations_continent_4 = Continent()
    locations_continent_4.GeographicalUnitId = 'Continent_EU'
    locations_continent_4.GeographicalUnitCategory = 'Continent'
    locations_continent_4.GeographicalUnitName = 'Europe'
    locations_continent_4.GeographicalUnitShortName = 'Europe'
    locations_continent_4.HierarchyLevel = 20
    locations_continent_4.IsPartOf = None
    locations_continent_4.geographicalunit_ptr = locations_geographicalunit_2
    locations_continent_4.ContinentCode = 'EU'
    locations_continent_4 = importer.save_or_locate(locations_continent_4)

    locations_continent_5 = Continent()
    locations_continent_5.GeographicalUnitId = 'Continent_NA'
    locations_continent_5.GeographicalUnitCategory = 'Continent'
    locations_continent_5.GeographicalUnitName = 'North America'
    locations_continent_5.GeographicalUnitShortName = 'North America'
    locations_continent_5.HierarchyLevel = 20
    locations_continent_5.IsPartOf = None
    locations_continent_5.geographicalunit_ptr = locations_geographicalunit_7
    locations_continent_5.ContinentCode = 'NA'
    locations_continent_5 = importer.save_or_locate(locations_continent_5)

    locations_continent_6 = Continent()
    locations_continent_6.GeographicalUnitId = 'Continent_OC'
    locations_continent_6.GeographicalUnitCategory = 'Continent'
    locations_continent_6.GeographicalUnitName = 'Oceania'
    locations_continent_6.GeographicalUnitShortName = 'Oceania'
    locations_continent_6.HierarchyLevel = 20
    locations_continent_6.IsPartOf = None
    locations_continent_6.geographicalunit_ptr = locations_geographicalunit_6
    locations_continent_6.ContinentCode = 'OC'
    locations_continent_6 = importer.save_or_locate(locations_continent_6)

    locations_continent_7 = Continent()
    locations_continent_7.GeographicalUnitId = 'Continent_SA'
    locations_continent_7.GeographicalUnitCategory = 'Continent'
    locations_continent_7.GeographicalUnitName = 'South America'
    locations_continent_7.GeographicalUnitShortName = 'South America'
    locations_continent_7.HierarchyLevel = 20
    locations_continent_7.IsPartOf = None
    locations_continent_7.geographicalunit_ptr = locations_geographicalunit_8
    locations_continent_7.ContinentCode = 'SA'
    locations_continent_7 = importer.save_or_locate(locations_continent_7)

    # Processing model: locations.models.Country

    from locations.models import Country

    locations_country_1 = Country()
    locations_country_1.GeographicalUnitId = 'Country_BE'
    locations_country_1.GeographicalUnitCategory = 'Country'
    locations_country_1.GeographicalUnitName = 'Belgium'
    locations_country_1.GeographicalUnitShortName = 'Belgium'
    locations_country_1.HierarchyLevel = 30
    locations_country_1.IsPartOf = locations_geographicalunit_2
    locations_country_1.geographicalunit_ptr = locations_geographicalunit_9
    locations_country_1.CountryCode = 'BE'
    locations_country_1.ISO3CountryCode = 'BEL'
    locations_country_1.PhonePrefix = '375'
    locations_country_1.InternetSuffix = '.be'
    locations_country_1.ISO3166Country = '56'
    locations_country_1 = importer.save_or_locate(locations_country_1)

    locations_country_2 = Country()
    locations_country_2.GeographicalUnitId = 'Country_FR'
    locations_country_2.GeographicalUnitCategory = 'Country'
    locations_country_2.GeographicalUnitName = 'France'
    locations_country_2.GeographicalUnitShortName = 'France'
    locations_country_2.HierarchyLevel = 30
    locations_country_2.IsPartOf = locations_geographicalunit_2
    locations_country_2.geographicalunit_ptr = locations_geographicalunit_1
    locations_country_2.CountryCode = 'FR'
    locations_country_2.ISO3CountryCode = 'FRA'
    locations_country_2.PhonePrefix = '358'
    locations_country_2.InternetSuffix = '.fr'
    locations_country_2.ISO3166Country = '250'
    locations_country_2 = importer.save_or_locate(locations_country_2)

    locations_country_3 = Country()
    locations_country_3.GeographicalUnitId = 'Country_AX'
    locations_country_3.GeographicalUnitCategory = 'Country'
    locations_country_3.GeographicalUnitName = 'Åland Islands'
    locations_country_3.GeographicalUnitShortName = 'Åland Islands'
    locations_country_3.HierarchyLevel = 30
    locations_country_3.IsPartOf = locations_geographicalunit_2
    locations_country_3.geographicalunit_ptr = locations_geographicalunit_12
    locations_country_3.CountryCode = 'AX'
    locations_country_3.ISO3CountryCode = 'ALA'
    locations_country_3.PhonePrefix = '263'
    locations_country_3.InternetSuffix = ' .ax'
    locations_country_3.ISO3166Country = '248'
    locations_country_3 = importer.save_or_locate(locations_country_3)

    locations_country_4 = Country()
    locations_country_4.GeographicalUnitId = 'Country_ZM'
    locations_country_4.GeographicalUnitCategory = 'Country'
    locations_country_4.GeographicalUnitName = 'Zambia'
    locations_country_4.GeographicalUnitShortName = 'Zambia'
    locations_country_4.HierarchyLevel = 30
    locations_country_4.IsPartOf = locations_geographicalunit_3
    locations_country_4.geographicalunit_ptr = locations_geographicalunit_13
    locations_country_4.CountryCode = 'ZM'
    locations_country_4.ISO3CountryCode = 'ZMB'
    locations_country_4.PhonePrefix = '967'
    locations_country_4.InternetSuffix = '.zm'
    locations_country_4.ISO3166Country = '894'
    locations_country_4 = importer.save_or_locate(locations_country_4)

    locations_country_5 = Country()
    locations_country_5.GeographicalUnitId = 'Country_YE'
    locations_country_5.GeographicalUnitCategory = 'Country'
    locations_country_5.GeographicalUnitName = 'Yemen'
    locations_country_5.GeographicalUnitShortName = 'Yemen'
    locations_country_5.HierarchyLevel = 30
    locations_country_5.IsPartOf = locations_geographicalunit_5
    locations_country_5.geographicalunit_ptr = locations_geographicalunit_14
    locations_country_5.CountryCode = 'YE'
    locations_country_5.ISO3CountryCode = 'YEM'
    locations_country_5.PhonePrefix = '212'
    locations_country_5.InternetSuffix = '.ye'
    locations_country_5.ISO3166Country = '887'
    locations_country_5 = importer.save_or_locate(locations_country_5)

    locations_country_6 = Country()
    locations_country_6.GeographicalUnitId = 'Country_EH'
    locations_country_6.GeographicalUnitCategory = 'Country'
    locations_country_6.GeographicalUnitName = 'Western Sahara'
    locations_country_6.GeographicalUnitShortName = 'Western Sahara'
    locations_country_6.HierarchyLevel = 30
    locations_country_6.IsPartOf = locations_geographicalunit_3
    locations_country_6.geographicalunit_ptr = locations_geographicalunit_15
    locations_country_6.CountryCode = 'EH'
    locations_country_6.ISO3CountryCode = 'ESH'
    locations_country_6.PhonePrefix = '681'
    locations_country_6.InternetSuffix = '.eh'
    locations_country_6.ISO3166Country = '732'
    locations_country_6 = importer.save_or_locate(locations_country_6)

    locations_country_7 = Country()
    locations_country_7.GeographicalUnitId = 'Country_WF'
    locations_country_7.GeographicalUnitCategory = 'Country'
    locations_country_7.GeographicalUnitName = 'Wallis and Futuna'
    locations_country_7.GeographicalUnitShortName = 'Wallis and Futuna'
    locations_country_7.HierarchyLevel = 30
    locations_country_7.IsPartOf = locations_geographicalunit_6
    locations_country_7.geographicalunit_ptr = locations_geographicalunit_16
    locations_country_7.CountryCode = 'WF'
    locations_country_7.ISO3CountryCode = 'WLF'
    locations_country_7.PhonePrefix = '1-340'
    locations_country_7.InternetSuffix = '.wf'
    locations_country_7.ISO3166Country = '876'
    locations_country_7 = importer.save_or_locate(locations_country_7)

    locations_country_8 = Country()
    locations_country_8.GeographicalUnitId = 'Country_VI'
    locations_country_8.GeographicalUnitCategory = 'Country'
    locations_country_8.GeographicalUnitName = 'Virgin Islands (U.S.)'
    locations_country_8.GeographicalUnitShortName = 'Virgin Islands '
    locations_country_8.HierarchyLevel = 30
    locations_country_8.IsPartOf = locations_geographicalunit_7
    locations_country_8.geographicalunit_ptr = locations_geographicalunit_17
    locations_country_8.CountryCode = 'VI'
    locations_country_8.ISO3CountryCode = 'VIR'
    locations_country_8.PhonePrefix = '1-284'
    locations_country_8.InternetSuffix = '.vi'
    locations_country_8.ISO3166Country = '850'
    locations_country_8 = importer.save_or_locate(locations_country_8)

    locations_country_9 = Country()
    locations_country_9.GeographicalUnitId = 'Country_VG'
    locations_country_9.GeographicalUnitCategory = 'Country'
    locations_country_9.GeographicalUnitName = 'Virgin Islands (British)'
    locations_country_9.GeographicalUnitShortName = 'Virgin Islands'
    locations_country_9.HierarchyLevel = 30
    locations_country_9.IsPartOf = locations_geographicalunit_7
    locations_country_9.geographicalunit_ptr = locations_geographicalunit_18
    locations_country_9.CountryCode = 'VG'
    locations_country_9.ISO3CountryCode = 'VGB'
    locations_country_9.PhonePrefix = '84'
    locations_country_9.InternetSuffix = '.vg'
    locations_country_9.ISO3166Country = '92'
    locations_country_9 = importer.save_or_locate(locations_country_9)

    locations_country_10 = Country()
    locations_country_10.GeographicalUnitId = 'Country_VN'
    locations_country_10.GeographicalUnitCategory = 'Country'
    locations_country_10.GeographicalUnitName = 'Vietnam'
    locations_country_10.GeographicalUnitShortName = 'Vietnam'
    locations_country_10.HierarchyLevel = 30
    locations_country_10.IsPartOf = locations_geographicalunit_5
    locations_country_10.geographicalunit_ptr = locations_geographicalunit_19
    locations_country_10.CountryCode = 'VN'
    locations_country_10.ISO3CountryCode = 'VNM'
    locations_country_10.PhonePrefix = '58'
    locations_country_10.InternetSuffix = '.vn'
    locations_country_10.ISO3166Country = '704'
    locations_country_10 = importer.save_or_locate(locations_country_10)

    locations_country_11 = Country()
    locations_country_11.GeographicalUnitId = 'Country_VE'
    locations_country_11.GeographicalUnitCategory = 'Country'
    locations_country_11.GeographicalUnitName = 'Venezuela (Bolivarian Republic of)'
    locations_country_11.GeographicalUnitShortName = 'Venezuela'
    locations_country_11.HierarchyLevel = 30
    locations_country_11.IsPartOf = locations_geographicalunit_8
    locations_country_11.geographicalunit_ptr = locations_geographicalunit_20
    locations_country_11.CountryCode = 'VE'
    locations_country_11.ISO3CountryCode = 'VEN'
    locations_country_11.PhonePrefix = '678'
    locations_country_11.InternetSuffix = '.ve'
    locations_country_11.ISO3166Country = '862'
    locations_country_11 = importer.save_or_locate(locations_country_11)

    locations_country_12 = Country()
    locations_country_12.GeographicalUnitId = 'Country_VU'
    locations_country_12.GeographicalUnitCategory = 'Country'
    locations_country_12.GeographicalUnitName = 'Vanuatu'
    locations_country_12.GeographicalUnitShortName = 'Vanuatu'
    locations_country_12.HierarchyLevel = 30
    locations_country_12.IsPartOf = locations_geographicalunit_6
    locations_country_12.geographicalunit_ptr = locations_geographicalunit_21
    locations_country_12.CountryCode = 'VU'
    locations_country_12.ISO3CountryCode = 'VUT'
    locations_country_12.PhonePrefix = '998'
    locations_country_12.InternetSuffix = '.vu'
    locations_country_12.ISO3166Country = '548'
    locations_country_12 = importer.save_or_locate(locations_country_12)

    locations_country_13 = Country()
    locations_country_13.GeographicalUnitId = 'Country_UZ'
    locations_country_13.GeographicalUnitCategory = 'Country'
    locations_country_13.GeographicalUnitName = 'Uzbekistan'
    locations_country_13.GeographicalUnitShortName = 'Uzbekistan'
    locations_country_13.HierarchyLevel = 30
    locations_country_13.IsPartOf = locations_geographicalunit_5
    locations_country_13.geographicalunit_ptr = locations_geographicalunit_22
    locations_country_13.CountryCode = 'UZ'
    locations_country_13.ISO3CountryCode = 'UZB'
    locations_country_13.PhonePrefix = '598'
    locations_country_13.InternetSuffix = '.uz'
    locations_country_13.ISO3166Country = '860'
    locations_country_13 = importer.save_or_locate(locations_country_13)

    locations_country_14 = Country()
    locations_country_14.GeographicalUnitId = 'Country_UY'
    locations_country_14.GeographicalUnitCategory = 'Country'
    locations_country_14.GeographicalUnitName = 'Uruguay'
    locations_country_14.GeographicalUnitShortName = 'Uruguay'
    locations_country_14.HierarchyLevel = 30
    locations_country_14.IsPartOf = locations_geographicalunit_8
    locations_country_14.geographicalunit_ptr = locations_geographicalunit_23
    locations_country_14.CountryCode = 'UY'
    locations_country_14.ISO3CountryCode = 'URY'
    locations_country_14.PhonePrefix = '598'
    locations_country_14.InternetSuffix = '.uy'
    locations_country_14.ISO3166Country = '858'
    locations_country_14 = importer.save_or_locate(locations_country_14)

    locations_country_15 = Country()
    locations_country_15.GeographicalUnitId = 'Country_US'
    locations_country_15.GeographicalUnitCategory = 'Country'
    locations_country_15.GeographicalUnitName = 'United States of America (the)'
    locations_country_15.GeographicalUnitShortName = 'USA'
    locations_country_15.HierarchyLevel = 30
    locations_country_15.IsPartOf = locations_geographicalunit_7
    locations_country_15.geographicalunit_ptr = locations_geographicalunit_24
    locations_country_15.CountryCode = 'US'
    locations_country_15.ISO3CountryCode = 'USA'
    locations_country_15.PhonePrefix = '1'
    locations_country_15.InternetSuffix = '.us'
    locations_country_15.ISO3166Country = '840'
    locations_country_15 = importer.save_or_locate(locations_country_15)

    locations_country_16 = Country()
    locations_country_16.GeographicalUnitId = 'Country_UM'
    locations_country_16.GeographicalUnitCategory = 'Country'
    locations_country_16.GeographicalUnitName = 'United States Minor Outlying Islands (the)'
    locations_country_16.GeographicalUnitShortName = 'United States Minor Outlying Islands '
    locations_country_16.HierarchyLevel = 30
    locations_country_16.IsPartOf = locations_geographicalunit_6
    locations_country_16.geographicalunit_ptr = locations_geographicalunit_25
    locations_country_16.CountryCode = 'UM'
    locations_country_16.ISO3CountryCode = 'UMI'
    locations_country_16.PhonePrefix = '44'
    locations_country_16.InternetSuffix = '.um'
    locations_country_16.ISO3166Country = '581'
    locations_country_16 = importer.save_or_locate(locations_country_16)

    locations_country_17 = Country()
    locations_country_17.GeographicalUnitId = 'Country_GB'
    locations_country_17.GeographicalUnitCategory = 'Country'
    locations_country_17.GeographicalUnitName = 'United Kingdom of Great Britain and Northern Ireland (the)'
    locations_country_17.GeographicalUnitShortName = 'UK'
    locations_country_17.HierarchyLevel = 30
    locations_country_17.IsPartOf = locations_geographicalunit_2
    locations_country_17.geographicalunit_ptr = locations_geographicalunit_26
    locations_country_17.CountryCode = 'GB'
    locations_country_17.ISO3CountryCode = 'GBR'
    locations_country_17.PhonePrefix = '971'
    locations_country_17.InternetSuffix = '.uk'
    locations_country_17.ISO3166Country = '826'
    locations_country_17 = importer.save_or_locate(locations_country_17)

    locations_country_18 = Country()
    locations_country_18.GeographicalUnitId = 'Country_AE'
    locations_country_18.GeographicalUnitCategory = 'Country'
    locations_country_18.GeographicalUnitName = 'United Arab Emirates (the)'
    locations_country_18.GeographicalUnitShortName = 'UAE'
    locations_country_18.HierarchyLevel = 30
    locations_country_18.IsPartOf = locations_geographicalunit_5
    locations_country_18.geographicalunit_ptr = locations_geographicalunit_27
    locations_country_18.CountryCode = 'AE'
    locations_country_18.ISO3CountryCode = 'ARE'
    locations_country_18.PhonePrefix = '380'
    locations_country_18.InternetSuffix = '.ae'
    locations_country_18.ISO3166Country = '784'
    locations_country_18 = importer.save_or_locate(locations_country_18)

    locations_country_19 = Country()
    locations_country_19.GeographicalUnitId = 'Country_UA'
    locations_country_19.GeographicalUnitCategory = 'Country'
    locations_country_19.GeographicalUnitName = 'Ukraine'
    locations_country_19.GeographicalUnitShortName = 'Ukraine'
    locations_country_19.HierarchyLevel = 30
    locations_country_19.IsPartOf = locations_geographicalunit_2
    locations_country_19.geographicalunit_ptr = locations_geographicalunit_28
    locations_country_19.CountryCode = 'UA'
    locations_country_19.ISO3CountryCode = 'UKR'
    locations_country_19.PhonePrefix = '256'
    locations_country_19.InternetSuffix = '.ua'
    locations_country_19.ISO3166Country = '804'
    locations_country_19 = importer.save_or_locate(locations_country_19)

    locations_country_20 = Country()
    locations_country_20.GeographicalUnitId = 'Country_UG'
    locations_country_20.GeographicalUnitCategory = 'Country'
    locations_country_20.GeographicalUnitName = 'Uganda'
    locations_country_20.GeographicalUnitShortName = 'Uganda'
    locations_country_20.HierarchyLevel = 30
    locations_country_20.IsPartOf = locations_geographicalunit_3
    locations_country_20.geographicalunit_ptr = locations_geographicalunit_29
    locations_country_20.CountryCode = 'UG'
    locations_country_20.ISO3CountryCode = 'UGA'
    locations_country_20.PhonePrefix = '688'
    locations_country_20.InternetSuffix = '.ug'
    locations_country_20.ISO3166Country = '800'
    locations_country_20 = importer.save_or_locate(locations_country_20)

    locations_country_21 = Country()
    locations_country_21.GeographicalUnitId = 'Country_TV'
    locations_country_21.GeographicalUnitCategory = 'Country'
    locations_country_21.GeographicalUnitName = 'Tuvalu'
    locations_country_21.GeographicalUnitShortName = 'Tuvalu'
    locations_country_21.HierarchyLevel = 30
    locations_country_21.IsPartOf = locations_geographicalunit_6
    locations_country_21.geographicalunit_ptr = locations_geographicalunit_30
    locations_country_21.CountryCode = 'TV'
    locations_country_21.ISO3CountryCode = 'TUV'
    locations_country_21.PhonePrefix = '1-649'
    locations_country_21.InternetSuffix = '.tv'
    locations_country_21.ISO3166Country = '798'
    locations_country_21 = importer.save_or_locate(locations_country_21)

    locations_country_22 = Country()
    locations_country_22.GeographicalUnitId = 'Country_TC'
    locations_country_22.GeographicalUnitCategory = 'Country'
    locations_country_22.GeographicalUnitName = 'Turks and Caicos Islands (the)'
    locations_country_22.GeographicalUnitShortName = 'Turks and Caicos Islands '
    locations_country_22.HierarchyLevel = 30
    locations_country_22.IsPartOf = locations_geographicalunit_7
    locations_country_22.geographicalunit_ptr = locations_geographicalunit_31
    locations_country_22.CountryCode = 'TC'
    locations_country_22.ISO3CountryCode = 'TCA'
    locations_country_22.PhonePrefix = '993'
    locations_country_22.InternetSuffix = '.tc'
    locations_country_22.ISO3166Country = '796'
    locations_country_22 = importer.save_or_locate(locations_country_22)

    locations_country_23 = Country()
    locations_country_23.GeographicalUnitId = 'Country_TM'
    locations_country_23.GeographicalUnitCategory = 'Country'
    locations_country_23.GeographicalUnitName = 'Turkmenistan'
    locations_country_23.GeographicalUnitShortName = 'Turkmenistan'
    locations_country_23.HierarchyLevel = 30
    locations_country_23.IsPartOf = locations_geographicalunit_5
    locations_country_23.geographicalunit_ptr = locations_geographicalunit_32
    locations_country_23.CountryCode = 'TM'
    locations_country_23.ISO3CountryCode = 'TKM'
    locations_country_23.PhonePrefix = '90'
    locations_country_23.InternetSuffix = '.tm'
    locations_country_23.ISO3166Country = '795'
    locations_country_23 = importer.save_or_locate(locations_country_23)

    locations_country_24 = Country()
    locations_country_24.GeographicalUnitId = 'Country_TR'
    locations_country_24.GeographicalUnitCategory = 'Country'
    locations_country_24.GeographicalUnitName = 'Turkey'
    locations_country_24.GeographicalUnitShortName = 'Turkey'
    locations_country_24.HierarchyLevel = 30
    locations_country_24.IsPartOf = locations_geographicalunit_2
    locations_country_24.geographicalunit_ptr = locations_geographicalunit_33
    locations_country_24.CountryCode = 'TR'
    locations_country_24.ISO3CountryCode = 'TUR'
    locations_country_24.PhonePrefix = '216'
    locations_country_24.InternetSuffix = '.tr'
    locations_country_24.ISO3166Country = '792'
    locations_country_24 = importer.save_or_locate(locations_country_24)

    locations_country_25 = Country()
    locations_country_25.GeographicalUnitId = 'Country_TN'
    locations_country_25.GeographicalUnitCategory = 'Country'
    locations_country_25.GeographicalUnitName = 'Tunisia'
    locations_country_25.GeographicalUnitShortName = 'Tunisia'
    locations_country_25.HierarchyLevel = 30
    locations_country_25.IsPartOf = locations_geographicalunit_3
    locations_country_25.geographicalunit_ptr = locations_geographicalunit_34
    locations_country_25.CountryCode = 'TN'
    locations_country_25.ISO3CountryCode = 'TUN'
    locations_country_25.PhonePrefix = '1-868'
    locations_country_25.InternetSuffix = '.tn'
    locations_country_25.ISO3166Country = '788'
    locations_country_25 = importer.save_or_locate(locations_country_25)

    locations_country_26 = Country()
    locations_country_26.GeographicalUnitId = 'Country_TT'
    locations_country_26.GeographicalUnitCategory = 'Country'
    locations_country_26.GeographicalUnitName = 'Trinidad and Tobago'
    locations_country_26.GeographicalUnitShortName = 'Trinidad'
    locations_country_26.HierarchyLevel = 30
    locations_country_26.IsPartOf = locations_geographicalunit_7
    locations_country_26.geographicalunit_ptr = locations_geographicalunit_35
    locations_country_26.CountryCode = 'TT'
    locations_country_26.ISO3CountryCode = 'TTO'
    locations_country_26.PhonePrefix = '676'
    locations_country_26.InternetSuffix = '.tt'
    locations_country_26.ISO3166Country = '780'
    locations_country_26 = importer.save_or_locate(locations_country_26)

    locations_country_27 = Country()
    locations_country_27.GeographicalUnitId = 'Country_TO'
    locations_country_27.GeographicalUnitCategory = 'Country'
    locations_country_27.GeographicalUnitName = 'Tonga'
    locations_country_27.GeographicalUnitShortName = 'Tonga'
    locations_country_27.HierarchyLevel = 30
    locations_country_27.IsPartOf = locations_geographicalunit_6
    locations_country_27.geographicalunit_ptr = locations_geographicalunit_36
    locations_country_27.CountryCode = 'TO'
    locations_country_27.ISO3CountryCode = 'TON'
    locations_country_27.PhonePrefix = '690'
    locations_country_27.InternetSuffix = '.to'
    locations_country_27.ISO3166Country = '776'
    locations_country_27 = importer.save_or_locate(locations_country_27)

    locations_country_28 = Country()
    locations_country_28.GeographicalUnitId = 'Country_TK'
    locations_country_28.GeographicalUnitCategory = 'Country'
    locations_country_28.GeographicalUnitName = 'Tokelau'
    locations_country_28.GeographicalUnitShortName = 'Tokelau'
    locations_country_28.HierarchyLevel = 30
    locations_country_28.IsPartOf = locations_geographicalunit_6
    locations_country_28.geographicalunit_ptr = locations_geographicalunit_37
    locations_country_28.CountryCode = 'TK'
    locations_country_28.ISO3CountryCode = 'TKL'
    locations_country_28.PhonePrefix = '228'
    locations_country_28.InternetSuffix = '.tk'
    locations_country_28.ISO3166Country = '772'
    locations_country_28 = importer.save_or_locate(locations_country_28)

    locations_country_29 = Country()
    locations_country_29.GeographicalUnitId = 'Country_TG'
    locations_country_29.GeographicalUnitCategory = 'Country'
    locations_country_29.GeographicalUnitName = 'Togo'
    locations_country_29.GeographicalUnitShortName = 'Togo'
    locations_country_29.HierarchyLevel = 30
    locations_country_29.IsPartOf = locations_geographicalunit_3
    locations_country_29.geographicalunit_ptr = locations_geographicalunit_38
    locations_country_29.CountryCode = 'TG'
    locations_country_29.ISO3CountryCode = 'TGO'
    locations_country_29.PhonePrefix = '670'
    locations_country_29.InternetSuffix = '.tg'
    locations_country_29.ISO3166Country = '768'
    locations_country_29 = importer.save_or_locate(locations_country_29)

    locations_country_30 = Country()
    locations_country_30.GeographicalUnitId = 'Country_TL'
    locations_country_30.GeographicalUnitCategory = 'Country'
    locations_country_30.GeographicalUnitName = 'Timor-Leste'
    locations_country_30.GeographicalUnitShortName = 'East Timor'
    locations_country_30.HierarchyLevel = 30
    locations_country_30.IsPartOf = locations_geographicalunit_5
    locations_country_30.geographicalunit_ptr = locations_geographicalunit_39
    locations_country_30.CountryCode = 'TL'
    locations_country_30.ISO3CountryCode = 'TLS'
    locations_country_30.PhonePrefix = '66'
    locations_country_30.InternetSuffix = '.tl'
    locations_country_30.ISO3166Country = '626'
    locations_country_30 = importer.save_or_locate(locations_country_30)

    locations_country_31 = Country()
    locations_country_31.GeographicalUnitId = 'Country_TH'
    locations_country_31.GeographicalUnitCategory = 'Country'
    locations_country_31.GeographicalUnitName = 'Thailand'
    locations_country_31.GeographicalUnitShortName = 'Thailand'
    locations_country_31.HierarchyLevel = 30
    locations_country_31.IsPartOf = locations_geographicalunit_5
    locations_country_31.geographicalunit_ptr = locations_geographicalunit_40
    locations_country_31.CountryCode = 'TH'
    locations_country_31.ISO3CountryCode = 'THA'
    locations_country_31.PhonePrefix = '255'
    locations_country_31.InternetSuffix = '.th'
    locations_country_31.ISO3166Country = '764'
    locations_country_31 = importer.save_or_locate(locations_country_31)

    locations_country_32 = Country()
    locations_country_32.GeographicalUnitId = 'Country_TZ'
    locations_country_32.GeographicalUnitCategory = 'Country'
    locations_country_32.GeographicalUnitName = 'Tanzania, United Republic of'
    locations_country_32.GeographicalUnitShortName = 'Tanzania'
    locations_country_32.HierarchyLevel = 30
    locations_country_32.IsPartOf = locations_geographicalunit_3
    locations_country_32.geographicalunit_ptr = locations_geographicalunit_41
    locations_country_32.CountryCode = 'TZ'
    locations_country_32.ISO3CountryCode = 'TZA'
    locations_country_32.PhonePrefix = '992'
    locations_country_32.InternetSuffix = '.tz'
    locations_country_32.ISO3166Country = '834'
    locations_country_32 = importer.save_or_locate(locations_country_32)

    locations_country_33 = Country()
    locations_country_33.GeographicalUnitId = 'Country_TJ'
    locations_country_33.GeographicalUnitCategory = 'Country'
    locations_country_33.GeographicalUnitName = 'Tajikistan'
    locations_country_33.GeographicalUnitShortName = 'Tajikistan'
    locations_country_33.HierarchyLevel = 30
    locations_country_33.IsPartOf = locations_geographicalunit_5
    locations_country_33.geographicalunit_ptr = locations_geographicalunit_42
    locations_country_33.CountryCode = 'TJ'
    locations_country_33.ISO3CountryCode = 'TJK'
    locations_country_33.PhonePrefix = '886'
    locations_country_33.InternetSuffix = '.tj'
    locations_country_33.ISO3166Country = '762'
    locations_country_33 = importer.save_or_locate(locations_country_33)

    locations_country_34 = Country()
    locations_country_34.GeographicalUnitId = 'Country_TW'
    locations_country_34.GeographicalUnitCategory = 'Country'
    locations_country_34.GeographicalUnitName = 'Taiwan (Province of China)'
    locations_country_34.GeographicalUnitShortName = 'Taiwan'
    locations_country_34.HierarchyLevel = 30
    locations_country_34.IsPartOf = locations_geographicalunit_5
    locations_country_34.geographicalunit_ptr = locations_geographicalunit_43
    locations_country_34.CountryCode = 'TW'
    locations_country_34.ISO3CountryCode = 'TWN'
    locations_country_34.PhonePrefix = '963'
    locations_country_34.InternetSuffix = '.tw'
    locations_country_34.ISO3166Country = '158'
    locations_country_34 = importer.save_or_locate(locations_country_34)

    locations_country_35 = Country()
    locations_country_35.GeographicalUnitId = 'Country_SY'
    locations_country_35.GeographicalUnitCategory = 'Country'
    locations_country_35.GeographicalUnitName = 'Syrian Arab Republic'
    locations_country_35.GeographicalUnitShortName = 'Syrian Arab Republic'
    locations_country_35.HierarchyLevel = 30
    locations_country_35.IsPartOf = locations_geographicalunit_5
    locations_country_35.geographicalunit_ptr = locations_geographicalunit_44
    locations_country_35.CountryCode = 'SY'
    locations_country_35.ISO3CountryCode = 'SYR'
    locations_country_35.PhonePrefix = '41'
    locations_country_35.InternetSuffix = '.sy'
    locations_country_35.ISO3166Country = '760'
    locations_country_35 = importer.save_or_locate(locations_country_35)

    locations_country_36 = Country()
    locations_country_36.GeographicalUnitId = 'Country_CH'
    locations_country_36.GeographicalUnitCategory = 'Country'
    locations_country_36.GeographicalUnitName = 'Switzerland'
    locations_country_36.GeographicalUnitShortName = 'Switzerland'
    locations_country_36.HierarchyLevel = 30
    locations_country_36.IsPartOf = locations_geographicalunit_2
    locations_country_36.geographicalunit_ptr = locations_geographicalunit_45
    locations_country_36.CountryCode = 'CH'
    locations_country_36.ISO3CountryCode = 'CHE'
    locations_country_36.PhonePrefix = '46'
    locations_country_36.InternetSuffix = '.ch'
    locations_country_36.ISO3166Country = '756'
    locations_country_36 = importer.save_or_locate(locations_country_36)

    locations_country_37 = Country()
    locations_country_37.GeographicalUnitId = 'Country_SE'
    locations_country_37.GeographicalUnitCategory = 'Country'
    locations_country_37.GeographicalUnitName = 'Sweden'
    locations_country_37.GeographicalUnitShortName = 'Sweden'
    locations_country_37.HierarchyLevel = 30
    locations_country_37.IsPartOf = locations_geographicalunit_2
    locations_country_37.geographicalunit_ptr = locations_geographicalunit_46
    locations_country_37.CountryCode = 'SE'
    locations_country_37.ISO3CountryCode = 'SWE'
    locations_country_37.PhonePrefix = '47'
    locations_country_37.InternetSuffix = '.se'
    locations_country_37.ISO3166Country = '752'
    locations_country_37 = importer.save_or_locate(locations_country_37)

    locations_country_38 = Country()
    locations_country_38.GeographicalUnitId = 'Country_SJ'
    locations_country_38.GeographicalUnitCategory = 'Country'
    locations_country_38.GeographicalUnitName = 'Svalbard and Jan Mayen'
    locations_country_38.GeographicalUnitShortName = 'Svalbard and Jan Mayen'
    locations_country_38.HierarchyLevel = 30
    locations_country_38.IsPartOf = locations_geographicalunit_2
    locations_country_38.geographicalunit_ptr = locations_geographicalunit_47
    locations_country_38.CountryCode = 'SJ'
    locations_country_38.ISO3CountryCode = 'SJM'
    locations_country_38.PhonePrefix = '597'
    locations_country_38.InternetSuffix = '.sj'
    locations_country_38.ISO3166Country = '744'
    locations_country_38 = importer.save_or_locate(locations_country_38)

    locations_country_39 = Country()
    locations_country_39.GeographicalUnitId = 'Country_SR'
    locations_country_39.GeographicalUnitCategory = 'Country'
    locations_country_39.GeographicalUnitName = 'Suriname'
    locations_country_39.GeographicalUnitShortName = 'Suriname'
    locations_country_39.HierarchyLevel = 30
    locations_country_39.IsPartOf = locations_geographicalunit_8
    locations_country_39.geographicalunit_ptr = locations_geographicalunit_48
    locations_country_39.CountryCode = 'SR'
    locations_country_39.ISO3CountryCode = 'SUR'
    locations_country_39.PhonePrefix = '249'
    locations_country_39.InternetSuffix = '.sr'
    locations_country_39.ISO3166Country = '740'
    locations_country_39 = importer.save_or_locate(locations_country_39)

    locations_country_40 = Country()
    locations_country_40.GeographicalUnitId = 'Country_SD'
    locations_country_40.GeographicalUnitCategory = 'Country'
    locations_country_40.GeographicalUnitName = 'Sudan (the)'
    locations_country_40.GeographicalUnitShortName = 'Sudan'
    locations_country_40.HierarchyLevel = 30
    locations_country_40.IsPartOf = locations_geographicalunit_3
    locations_country_40.geographicalunit_ptr = locations_geographicalunit_49
    locations_country_40.CountryCode = 'SD'
    locations_country_40.ISO3CountryCode = 'SDN'
    locations_country_40.PhonePrefix = '94'
    locations_country_40.InternetSuffix = '.sd'
    locations_country_40.ISO3166Country = '729'
    locations_country_40 = importer.save_or_locate(locations_country_40)

    locations_country_41 = Country()
    locations_country_41.GeographicalUnitId = 'Country_LK'
    locations_country_41.GeographicalUnitCategory = 'Country'
    locations_country_41.GeographicalUnitName = 'Sri Lanka'
    locations_country_41.GeographicalUnitShortName = 'Sri Lanka'
    locations_country_41.HierarchyLevel = 30
    locations_country_41.IsPartOf = locations_geographicalunit_5
    locations_country_41.geographicalunit_ptr = locations_geographicalunit_50
    locations_country_41.CountryCode = 'LK'
    locations_country_41.ISO3CountryCode = 'LKA'
    locations_country_41.PhonePrefix = '34'
    locations_country_41.InternetSuffix = '.lk'
    locations_country_41.ISO3166Country = '144'
    locations_country_41 = importer.save_or_locate(locations_country_41)

    locations_country_42 = Country()
    locations_country_42.GeographicalUnitId = 'Country_ES'
    locations_country_42.GeographicalUnitCategory = 'Country'
    locations_country_42.GeographicalUnitName = 'Spain'
    locations_country_42.GeographicalUnitShortName = 'Spain'
    locations_country_42.HierarchyLevel = 30
    locations_country_42.IsPartOf = locations_geographicalunit_2
    locations_country_42.geographicalunit_ptr = locations_geographicalunit_51
    locations_country_42.CountryCode = 'ES'
    locations_country_42.ISO3CountryCode = 'ESP'
    locations_country_42.PhonePrefix = '211'
    locations_country_42.InternetSuffix = '.es'
    locations_country_42.ISO3166Country = '724'
    locations_country_42 = importer.save_or_locate(locations_country_42)

    locations_country_43 = Country()
    locations_country_43.GeographicalUnitId = 'Country_SS'
    locations_country_43.GeographicalUnitCategory = 'Country'
    locations_country_43.GeographicalUnitName = 'South Sudan'
    locations_country_43.GeographicalUnitShortName = 'South Sudan'
    locations_country_43.HierarchyLevel = 30
    locations_country_43.IsPartOf = locations_geographicalunit_3
    locations_country_43.geographicalunit_ptr = locations_geographicalunit_52
    locations_country_43.CountryCode = 'SS'
    locations_country_43.ISO3CountryCode = 'SSD'
    locations_country_43.PhonePrefix = None
    locations_country_43.InternetSuffix = '.ss'
    locations_country_43.ISO3166Country = '728'
    locations_country_43 = importer.save_or_locate(locations_country_43)

    locations_country_44 = Country()
    locations_country_44.GeographicalUnitId = 'Country_GS'
    locations_country_44.GeographicalUnitCategory = 'Country'
    locations_country_44.GeographicalUnitName = 'South Georgia and the South Sandwich Islands'
    locations_country_44.GeographicalUnitShortName = 'South Georgia and the South Sandwich Islands'
    locations_country_44.HierarchyLevel = 30
    locations_country_44.IsPartOf = locations_geographicalunit_4
    locations_country_44.geographicalunit_ptr = locations_geographicalunit_53
    locations_country_44.CountryCode = 'GS'
    locations_country_44.ISO3CountryCode = 'SGS'
    locations_country_44.PhonePrefix = '27'
    locations_country_44.InternetSuffix = '.gs'
    locations_country_44.ISO3166Country = '239'
    locations_country_44 = importer.save_or_locate(locations_country_44)

    locations_country_45 = Country()
    locations_country_45.GeographicalUnitId = 'Country_ZA'
    locations_country_45.GeographicalUnitCategory = 'Country'
    locations_country_45.GeographicalUnitName = 'South Africa'
    locations_country_45.GeographicalUnitShortName = 'South Africa'
    locations_country_45.HierarchyLevel = 30
    locations_country_45.IsPartOf = locations_geographicalunit_3
    locations_country_45.geographicalunit_ptr = locations_geographicalunit_54
    locations_country_45.CountryCode = 'ZA'
    locations_country_45.ISO3CountryCode = 'ZAF'
    locations_country_45.PhonePrefix = '252'
    locations_country_45.InternetSuffix = '.za'
    locations_country_45.ISO3166Country = '710'
    locations_country_45 = importer.save_or_locate(locations_country_45)

    locations_country_46 = Country()
    locations_country_46.GeographicalUnitId = 'Country_SO'
    locations_country_46.GeographicalUnitCategory = 'Country'
    locations_country_46.GeographicalUnitName = 'Somalia'
    locations_country_46.GeographicalUnitShortName = 'Somalia'
    locations_country_46.HierarchyLevel = 30
    locations_country_46.IsPartOf = locations_geographicalunit_3
    locations_country_46.geographicalunit_ptr = locations_geographicalunit_55
    locations_country_46.CountryCode = 'SO'
    locations_country_46.ISO3CountryCode = 'SOM'
    locations_country_46.PhonePrefix = '677'
    locations_country_46.InternetSuffix = '.so'
    locations_country_46.ISO3166Country = '706'
    locations_country_46 = importer.save_or_locate(locations_country_46)

    locations_country_47 = Country()
    locations_country_47.GeographicalUnitId = 'Country_SB'
    locations_country_47.GeographicalUnitCategory = 'Country'
    locations_country_47.GeographicalUnitName = 'Solomon Islands'
    locations_country_47.GeographicalUnitShortName = 'Solomon Islands'
    locations_country_47.HierarchyLevel = 30
    locations_country_47.IsPartOf = locations_geographicalunit_6
    locations_country_47.geographicalunit_ptr = locations_geographicalunit_56
    locations_country_47.CountryCode = 'SB'
    locations_country_47.ISO3CountryCode = 'SLB'
    locations_country_47.PhonePrefix = '386'
    locations_country_47.InternetSuffix = '.sb'
    locations_country_47.ISO3166Country = '90'
    locations_country_47 = importer.save_or_locate(locations_country_47)

    locations_country_48 = Country()
    locations_country_48.GeographicalUnitId = 'Country_SI'
    locations_country_48.GeographicalUnitCategory = 'Country'
    locations_country_48.GeographicalUnitName = 'Slovenia'
    locations_country_48.GeographicalUnitShortName = 'Slovenia'
    locations_country_48.HierarchyLevel = 30
    locations_country_48.IsPartOf = locations_geographicalunit_2
    locations_country_48.geographicalunit_ptr = locations_geographicalunit_57
    locations_country_48.CountryCode = 'SI'
    locations_country_48.ISO3CountryCode = 'SVN'
    locations_country_48.PhonePrefix = '421'
    locations_country_48.InternetSuffix = '.si'
    locations_country_48.ISO3166Country = '705'
    locations_country_48 = importer.save_or_locate(locations_country_48)

    locations_country_49 = Country()
    locations_country_49.GeographicalUnitId = 'Country_SK'
    locations_country_49.GeographicalUnitCategory = 'Country'
    locations_country_49.GeographicalUnitName = 'Slovakia'
    locations_country_49.GeographicalUnitShortName = 'Slovakia'
    locations_country_49.HierarchyLevel = 30
    locations_country_49.IsPartOf = locations_geographicalunit_2
    locations_country_49.geographicalunit_ptr = locations_geographicalunit_58
    locations_country_49.CountryCode = 'SK'
    locations_country_49.ISO3CountryCode = 'SVK'
    locations_country_49.PhonePrefix = '1-721'
    locations_country_49.InternetSuffix = '.sk'
    locations_country_49.ISO3166Country = '703'
    locations_country_49 = importer.save_or_locate(locations_country_49)

    locations_country_50 = Country()
    locations_country_50.GeographicalUnitId = 'Country_SX'
    locations_country_50.GeographicalUnitCategory = 'Country'
    locations_country_50.GeographicalUnitName = 'Sint Maarten (Dutch part)'
    locations_country_50.GeographicalUnitShortName = 'Sint Maarten'
    locations_country_50.HierarchyLevel = 30
    locations_country_50.IsPartOf = locations_geographicalunit_7
    locations_country_50.geographicalunit_ptr = locations_geographicalunit_59
    locations_country_50.CountryCode = 'SX'
    locations_country_50.ISO3CountryCode = 'SXM'
    locations_country_50.PhonePrefix = '65'
    locations_country_50.InternetSuffix = '.sx'
    locations_country_50.ISO3166Country = '534'
    locations_country_50 = importer.save_or_locate(locations_country_50)

    locations_country_51 = Country()
    locations_country_51.GeographicalUnitId = 'Country_SG'
    locations_country_51.GeographicalUnitCategory = 'Country'
    locations_country_51.GeographicalUnitName = 'Singapore'
    locations_country_51.GeographicalUnitShortName = 'Singapore'
    locations_country_51.HierarchyLevel = 30
    locations_country_51.IsPartOf = locations_geographicalunit_5
    locations_country_51.geographicalunit_ptr = locations_geographicalunit_60
    locations_country_51.CountryCode = 'SG'
    locations_country_51.ISO3CountryCode = 'SGP'
    locations_country_51.PhonePrefix = '232'
    locations_country_51.InternetSuffix = '.sg'
    locations_country_51.ISO3166Country = '702'
    locations_country_51 = importer.save_or_locate(locations_country_51)

    locations_country_52 = Country()
    locations_country_52.GeographicalUnitId = 'Country_SL'
    locations_country_52.GeographicalUnitCategory = 'Country'
    locations_country_52.GeographicalUnitName = 'Sierra Leone'
    locations_country_52.GeographicalUnitShortName = 'Sierra Leone'
    locations_country_52.HierarchyLevel = 30
    locations_country_52.IsPartOf = locations_geographicalunit_3
    locations_country_52.geographicalunit_ptr = locations_geographicalunit_61
    locations_country_52.CountryCode = 'SL'
    locations_country_52.ISO3CountryCode = 'SLE'
    locations_country_52.PhonePrefix = '248'
    locations_country_52.InternetSuffix = '.sl'
    locations_country_52.ISO3166Country = '694'
    locations_country_52 = importer.save_or_locate(locations_country_52)

    locations_country_53 = Country()
    locations_country_53.GeographicalUnitId = 'Country_SC'
    locations_country_53.GeographicalUnitCategory = 'Country'
    locations_country_53.GeographicalUnitName = 'Seychelles'
    locations_country_53.GeographicalUnitShortName = 'Seychelles'
    locations_country_53.HierarchyLevel = 30
    locations_country_53.IsPartOf = locations_geographicalunit_3
    locations_country_53.geographicalunit_ptr = locations_geographicalunit_62
    locations_country_53.CountryCode = 'SC'
    locations_country_53.ISO3CountryCode = 'SYC'
    locations_country_53.PhonePrefix = '381'
    locations_country_53.InternetSuffix = '.sc'
    locations_country_53.ISO3166Country = '690'
    locations_country_53 = importer.save_or_locate(locations_country_53)

    locations_country_54 = Country()
    locations_country_54.GeographicalUnitId = 'Country_RS'
    locations_country_54.GeographicalUnitCategory = 'Country'
    locations_country_54.GeographicalUnitName = 'Serbia'
    locations_country_54.GeographicalUnitShortName = 'Serbia'
    locations_country_54.HierarchyLevel = 30
    locations_country_54.IsPartOf = locations_geographicalunit_2
    locations_country_54.geographicalunit_ptr = locations_geographicalunit_63
    locations_country_54.CountryCode = 'RS'
    locations_country_54.ISO3CountryCode = 'SRB'
    locations_country_54.PhonePrefix = '221'
    locations_country_54.InternetSuffix = '.rs'
    locations_country_54.ISO3166Country = '688'
    locations_country_54 = importer.save_or_locate(locations_country_54)

    locations_country_55 = Country()
    locations_country_55.GeographicalUnitId = 'Country_SN'
    locations_country_55.GeographicalUnitCategory = 'Country'
    locations_country_55.GeographicalUnitName = 'Senegal'
    locations_country_55.GeographicalUnitShortName = 'Senegal'
    locations_country_55.HierarchyLevel = 30
    locations_country_55.IsPartOf = locations_geographicalunit_3
    locations_country_55.geographicalunit_ptr = locations_geographicalunit_64
    locations_country_55.CountryCode = 'SN'
    locations_country_55.ISO3CountryCode = 'SEN'
    locations_country_55.PhonePrefix = '966'
    locations_country_55.InternetSuffix = '.sn'
    locations_country_55.ISO3166Country = '686'
    locations_country_55 = importer.save_or_locate(locations_country_55)

    locations_country_56 = Country()
    locations_country_56.GeographicalUnitId = 'Country_SA'
    locations_country_56.GeographicalUnitCategory = 'Country'
    locations_country_56.GeographicalUnitName = 'Saudi Arabia'
    locations_country_56.GeographicalUnitShortName = 'Saudi Arabia'
    locations_country_56.HierarchyLevel = 30
    locations_country_56.IsPartOf = locations_geographicalunit_5
    locations_country_56.geographicalunit_ptr = locations_geographicalunit_65
    locations_country_56.CountryCode = 'SA'
    locations_country_56.ISO3CountryCode = 'SAU'
    locations_country_56.PhonePrefix = '239'
    locations_country_56.InternetSuffix = '.sa'
    locations_country_56.ISO3166Country = '682'
    locations_country_56 = importer.save_or_locate(locations_country_56)

    locations_country_57 = Country()
    locations_country_57.GeographicalUnitId = 'Country_ST'
    locations_country_57.GeographicalUnitCategory = 'Country'
    locations_country_57.GeographicalUnitName = 'Sao Tome and Principe'
    locations_country_57.GeographicalUnitShortName = 'Sao Tome and Principe'
    locations_country_57.HierarchyLevel = 30
    locations_country_57.IsPartOf = locations_geographicalunit_3
    locations_country_57.geographicalunit_ptr = locations_geographicalunit_66
    locations_country_57.CountryCode = 'ST'
    locations_country_57.ISO3CountryCode = 'STP'
    locations_country_57.PhonePrefix = '378'
    locations_country_57.InternetSuffix = '.st'
    locations_country_57.ISO3166Country = '678'
    locations_country_57 = importer.save_or_locate(locations_country_57)

    locations_country_58 = Country()
    locations_country_58.GeographicalUnitId = 'Country_SM'
    locations_country_58.GeographicalUnitCategory = 'Country'
    locations_country_58.GeographicalUnitName = 'San Marino'
    locations_country_58.GeographicalUnitShortName = 'San Marino'
    locations_country_58.HierarchyLevel = 30
    locations_country_58.IsPartOf = locations_geographicalunit_2
    locations_country_58.geographicalunit_ptr = locations_geographicalunit_67
    locations_country_58.CountryCode = 'SM'
    locations_country_58.ISO3CountryCode = 'SMR'
    locations_country_58.PhonePrefix = '685'
    locations_country_58.InternetSuffix = '.sm'
    locations_country_58.ISO3166Country = '674'
    locations_country_58 = importer.save_or_locate(locations_country_58)

    locations_country_59 = Country()
    locations_country_59.GeographicalUnitId = 'Country_WS'
    locations_country_59.GeographicalUnitCategory = 'Country'
    locations_country_59.GeographicalUnitName = 'Samoa'
    locations_country_59.GeographicalUnitShortName = 'Samoa'
    locations_country_59.HierarchyLevel = 30
    locations_country_59.IsPartOf = locations_geographicalunit_6
    locations_country_59.geographicalunit_ptr = locations_geographicalunit_68
    locations_country_59.CountryCode = 'WS'
    locations_country_59.ISO3CountryCode = 'WSM'
    locations_country_59.PhonePrefix = '1-784'
    locations_country_59.InternetSuffix = '.ws'
    locations_country_59.ISO3166Country = '882'
    locations_country_59 = importer.save_or_locate(locations_country_59)

    locations_country_60 = Country()
    locations_country_60.GeographicalUnitId = 'Country_VC'
    locations_country_60.GeographicalUnitCategory = 'Country'
    locations_country_60.GeographicalUnitName = 'Saint Vincent and the Grenadines'
    locations_country_60.GeographicalUnitShortName = 'Saint Vincent and the Grenadines'
    locations_country_60.HierarchyLevel = 30
    locations_country_60.IsPartOf = locations_geographicalunit_7
    locations_country_60.geographicalunit_ptr = locations_geographicalunit_69
    locations_country_60.CountryCode = 'VC'
    locations_country_60.ISO3CountryCode = 'VCT'
    locations_country_60.PhonePrefix = '508'
    locations_country_60.InternetSuffix = '.vc'
    locations_country_60.ISO3166Country = '670'
    locations_country_60 = importer.save_or_locate(locations_country_60)

    locations_country_61 = Country()
    locations_country_61.GeographicalUnitId = 'Country_PM'
    locations_country_61.GeographicalUnitCategory = 'Country'
    locations_country_61.GeographicalUnitName = 'Saint Pierre and Miquelon'
    locations_country_61.GeographicalUnitShortName = 'Saint Pierre and Miquelon'
    locations_country_61.HierarchyLevel = 30
    locations_country_61.IsPartOf = locations_geographicalunit_7
    locations_country_61.geographicalunit_ptr = locations_geographicalunit_70
    locations_country_61.CountryCode = 'PM'
    locations_country_61.ISO3CountryCode = 'SPM'
    locations_country_61.PhonePrefix = '590'
    locations_country_61.InternetSuffix = '.pm'
    locations_country_61.ISO3166Country = '666'
    locations_country_61 = importer.save_or_locate(locations_country_61)

    locations_country_62 = Country()
    locations_country_62.GeographicalUnitId = 'Country_MF'
    locations_country_62.GeographicalUnitCategory = 'Country'
    locations_country_62.GeographicalUnitName = 'Saint Martin (French part)'
    locations_country_62.GeographicalUnitShortName = 'Saint Martin'
    locations_country_62.HierarchyLevel = 30
    locations_country_62.IsPartOf = locations_geographicalunit_7
    locations_country_62.geographicalunit_ptr = locations_geographicalunit_71
    locations_country_62.CountryCode = 'MF'
    locations_country_62.ISO3CountryCode = 'MAF'
    locations_country_62.PhonePrefix = '1-758'
    locations_country_62.InternetSuffix = '.mf'
    locations_country_62.ISO3166Country = '663'
    locations_country_62 = importer.save_or_locate(locations_country_62)

    locations_country_63 = Country()
    locations_country_63.GeographicalUnitId = 'Country_LC'
    locations_country_63.GeographicalUnitCategory = 'Country'
    locations_country_63.GeographicalUnitName = 'Saint Lucia'
    locations_country_63.GeographicalUnitShortName = 'Saint Lucia'
    locations_country_63.HierarchyLevel = 30
    locations_country_63.IsPartOf = locations_geographicalunit_7
    locations_country_63.geographicalunit_ptr = locations_geographicalunit_72
    locations_country_63.CountryCode = 'LC'
    locations_country_63.ISO3CountryCode = 'LCA'
    locations_country_63.PhonePrefix = '1-869'
    locations_country_63.InternetSuffix = '.lc'
    locations_country_63.ISO3166Country = '662'
    locations_country_63 = importer.save_or_locate(locations_country_63)

    locations_country_64 = Country()
    locations_country_64.GeographicalUnitId = 'Country_KN'
    locations_country_64.GeographicalUnitCategory = 'Country'
    locations_country_64.GeographicalUnitName = 'Saint Kitts and Nevis'
    locations_country_64.GeographicalUnitShortName = 'Saint Kitts and Nevis'
    locations_country_64.HierarchyLevel = 30
    locations_country_64.IsPartOf = locations_geographicalunit_7
    locations_country_64.geographicalunit_ptr = locations_geographicalunit_73
    locations_country_64.CountryCode = 'KN'
    locations_country_64.ISO3CountryCode = 'KNA'
    locations_country_64.PhonePrefix = '290'
    locations_country_64.InternetSuffix = '.kn'
    locations_country_64.ISO3166Country = '659'
    locations_country_64 = importer.save_or_locate(locations_country_64)

    locations_country_65 = Country()
    locations_country_65.GeographicalUnitId = 'Country_SH'
    locations_country_65.GeographicalUnitCategory = 'Country'
    locations_country_65.GeographicalUnitName = 'Saint Helena, Ascension and Tristan da Cunha'
    locations_country_65.GeographicalUnitShortName = 'Saint Helena, Ascension and Tristan da Cunha'
    locations_country_65.HierarchyLevel = 30
    locations_country_65.IsPartOf = locations_geographicalunit_3
    locations_country_65.geographicalunit_ptr = locations_geographicalunit_74
    locations_country_65.CountryCode = 'SH'
    locations_country_65.ISO3CountryCode = 'SHN'
    locations_country_65.PhonePrefix = '590'
    locations_country_65.InternetSuffix = '.sh'
    locations_country_65.ISO3166Country = '654'
    locations_country_65 = importer.save_or_locate(locations_country_65)

    locations_country_66 = Country()
    locations_country_66.GeographicalUnitId = 'Country_BL'
    locations_country_66.GeographicalUnitCategory = 'Country'
    locations_country_66.GeographicalUnitName = 'Saint Barthélemy'
    locations_country_66.GeographicalUnitShortName = 'Saint Barthélemy'
    locations_country_66.HierarchyLevel = 30
    locations_country_66.IsPartOf = locations_geographicalunit_7
    locations_country_66.geographicalunit_ptr = locations_geographicalunit_75
    locations_country_66.CountryCode = 'BL'
    locations_country_66.ISO3CountryCode = 'BLM'
    locations_country_66.PhonePrefix = '262'
    locations_country_66.InternetSuffix = '.bl'
    locations_country_66.ISO3166Country = '652'
    locations_country_66 = importer.save_or_locate(locations_country_66)

    locations_country_67 = Country()
    locations_country_67.GeographicalUnitId = 'Country_RE'
    locations_country_67.GeographicalUnitCategory = 'Country'
    locations_country_67.GeographicalUnitName = 'Réunion'
    locations_country_67.GeographicalUnitShortName = 'Réunion'
    locations_country_67.HierarchyLevel = 30
    locations_country_67.IsPartOf = locations_geographicalunit_3
    locations_country_67.geographicalunit_ptr = locations_geographicalunit_76
    locations_country_67.CountryCode = 'RE'
    locations_country_67.ISO3CountryCode = 'REU'
    locations_country_67.PhonePrefix = '250'
    locations_country_67.InternetSuffix = '.re'
    locations_country_67.ISO3166Country = '638'
    locations_country_67 = importer.save_or_locate(locations_country_67)

    locations_country_68 = Country()
    locations_country_68.GeographicalUnitId = 'Country_RW'
    locations_country_68.GeographicalUnitCategory = 'Country'
    locations_country_68.GeographicalUnitName = 'Rwanda'
    locations_country_68.GeographicalUnitShortName = 'Rwanda'
    locations_country_68.HierarchyLevel = 30
    locations_country_68.IsPartOf = locations_geographicalunit_3
    locations_country_68.geographicalunit_ptr = locations_geographicalunit_77
    locations_country_68.CountryCode = 'RW'
    locations_country_68.ISO3CountryCode = 'RWA'
    locations_country_68.PhonePrefix = '7'
    locations_country_68.InternetSuffix = '.rw'
    locations_country_68.ISO3166Country = '646'
    locations_country_68 = importer.save_or_locate(locations_country_68)

    locations_country_69 = Country()
    locations_country_69.GeographicalUnitId = 'Country_RU'
    locations_country_69.GeographicalUnitCategory = 'Country'
    locations_country_69.GeographicalUnitName = 'Russian Federation (the)'
    locations_country_69.GeographicalUnitShortName = 'Russia'
    locations_country_69.HierarchyLevel = 30
    locations_country_69.IsPartOf = locations_geographicalunit_2
    locations_country_69.geographicalunit_ptr = locations_geographicalunit_78
    locations_country_69.CountryCode = 'RU'
    locations_country_69.ISO3CountryCode = 'RUS'
    locations_country_69.PhonePrefix = '40'
    locations_country_69.InternetSuffix = '.ru'
    locations_country_69.ISO3166Country = '643'
    locations_country_69 = importer.save_or_locate(locations_country_69)

    locations_country_70 = Country()
    locations_country_70.GeographicalUnitId = 'Country_RO'
    locations_country_70.GeographicalUnitCategory = 'Country'
    locations_country_70.GeographicalUnitName = 'Romania'
    locations_country_70.GeographicalUnitShortName = 'Romania'
    locations_country_70.HierarchyLevel = 30
    locations_country_70.IsPartOf = locations_geographicalunit_2
    locations_country_70.geographicalunit_ptr = locations_geographicalunit_79
    locations_country_70.CountryCode = 'RO'
    locations_country_70.ISO3CountryCode = 'ROU'
    locations_country_70.PhonePrefix = '389'
    locations_country_70.InternetSuffix = '.ro'
    locations_country_70.ISO3166Country = '642'
    locations_country_70 = importer.save_or_locate(locations_country_70)

    locations_country_71 = Country()
    locations_country_71.GeographicalUnitId = 'Country_MK'
    locations_country_71.GeographicalUnitCategory = 'Country'
    locations_country_71.GeographicalUnitName = 'Republic of North Macedonia'
    locations_country_71.GeographicalUnitShortName = 'North Macedonia'
    locations_country_71.HierarchyLevel = 30
    locations_country_71.IsPartOf = locations_geographicalunit_2
    locations_country_71.geographicalunit_ptr = locations_geographicalunit_80
    locations_country_71.CountryCode = 'MK'
    locations_country_71.ISO3CountryCode = 'MKD'
    locations_country_71.PhonePrefix = '974'
    locations_country_71.InternetSuffix = '.mk'
    locations_country_71.ISO3166Country = '807'
    locations_country_71 = importer.save_or_locate(locations_country_71)

    locations_country_72 = Country()
    locations_country_72.GeographicalUnitId = 'Country_QA'
    locations_country_72.GeographicalUnitCategory = 'Country'
    locations_country_72.GeographicalUnitName = 'Qatar'
    locations_country_72.GeographicalUnitShortName = 'Qatar'
    locations_country_72.HierarchyLevel = 30
    locations_country_72.IsPartOf = locations_geographicalunit_5
    locations_country_72.geographicalunit_ptr = locations_geographicalunit_81
    locations_country_72.CountryCode = 'QA'
    locations_country_72.ISO3CountryCode = 'QAT'
    locations_country_72.PhonePrefix = '1-787, 1-939'
    locations_country_72.InternetSuffix = '.qa'
    locations_country_72.ISO3166Country = '634'
    locations_country_72 = importer.save_or_locate(locations_country_72)

    locations_country_73 = Country()
    locations_country_73.GeographicalUnitId = 'Country_PR'
    locations_country_73.GeographicalUnitCategory = 'Country'
    locations_country_73.GeographicalUnitName = 'Puerto Rico'
    locations_country_73.GeographicalUnitShortName = 'Puerto Rico'
    locations_country_73.HierarchyLevel = 30
    locations_country_73.IsPartOf = locations_geographicalunit_7
    locations_country_73.geographicalunit_ptr = locations_geographicalunit_82
    locations_country_73.CountryCode = 'PR'
    locations_country_73.ISO3CountryCode = 'PRI'
    locations_country_73.PhonePrefix = '351'
    locations_country_73.InternetSuffix = '.pr'
    locations_country_73.ISO3166Country = '630'
    locations_country_73 = importer.save_or_locate(locations_country_73)

    locations_country_74 = Country()
    locations_country_74.GeographicalUnitId = 'Country_PT'
    locations_country_74.GeographicalUnitCategory = 'Country'
    locations_country_74.GeographicalUnitName = 'Portugal'
    locations_country_74.GeographicalUnitShortName = 'Portugal'
    locations_country_74.HierarchyLevel = 30
    locations_country_74.IsPartOf = locations_geographicalunit_2
    locations_country_74.geographicalunit_ptr = locations_geographicalunit_83
    locations_country_74.CountryCode = 'PT'
    locations_country_74.ISO3CountryCode = 'PRT'
    locations_country_74.PhonePrefix = '48'
    locations_country_74.InternetSuffix = '.pt'
    locations_country_74.ISO3166Country = '620'
    locations_country_74 = importer.save_or_locate(locations_country_74)

    locations_country_75 = Country()
    locations_country_75.GeographicalUnitId = 'Country_PL'
    locations_country_75.GeographicalUnitCategory = 'Country'
    locations_country_75.GeographicalUnitName = 'Poland'
    locations_country_75.GeographicalUnitShortName = 'Poland'
    locations_country_75.HierarchyLevel = 30
    locations_country_75.IsPartOf = locations_geographicalunit_2
    locations_country_75.geographicalunit_ptr = locations_geographicalunit_84
    locations_country_75.CountryCode = 'PL'
    locations_country_75.ISO3CountryCode = 'POL'
    locations_country_75.PhonePrefix = '64'
    locations_country_75.InternetSuffix = '.pl'
    locations_country_75.ISO3166Country = '616'
    locations_country_75 = importer.save_or_locate(locations_country_75)

    locations_country_76 = Country()
    locations_country_76.GeographicalUnitId = 'Country_PN'
    locations_country_76.GeographicalUnitCategory = 'Country'
    locations_country_76.GeographicalUnitName = 'Pitcairn'
    locations_country_76.GeographicalUnitShortName = 'Pitcairn'
    locations_country_76.HierarchyLevel = 30
    locations_country_76.IsPartOf = locations_geographicalunit_6
    locations_country_76.geographicalunit_ptr = locations_geographicalunit_85
    locations_country_76.CountryCode = 'PN'
    locations_country_76.ISO3CountryCode = 'PCN'
    locations_country_76.PhonePrefix = '63'
    locations_country_76.InternetSuffix = '.pn'
    locations_country_76.ISO3166Country = '612'
    locations_country_76 = importer.save_or_locate(locations_country_76)

    locations_country_77 = Country()
    locations_country_77.GeographicalUnitId = 'Country_PH'
    locations_country_77.GeographicalUnitCategory = 'Country'
    locations_country_77.GeographicalUnitName = 'Philippines (the)'
    locations_country_77.GeographicalUnitShortName = 'Philippines'
    locations_country_77.HierarchyLevel = 30
    locations_country_77.IsPartOf = locations_geographicalunit_5
    locations_country_77.geographicalunit_ptr = locations_geographicalunit_86
    locations_country_77.CountryCode = 'PH'
    locations_country_77.ISO3CountryCode = 'PHL'
    locations_country_77.PhonePrefix = '51'
    locations_country_77.InternetSuffix = '.ph'
    locations_country_77.ISO3166Country = '608'
    locations_country_77 = importer.save_or_locate(locations_country_77)

    locations_country_78 = Country()
    locations_country_78.GeographicalUnitId = 'Country_PE'
    locations_country_78.GeographicalUnitCategory = 'Country'
    locations_country_78.GeographicalUnitName = 'Peru'
    locations_country_78.GeographicalUnitShortName = 'Peru'
    locations_country_78.HierarchyLevel = 30
    locations_country_78.IsPartOf = locations_geographicalunit_8
    locations_country_78.geographicalunit_ptr = locations_geographicalunit_87
    locations_country_78.CountryCode = 'PE'
    locations_country_78.ISO3CountryCode = 'PER'
    locations_country_78.PhonePrefix = '595'
    locations_country_78.InternetSuffix = '.pe'
    locations_country_78.ISO3166Country = '604'
    locations_country_78 = importer.save_or_locate(locations_country_78)

    locations_country_79 = Country()
    locations_country_79.GeographicalUnitId = 'Country_PY'
    locations_country_79.GeographicalUnitCategory = 'Country'
    locations_country_79.GeographicalUnitName = 'Paraguay'
    locations_country_79.GeographicalUnitShortName = 'Paraguay'
    locations_country_79.HierarchyLevel = 30
    locations_country_79.IsPartOf = locations_geographicalunit_8
    locations_country_79.geographicalunit_ptr = locations_geographicalunit_88
    locations_country_79.CountryCode = 'PY'
    locations_country_79.ISO3CountryCode = 'PRY'
    locations_country_79.PhonePrefix = '675'
    locations_country_79.InternetSuffix = '.py'
    locations_country_79.ISO3166Country = '600'
    locations_country_79 = importer.save_or_locate(locations_country_79)

    locations_country_80 = Country()
    locations_country_80.GeographicalUnitId = 'Country_PG'
    locations_country_80.GeographicalUnitCategory = 'Country'
    locations_country_80.GeographicalUnitName = 'Papua New Guinea'
    locations_country_80.GeographicalUnitShortName = 'Papua New Guinea'
    locations_country_80.HierarchyLevel = 30
    locations_country_80.IsPartOf = locations_geographicalunit_6
    locations_country_80.geographicalunit_ptr = locations_geographicalunit_89
    locations_country_80.CountryCode = 'PG'
    locations_country_80.ISO3CountryCode = 'PNG'
    locations_country_80.PhonePrefix = '507'
    locations_country_80.InternetSuffix = '.pg'
    locations_country_80.ISO3166Country = '598'
    locations_country_80 = importer.save_or_locate(locations_country_80)

    locations_country_81 = Country()
    locations_country_81.GeographicalUnitId = 'Country_PA'
    locations_country_81.GeographicalUnitCategory = 'Country'
    locations_country_81.GeographicalUnitName = 'Panama'
    locations_country_81.GeographicalUnitShortName = 'Panama'
    locations_country_81.HierarchyLevel = 30
    locations_country_81.IsPartOf = locations_geographicalunit_7
    locations_country_81.geographicalunit_ptr = locations_geographicalunit_90
    locations_country_81.CountryCode = 'PA'
    locations_country_81.ISO3CountryCode = 'PAN'
    locations_country_81.PhonePrefix = '970'
    locations_country_81.InternetSuffix = '.pa'
    locations_country_81.ISO3166Country = '591'
    locations_country_81 = importer.save_or_locate(locations_country_81)

    locations_country_82 = Country()
    locations_country_82.GeographicalUnitId = 'Country_PS'
    locations_country_82.GeographicalUnitCategory = 'Country'
    locations_country_82.GeographicalUnitName = 'Palestine, State of'
    locations_country_82.GeographicalUnitShortName = 'Palestine'
    locations_country_82.HierarchyLevel = 30
    locations_country_82.IsPartOf = locations_geographicalunit_5
    locations_country_82.geographicalunit_ptr = locations_geographicalunit_91
    locations_country_82.CountryCode = 'PS'
    locations_country_82.ISO3CountryCode = 'PSE'
    locations_country_82.PhonePrefix = '680'
    locations_country_82.InternetSuffix = '.ps'
    locations_country_82.ISO3166Country = '275'
    locations_country_82 = importer.save_or_locate(locations_country_82)

    locations_country_83 = Country()
    locations_country_83.GeographicalUnitId = 'Country_PW'
    locations_country_83.GeographicalUnitCategory = 'Country'
    locations_country_83.GeographicalUnitName = 'Palau'
    locations_country_83.GeographicalUnitShortName = 'Palau'
    locations_country_83.HierarchyLevel = 30
    locations_country_83.IsPartOf = locations_geographicalunit_6
    locations_country_83.geographicalunit_ptr = locations_geographicalunit_92
    locations_country_83.CountryCode = 'PW'
    locations_country_83.ISO3CountryCode = 'PLW'
    locations_country_83.PhonePrefix = '92'
    locations_country_83.InternetSuffix = '.pw'
    locations_country_83.ISO3166Country = '585'
    locations_country_83 = importer.save_or_locate(locations_country_83)

    locations_country_84 = Country()
    locations_country_84.GeographicalUnitId = 'Country_PK'
    locations_country_84.GeographicalUnitCategory = 'Country'
    locations_country_84.GeographicalUnitName = 'Pakistan'
    locations_country_84.GeographicalUnitShortName = 'Pakistan'
    locations_country_84.HierarchyLevel = 30
    locations_country_84.IsPartOf = locations_geographicalunit_5
    locations_country_84.geographicalunit_ptr = locations_geographicalunit_93
    locations_country_84.CountryCode = 'PK'
    locations_country_84.ISO3CountryCode = 'PAK'
    locations_country_84.PhonePrefix = '968'
    locations_country_84.InternetSuffix = '.pk'
    locations_country_84.ISO3166Country = '586'
    locations_country_84 = importer.save_or_locate(locations_country_84)

    locations_country_85 = Country()
    locations_country_85.GeographicalUnitId = 'Country_OM'
    locations_country_85.GeographicalUnitCategory = 'Country'
    locations_country_85.GeographicalUnitName = 'Oman'
    locations_country_85.GeographicalUnitShortName = 'Oman'
    locations_country_85.HierarchyLevel = 30
    locations_country_85.IsPartOf = locations_geographicalunit_5
    locations_country_85.geographicalunit_ptr = locations_geographicalunit_94
    locations_country_85.CountryCode = 'OM'
    locations_country_85.ISO3CountryCode = 'OMN'
    locations_country_85.PhonePrefix = '47'
    locations_country_85.InternetSuffix = '.om'
    locations_country_85.ISO3166Country = '512'
    locations_country_85 = importer.save_or_locate(locations_country_85)

    locations_country_86 = Country()
    locations_country_86.GeographicalUnitId = 'Country_NO'
    locations_country_86.GeographicalUnitCategory = 'Country'
    locations_country_86.GeographicalUnitName = 'Norway'
    locations_country_86.GeographicalUnitShortName = 'Norway'
    locations_country_86.HierarchyLevel = 30
    locations_country_86.IsPartOf = locations_geographicalunit_2
    locations_country_86.geographicalunit_ptr = locations_geographicalunit_95
    locations_country_86.CountryCode = 'NO'
    locations_country_86.ISO3CountryCode = 'NOR'
    locations_country_86.PhonePrefix = '1-670'
    locations_country_86.InternetSuffix = '.no'
    locations_country_86.ISO3166Country = '578'
    locations_country_86 = importer.save_or_locate(locations_country_86)

    locations_country_87 = Country()
    locations_country_87.GeographicalUnitId = 'Country_MP'
    locations_country_87.GeographicalUnitCategory = 'Country'
    locations_country_87.GeographicalUnitName = 'Northern Mariana Islands (the)'
    locations_country_87.GeographicalUnitShortName = 'Northern Mariana Islands'
    locations_country_87.HierarchyLevel = 30
    locations_country_87.IsPartOf = locations_geographicalunit_6
    locations_country_87.geographicalunit_ptr = locations_geographicalunit_96
    locations_country_87.CountryCode = 'MP'
    locations_country_87.ISO3CountryCode = 'MNP'
    locations_country_87.PhonePrefix = None
    locations_country_87.InternetSuffix = '.mp'
    locations_country_87.ISO3166Country = '580'
    locations_country_87 = importer.save_or_locate(locations_country_87)

    locations_country_88 = Country()
    locations_country_88.GeographicalUnitId = 'Country_NF'
    locations_country_88.GeographicalUnitCategory = 'Country'
    locations_country_88.GeographicalUnitName = 'Norfolk Island'
    locations_country_88.GeographicalUnitShortName = 'Norfolk Island'
    locations_country_88.HierarchyLevel = 30
    locations_country_88.IsPartOf = locations_geographicalunit_6
    locations_country_88.geographicalunit_ptr = locations_geographicalunit_97
    locations_country_88.CountryCode = 'NF'
    locations_country_88.ISO3CountryCode = 'NFK'
    locations_country_88.PhonePrefix = '683'
    locations_country_88.InternetSuffix = '.nf'
    locations_country_88.ISO3166Country = '574'
    locations_country_88 = importer.save_or_locate(locations_country_88)

    locations_country_89 = Country()
    locations_country_89.GeographicalUnitId = 'Country_NU'
    locations_country_89.GeographicalUnitCategory = 'Country'
    locations_country_89.GeographicalUnitName = 'Niue'
    locations_country_89.GeographicalUnitShortName = 'Niue'
    locations_country_89.HierarchyLevel = 30
    locations_country_89.IsPartOf = locations_geographicalunit_6
    locations_country_89.geographicalunit_ptr = locations_geographicalunit_98
    locations_country_89.CountryCode = 'NU'
    locations_country_89.ISO3CountryCode = 'NIU'
    locations_country_89.PhonePrefix = '234'
    locations_country_89.InternetSuffix = '.nu'
    locations_country_89.ISO3166Country = '570'
    locations_country_89 = importer.save_or_locate(locations_country_89)

    locations_country_90 = Country()
    locations_country_90.GeographicalUnitId = 'Country_NG'
    locations_country_90.GeographicalUnitCategory = 'Country'
    locations_country_90.GeographicalUnitName = 'Nigeria'
    locations_country_90.GeographicalUnitShortName = 'Nigeria'
    locations_country_90.HierarchyLevel = 30
    locations_country_90.IsPartOf = locations_geographicalunit_3
    locations_country_90.geographicalunit_ptr = locations_geographicalunit_99
    locations_country_90.CountryCode = 'NG'
    locations_country_90.ISO3CountryCode = 'NGA'
    locations_country_90.PhonePrefix = '227'
    locations_country_90.InternetSuffix = '.ng'
    locations_country_90.ISO3166Country = '566'
    locations_country_90 = importer.save_or_locate(locations_country_90)

    locations_country_91 = Country()
    locations_country_91.GeographicalUnitId = 'Country_NE'
    locations_country_91.GeographicalUnitCategory = 'Country'
    locations_country_91.GeographicalUnitName = 'Niger (the)'
    locations_country_91.GeographicalUnitShortName = 'Niger (the)'
    locations_country_91.HierarchyLevel = 30
    locations_country_91.IsPartOf = locations_geographicalunit_3
    locations_country_91.geographicalunit_ptr = locations_geographicalunit_100
    locations_country_91.CountryCode = 'NE'
    locations_country_91.ISO3CountryCode = 'NER'
    locations_country_91.PhonePrefix = '505'
    locations_country_91.InternetSuffix = '.ne'
    locations_country_91.ISO3166Country = '562'
    locations_country_91 = importer.save_or_locate(locations_country_91)

    locations_country_92 = Country()
    locations_country_92.GeographicalUnitId = 'Country_NI'
    locations_country_92.GeographicalUnitCategory = 'Country'
    locations_country_92.GeographicalUnitName = 'Nicaragua'
    locations_country_92.GeographicalUnitShortName = 'Nicaragua'
    locations_country_92.HierarchyLevel = 30
    locations_country_92.IsPartOf = locations_geographicalunit_7
    locations_country_92.geographicalunit_ptr = locations_geographicalunit_101
    locations_country_92.CountryCode = 'NI'
    locations_country_92.ISO3CountryCode = 'NIC'
    locations_country_92.PhonePrefix = '64'
    locations_country_92.InternetSuffix = '.ni'
    locations_country_92.ISO3166Country = '558'
    locations_country_92 = importer.save_or_locate(locations_country_92)

    locations_country_93 = Country()
    locations_country_93.GeographicalUnitId = 'Country_NZ'
    locations_country_93.GeographicalUnitCategory = 'Country'
    locations_country_93.GeographicalUnitName = 'New Zealand'
    locations_country_93.GeographicalUnitShortName = 'New Zealand'
    locations_country_93.HierarchyLevel = 30
    locations_country_93.IsPartOf = locations_geographicalunit_6
    locations_country_93.geographicalunit_ptr = locations_geographicalunit_102
    locations_country_93.CountryCode = 'NZ'
    locations_country_93.ISO3CountryCode = 'NZL'
    locations_country_93.PhonePrefix = '687'
    locations_country_93.InternetSuffix = '.nz'
    locations_country_93.ISO3166Country = '554'
    locations_country_93 = importer.save_or_locate(locations_country_93)

    locations_country_94 = Country()
    locations_country_94.GeographicalUnitId = 'Country_NC'
    locations_country_94.GeographicalUnitCategory = 'Country'
    locations_country_94.GeographicalUnitName = 'New Caledonia'
    locations_country_94.GeographicalUnitShortName = 'New Caledonia'
    locations_country_94.HierarchyLevel = 30
    locations_country_94.IsPartOf = locations_geographicalunit_6
    locations_country_94.geographicalunit_ptr = locations_geographicalunit_103
    locations_country_94.CountryCode = 'NC'
    locations_country_94.ISO3CountryCode = 'NCL'
    locations_country_94.PhonePrefix = '31'
    locations_country_94.InternetSuffix = '.nc'
    locations_country_94.ISO3166Country = '540'
    locations_country_94 = importer.save_or_locate(locations_country_94)

    locations_country_95 = Country()
    locations_country_95.GeographicalUnitId = 'Country_NL'
    locations_country_95.GeographicalUnitCategory = 'Country'
    locations_country_95.GeographicalUnitName = 'Netherlands (the)'
    locations_country_95.GeographicalUnitShortName = 'Netherlands'
    locations_country_95.HierarchyLevel = 30
    locations_country_95.IsPartOf = locations_geographicalunit_2
    locations_country_95.geographicalunit_ptr = locations_geographicalunit_104
    locations_country_95.CountryCode = 'NL'
    locations_country_95.ISO3CountryCode = 'NLD'
    locations_country_95.PhonePrefix = '977'
    locations_country_95.InternetSuffix = '.nl'
    locations_country_95.ISO3166Country = '528'
    locations_country_95 = importer.save_or_locate(locations_country_95)

    locations_country_96 = Country()
    locations_country_96.GeographicalUnitId = 'Country_NP'
    locations_country_96.GeographicalUnitCategory = 'Country'
    locations_country_96.GeographicalUnitName = 'Nepal'
    locations_country_96.GeographicalUnitShortName = 'Nepal'
    locations_country_96.HierarchyLevel = 30
    locations_country_96.IsPartOf = locations_geographicalunit_5
    locations_country_96.geographicalunit_ptr = locations_geographicalunit_105
    locations_country_96.CountryCode = 'NP'
    locations_country_96.ISO3CountryCode = 'NPL'
    locations_country_96.PhonePrefix = '674'
    locations_country_96.InternetSuffix = '.np'
    locations_country_96.ISO3166Country = '524'
    locations_country_96 = importer.save_or_locate(locations_country_96)

    locations_country_97 = Country()
    locations_country_97.GeographicalUnitId = 'Country_NR'
    locations_country_97.GeographicalUnitCategory = 'Country'
    locations_country_97.GeographicalUnitName = 'Nauru'
    locations_country_97.GeographicalUnitShortName = 'Nauru'
    locations_country_97.HierarchyLevel = 30
    locations_country_97.IsPartOf = locations_geographicalunit_6
    locations_country_97.geographicalunit_ptr = locations_geographicalunit_106
    locations_country_97.CountryCode = 'NR'
    locations_country_97.ISO3CountryCode = 'NRU'
    locations_country_97.PhonePrefix = '264'
    locations_country_97.InternetSuffix = '.nr'
    locations_country_97.ISO3166Country = '520'
    locations_country_97 = importer.save_or_locate(locations_country_97)

    locations_country_98 = Country()
    locations_country_98.GeographicalUnitId = 'Country_NA'
    locations_country_98.GeographicalUnitCategory = 'Country'
    locations_country_98.GeographicalUnitName = 'Namibia'
    locations_country_98.GeographicalUnitShortName = 'Namibia'
    locations_country_98.HierarchyLevel = 30
    locations_country_98.IsPartOf = locations_geographicalunit_3
    locations_country_98.geographicalunit_ptr = locations_geographicalunit_107
    locations_country_98.CountryCode = 'NA'
    locations_country_98.ISO3CountryCode = 'NAM'
    locations_country_98.PhonePrefix = '95'
    locations_country_98.InternetSuffix = '.na'
    locations_country_98.ISO3166Country = '516'
    locations_country_98 = importer.save_or_locate(locations_country_98)

    locations_country_99 = Country()
    locations_country_99.GeographicalUnitId = 'Country_MM'
    locations_country_99.GeographicalUnitCategory = 'Country'
    locations_country_99.GeographicalUnitName = 'Myanmar'
    locations_country_99.GeographicalUnitShortName = 'Myanmar'
    locations_country_99.HierarchyLevel = 30
    locations_country_99.IsPartOf = locations_geographicalunit_5
    locations_country_99.geographicalunit_ptr = locations_geographicalunit_108
    locations_country_99.CountryCode = 'MM'
    locations_country_99.ISO3CountryCode = 'MMR'
    locations_country_99.PhonePrefix = '258'
    locations_country_99.InternetSuffix = '.mm'
    locations_country_99.ISO3166Country = '104'
    locations_country_99 = importer.save_or_locate(locations_country_99)

    locations_country_100 = Country()
    locations_country_100.GeographicalUnitId = 'Country_MZ'
    locations_country_100.GeographicalUnitCategory = 'Country'
    locations_country_100.GeographicalUnitName = 'Mozambique'
    locations_country_100.GeographicalUnitShortName = 'Mozambique'
    locations_country_100.HierarchyLevel = 30
    locations_country_100.IsPartOf = locations_geographicalunit_3
    locations_country_100.geographicalunit_ptr = locations_geographicalunit_109
    locations_country_100.CountryCode = 'MZ'
    locations_country_100.ISO3CountryCode = 'MOZ'
    locations_country_100.PhonePrefix = '212'
    locations_country_100.InternetSuffix = '.mz'
    locations_country_100.ISO3166Country = '508'
    locations_country_100 = importer.save_or_locate(locations_country_100)

    locations_country_101 = Country()
    locations_country_101.GeographicalUnitId = 'Country_MA'
    locations_country_101.GeographicalUnitCategory = 'Country'
    locations_country_101.GeographicalUnitName = 'Morocco'
    locations_country_101.GeographicalUnitShortName = 'Morocco'
    locations_country_101.HierarchyLevel = 30
    locations_country_101.IsPartOf = locations_geographicalunit_3
    locations_country_101.geographicalunit_ptr = locations_geographicalunit_110
    locations_country_101.CountryCode = 'MA'
    locations_country_101.ISO3CountryCode = 'MAR'
    locations_country_101.PhonePrefix = '1-664'
    locations_country_101.InternetSuffix = '.ma'
    locations_country_101.ISO3166Country = '504'
    locations_country_101 = importer.save_or_locate(locations_country_101)

    locations_country_102 = Country()
    locations_country_102.GeographicalUnitId = 'Country_MS'
    locations_country_102.GeographicalUnitCategory = 'Country'
    locations_country_102.GeographicalUnitName = 'Montserrat'
    locations_country_102.GeographicalUnitShortName = 'Montserrat'
    locations_country_102.HierarchyLevel = 30
    locations_country_102.IsPartOf = locations_geographicalunit_7
    locations_country_102.geographicalunit_ptr = locations_geographicalunit_111
    locations_country_102.CountryCode = 'MS'
    locations_country_102.ISO3CountryCode = 'MSR'
    locations_country_102.PhonePrefix = '382'
    locations_country_102.InternetSuffix = '.ms'
    locations_country_102.ISO3166Country = '500'
    locations_country_102 = importer.save_or_locate(locations_country_102)

    locations_country_103 = Country()
    locations_country_103.GeographicalUnitId = 'Country_ME'
    locations_country_103.GeographicalUnitCategory = 'Country'
    locations_country_103.GeographicalUnitName = 'Montenegro'
    locations_country_103.GeographicalUnitShortName = 'Montenegro'
    locations_country_103.HierarchyLevel = 30
    locations_country_103.IsPartOf = locations_geographicalunit_2
    locations_country_103.geographicalunit_ptr = locations_geographicalunit_112
    locations_country_103.CountryCode = 'ME'
    locations_country_103.ISO3CountryCode = 'MNE'
    locations_country_103.PhonePrefix = '976'
    locations_country_103.InternetSuffix = '.me'
    locations_country_103.ISO3166Country = '499'
    locations_country_103 = importer.save_or_locate(locations_country_103)

    locations_country_104 = Country()
    locations_country_104.GeographicalUnitId = 'Country_MN'
    locations_country_104.GeographicalUnitCategory = 'Country'
    locations_country_104.GeographicalUnitName = 'Mongolia'
    locations_country_104.GeographicalUnitShortName = 'Mongolia'
    locations_country_104.HierarchyLevel = 30
    locations_country_104.IsPartOf = locations_geographicalunit_5
    locations_country_104.geographicalunit_ptr = locations_geographicalunit_113
    locations_country_104.CountryCode = 'MN'
    locations_country_104.ISO3CountryCode = 'MNG'
    locations_country_104.PhonePrefix = '377'
    locations_country_104.InternetSuffix = '.mn'
    locations_country_104.ISO3166Country = '496'
    locations_country_104 = importer.save_or_locate(locations_country_104)

    locations_country_105 = Country()
    locations_country_105.GeographicalUnitId = 'Country_MC'
    locations_country_105.GeographicalUnitCategory = 'Country'
    locations_country_105.GeographicalUnitName = 'Monaco'
    locations_country_105.GeographicalUnitShortName = 'Monaco'
    locations_country_105.HierarchyLevel = 30
    locations_country_105.IsPartOf = locations_geographicalunit_2
    locations_country_105.geographicalunit_ptr = locations_geographicalunit_114
    locations_country_105.CountryCode = 'MC'
    locations_country_105.ISO3CountryCode = 'MCO'
    locations_country_105.PhonePrefix = '373'
    locations_country_105.InternetSuffix = '.mc'
    locations_country_105.ISO3166Country = '492'
    locations_country_105 = importer.save_or_locate(locations_country_105)

    locations_country_106 = Country()
    locations_country_106.GeographicalUnitId = 'Country_MD'
    locations_country_106.GeographicalUnitCategory = 'Country'
    locations_country_106.GeographicalUnitName = 'Moldova (the Republic of)'
    locations_country_106.GeographicalUnitShortName = 'Moldova'
    locations_country_106.HierarchyLevel = 30
    locations_country_106.IsPartOf = locations_geographicalunit_2
    locations_country_106.geographicalunit_ptr = locations_geographicalunit_115
    locations_country_106.CountryCode = 'MD'
    locations_country_106.ISO3CountryCode = 'MDA'
    locations_country_106.PhonePrefix = '691'
    locations_country_106.InternetSuffix = '.md'
    locations_country_106.ISO3166Country = '498'
    locations_country_106 = importer.save_or_locate(locations_country_106)

    locations_country_107 = Country()
    locations_country_107.GeographicalUnitId = 'Country_FM'
    locations_country_107.GeographicalUnitCategory = 'Country'
    locations_country_107.GeographicalUnitName = 'Micronesia (Federated States of)'
    locations_country_107.GeographicalUnitShortName = 'Micronesia'
    locations_country_107.HierarchyLevel = 30
    locations_country_107.IsPartOf = locations_geographicalunit_6
    locations_country_107.geographicalunit_ptr = locations_geographicalunit_116
    locations_country_107.CountryCode = 'FM'
    locations_country_107.ISO3CountryCode = 'FSM'
    locations_country_107.PhonePrefix = '52'
    locations_country_107.InternetSuffix = '.fm'
    locations_country_107.ISO3166Country = '583'
    locations_country_107 = importer.save_or_locate(locations_country_107)

    locations_country_108 = Country()
    locations_country_108.GeographicalUnitId = 'Country_MX'
    locations_country_108.GeographicalUnitCategory = 'Country'
    locations_country_108.GeographicalUnitName = 'Mexico'
    locations_country_108.GeographicalUnitShortName = 'Mexico'
    locations_country_108.HierarchyLevel = 30
    locations_country_108.IsPartOf = locations_geographicalunit_7
    locations_country_108.geographicalunit_ptr = locations_geographicalunit_117
    locations_country_108.CountryCode = 'MX'
    locations_country_108.ISO3CountryCode = 'MEX'
    locations_country_108.PhonePrefix = '262'
    locations_country_108.InternetSuffix = '.mx'
    locations_country_108.ISO3166Country = '484'
    locations_country_108 = importer.save_or_locate(locations_country_108)

    locations_country_109 = Country()
    locations_country_109.GeographicalUnitId = 'Country_YT'
    locations_country_109.GeographicalUnitCategory = 'Country'
    locations_country_109.GeographicalUnitName = 'Mayotte'
    locations_country_109.GeographicalUnitShortName = 'Mayotte'
    locations_country_109.HierarchyLevel = 30
    locations_country_109.IsPartOf = locations_geographicalunit_3
    locations_country_109.geographicalunit_ptr = locations_geographicalunit_118
    locations_country_109.CountryCode = 'YT'
    locations_country_109.ISO3CountryCode = 'MYT'
    locations_country_109.PhonePrefix = '230'
    locations_country_109.InternetSuffix = '.yt'
    locations_country_109.ISO3166Country = '175'
    locations_country_109 = importer.save_or_locate(locations_country_109)

    locations_country_110 = Country()
    locations_country_110.GeographicalUnitId = 'Country_MU'
    locations_country_110.GeographicalUnitCategory = 'Country'
    locations_country_110.GeographicalUnitName = 'Mauritius'
    locations_country_110.GeographicalUnitShortName = 'Mauritius'
    locations_country_110.HierarchyLevel = 30
    locations_country_110.IsPartOf = locations_geographicalunit_3
    locations_country_110.geographicalunit_ptr = locations_geographicalunit_119
    locations_country_110.CountryCode = 'MU'
    locations_country_110.ISO3CountryCode = 'MUS'
    locations_country_110.PhonePrefix = '222'
    locations_country_110.InternetSuffix = '.mu'
    locations_country_110.ISO3166Country = '480'
    locations_country_110 = importer.save_or_locate(locations_country_110)

    locations_country_111 = Country()
    locations_country_111.GeographicalUnitId = 'Country_MR'
    locations_country_111.GeographicalUnitCategory = 'Country'
    locations_country_111.GeographicalUnitName = 'Mauritania'
    locations_country_111.GeographicalUnitShortName = 'Mauritania'
    locations_country_111.HierarchyLevel = 30
    locations_country_111.IsPartOf = locations_geographicalunit_3
    locations_country_111.geographicalunit_ptr = locations_geographicalunit_120
    locations_country_111.CountryCode = 'MR'
    locations_country_111.ISO3CountryCode = 'MRT'
    locations_country_111.PhonePrefix = None
    locations_country_111.InternetSuffix = '.mr'
    locations_country_111.ISO3166Country = '478'
    locations_country_111 = importer.save_or_locate(locations_country_111)

    locations_country_112 = Country()
    locations_country_112.GeographicalUnitId = 'Country_MQ'
    locations_country_112.GeographicalUnitCategory = 'Country'
    locations_country_112.GeographicalUnitName = 'Martinique'
    locations_country_112.GeographicalUnitShortName = 'Martinique'
    locations_country_112.HierarchyLevel = 30
    locations_country_112.IsPartOf = locations_geographicalunit_7
    locations_country_112.geographicalunit_ptr = locations_geographicalunit_121
    locations_country_112.CountryCode = 'MQ'
    locations_country_112.ISO3CountryCode = 'MTQ'
    locations_country_112.PhonePrefix = '692'
    locations_country_112.InternetSuffix = '.mq'
    locations_country_112.ISO3166Country = '474'
    locations_country_112 = importer.save_or_locate(locations_country_112)

    locations_country_113 = Country()
    locations_country_113.GeographicalUnitId = 'Country_MH'
    locations_country_113.GeographicalUnitCategory = 'Country'
    locations_country_113.GeographicalUnitName = 'Marshall Islands (the)'
    locations_country_113.GeographicalUnitShortName = 'Marshall Islands'
    locations_country_113.HierarchyLevel = 30
    locations_country_113.IsPartOf = locations_geographicalunit_6
    locations_country_113.geographicalunit_ptr = locations_geographicalunit_122
    locations_country_113.CountryCode = 'MH'
    locations_country_113.ISO3CountryCode = 'MHL'
    locations_country_113.PhonePrefix = '356'
    locations_country_113.InternetSuffix = '.mh'
    locations_country_113.ISO3166Country = '584'
    locations_country_113 = importer.save_or_locate(locations_country_113)

    locations_country_114 = Country()
    locations_country_114.GeographicalUnitId = 'Country_MT'
    locations_country_114.GeographicalUnitCategory = 'Country'
    locations_country_114.GeographicalUnitName = 'Malta'
    locations_country_114.GeographicalUnitShortName = 'Malta'
    locations_country_114.HierarchyLevel = 30
    locations_country_114.IsPartOf = locations_geographicalunit_2
    locations_country_114.geographicalunit_ptr = locations_geographicalunit_123
    locations_country_114.CountryCode = 'MT'
    locations_country_114.ISO3CountryCode = 'MLT'
    locations_country_114.PhonePrefix = '223'
    locations_country_114.InternetSuffix = '.mt'
    locations_country_114.ISO3166Country = '470'
    locations_country_114 = importer.save_or_locate(locations_country_114)

    locations_country_115 = Country()
    locations_country_115.GeographicalUnitId = 'Country_ML'
    locations_country_115.GeographicalUnitCategory = 'Country'
    locations_country_115.GeographicalUnitName = 'Mali'
    locations_country_115.GeographicalUnitShortName = 'Mali'
    locations_country_115.HierarchyLevel = 30
    locations_country_115.IsPartOf = locations_geographicalunit_3
    locations_country_115.geographicalunit_ptr = locations_geographicalunit_124
    locations_country_115.CountryCode = 'ML'
    locations_country_115.ISO3CountryCode = 'MLI'
    locations_country_115.PhonePrefix = '960'
    locations_country_115.InternetSuffix = '.ml'
    locations_country_115.ISO3166Country = '466'
    locations_country_115 = importer.save_or_locate(locations_country_115)

    locations_country_116 = Country()
    locations_country_116.GeographicalUnitId = 'Country_MV'
    locations_country_116.GeographicalUnitCategory = 'Country'
    locations_country_116.GeographicalUnitName = 'Maldives'
    locations_country_116.GeographicalUnitShortName = 'Maldives'
    locations_country_116.HierarchyLevel = 30
    locations_country_116.IsPartOf = locations_geographicalunit_5
    locations_country_116.geographicalunit_ptr = locations_geographicalunit_125
    locations_country_116.CountryCode = 'MV'
    locations_country_116.ISO3CountryCode = 'MDV'
    locations_country_116.PhonePrefix = '60'
    locations_country_116.InternetSuffix = '.mv'
    locations_country_116.ISO3166Country = '462'
    locations_country_116 = importer.save_or_locate(locations_country_116)

    locations_country_117 = Country()
    locations_country_117.GeographicalUnitId = 'Country_MY'
    locations_country_117.GeographicalUnitCategory = 'Country'
    locations_country_117.GeographicalUnitName = 'Malaysia'
    locations_country_117.GeographicalUnitShortName = 'Malaysia'
    locations_country_117.HierarchyLevel = 30
    locations_country_117.IsPartOf = locations_geographicalunit_5
    locations_country_117.geographicalunit_ptr = locations_geographicalunit_126
    locations_country_117.CountryCode = 'MY'
    locations_country_117.ISO3CountryCode = 'MYS'
    locations_country_117.PhonePrefix = '265'
    locations_country_117.InternetSuffix = '.my'
    locations_country_117.ISO3166Country = '458'
    locations_country_117 = importer.save_or_locate(locations_country_117)

    locations_country_118 = Country()
    locations_country_118.GeographicalUnitId = 'Country_MW'
    locations_country_118.GeographicalUnitCategory = 'Country'
    locations_country_118.GeographicalUnitName = 'Malawi'
    locations_country_118.GeographicalUnitShortName = 'Malawi'
    locations_country_118.HierarchyLevel = 30
    locations_country_118.IsPartOf = locations_geographicalunit_3
    locations_country_118.geographicalunit_ptr = locations_geographicalunit_127
    locations_country_118.CountryCode = 'MW'
    locations_country_118.ISO3CountryCode = 'MWI'
    locations_country_118.PhonePrefix = '261'
    locations_country_118.InternetSuffix = '.mw'
    locations_country_118.ISO3166Country = '454'
    locations_country_118 = importer.save_or_locate(locations_country_118)

    locations_country_119 = Country()
    locations_country_119.GeographicalUnitId = 'Country_MG'
    locations_country_119.GeographicalUnitCategory = 'Country'
    locations_country_119.GeographicalUnitName = 'Madagascar'
    locations_country_119.GeographicalUnitShortName = 'Madagascar'
    locations_country_119.HierarchyLevel = 30
    locations_country_119.IsPartOf = locations_geographicalunit_3
    locations_country_119.geographicalunit_ptr = locations_geographicalunit_128
    locations_country_119.CountryCode = 'MG'
    locations_country_119.ISO3CountryCode = 'MDG'
    locations_country_119.PhonePrefix = '853'
    locations_country_119.InternetSuffix = '.mg'
    locations_country_119.ISO3166Country = '450'
    locations_country_119 = importer.save_or_locate(locations_country_119)

    locations_country_120 = Country()
    locations_country_120.GeographicalUnitId = 'Country_MO'
    locations_country_120.GeographicalUnitCategory = 'Country'
    locations_country_120.GeographicalUnitName = 'Macao'
    locations_country_120.GeographicalUnitShortName = 'Macao'
    locations_country_120.HierarchyLevel = 30
    locations_country_120.IsPartOf = locations_geographicalunit_5
    locations_country_120.geographicalunit_ptr = locations_geographicalunit_129
    locations_country_120.CountryCode = 'MO'
    locations_country_120.ISO3CountryCode = 'MAC'
    locations_country_120.PhonePrefix = '352'
    locations_country_120.InternetSuffix = '.mo'
    locations_country_120.ISO3166Country = '446'
    locations_country_120 = importer.save_or_locate(locations_country_120)

    locations_country_121 = Country()
    locations_country_121.GeographicalUnitId = 'Country_LU'
    locations_country_121.GeographicalUnitCategory = 'Country'
    locations_country_121.GeographicalUnitName = 'Luxembourg'
    locations_country_121.GeographicalUnitShortName = 'Luxembourg'
    locations_country_121.HierarchyLevel = 30
    locations_country_121.IsPartOf = locations_geographicalunit_2
    locations_country_121.geographicalunit_ptr = locations_geographicalunit_130
    locations_country_121.CountryCode = 'LU'
    locations_country_121.ISO3CountryCode = 'LUX'
    locations_country_121.PhonePrefix = '370'
    locations_country_121.InternetSuffix = '.lu'
    locations_country_121.ISO3166Country = '442'
    locations_country_121 = importer.save_or_locate(locations_country_121)

    locations_country_122 = Country()
    locations_country_122.GeographicalUnitId = 'Country_LT'
    locations_country_122.GeographicalUnitCategory = 'Country'
    locations_country_122.GeographicalUnitName = 'Lithuania'
    locations_country_122.GeographicalUnitShortName = 'Lithuania'
    locations_country_122.HierarchyLevel = 30
    locations_country_122.IsPartOf = locations_geographicalunit_2
    locations_country_122.geographicalunit_ptr = locations_geographicalunit_131
    locations_country_122.CountryCode = 'LT'
    locations_country_122.ISO3CountryCode = 'LTU'
    locations_country_122.PhonePrefix = '423'
    locations_country_122.InternetSuffix = '.lt'
    locations_country_122.ISO3166Country = '440'
    locations_country_122 = importer.save_or_locate(locations_country_122)

    locations_country_123 = Country()
    locations_country_123.GeographicalUnitId = 'Country_LI'
    locations_country_123.GeographicalUnitCategory = 'Country'
    locations_country_123.GeographicalUnitName = 'Liechtenstein'
    locations_country_123.GeographicalUnitShortName = 'Liechtenstein'
    locations_country_123.HierarchyLevel = 30
    locations_country_123.IsPartOf = locations_geographicalunit_2
    locations_country_123.geographicalunit_ptr = locations_geographicalunit_132
    locations_country_123.CountryCode = 'LI'
    locations_country_123.ISO3CountryCode = 'LIE'
    locations_country_123.PhonePrefix = '218'
    locations_country_123.InternetSuffix = '.li'
    locations_country_123.ISO3166Country = '438'
    locations_country_123 = importer.save_or_locate(locations_country_123)

    locations_country_124 = Country()
    locations_country_124.GeographicalUnitId = 'Country_LY'
    locations_country_124.GeographicalUnitCategory = 'Country'
    locations_country_124.GeographicalUnitName = 'Libya'
    locations_country_124.GeographicalUnitShortName = 'Libya'
    locations_country_124.HierarchyLevel = 30
    locations_country_124.IsPartOf = locations_geographicalunit_3
    locations_country_124.geographicalunit_ptr = locations_geographicalunit_133
    locations_country_124.CountryCode = 'LY'
    locations_country_124.ISO3CountryCode = 'LBY'
    locations_country_124.PhonePrefix = '231'
    locations_country_124.InternetSuffix = '.ly'
    locations_country_124.ISO3166Country = '434'
    locations_country_124 = importer.save_or_locate(locations_country_124)

    locations_country_125 = Country()
    locations_country_125.GeographicalUnitId = 'Country_LR'
    locations_country_125.GeographicalUnitCategory = 'Country'
    locations_country_125.GeographicalUnitName = 'Liberia'
    locations_country_125.GeographicalUnitShortName = 'Liberia'
    locations_country_125.HierarchyLevel = 30
    locations_country_125.IsPartOf = locations_geographicalunit_3
    locations_country_125.geographicalunit_ptr = locations_geographicalunit_134
    locations_country_125.CountryCode = 'LR'
    locations_country_125.ISO3CountryCode = 'LBR'
    locations_country_125.PhonePrefix = '266'
    locations_country_125.InternetSuffix = '.lr'
    locations_country_125.ISO3166Country = '430'
    locations_country_125 = importer.save_or_locate(locations_country_125)

    locations_country_126 = Country()
    locations_country_126.GeographicalUnitId = 'Country_LS'
    locations_country_126.GeographicalUnitCategory = 'Country'
    locations_country_126.GeographicalUnitName = 'Lesotho'
    locations_country_126.GeographicalUnitShortName = 'Lesotho'
    locations_country_126.HierarchyLevel = 30
    locations_country_126.IsPartOf = locations_geographicalunit_3
    locations_country_126.geographicalunit_ptr = locations_geographicalunit_135
    locations_country_126.CountryCode = 'LS'
    locations_country_126.ISO3CountryCode = 'LSO'
    locations_country_126.PhonePrefix = '961'
    locations_country_126.InternetSuffix = '.ls'
    locations_country_126.ISO3166Country = '426'
    locations_country_126 = importer.save_or_locate(locations_country_126)

    locations_country_127 = Country()
    locations_country_127.GeographicalUnitId = 'Country_LB'
    locations_country_127.GeographicalUnitCategory = 'Country'
    locations_country_127.GeographicalUnitName = 'Lebanon'
    locations_country_127.GeographicalUnitShortName = 'Lebanon'
    locations_country_127.HierarchyLevel = 30
    locations_country_127.IsPartOf = locations_geographicalunit_5
    locations_country_127.geographicalunit_ptr = locations_geographicalunit_136
    locations_country_127.CountryCode = 'LB'
    locations_country_127.ISO3CountryCode = 'LBN'
    locations_country_127.PhonePrefix = '371'
    locations_country_127.InternetSuffix = '.lb'
    locations_country_127.ISO3166Country = '422'
    locations_country_127 = importer.save_or_locate(locations_country_127)

    locations_country_128 = Country()
    locations_country_128.GeographicalUnitId = 'Country_LV'
    locations_country_128.GeographicalUnitCategory = 'Country'
    locations_country_128.GeographicalUnitName = 'Latvia'
    locations_country_128.GeographicalUnitShortName = 'Latvia'
    locations_country_128.HierarchyLevel = 30
    locations_country_128.IsPartOf = locations_geographicalunit_2
    locations_country_128.geographicalunit_ptr = locations_geographicalunit_137
    locations_country_128.CountryCode = 'LV'
    locations_country_128.ISO3CountryCode = 'LVA'
    locations_country_128.PhonePrefix = '856'
    locations_country_128.InternetSuffix = '.lv'
    locations_country_128.ISO3166Country = '428'
    locations_country_128 = importer.save_or_locate(locations_country_128)

    locations_country_129 = Country()
    locations_country_129.GeographicalUnitId = 'Country_LA'
    locations_country_129.GeographicalUnitCategory = 'Country'
    locations_country_129.GeographicalUnitName = "Lao People's Democratic Republic (the)"
    locations_country_129.GeographicalUnitShortName = 'Lao'
    locations_country_129.HierarchyLevel = 30
    locations_country_129.IsPartOf = locations_geographicalunit_5
    locations_country_129.geographicalunit_ptr = locations_geographicalunit_138
    locations_country_129.CountryCode = 'LA'
    locations_country_129.ISO3CountryCode = 'LAO'
    locations_country_129.PhonePrefix = '996'
    locations_country_129.InternetSuffix = '.la'
    locations_country_129.ISO3166Country = '418'
    locations_country_129 = importer.save_or_locate(locations_country_129)

    locations_country_130 = Country()
    locations_country_130.GeographicalUnitId = 'Country_KG'
    locations_country_130.GeographicalUnitCategory = 'Country'
    locations_country_130.GeographicalUnitName = 'Kyrgyzstan'
    locations_country_130.GeographicalUnitShortName = 'Kyrgyzstan'
    locations_country_130.HierarchyLevel = 30
    locations_country_130.IsPartOf = locations_geographicalunit_5
    locations_country_130.geographicalunit_ptr = locations_geographicalunit_139
    locations_country_130.CountryCode = 'KG'
    locations_country_130.ISO3CountryCode = 'KGZ'
    locations_country_130.PhonePrefix = '965'
    locations_country_130.InternetSuffix = '.kg'
    locations_country_130.ISO3166Country = '417'
    locations_country_130 = importer.save_or_locate(locations_country_130)

    locations_country_131 = Country()
    locations_country_131.GeographicalUnitId = 'Country_KW'
    locations_country_131.GeographicalUnitCategory = 'Country'
    locations_country_131.GeographicalUnitName = 'Kuwait'
    locations_country_131.GeographicalUnitShortName = 'Kuwait'
    locations_country_131.HierarchyLevel = 30
    locations_country_131.IsPartOf = locations_geographicalunit_5
    locations_country_131.geographicalunit_ptr = locations_geographicalunit_140
    locations_country_131.CountryCode = 'KW'
    locations_country_131.ISO3CountryCode = 'KWT'
    locations_country_131.PhonePrefix = '82'
    locations_country_131.InternetSuffix = '.kw'
    locations_country_131.ISO3166Country = '414'
    locations_country_131 = importer.save_or_locate(locations_country_131)

    locations_country_132 = Country()
    locations_country_132.GeographicalUnitId = 'Country_KR'
    locations_country_132.GeographicalUnitCategory = 'Country'
    locations_country_132.GeographicalUnitName = 'Korea (the Republic of)'
    locations_country_132.GeographicalUnitShortName = 'South Korea'
    locations_country_132.HierarchyLevel = 30
    locations_country_132.IsPartOf = locations_geographicalunit_5
    locations_country_132.geographicalunit_ptr = locations_geographicalunit_141
    locations_country_132.CountryCode = 'KR'
    locations_country_132.ISO3CountryCode = 'KOR'
    locations_country_132.PhonePrefix = '850'
    locations_country_132.InternetSuffix = '.kr'
    locations_country_132.ISO3166Country = '410'
    locations_country_132 = importer.save_or_locate(locations_country_132)

    locations_country_133 = Country()
    locations_country_133.GeographicalUnitId = 'Country_KP'
    locations_country_133.GeographicalUnitCategory = 'Country'
    locations_country_133.GeographicalUnitName = "Korea (the Democratic People's Republic of)"
    locations_country_133.GeographicalUnitShortName = 'North Korea'
    locations_country_133.HierarchyLevel = 30
    locations_country_133.IsPartOf = locations_geographicalunit_5
    locations_country_133.geographicalunit_ptr = locations_geographicalunit_142
    locations_country_133.CountryCode = 'KP'
    locations_country_133.ISO3CountryCode = 'PRK'
    locations_country_133.PhonePrefix = '686'
    locations_country_133.InternetSuffix = '.kp'
    locations_country_133.ISO3166Country = '408'
    locations_country_133 = importer.save_or_locate(locations_country_133)

    locations_country_134 = Country()
    locations_country_134.GeographicalUnitId = 'Country_KI'
    locations_country_134.GeographicalUnitCategory = 'Country'
    locations_country_134.GeographicalUnitName = 'Kiribati'
    locations_country_134.GeographicalUnitShortName = 'Kiribati'
    locations_country_134.HierarchyLevel = 30
    locations_country_134.IsPartOf = locations_geographicalunit_6
    locations_country_134.geographicalunit_ptr = locations_geographicalunit_143
    locations_country_134.CountryCode = 'KI'
    locations_country_134.ISO3CountryCode = 'KIR'
    locations_country_134.PhonePrefix = '254'
    locations_country_134.InternetSuffix = '.ki'
    locations_country_134.ISO3166Country = '296'
    locations_country_134 = importer.save_or_locate(locations_country_134)

    locations_country_135 = Country()
    locations_country_135.GeographicalUnitId = 'Country_KE'
    locations_country_135.GeographicalUnitCategory = 'Country'
    locations_country_135.GeographicalUnitName = 'Kenya'
    locations_country_135.GeographicalUnitShortName = 'Kenya'
    locations_country_135.HierarchyLevel = 30
    locations_country_135.IsPartOf = locations_geographicalunit_3
    locations_country_135.geographicalunit_ptr = locations_geographicalunit_144
    locations_country_135.CountryCode = 'KE'
    locations_country_135.ISO3CountryCode = 'KEN'
    locations_country_135.PhonePrefix = '7'
    locations_country_135.InternetSuffix = '.ke'
    locations_country_135.ISO3166Country = '404'
    locations_country_135 = importer.save_or_locate(locations_country_135)

    locations_country_136 = Country()
    locations_country_136.GeographicalUnitId = 'Country_KZ'
    locations_country_136.GeographicalUnitCategory = 'Country'
    locations_country_136.GeographicalUnitName = 'Kazakhstan'
    locations_country_136.GeographicalUnitShortName = 'Kazakhstan'
    locations_country_136.HierarchyLevel = 30
    locations_country_136.IsPartOf = locations_geographicalunit_2
    locations_country_136.geographicalunit_ptr = locations_geographicalunit_145
    locations_country_136.CountryCode = 'KZ'
    locations_country_136.ISO3CountryCode = 'KAZ'
    locations_country_136.PhonePrefix = '962'
    locations_country_136.InternetSuffix = '.kz'
    locations_country_136.ISO3166Country = '398'
    locations_country_136 = importer.save_or_locate(locations_country_136)

    locations_country_137 = Country()
    locations_country_137.GeographicalUnitId = 'Country_JO'
    locations_country_137.GeographicalUnitCategory = 'Country'
    locations_country_137.GeographicalUnitName = 'Jordan'
    locations_country_137.GeographicalUnitShortName = 'Jordan'
    locations_country_137.HierarchyLevel = 30
    locations_country_137.IsPartOf = locations_geographicalunit_5
    locations_country_137.geographicalunit_ptr = locations_geographicalunit_146
    locations_country_137.CountryCode = 'JO'
    locations_country_137.ISO3CountryCode = 'JOR'
    locations_country_137.PhonePrefix = '44-1534'
    locations_country_137.InternetSuffix = '.jo'
    locations_country_137.ISO3166Country = '400'
    locations_country_137 = importer.save_or_locate(locations_country_137)

    locations_country_138 = Country()
    locations_country_138.GeographicalUnitId = 'Country_JE'
    locations_country_138.GeographicalUnitCategory = 'Country'
    locations_country_138.GeographicalUnitName = 'Jersey'
    locations_country_138.GeographicalUnitShortName = 'Jersey'
    locations_country_138.HierarchyLevel = 30
    locations_country_138.IsPartOf = locations_geographicalunit_2
    locations_country_138.geographicalunit_ptr = locations_geographicalunit_147
    locations_country_138.CountryCode = 'JE'
    locations_country_138.ISO3CountryCode = 'JEY'
    locations_country_138.PhonePrefix = '81'
    locations_country_138.InternetSuffix = '.je'
    locations_country_138.ISO3166Country = '832'
    locations_country_138 = importer.save_or_locate(locations_country_138)

    locations_country_139 = Country()
    locations_country_139.GeographicalUnitId = 'Country_JP'
    locations_country_139.GeographicalUnitCategory = 'Country'
    locations_country_139.GeographicalUnitName = 'Japan'
    locations_country_139.GeographicalUnitShortName = 'Japan'
    locations_country_139.HierarchyLevel = 30
    locations_country_139.IsPartOf = locations_geographicalunit_5
    locations_country_139.geographicalunit_ptr = locations_geographicalunit_148
    locations_country_139.CountryCode = 'JP'
    locations_country_139.ISO3CountryCode = 'JPN'
    locations_country_139.PhonePrefix = '1-876'
    locations_country_139.InternetSuffix = '.jp'
    locations_country_139.ISO3166Country = '392'
    locations_country_139 = importer.save_or_locate(locations_country_139)

    locations_country_140 = Country()
    locations_country_140.GeographicalUnitId = 'Country_JM'
    locations_country_140.GeographicalUnitCategory = 'Country'
    locations_country_140.GeographicalUnitName = 'Jamaica'
    locations_country_140.GeographicalUnitShortName = 'Jamaica'
    locations_country_140.HierarchyLevel = 30
    locations_country_140.IsPartOf = locations_geographicalunit_7
    locations_country_140.geographicalunit_ptr = locations_geographicalunit_149
    locations_country_140.CountryCode = 'JM'
    locations_country_140.ISO3CountryCode = 'JAM'
    locations_country_140.PhonePrefix = '39'
    locations_country_140.InternetSuffix = '.jm'
    locations_country_140.ISO3166Country = '388'
    locations_country_140 = importer.save_or_locate(locations_country_140)

    locations_country_141 = Country()
    locations_country_141.GeographicalUnitId = 'Country_IT'
    locations_country_141.GeographicalUnitCategory = 'Country'
    locations_country_141.GeographicalUnitName = 'Italy'
    locations_country_141.GeographicalUnitShortName = 'Italy'
    locations_country_141.HierarchyLevel = 30
    locations_country_141.IsPartOf = locations_geographicalunit_2
    locations_country_141.geographicalunit_ptr = locations_geographicalunit_150
    locations_country_141.CountryCode = 'IT'
    locations_country_141.ISO3CountryCode = 'ITA'
    locations_country_141.PhonePrefix = '972'
    locations_country_141.InternetSuffix = '.it'
    locations_country_141.ISO3166Country = '380'
    locations_country_141 = importer.save_or_locate(locations_country_141)

    locations_country_142 = Country()
    locations_country_142.GeographicalUnitId = 'Country_IL'
    locations_country_142.GeographicalUnitCategory = 'Country'
    locations_country_142.GeographicalUnitName = 'Israel'
    locations_country_142.GeographicalUnitShortName = 'Israel'
    locations_country_142.HierarchyLevel = 30
    locations_country_142.IsPartOf = locations_geographicalunit_5
    locations_country_142.geographicalunit_ptr = locations_geographicalunit_151
    locations_country_142.CountryCode = 'IL'
    locations_country_142.ISO3CountryCode = 'ISR'
    locations_country_142.PhonePrefix = '44-1624'
    locations_country_142.InternetSuffix = '.il'
    locations_country_142.ISO3166Country = '376'
    locations_country_142 = importer.save_or_locate(locations_country_142)

    locations_country_143 = Country()
    locations_country_143.GeographicalUnitId = 'Country_IM'
    locations_country_143.GeographicalUnitCategory = 'Country'
    locations_country_143.GeographicalUnitName = 'Isle of Man'
    locations_country_143.GeographicalUnitShortName = 'Isle of Man'
    locations_country_143.HierarchyLevel = 30
    locations_country_143.IsPartOf = locations_geographicalunit_2
    locations_country_143.geographicalunit_ptr = locations_geographicalunit_152
    locations_country_143.CountryCode = 'IM'
    locations_country_143.ISO3CountryCode = 'IMN'
    locations_country_143.PhonePrefix = '353'
    locations_country_143.InternetSuffix = '.im'
    locations_country_143.ISO3166Country = '833'
    locations_country_143 = importer.save_or_locate(locations_country_143)

    locations_country_144 = Country()
    locations_country_144.GeographicalUnitId = 'Country_IE'
    locations_country_144.GeographicalUnitCategory = 'Country'
    locations_country_144.GeographicalUnitName = 'Ireland'
    locations_country_144.GeographicalUnitShortName = 'Ireland'
    locations_country_144.HierarchyLevel = 30
    locations_country_144.IsPartOf = locations_geographicalunit_2
    locations_country_144.geographicalunit_ptr = locations_geographicalunit_153
    locations_country_144.CountryCode = 'IE'
    locations_country_144.ISO3CountryCode = 'IRL'
    locations_country_144.PhonePrefix = '964'
    locations_country_144.InternetSuffix = '.ie'
    locations_country_144.ISO3166Country = '372'
    locations_country_144 = importer.save_or_locate(locations_country_144)

    locations_country_145 = Country()
    locations_country_145.GeographicalUnitId = 'Country_IQ'
    locations_country_145.GeographicalUnitCategory = 'Country'
    locations_country_145.GeographicalUnitName = 'Iraq'
    locations_country_145.GeographicalUnitShortName = 'Iraq'
    locations_country_145.HierarchyLevel = 30
    locations_country_145.IsPartOf = locations_geographicalunit_5
    locations_country_145.geographicalunit_ptr = locations_geographicalunit_154
    locations_country_145.CountryCode = 'IQ'
    locations_country_145.ISO3CountryCode = 'IRQ'
    locations_country_145.PhonePrefix = '98'
    locations_country_145.InternetSuffix = '.iq'
    locations_country_145.ISO3166Country = '368'
    locations_country_145 = importer.save_or_locate(locations_country_145)

    locations_country_146 = Country()
    locations_country_146.GeographicalUnitId = 'Country_IR'
    locations_country_146.GeographicalUnitCategory = 'Country'
    locations_country_146.GeographicalUnitName = 'Iran (Islamic Republic of)'
    locations_country_146.GeographicalUnitShortName = 'Iran (Islamic Republic of)'
    locations_country_146.HierarchyLevel = 30
    locations_country_146.IsPartOf = locations_geographicalunit_5
    locations_country_146.geographicalunit_ptr = locations_geographicalunit_155
    locations_country_146.CountryCode = 'IR'
    locations_country_146.ISO3CountryCode = 'IRN'
    locations_country_146.PhonePrefix = '62'
    locations_country_146.InternetSuffix = '.ir'
    locations_country_146.ISO3166Country = '364'
    locations_country_146 = importer.save_or_locate(locations_country_146)

    locations_country_147 = Country()
    locations_country_147.GeographicalUnitId = 'Country_ID'
    locations_country_147.GeographicalUnitCategory = 'Country'
    locations_country_147.GeographicalUnitName = 'Indonesia'
    locations_country_147.GeographicalUnitShortName = 'Indonesia'
    locations_country_147.HierarchyLevel = 30
    locations_country_147.IsPartOf = locations_geographicalunit_5
    locations_country_147.geographicalunit_ptr = locations_geographicalunit_156
    locations_country_147.CountryCode = 'ID'
    locations_country_147.ISO3CountryCode = 'IDN'
    locations_country_147.PhonePrefix = '91'
    locations_country_147.InternetSuffix = '.id'
    locations_country_147.ISO3166Country = '360'
    locations_country_147 = importer.save_or_locate(locations_country_147)

    locations_country_148 = Country()
    locations_country_148.GeographicalUnitId = 'Country_IN'
    locations_country_148.GeographicalUnitCategory = 'Country'
    locations_country_148.GeographicalUnitName = 'India'
    locations_country_148.GeographicalUnitShortName = 'India'
    locations_country_148.HierarchyLevel = 30
    locations_country_148.IsPartOf = locations_geographicalunit_5
    locations_country_148.geographicalunit_ptr = locations_geographicalunit_157
    locations_country_148.CountryCode = 'IN'
    locations_country_148.ISO3CountryCode = 'IND'
    locations_country_148.PhonePrefix = '354'
    locations_country_148.InternetSuffix = '.in'
    locations_country_148.ISO3166Country = '356'
    locations_country_148 = importer.save_or_locate(locations_country_148)

    locations_country_149 = Country()
    locations_country_149.GeographicalUnitId = 'Country_IS'
    locations_country_149.GeographicalUnitCategory = 'Country'
    locations_country_149.GeographicalUnitName = 'Iceland'
    locations_country_149.GeographicalUnitShortName = 'Iceland'
    locations_country_149.HierarchyLevel = 30
    locations_country_149.IsPartOf = locations_geographicalunit_2
    locations_country_149.geographicalunit_ptr = locations_geographicalunit_158
    locations_country_149.CountryCode = 'IS'
    locations_country_149.ISO3CountryCode = 'ISL'
    locations_country_149.PhonePrefix = '36'
    locations_country_149.InternetSuffix = '.is'
    locations_country_149.ISO3166Country = '352'
    locations_country_149 = importer.save_or_locate(locations_country_149)

    locations_country_150 = Country()
    locations_country_150.GeographicalUnitId = 'Country_HU'
    locations_country_150.GeographicalUnitCategory = 'Country'
    locations_country_150.GeographicalUnitName = 'Hungary'
    locations_country_150.GeographicalUnitShortName = 'Hungary'
    locations_country_150.HierarchyLevel = 30
    locations_country_150.IsPartOf = locations_geographicalunit_2
    locations_country_150.geographicalunit_ptr = locations_geographicalunit_159
    locations_country_150.CountryCode = 'HU'
    locations_country_150.ISO3CountryCode = 'HUN'
    locations_country_150.PhonePrefix = '852'
    locations_country_150.InternetSuffix = '.hu'
    locations_country_150.ISO3166Country = '348'
    locations_country_150 = importer.save_or_locate(locations_country_150)

    locations_country_151 = Country()
    locations_country_151.GeographicalUnitId = 'Country_HK'
    locations_country_151.GeographicalUnitCategory = 'Country'
    locations_country_151.GeographicalUnitName = 'Hong Kong'
    locations_country_151.GeographicalUnitShortName = 'Hong Kong'
    locations_country_151.HierarchyLevel = 30
    locations_country_151.IsPartOf = locations_geographicalunit_5
    locations_country_151.geographicalunit_ptr = locations_geographicalunit_160
    locations_country_151.CountryCode = 'HK'
    locations_country_151.ISO3CountryCode = 'HKG'
    locations_country_151.PhonePrefix = '504'
    locations_country_151.InternetSuffix = '.hk'
    locations_country_151.ISO3166Country = '344'
    locations_country_151 = importer.save_or_locate(locations_country_151)

    locations_country_152 = Country()
    locations_country_152.GeographicalUnitId = 'Country_HN'
    locations_country_152.GeographicalUnitCategory = 'Country'
    locations_country_152.GeographicalUnitName = 'Honduras'
    locations_country_152.GeographicalUnitShortName = 'Honduras'
    locations_country_152.HierarchyLevel = 30
    locations_country_152.IsPartOf = locations_geographicalunit_7
    locations_country_152.geographicalunit_ptr = locations_geographicalunit_161
    locations_country_152.CountryCode = 'HN'
    locations_country_152.ISO3CountryCode = 'HND'
    locations_country_152.PhonePrefix = '379'
    locations_country_152.InternetSuffix = '.hn'
    locations_country_152.ISO3166Country = '340'
    locations_country_152 = importer.save_or_locate(locations_country_152)

    locations_country_153 = Country()
    locations_country_153.GeographicalUnitId = 'Country_VA'
    locations_country_153.GeographicalUnitCategory = 'Country'
    locations_country_153.GeographicalUnitName = 'Holy See (the)'
    locations_country_153.GeographicalUnitShortName = 'Holy See (the)'
    locations_country_153.HierarchyLevel = 30
    locations_country_153.IsPartOf = locations_geographicalunit_2
    locations_country_153.geographicalunit_ptr = locations_geographicalunit_162
    locations_country_153.CountryCode = 'VA'
    locations_country_153.ISO3CountryCode = 'VAT'
    locations_country_153.PhonePrefix = None
    locations_country_153.InternetSuffix = '.va'
    locations_country_153.ISO3166Country = '336'
    locations_country_153 = importer.save_or_locate(locations_country_153)

    locations_country_154 = Country()
    locations_country_154.GeographicalUnitId = 'Country_HM'
    locations_country_154.GeographicalUnitCategory = 'Country'
    locations_country_154.GeographicalUnitName = 'Heard Island and McDonald Islands'
    locations_country_154.GeographicalUnitShortName = 'Heard Island and McDonald Islands'
    locations_country_154.HierarchyLevel = 30
    locations_country_154.IsPartOf = locations_geographicalunit_4
    locations_country_154.geographicalunit_ptr = locations_geographicalunit_163
    locations_country_154.CountryCode = 'HM'
    locations_country_154.ISO3CountryCode = 'HMD'
    locations_country_154.PhonePrefix = '509'
    locations_country_154.InternetSuffix = '.hm'
    locations_country_154.ISO3166Country = '334'
    locations_country_154 = importer.save_or_locate(locations_country_154)

    locations_country_155 = Country()
    locations_country_155.GeographicalUnitId = 'Country_HT'
    locations_country_155.GeographicalUnitCategory = 'Country'
    locations_country_155.GeographicalUnitName = 'Haiti'
    locations_country_155.GeographicalUnitShortName = 'Haiti'
    locations_country_155.HierarchyLevel = 30
    locations_country_155.IsPartOf = locations_geographicalunit_7
    locations_country_155.geographicalunit_ptr = locations_geographicalunit_164
    locations_country_155.CountryCode = 'HT'
    locations_country_155.ISO3CountryCode = 'HTI'
    locations_country_155.PhonePrefix = '592'
    locations_country_155.InternetSuffix = '.ht'
    locations_country_155.ISO3166Country = '332'
    locations_country_155 = importer.save_or_locate(locations_country_155)

    locations_country_156 = Country()
    locations_country_156.GeographicalUnitId = 'Country_GY'
    locations_country_156.GeographicalUnitCategory = 'Country'
    locations_country_156.GeographicalUnitName = 'Guyana'
    locations_country_156.GeographicalUnitShortName = 'Guyana'
    locations_country_156.HierarchyLevel = 30
    locations_country_156.IsPartOf = locations_geographicalunit_8
    locations_country_156.geographicalunit_ptr = locations_geographicalunit_165
    locations_country_156.CountryCode = 'GY'
    locations_country_156.ISO3CountryCode = 'GUY'
    locations_country_156.PhonePrefix = '245'
    locations_country_156.InternetSuffix = '.gy'
    locations_country_156.ISO3166Country = '328'
    locations_country_156 = importer.save_or_locate(locations_country_156)

    locations_country_157 = Country()
    locations_country_157.GeographicalUnitId = 'Country_GW'
    locations_country_157.GeographicalUnitCategory = 'Country'
    locations_country_157.GeographicalUnitName = 'Guinea-Bissau'
    locations_country_157.GeographicalUnitShortName = 'Guinea-Bissau'
    locations_country_157.HierarchyLevel = 30
    locations_country_157.IsPartOf = locations_geographicalunit_3
    locations_country_157.geographicalunit_ptr = locations_geographicalunit_166
    locations_country_157.CountryCode = 'GW'
    locations_country_157.ISO3CountryCode = 'GNB'
    locations_country_157.PhonePrefix = '224'
    locations_country_157.InternetSuffix = '.gw'
    locations_country_157.ISO3166Country = '624'
    locations_country_157 = importer.save_or_locate(locations_country_157)

    locations_country_158 = Country()
    locations_country_158.GeographicalUnitId = 'Country_GN'
    locations_country_158.GeographicalUnitCategory = 'Country'
    locations_country_158.GeographicalUnitName = 'Guinea'
    locations_country_158.GeographicalUnitShortName = 'Guinea'
    locations_country_158.HierarchyLevel = 30
    locations_country_158.IsPartOf = locations_geographicalunit_3
    locations_country_158.geographicalunit_ptr = locations_geographicalunit_167
    locations_country_158.CountryCode = 'GN'
    locations_country_158.ISO3CountryCode = 'GIN'
    locations_country_158.PhonePrefix = '44-1481'
    locations_country_158.InternetSuffix = '.gn'
    locations_country_158.ISO3166Country = '324'
    locations_country_158 = importer.save_or_locate(locations_country_158)

    locations_country_159 = Country()
    locations_country_159.GeographicalUnitId = 'Country_GG'
    locations_country_159.GeographicalUnitCategory = 'Country'
    locations_country_159.GeographicalUnitName = 'Guernsey'
    locations_country_159.GeographicalUnitShortName = 'Guernsey'
    locations_country_159.HierarchyLevel = 30
    locations_country_159.IsPartOf = locations_geographicalunit_2
    locations_country_159.geographicalunit_ptr = locations_geographicalunit_168
    locations_country_159.CountryCode = 'GG'
    locations_country_159.ISO3CountryCode = 'GGY'
    locations_country_159.PhonePrefix = '502'
    locations_country_159.InternetSuffix = '.gg'
    locations_country_159.ISO3166Country = '831'
    locations_country_159 = importer.save_or_locate(locations_country_159)

    locations_country_160 = Country()
    locations_country_160.GeographicalUnitId = 'Country_GT'
    locations_country_160.GeographicalUnitCategory = 'Country'
    locations_country_160.GeographicalUnitName = 'Guatemala'
    locations_country_160.GeographicalUnitShortName = 'Guatemala'
    locations_country_160.HierarchyLevel = 30
    locations_country_160.IsPartOf = locations_geographicalunit_7
    locations_country_160.geographicalunit_ptr = locations_geographicalunit_169
    locations_country_160.CountryCode = 'GT'
    locations_country_160.ISO3CountryCode = 'GTM'
    locations_country_160.PhonePrefix = '1-671'
    locations_country_160.InternetSuffix = '.gt'
    locations_country_160.ISO3166Country = '320'
    locations_country_160 = importer.save_or_locate(locations_country_160)

    locations_country_161 = Country()
    locations_country_161.GeographicalUnitId = 'Country_GU'
    locations_country_161.GeographicalUnitCategory = 'Country'
    locations_country_161.GeographicalUnitName = 'Guam'
    locations_country_161.GeographicalUnitShortName = 'Guam'
    locations_country_161.HierarchyLevel = 30
    locations_country_161.IsPartOf = locations_geographicalunit_6
    locations_country_161.geographicalunit_ptr = locations_geographicalunit_170
    locations_country_161.CountryCode = 'GU'
    locations_country_161.ISO3CountryCode = 'GUM'
    locations_country_161.PhonePrefix = None
    locations_country_161.InternetSuffix = '.gu'
    locations_country_161.ISO3166Country = '316'
    locations_country_161 = importer.save_or_locate(locations_country_161)

    locations_country_162 = Country()
    locations_country_162.GeographicalUnitId = 'Country_GP'
    locations_country_162.GeographicalUnitCategory = 'Country'
    locations_country_162.GeographicalUnitName = 'Guadeloupe'
    locations_country_162.GeographicalUnitShortName = 'Guadeloupe'
    locations_country_162.HierarchyLevel = 30
    locations_country_162.IsPartOf = locations_geographicalunit_7
    locations_country_162.geographicalunit_ptr = locations_geographicalunit_171
    locations_country_162.CountryCode = 'GP'
    locations_country_162.ISO3CountryCode = 'GLP'
    locations_country_162.PhonePrefix = '1-473'
    locations_country_162.InternetSuffix = '.gp'
    locations_country_162.ISO3166Country = '312'
    locations_country_162 = importer.save_or_locate(locations_country_162)

    locations_country_163 = Country()
    locations_country_163.GeographicalUnitId = 'Country_GD'
    locations_country_163.GeographicalUnitCategory = 'Country'
    locations_country_163.GeographicalUnitName = 'Grenada'
    locations_country_163.GeographicalUnitShortName = 'Grenada'
    locations_country_163.HierarchyLevel = 30
    locations_country_163.IsPartOf = locations_geographicalunit_7
    locations_country_163.geographicalunit_ptr = locations_geographicalunit_172
    locations_country_163.CountryCode = 'GD'
    locations_country_163.ISO3CountryCode = 'GRD'
    locations_country_163.PhonePrefix = '299'
    locations_country_163.InternetSuffix = '.gd'
    locations_country_163.ISO3166Country = '308'
    locations_country_163 = importer.save_or_locate(locations_country_163)

    locations_country_164 = Country()
    locations_country_164.GeographicalUnitId = 'Country_GL'
    locations_country_164.GeographicalUnitCategory = 'Country'
    locations_country_164.GeographicalUnitName = 'Greenland'
    locations_country_164.GeographicalUnitShortName = 'Greenland'
    locations_country_164.HierarchyLevel = 30
    locations_country_164.IsPartOf = locations_geographicalunit_7
    locations_country_164.geographicalunit_ptr = locations_geographicalunit_173
    locations_country_164.CountryCode = 'GL'
    locations_country_164.ISO3CountryCode = 'GRL'
    locations_country_164.PhonePrefix = '30'
    locations_country_164.InternetSuffix = '.gl'
    locations_country_164.ISO3166Country = '304'
    locations_country_164 = importer.save_or_locate(locations_country_164)

    locations_country_165 = Country()
    locations_country_165.GeographicalUnitId = 'Country_GR'
    locations_country_165.GeographicalUnitCategory = 'Country'
    locations_country_165.GeographicalUnitName = 'Greece'
    locations_country_165.GeographicalUnitShortName = 'Greece'
    locations_country_165.HierarchyLevel = 30
    locations_country_165.IsPartOf = locations_geographicalunit_2
    locations_country_165.geographicalunit_ptr = locations_geographicalunit_174
    locations_country_165.CountryCode = 'GR'
    locations_country_165.ISO3CountryCode = 'GRC'
    locations_country_165.PhonePrefix = '350'
    locations_country_165.InternetSuffix = '.gr'
    locations_country_165.ISO3166Country = '300'
    locations_country_165 = importer.save_or_locate(locations_country_165)

    locations_country_166 = Country()
    locations_country_166.GeographicalUnitId = 'Country_GI'
    locations_country_166.GeographicalUnitCategory = 'Country'
    locations_country_166.GeographicalUnitName = 'Gibraltar'
    locations_country_166.GeographicalUnitShortName = 'Gibraltar'
    locations_country_166.HierarchyLevel = 30
    locations_country_166.IsPartOf = locations_geographicalunit_2
    locations_country_166.geographicalunit_ptr = locations_geographicalunit_175
    locations_country_166.CountryCode = 'GI'
    locations_country_166.ISO3CountryCode = 'GIB'
    locations_country_166.PhonePrefix = '233'
    locations_country_166.InternetSuffix = '.gi'
    locations_country_166.ISO3166Country = '292'
    locations_country_166 = importer.save_or_locate(locations_country_166)

    locations_country_167 = Country()
    locations_country_167.GeographicalUnitId = 'Country_GH'
    locations_country_167.GeographicalUnitCategory = 'Country'
    locations_country_167.GeographicalUnitName = 'Ghana'
    locations_country_167.GeographicalUnitShortName = 'Ghana'
    locations_country_167.HierarchyLevel = 30
    locations_country_167.IsPartOf = locations_geographicalunit_3
    locations_country_167.geographicalunit_ptr = locations_geographicalunit_176
    locations_country_167.CountryCode = 'GH'
    locations_country_167.ISO3CountryCode = 'GHA'
    locations_country_167.PhonePrefix = '49'
    locations_country_167.InternetSuffix = '.gh'
    locations_country_167.ISO3166Country = '288'
    locations_country_167 = importer.save_or_locate(locations_country_167)

    locations_country_168 = Country()
    locations_country_168.GeographicalUnitId = 'Country_DE'
    locations_country_168.GeographicalUnitCategory = 'Country'
    locations_country_168.GeographicalUnitName = 'Germany'
    locations_country_168.GeographicalUnitShortName = 'Germany'
    locations_country_168.HierarchyLevel = 30
    locations_country_168.IsPartOf = locations_geographicalunit_2
    locations_country_168.geographicalunit_ptr = locations_geographicalunit_177
    locations_country_168.CountryCode = 'DE'
    locations_country_168.ISO3CountryCode = 'DEU'
    locations_country_168.PhonePrefix = '995'
    locations_country_168.InternetSuffix = '.de'
    locations_country_168.ISO3166Country = '276'
    locations_country_168 = importer.save_or_locate(locations_country_168)

    locations_country_169 = Country()
    locations_country_169.GeographicalUnitId = 'Country_GE'
    locations_country_169.GeographicalUnitCategory = 'Country'
    locations_country_169.GeographicalUnitName = 'Georgia'
    locations_country_169.GeographicalUnitShortName = 'Georgia'
    locations_country_169.HierarchyLevel = 30
    locations_country_169.IsPartOf = locations_geographicalunit_2
    locations_country_169.geographicalunit_ptr = locations_geographicalunit_178
    locations_country_169.CountryCode = 'GE'
    locations_country_169.ISO3CountryCode = 'GEO'
    locations_country_169.PhonePrefix = '220'
    locations_country_169.InternetSuffix = '.ge'
    locations_country_169.ISO3166Country = '268'
    locations_country_169 = importer.save_or_locate(locations_country_169)

    locations_country_170 = Country()
    locations_country_170.GeographicalUnitId = 'Country_GM'
    locations_country_170.GeographicalUnitCategory = 'Country'
    locations_country_170.GeographicalUnitName = 'Gambia (the)'
    locations_country_170.GeographicalUnitShortName = 'Gambia'
    locations_country_170.HierarchyLevel = 30
    locations_country_170.IsPartOf = locations_geographicalunit_3
    locations_country_170.geographicalunit_ptr = locations_geographicalunit_179
    locations_country_170.CountryCode = 'GM'
    locations_country_170.ISO3CountryCode = 'GMB'
    locations_country_170.PhonePrefix = '241'
    locations_country_170.InternetSuffix = '.gm'
    locations_country_170.ISO3166Country = '270'
    locations_country_170 = importer.save_or_locate(locations_country_170)

    locations_country_171 = Country()
    locations_country_171.GeographicalUnitId = 'Country_GA'
    locations_country_171.GeographicalUnitCategory = 'Country'
    locations_country_171.GeographicalUnitName = 'Gabon'
    locations_country_171.GeographicalUnitShortName = 'Gabon'
    locations_country_171.HierarchyLevel = 30
    locations_country_171.IsPartOf = locations_geographicalunit_3
    locations_country_171.geographicalunit_ptr = locations_geographicalunit_180
    locations_country_171.CountryCode = 'GA'
    locations_country_171.ISO3CountryCode = 'GAB'
    locations_country_171.PhonePrefix = None
    locations_country_171.InternetSuffix = '.ga'
    locations_country_171.ISO3166Country = '266'
    locations_country_171 = importer.save_or_locate(locations_country_171)

    locations_country_172 = Country()
    locations_country_172.GeographicalUnitId = 'Country_TF'
    locations_country_172.GeographicalUnitCategory = 'Country'
    locations_country_172.GeographicalUnitName = 'French Southern Territories (the)'
    locations_country_172.GeographicalUnitShortName = 'French Southern Territories'
    locations_country_172.HierarchyLevel = 30
    locations_country_172.IsPartOf = locations_geographicalunit_4
    locations_country_172.geographicalunit_ptr = locations_geographicalunit_181
    locations_country_172.CountryCode = 'TF'
    locations_country_172.ISO3CountryCode = 'ATF'
    locations_country_172.PhonePrefix = '689'
    locations_country_172.InternetSuffix = '.tf'
    locations_country_172.ISO3166Country = '260'
    locations_country_172 = importer.save_or_locate(locations_country_172)

    locations_country_173 = Country()
    locations_country_173.GeographicalUnitId = 'Country_PF'
    locations_country_173.GeographicalUnitCategory = 'Country'
    locations_country_173.GeographicalUnitName = 'French Polynesia'
    locations_country_173.GeographicalUnitShortName = 'French Polynesia'
    locations_country_173.HierarchyLevel = 30
    locations_country_173.IsPartOf = locations_geographicalunit_6
    locations_country_173.geographicalunit_ptr = locations_geographicalunit_182
    locations_country_173.CountryCode = 'PF'
    locations_country_173.ISO3CountryCode = 'PYF'
    locations_country_173.PhonePrefix = None
    locations_country_173.InternetSuffix = '.pf'
    locations_country_173.ISO3166Country = '258'
    locations_country_173 = importer.save_or_locate(locations_country_173)

    locations_country_174 = Country()
    locations_country_174.GeographicalUnitId = 'Country_GF'
    locations_country_174.GeographicalUnitCategory = 'Country'
    locations_country_174.GeographicalUnitName = 'French Guiana'
    locations_country_174.GeographicalUnitShortName = 'French Guiana'
    locations_country_174.HierarchyLevel = 30
    locations_country_174.IsPartOf = locations_geographicalunit_8
    locations_country_174.geographicalunit_ptr = locations_geographicalunit_183
    locations_country_174.CountryCode = 'GF'
    locations_country_174.ISO3CountryCode = 'GUF'
    locations_country_174.PhonePrefix = '33'
    locations_country_174.InternetSuffix = '.fr'
    locations_country_174.ISO3166Country = '254'
    locations_country_174 = importer.save_or_locate(locations_country_174)

    locations_country_175 = Country()
    locations_country_175.GeographicalUnitId = 'Country_FI'
    locations_country_175.GeographicalUnitCategory = 'Country'
    locations_country_175.GeographicalUnitName = 'Finland'
    locations_country_175.GeographicalUnitShortName = 'Finland'
    locations_country_175.HierarchyLevel = 30
    locations_country_175.IsPartOf = locations_geographicalunit_2
    locations_country_175.geographicalunit_ptr = locations_geographicalunit_184
    locations_country_175.CountryCode = 'FI'
    locations_country_175.ISO3CountryCode = 'FIN'
    locations_country_175.PhonePrefix = '679'
    locations_country_175.InternetSuffix = '.fi'
    locations_country_175.ISO3166Country = '246'
    locations_country_175 = importer.save_or_locate(locations_country_175)

    locations_country_176 = Country()
    locations_country_176.GeographicalUnitId = 'Country_FJ'
    locations_country_176.GeographicalUnitCategory = 'Country'
    locations_country_176.GeographicalUnitName = 'Fiji'
    locations_country_176.GeographicalUnitShortName = 'Fiji'
    locations_country_176.HierarchyLevel = 30
    locations_country_176.IsPartOf = locations_geographicalunit_6
    locations_country_176.geographicalunit_ptr = locations_geographicalunit_185
    locations_country_176.CountryCode = 'FJ'
    locations_country_176.ISO3CountryCode = 'FJI'
    locations_country_176.PhonePrefix = '298'
    locations_country_176.InternetSuffix = '.fj'
    locations_country_176.ISO3166Country = '242'
    locations_country_176 = importer.save_or_locate(locations_country_176)

    locations_country_177 = Country()
    locations_country_177.GeographicalUnitId = 'Country_FO'
    locations_country_177.GeographicalUnitCategory = 'Country'
    locations_country_177.GeographicalUnitName = 'Faroe Islands (the)'
    locations_country_177.GeographicalUnitShortName = 'Faroe Islands'
    locations_country_177.HierarchyLevel = 30
    locations_country_177.IsPartOf = locations_geographicalunit_2
    locations_country_177.geographicalunit_ptr = locations_geographicalunit_186
    locations_country_177.CountryCode = 'FO'
    locations_country_177.ISO3CountryCode = 'FRO'
    locations_country_177.PhonePrefix = '500'
    locations_country_177.InternetSuffix = '.fo'
    locations_country_177.ISO3166Country = '234'
    locations_country_177 = importer.save_or_locate(locations_country_177)

    locations_country_178 = Country()
    locations_country_178.GeographicalUnitId = 'Country_FK'
    locations_country_178.GeographicalUnitCategory = 'Country'
    locations_country_178.GeographicalUnitName = 'Falkland Islands (the) [Malvinas]'
    locations_country_178.GeographicalUnitShortName = 'Falkland Islands'
    locations_country_178.HierarchyLevel = 30
    locations_country_178.IsPartOf = locations_geographicalunit_8
    locations_country_178.geographicalunit_ptr = locations_geographicalunit_187
    locations_country_178.CountryCode = 'FK'
    locations_country_178.ISO3CountryCode = 'FLK'
    locations_country_178.PhonePrefix = '251'
    locations_country_178.InternetSuffix = '.fk'
    locations_country_178.ISO3166Country = '238'
    locations_country_178 = importer.save_or_locate(locations_country_178)

    locations_country_179 = Country()
    locations_country_179.GeographicalUnitId = 'Country_ET'
    locations_country_179.GeographicalUnitCategory = 'Country'
    locations_country_179.GeographicalUnitName = 'Ethiopia'
    locations_country_179.GeographicalUnitShortName = 'Ethiopia'
    locations_country_179.HierarchyLevel = 30
    locations_country_179.IsPartOf = locations_geographicalunit_3
    locations_country_179.geographicalunit_ptr = locations_geographicalunit_188
    locations_country_179.CountryCode = 'ET'
    locations_country_179.ISO3CountryCode = 'ETH'
    locations_country_179.PhonePrefix = '268'
    locations_country_179.InternetSuffix = '.et'
    locations_country_179.ISO3166Country = '231'
    locations_country_179 = importer.save_or_locate(locations_country_179)

    locations_country_180 = Country()
    locations_country_180.GeographicalUnitId = 'Country_SZ'
    locations_country_180.GeographicalUnitCategory = 'Country'
    locations_country_180.GeographicalUnitName = 'Eswatini'
    locations_country_180.GeographicalUnitShortName = 'Eswatini'
    locations_country_180.HierarchyLevel = 30
    locations_country_180.IsPartOf = locations_geographicalunit_3
    locations_country_180.geographicalunit_ptr = locations_geographicalunit_189
    locations_country_180.CountryCode = 'SZ'
    locations_country_180.ISO3CountryCode = 'SWZ'
    locations_country_180.PhonePrefix = '372'
    locations_country_180.InternetSuffix = '.sz'
    locations_country_180.ISO3166Country = '748'
    locations_country_180 = importer.save_or_locate(locations_country_180)

    locations_country_181 = Country()
    locations_country_181.GeographicalUnitId = 'Country_EE'
    locations_country_181.GeographicalUnitCategory = 'Country'
    locations_country_181.GeographicalUnitName = 'Estonia'
    locations_country_181.GeographicalUnitShortName = 'Estonia'
    locations_country_181.HierarchyLevel = 30
    locations_country_181.IsPartOf = locations_geographicalunit_2
    locations_country_181.geographicalunit_ptr = locations_geographicalunit_190
    locations_country_181.CountryCode = 'EE'
    locations_country_181.ISO3CountryCode = 'EST'
    locations_country_181.PhonePrefix = '291'
    locations_country_181.InternetSuffix = '.ee'
    locations_country_181.ISO3166Country = '233'
    locations_country_181 = importer.save_or_locate(locations_country_181)

    locations_country_182 = Country()
    locations_country_182.GeographicalUnitId = 'Country_ER'
    locations_country_182.GeographicalUnitCategory = 'Country'
    locations_country_182.GeographicalUnitName = 'Eritrea'
    locations_country_182.GeographicalUnitShortName = 'Eritrea'
    locations_country_182.HierarchyLevel = 30
    locations_country_182.IsPartOf = locations_geographicalunit_3
    locations_country_182.geographicalunit_ptr = locations_geographicalunit_191
    locations_country_182.CountryCode = 'ER'
    locations_country_182.ISO3CountryCode = 'ERI'
    locations_country_182.PhonePrefix = '240'
    locations_country_182.InternetSuffix = '.er'
    locations_country_182.ISO3166Country = '232'
    locations_country_182 = importer.save_or_locate(locations_country_182)

    locations_country_183 = Country()
    locations_country_183.GeographicalUnitId = 'Country_GQ'
    locations_country_183.GeographicalUnitCategory = 'Country'
    locations_country_183.GeographicalUnitName = 'Equatorial Guinea'
    locations_country_183.GeographicalUnitShortName = 'Equatorial Guinea'
    locations_country_183.HierarchyLevel = 30
    locations_country_183.IsPartOf = locations_geographicalunit_3
    locations_country_183.geographicalunit_ptr = locations_geographicalunit_192
    locations_country_183.CountryCode = 'GQ'
    locations_country_183.ISO3CountryCode = 'GNQ'
    locations_country_183.PhonePrefix = '503'
    locations_country_183.InternetSuffix = '.gq'
    locations_country_183.ISO3166Country = '226'
    locations_country_183 = importer.save_or_locate(locations_country_183)

    locations_country_184 = Country()
    locations_country_184.GeographicalUnitId = 'Country_SV'
    locations_country_184.GeographicalUnitCategory = 'Country'
    locations_country_184.GeographicalUnitName = 'El Salvador'
    locations_country_184.GeographicalUnitShortName = 'El Salvador'
    locations_country_184.HierarchyLevel = 30
    locations_country_184.IsPartOf = locations_geographicalunit_7
    locations_country_184.geographicalunit_ptr = locations_geographicalunit_193
    locations_country_184.CountryCode = 'SV'
    locations_country_184.ISO3CountryCode = 'SLV'
    locations_country_184.PhonePrefix = '20'
    locations_country_184.InternetSuffix = '.sv'
    locations_country_184.ISO3166Country = '222'
    locations_country_184 = importer.save_or_locate(locations_country_184)

    locations_country_185 = Country()
    locations_country_185.GeographicalUnitId = 'Country_EG'
    locations_country_185.GeographicalUnitCategory = 'Country'
    locations_country_185.GeographicalUnitName = 'Egypt'
    locations_country_185.GeographicalUnitShortName = 'Egypt'
    locations_country_185.HierarchyLevel = 30
    locations_country_185.IsPartOf = locations_geographicalunit_3
    locations_country_185.geographicalunit_ptr = locations_geographicalunit_194
    locations_country_185.CountryCode = 'EG'
    locations_country_185.ISO3CountryCode = 'EGY'
    locations_country_185.PhonePrefix = '593'
    locations_country_185.InternetSuffix = '.eg'
    locations_country_185.ISO3166Country = '818'
    locations_country_185 = importer.save_or_locate(locations_country_185)

    locations_country_186 = Country()
    locations_country_186.GeographicalUnitId = 'Country_EC'
    locations_country_186.GeographicalUnitCategory = 'Country'
    locations_country_186.GeographicalUnitName = 'Ecuador'
    locations_country_186.GeographicalUnitShortName = 'Ecuador'
    locations_country_186.HierarchyLevel = 30
    locations_country_186.IsPartOf = locations_geographicalunit_8
    locations_country_186.geographicalunit_ptr = locations_geographicalunit_195
    locations_country_186.CountryCode = 'EC'
    locations_country_186.ISO3CountryCode = 'ECU'
    locations_country_186.PhonePrefix = '1-809, 1-829, 1-849'
    locations_country_186.InternetSuffix = '.ec'
    locations_country_186.ISO3166Country = '218'
    locations_country_186 = importer.save_or_locate(locations_country_186)

    locations_country_187 = Country()
    locations_country_187.GeographicalUnitId = 'Country_DO'
    locations_country_187.GeographicalUnitCategory = 'Country'
    locations_country_187.GeographicalUnitName = 'Dominican Republic (the)'
    locations_country_187.GeographicalUnitShortName = 'Dominican Republic'
    locations_country_187.HierarchyLevel = 30
    locations_country_187.IsPartOf = locations_geographicalunit_7
    locations_country_187.geographicalunit_ptr = locations_geographicalunit_196
    locations_country_187.CountryCode = 'DO'
    locations_country_187.ISO3CountryCode = 'DOM'
    locations_country_187.PhonePrefix = '1-767'
    locations_country_187.InternetSuffix = '.do'
    locations_country_187.ISO3166Country = '214'
    locations_country_187 = importer.save_or_locate(locations_country_187)

    locations_country_188 = Country()
    locations_country_188.GeographicalUnitId = 'Country_DM'
    locations_country_188.GeographicalUnitCategory = 'Country'
    locations_country_188.GeographicalUnitName = 'Dominica'
    locations_country_188.GeographicalUnitShortName = 'Dominica'
    locations_country_188.HierarchyLevel = 30
    locations_country_188.IsPartOf = locations_geographicalunit_7
    locations_country_188.geographicalunit_ptr = locations_geographicalunit_197
    locations_country_188.CountryCode = 'DM'
    locations_country_188.ISO3CountryCode = 'DMA'
    locations_country_188.PhonePrefix = '253'
    locations_country_188.InternetSuffix = '.dm'
    locations_country_188.ISO3166Country = '212'
    locations_country_188 = importer.save_or_locate(locations_country_188)

    locations_country_189 = Country()
    locations_country_189.GeographicalUnitId = 'Country_DJ'
    locations_country_189.GeographicalUnitCategory = 'Country'
    locations_country_189.GeographicalUnitName = 'Djibouti'
    locations_country_189.GeographicalUnitShortName = 'Djibouti'
    locations_country_189.HierarchyLevel = 30
    locations_country_189.IsPartOf = locations_geographicalunit_3
    locations_country_189.geographicalunit_ptr = locations_geographicalunit_198
    locations_country_189.CountryCode = 'DJ'
    locations_country_189.ISO3CountryCode = 'DJI'
    locations_country_189.PhonePrefix = '45'
    locations_country_189.InternetSuffix = '.dj'
    locations_country_189.ISO3166Country = '262'
    locations_country_189 = importer.save_or_locate(locations_country_189)

    locations_country_190 = Country()
    locations_country_190.GeographicalUnitId = 'Country_DK'
    locations_country_190.GeographicalUnitCategory = 'Country'
    locations_country_190.GeographicalUnitName = 'Denmark'
    locations_country_190.GeographicalUnitShortName = 'Denmark'
    locations_country_190.HierarchyLevel = 30
    locations_country_190.IsPartOf = locations_geographicalunit_2
    locations_country_190.geographicalunit_ptr = locations_geographicalunit_199
    locations_country_190.CountryCode = 'DK'
    locations_country_190.ISO3CountryCode = 'DNK'
    locations_country_190.PhonePrefix = '225'
    locations_country_190.InternetSuffix = '.dk'
    locations_country_190.ISO3166Country = '208'
    locations_country_190 = importer.save_or_locate(locations_country_190)

    locations_country_191 = Country()
    locations_country_191.GeographicalUnitId = 'Country_CI'
    locations_country_191.GeographicalUnitCategory = 'Country'
    locations_country_191.GeographicalUnitName = "Côte d'Ivoire"
    locations_country_191.GeographicalUnitShortName = "Côte d'Ivoire"
    locations_country_191.HierarchyLevel = 30
    locations_country_191.IsPartOf = locations_geographicalunit_3
    locations_country_191.geographicalunit_ptr = locations_geographicalunit_200
    locations_country_191.CountryCode = 'CI'
    locations_country_191.ISO3CountryCode = 'CIV'
    locations_country_191.PhonePrefix = '420'
    locations_country_191.InternetSuffix = '.ci'
    locations_country_191.ISO3166Country = '384'
    locations_country_191 = importer.save_or_locate(locations_country_191)

    locations_country_192 = Country()
    locations_country_192.GeographicalUnitId = 'Country_CZ'
    locations_country_192.GeographicalUnitCategory = 'Country'
    locations_country_192.GeographicalUnitName = 'Czechia'
    locations_country_192.GeographicalUnitShortName = 'Czechia'
    locations_country_192.HierarchyLevel = 30
    locations_country_192.IsPartOf = locations_geographicalunit_2
    locations_country_192.geographicalunit_ptr = locations_geographicalunit_201
    locations_country_192.CountryCode = 'CZ'
    locations_country_192.ISO3CountryCode = 'CZE'
    locations_country_192.PhonePrefix = '357'
    locations_country_192.InternetSuffix = '.cz'
    locations_country_192.ISO3166Country = '203'
    locations_country_192 = importer.save_or_locate(locations_country_192)

    locations_country_193 = Country()
    locations_country_193.GeographicalUnitId = 'Country_CY'
    locations_country_193.GeographicalUnitCategory = 'Country'
    locations_country_193.GeographicalUnitName = 'Cyprus'
    locations_country_193.GeographicalUnitShortName = 'Cyprus'
    locations_country_193.HierarchyLevel = 30
    locations_country_193.IsPartOf = locations_geographicalunit_2
    locations_country_193.geographicalunit_ptr = locations_geographicalunit_202
    locations_country_193.CountryCode = 'CY'
    locations_country_193.ISO3CountryCode = 'CYP'
    locations_country_193.PhonePrefix = '599'
    locations_country_193.InternetSuffix = '.cy'
    locations_country_193.ISO3166Country = '196'
    locations_country_193 = importer.save_or_locate(locations_country_193)

    locations_country_194 = Country()
    locations_country_194.GeographicalUnitId = 'Country_CW'
    locations_country_194.GeographicalUnitCategory = 'Country'
    locations_country_194.GeographicalUnitName = 'Curacao'
    locations_country_194.GeographicalUnitShortName = 'Curacao'
    locations_country_194.HierarchyLevel = 30
    locations_country_194.IsPartOf = locations_geographicalunit_7
    locations_country_194.geographicalunit_ptr = locations_geographicalunit_203
    locations_country_194.CountryCode = 'CW'
    locations_country_194.ISO3CountryCode = 'CUW'
    locations_country_194.PhonePrefix = '53'
    locations_country_194.InternetSuffix = '.cw'
    locations_country_194.ISO3166Country = '531'
    locations_country_194 = importer.save_or_locate(locations_country_194)

    locations_country_195 = Country()
    locations_country_195.GeographicalUnitId = 'Country_CU'
    locations_country_195.GeographicalUnitCategory = 'Country'
    locations_country_195.GeographicalUnitName = 'Cuba'
    locations_country_195.GeographicalUnitShortName = 'Cuba'
    locations_country_195.HierarchyLevel = 30
    locations_country_195.IsPartOf = locations_geographicalunit_7
    locations_country_195.geographicalunit_ptr = locations_geographicalunit_204
    locations_country_195.CountryCode = 'CU'
    locations_country_195.ISO3CountryCode = 'CUB'
    locations_country_195.PhonePrefix = '385'
    locations_country_195.InternetSuffix = '.cu'
    locations_country_195.ISO3166Country = '192'
    locations_country_195 = importer.save_or_locate(locations_country_195)

    locations_country_196 = Country()
    locations_country_196.GeographicalUnitId = 'Country_HR'
    locations_country_196.GeographicalUnitCategory = 'Country'
    locations_country_196.GeographicalUnitName = 'Croatia'
    locations_country_196.GeographicalUnitShortName = 'Croatia'
    locations_country_196.HierarchyLevel = 30
    locations_country_196.IsPartOf = locations_geographicalunit_2
    locations_country_196.geographicalunit_ptr = locations_geographicalunit_205
    locations_country_196.CountryCode = 'HR'
    locations_country_196.ISO3CountryCode = 'HRV'
    locations_country_196.PhonePrefix = '506'
    locations_country_196.InternetSuffix = '.hr'
    locations_country_196.ISO3166Country = '191'
    locations_country_196 = importer.save_or_locate(locations_country_196)

    locations_country_197 = Country()
    locations_country_197.GeographicalUnitId = 'Country_CR'
    locations_country_197.GeographicalUnitCategory = 'Country'
    locations_country_197.GeographicalUnitName = 'Costa Rica'
    locations_country_197.GeographicalUnitShortName = 'Costa Rica'
    locations_country_197.HierarchyLevel = 30
    locations_country_197.IsPartOf = locations_geographicalunit_7
    locations_country_197.geographicalunit_ptr = locations_geographicalunit_206
    locations_country_197.CountryCode = 'CR'
    locations_country_197.ISO3CountryCode = 'CRI'
    locations_country_197.PhonePrefix = '682'
    locations_country_197.InternetSuffix = '.cr'
    locations_country_197.ISO3166Country = '188'
    locations_country_197 = importer.save_or_locate(locations_country_197)

    locations_country_198 = Country()
    locations_country_198.GeographicalUnitId = 'Country_CK'
    locations_country_198.GeographicalUnitCategory = 'Country'
    locations_country_198.GeographicalUnitName = 'Cook Islands (the)'
    locations_country_198.GeographicalUnitShortName = 'Cook Islands'
    locations_country_198.HierarchyLevel = 30
    locations_country_198.IsPartOf = locations_geographicalunit_6
    locations_country_198.geographicalunit_ptr = locations_geographicalunit_207
    locations_country_198.CountryCode = 'CK'
    locations_country_198.ISO3CountryCode = 'COK'
    locations_country_198.PhonePrefix = '242'
    locations_country_198.InternetSuffix = '.ck'
    locations_country_198.ISO3166Country = '184'
    locations_country_198 = importer.save_or_locate(locations_country_198)

    locations_country_199 = Country()
    locations_country_199.GeographicalUnitId = 'Country_CG'
    locations_country_199.GeographicalUnitCategory = 'Country'
    locations_country_199.GeographicalUnitName = 'Congo, Republic of the'
    locations_country_199.GeographicalUnitShortName = 'Congo Brazzaville'
    locations_country_199.HierarchyLevel = 30
    locations_country_199.IsPartOf = locations_geographicalunit_3
    locations_country_199.geographicalunit_ptr = locations_geographicalunit_208
    locations_country_199.CountryCode = 'CG'
    locations_country_199.ISO3CountryCode = 'COG'
    locations_country_199.PhonePrefix = '243'
    locations_country_199.InternetSuffix = '.cg'
    locations_country_199.ISO3166Country = '178'
    locations_country_199 = importer.save_or_locate(locations_country_199)

    locations_country_200 = Country()
    locations_country_200.GeographicalUnitId = 'Country_CD'
    locations_country_200.GeographicalUnitCategory = 'Country'
    locations_country_200.GeographicalUnitName = 'Congo, Democratic Republic of the'
    locations_country_200.GeographicalUnitShortName = 'Congo, Democratic Republic of the'
    locations_country_200.HierarchyLevel = 30
    locations_country_200.IsPartOf = locations_geographicalunit_3
    locations_country_200.geographicalunit_ptr = locations_geographicalunit_209
    locations_country_200.CountryCode = 'CD'
    locations_country_200.ISO3CountryCode = 'COD'
    locations_country_200.PhonePrefix = '269'
    locations_country_200.InternetSuffix = '.cd'
    locations_country_200.ISO3166Country = '180'
    locations_country_200 = importer.save_or_locate(locations_country_200)

    locations_country_201 = Country()
    locations_country_201.GeographicalUnitId = 'Country_KM'
    locations_country_201.GeographicalUnitCategory = 'Country'
    locations_country_201.GeographicalUnitName = 'Comoros (the)'
    locations_country_201.GeographicalUnitShortName = 'Comoros '
    locations_country_201.HierarchyLevel = 30
    locations_country_201.IsPartOf = locations_geographicalunit_3
    locations_country_201.geographicalunit_ptr = locations_geographicalunit_210
    locations_country_201.CountryCode = 'KM'
    locations_country_201.ISO3CountryCode = 'COM'
    locations_country_201.PhonePrefix = '57'
    locations_country_201.InternetSuffix = '.km'
    locations_country_201.ISO3166Country = '174'
    locations_country_201 = importer.save_or_locate(locations_country_201)

    locations_country_202 = Country()
    locations_country_202.GeographicalUnitId = 'Country_CO'
    locations_country_202.GeographicalUnitCategory = 'Country'
    locations_country_202.GeographicalUnitName = 'Colombia'
    locations_country_202.GeographicalUnitShortName = 'Colombia'
    locations_country_202.HierarchyLevel = 30
    locations_country_202.IsPartOf = locations_geographicalunit_8
    locations_country_202.geographicalunit_ptr = locations_geographicalunit_211
    locations_country_202.CountryCode = 'CO'
    locations_country_202.ISO3CountryCode = 'COL'
    locations_country_202.PhonePrefix = '61'
    locations_country_202.InternetSuffix = '.co'
    locations_country_202.ISO3166Country = '170'
    locations_country_202 = importer.save_or_locate(locations_country_202)

    locations_country_203 = Country()
    locations_country_203.GeographicalUnitId = 'Country_CC'
    locations_country_203.GeographicalUnitCategory = 'Country'
    locations_country_203.GeographicalUnitName = 'Cocos (Keeling) Islands (the)'
    locations_country_203.GeographicalUnitShortName = 'Cocos Islands '
    locations_country_203.HierarchyLevel = 30
    locations_country_203.IsPartOf = locations_geographicalunit_5
    locations_country_203.geographicalunit_ptr = locations_geographicalunit_212
    locations_country_203.CountryCode = 'CC'
    locations_country_203.ISO3CountryCode = 'CCK'
    locations_country_203.PhonePrefix = '61'
    locations_country_203.InternetSuffix = '.cf'
    locations_country_203.ISO3166Country = '166'
    locations_country_203 = importer.save_or_locate(locations_country_203)

    locations_country_204 = Country()
    locations_country_204.GeographicalUnitId = 'Country_CX'
    locations_country_204.GeographicalUnitCategory = 'Country'
    locations_country_204.GeographicalUnitName = 'Christmas Island'
    locations_country_204.GeographicalUnitShortName = 'Christmas Island'
    locations_country_204.HierarchyLevel = 30
    locations_country_204.IsPartOf = locations_geographicalunit_5
    locations_country_204.geographicalunit_ptr = locations_geographicalunit_213
    locations_country_204.CountryCode = 'CX'
    locations_country_204.ISO3CountryCode = 'CXR'
    locations_country_204.PhonePrefix = '86'
    locations_country_204.InternetSuffix = '.cx'
    locations_country_204.ISO3166Country = '162'
    locations_country_204 = importer.save_or_locate(locations_country_204)

    locations_country_205 = Country()
    locations_country_205.GeographicalUnitId = 'Country_CN'
    locations_country_205.GeographicalUnitCategory = 'Country'
    locations_country_205.GeographicalUnitName = 'China'
    locations_country_205.GeographicalUnitShortName = 'China'
    locations_country_205.HierarchyLevel = 30
    locations_country_205.IsPartOf = locations_geographicalunit_5
    locations_country_205.geographicalunit_ptr = locations_geographicalunit_214
    locations_country_205.CountryCode = 'CN'
    locations_country_205.ISO3CountryCode = 'CHN'
    locations_country_205.PhonePrefix = '56'
    locations_country_205.InternetSuffix = '.cn'
    locations_country_205.ISO3166Country = '156'
    locations_country_205 = importer.save_or_locate(locations_country_205)

    locations_country_206 = Country()
    locations_country_206.GeographicalUnitId = 'Country_CL'
    locations_country_206.GeographicalUnitCategory = 'Country'
    locations_country_206.GeographicalUnitName = 'Chile'
    locations_country_206.GeographicalUnitShortName = 'Chile'
    locations_country_206.HierarchyLevel = 30
    locations_country_206.IsPartOf = locations_geographicalunit_8
    locations_country_206.geographicalunit_ptr = locations_geographicalunit_215
    locations_country_206.CountryCode = 'CL'
    locations_country_206.ISO3CountryCode = 'CHL'
    locations_country_206.PhonePrefix = '235'
    locations_country_206.InternetSuffix = '.cl'
    locations_country_206.ISO3166Country = '152'
    locations_country_206 = importer.save_or_locate(locations_country_206)

    locations_country_207 = Country()
    locations_country_207.GeographicalUnitId = 'Country_TD'
    locations_country_207.GeographicalUnitCategory = 'Country'
    locations_country_207.GeographicalUnitName = 'Chad'
    locations_country_207.GeographicalUnitShortName = 'Chad'
    locations_country_207.HierarchyLevel = 30
    locations_country_207.IsPartOf = locations_geographicalunit_3
    locations_country_207.geographicalunit_ptr = locations_geographicalunit_216
    locations_country_207.CountryCode = 'TD'
    locations_country_207.ISO3CountryCode = 'TCD'
    locations_country_207.PhonePrefix = '236'
    locations_country_207.InternetSuffix = '.td'
    locations_country_207.ISO3166Country = '148'
    locations_country_207 = importer.save_or_locate(locations_country_207)

    locations_country_208 = Country()
    locations_country_208.GeographicalUnitId = 'Country_CF'
    locations_country_208.GeographicalUnitCategory = 'Country'
    locations_country_208.GeographicalUnitName = 'Central African Republic (the)'
    locations_country_208.GeographicalUnitShortName = 'Central African Republic'
    locations_country_208.HierarchyLevel = 30
    locations_country_208.IsPartOf = locations_geographicalunit_3
    locations_country_208.geographicalunit_ptr = locations_geographicalunit_217
    locations_country_208.CountryCode = 'CF'
    locations_country_208.ISO3CountryCode = 'CAF'
    locations_country_208.PhonePrefix = '1-345'
    locations_country_208.InternetSuffix = '.cf'
    locations_country_208.ISO3166Country = '140'
    locations_country_208 = importer.save_or_locate(locations_country_208)

    locations_country_209 = Country()
    locations_country_209.GeographicalUnitId = 'Country_KY'
    locations_country_209.GeographicalUnitCategory = 'Country'
    locations_country_209.GeographicalUnitName = 'Cayman Islands (the)'
    locations_country_209.GeographicalUnitShortName = 'Cayman Islands'
    locations_country_209.HierarchyLevel = 30
    locations_country_209.IsPartOf = locations_geographicalunit_7
    locations_country_209.geographicalunit_ptr = locations_geographicalunit_218
    locations_country_209.CountryCode = 'KY'
    locations_country_209.ISO3CountryCode = 'CYM'
    locations_country_209.PhonePrefix = '1'
    locations_country_209.InternetSuffix = '.ky'
    locations_country_209.ISO3166Country = '136'
    locations_country_209 = importer.save_or_locate(locations_country_209)

    locations_country_210 = Country()
    locations_country_210.GeographicalUnitId = 'Country_CA'
    locations_country_210.GeographicalUnitCategory = 'Country'
    locations_country_210.GeographicalUnitName = 'Canada'
    locations_country_210.GeographicalUnitShortName = 'Canada'
    locations_country_210.HierarchyLevel = 30
    locations_country_210.IsPartOf = locations_geographicalunit_7
    locations_country_210.geographicalunit_ptr = locations_geographicalunit_219
    locations_country_210.CountryCode = 'CA'
    locations_country_210.ISO3CountryCode = 'CAN'
    locations_country_210.PhonePrefix = '237'
    locations_country_210.InternetSuffix = '.ca'
    locations_country_210.ISO3166Country = '124'
    locations_country_210 = importer.save_or_locate(locations_country_210)

    locations_country_211 = Country()
    locations_country_211.GeographicalUnitId = 'Country_CM'
    locations_country_211.GeographicalUnitCategory = 'Country'
    locations_country_211.GeographicalUnitName = 'Cameroon'
    locations_country_211.GeographicalUnitShortName = 'Cameroon'
    locations_country_211.HierarchyLevel = 30
    locations_country_211.IsPartOf = locations_geographicalunit_3
    locations_country_211.geographicalunit_ptr = locations_geographicalunit_220
    locations_country_211.CountryCode = 'CM'
    locations_country_211.ISO3CountryCode = 'CMR'
    locations_country_211.PhonePrefix = '855'
    locations_country_211.InternetSuffix = '.cm'
    locations_country_211.ISO3166Country = '120'
    locations_country_211 = importer.save_or_locate(locations_country_211)

    locations_country_212 = Country()
    locations_country_212.GeographicalUnitId = 'Country_KH'
    locations_country_212.GeographicalUnitCategory = 'Country'
    locations_country_212.GeographicalUnitName = 'Cambodia'
    locations_country_212.GeographicalUnitShortName = 'Cambodia'
    locations_country_212.HierarchyLevel = 30
    locations_country_212.IsPartOf = locations_geographicalunit_5
    locations_country_212.geographicalunit_ptr = locations_geographicalunit_221
    locations_country_212.CountryCode = 'KH'
    locations_country_212.ISO3CountryCode = 'KHM'
    locations_country_212.PhonePrefix = '238'
    locations_country_212.InternetSuffix = '.kh'
    locations_country_212.ISO3166Country = '116'
    locations_country_212 = importer.save_or_locate(locations_country_212)

    locations_country_213 = Country()
    locations_country_213.GeographicalUnitId = 'Country_CV'
    locations_country_213.GeographicalUnitCategory = 'Country'
    locations_country_213.GeographicalUnitName = 'Cabo Verde'
    locations_country_213.GeographicalUnitShortName = 'Cabo Verde'
    locations_country_213.HierarchyLevel = 30
    locations_country_213.IsPartOf = locations_geographicalunit_3
    locations_country_213.geographicalunit_ptr = locations_geographicalunit_222
    locations_country_213.CountryCode = 'CV'
    locations_country_213.ISO3CountryCode = 'CPV'
    locations_country_213.PhonePrefix = '257'
    locations_country_213.InternetSuffix = '.cv'
    locations_country_213.ISO3166Country = '132'
    locations_country_213 = importer.save_or_locate(locations_country_213)

    locations_country_214 = Country()
    locations_country_214.GeographicalUnitId = 'Country_BI'
    locations_country_214.GeographicalUnitCategory = 'Country'
    locations_country_214.GeographicalUnitName = 'Burundi'
    locations_country_214.GeographicalUnitShortName = 'Burundi'
    locations_country_214.HierarchyLevel = 30
    locations_country_214.IsPartOf = locations_geographicalunit_3
    locations_country_214.geographicalunit_ptr = locations_geographicalunit_223
    locations_country_214.CountryCode = 'BI'
    locations_country_214.ISO3CountryCode = 'BDI'
    locations_country_214.PhonePrefix = '226'
    locations_country_214.InternetSuffix = '.bi'
    locations_country_214.ISO3166Country = '108'
    locations_country_214 = importer.save_or_locate(locations_country_214)

    locations_country_215 = Country()
    locations_country_215.GeographicalUnitId = 'Country_BF'
    locations_country_215.GeographicalUnitCategory = 'Country'
    locations_country_215.GeographicalUnitName = 'Burkina Faso'
    locations_country_215.GeographicalUnitShortName = 'Burkina Faso'
    locations_country_215.HierarchyLevel = 30
    locations_country_215.IsPartOf = locations_geographicalunit_3
    locations_country_215.geographicalunit_ptr = locations_geographicalunit_224
    locations_country_215.CountryCode = 'BF'
    locations_country_215.ISO3CountryCode = 'BFA'
    locations_country_215.PhonePrefix = '359'
    locations_country_215.InternetSuffix = '.bf'
    locations_country_215.ISO3166Country = '854'
    locations_country_215 = importer.save_or_locate(locations_country_215)

    locations_country_216 = Country()
    locations_country_216.GeographicalUnitId = 'Country_BG'
    locations_country_216.GeographicalUnitCategory = 'Country'
    locations_country_216.GeographicalUnitName = 'Bulgaria'
    locations_country_216.GeographicalUnitShortName = 'Bulgaria'
    locations_country_216.HierarchyLevel = 30
    locations_country_216.IsPartOf = locations_geographicalunit_2
    locations_country_216.geographicalunit_ptr = locations_geographicalunit_225
    locations_country_216.CountryCode = 'BG'
    locations_country_216.ISO3CountryCode = 'BGR'
    locations_country_216.PhonePrefix = '673'
    locations_country_216.InternetSuffix = '.bg'
    locations_country_216.ISO3166Country = '100'
    locations_country_216 = importer.save_or_locate(locations_country_216)

    locations_country_217 = Country()
    locations_country_217.GeographicalUnitId = 'Country_BN'
    locations_country_217.GeographicalUnitCategory = 'Country'
    locations_country_217.GeographicalUnitName = 'Brunei Darussalam'
    locations_country_217.GeographicalUnitShortName = 'Brunei Darussalam'
    locations_country_217.HierarchyLevel = 30
    locations_country_217.IsPartOf = locations_geographicalunit_5
    locations_country_217.geographicalunit_ptr = locations_geographicalunit_226
    locations_country_217.CountryCode = 'BN'
    locations_country_217.ISO3CountryCode = 'BRN'
    locations_country_217.PhonePrefix = '246'
    locations_country_217.InternetSuffix = '.bn'
    locations_country_217.ISO3166Country = '96'
    locations_country_217 = importer.save_or_locate(locations_country_217)

    locations_country_218 = Country()
    locations_country_218.GeographicalUnitId = 'Country_IO'
    locations_country_218.GeographicalUnitCategory = 'Country'
    locations_country_218.GeographicalUnitName = 'British Indian Ocean Territory (the)'
    locations_country_218.GeographicalUnitShortName = 'British Indian Ocean Territory'
    locations_country_218.HierarchyLevel = 30
    locations_country_218.IsPartOf = locations_geographicalunit_5
    locations_country_218.geographicalunit_ptr = locations_geographicalunit_227
    locations_country_218.CountryCode = 'IO'
    locations_country_218.ISO3CountryCode = 'IOT'
    locations_country_218.PhonePrefix = '55'
    locations_country_218.InternetSuffix = '.io'
    locations_country_218.ISO3166Country = '86'
    locations_country_218 = importer.save_or_locate(locations_country_218)

    locations_country_219 = Country()
    locations_country_219.GeographicalUnitId = 'Country_BR'
    locations_country_219.GeographicalUnitCategory = 'Country'
    locations_country_219.GeographicalUnitName = 'Brazil'
    locations_country_219.GeographicalUnitShortName = 'Brazil'
    locations_country_219.HierarchyLevel = 30
    locations_country_219.IsPartOf = locations_geographicalunit_8
    locations_country_219.geographicalunit_ptr = locations_geographicalunit_228
    locations_country_219.CountryCode = 'BR'
    locations_country_219.ISO3CountryCode = 'BRA'
    locations_country_219.PhonePrefix = None
    locations_country_219.InternetSuffix = '.br'
    locations_country_219.ISO3166Country = '76'
    locations_country_219 = importer.save_or_locate(locations_country_219)

    locations_country_220 = Country()
    locations_country_220.GeographicalUnitId = 'Country_BV'
    locations_country_220.GeographicalUnitCategory = 'Country'
    locations_country_220.GeographicalUnitName = 'Bouvet Island'
    locations_country_220.GeographicalUnitShortName = 'Bouvet Island'
    locations_country_220.HierarchyLevel = 30
    locations_country_220.IsPartOf = locations_geographicalunit_4
    locations_country_220.geographicalunit_ptr = locations_geographicalunit_229
    locations_country_220.CountryCode = 'BV'
    locations_country_220.ISO3CountryCode = 'BVT'
    locations_country_220.PhonePrefix = '267'
    locations_country_220.InternetSuffix = '.bv'
    locations_country_220.ISO3166Country = '74'
    locations_country_220 = importer.save_or_locate(locations_country_220)

    locations_country_221 = Country()
    locations_country_221.GeographicalUnitId = 'Country_BW'
    locations_country_221.GeographicalUnitCategory = 'Country'
    locations_country_221.GeographicalUnitName = 'Botswana'
    locations_country_221.GeographicalUnitShortName = 'Botswana'
    locations_country_221.HierarchyLevel = 30
    locations_country_221.IsPartOf = locations_geographicalunit_3
    locations_country_221.geographicalunit_ptr = locations_geographicalunit_230
    locations_country_221.CountryCode = 'BW'
    locations_country_221.ISO3CountryCode = 'BWA'
    locations_country_221.PhonePrefix = '387'
    locations_country_221.InternetSuffix = '.bw'
    locations_country_221.ISO3166Country = '72'
    locations_country_221 = importer.save_or_locate(locations_country_221)

    locations_country_222 = Country()
    locations_country_222.GeographicalUnitId = 'Country_BA'
    locations_country_222.GeographicalUnitCategory = 'Country'
    locations_country_222.GeographicalUnitName = 'Bosnia and Herzegovina'
    locations_country_222.GeographicalUnitShortName = 'Bosnia and Herzegovina'
    locations_country_222.HierarchyLevel = 30
    locations_country_222.IsPartOf = locations_geographicalunit_2
    locations_country_222.geographicalunit_ptr = locations_geographicalunit_231
    locations_country_222.CountryCode = 'BA'
    locations_country_222.ISO3CountryCode = 'BIH'
    locations_country_222.PhonePrefix = None
    locations_country_222.InternetSuffix = '.ba'
    locations_country_222.ISO3166Country = '70'
    locations_country_222 = importer.save_or_locate(locations_country_222)

    locations_country_223 = Country()
    locations_country_223.GeographicalUnitId = 'Country_BQ'
    locations_country_223.GeographicalUnitCategory = 'Country'
    locations_country_223.GeographicalUnitName = 'Bonaire, Sint Eustatius and Saba'
    locations_country_223.GeographicalUnitShortName = 'Bonaire, Sint Eustatius and Saba'
    locations_country_223.HierarchyLevel = 30
    locations_country_223.IsPartOf = locations_geographicalunit_7
    locations_country_223.geographicalunit_ptr = locations_geographicalunit_232
    locations_country_223.CountryCode = 'BQ'
    locations_country_223.ISO3CountryCode = 'BES'
    locations_country_223.PhonePrefix = '591'
    locations_country_223.InternetSuffix = '.bq'
    locations_country_223.ISO3166Country = '535'
    locations_country_223 = importer.save_or_locate(locations_country_223)

    locations_country_224 = Country()
    locations_country_224.GeographicalUnitId = 'Country_BO'
    locations_country_224.GeographicalUnitCategory = 'Country'
    locations_country_224.GeographicalUnitName = 'Bolivia (Plurinational State of)'
    locations_country_224.GeographicalUnitShortName = 'Bolivia'
    locations_country_224.HierarchyLevel = 30
    locations_country_224.IsPartOf = locations_geographicalunit_8
    locations_country_224.geographicalunit_ptr = locations_geographicalunit_233
    locations_country_224.CountryCode = 'BO'
    locations_country_224.ISO3CountryCode = 'BOL'
    locations_country_224.PhonePrefix = '975'
    locations_country_224.InternetSuffix = '.bo'
    locations_country_224.ISO3166Country = '68'
    locations_country_224 = importer.save_or_locate(locations_country_224)

    locations_country_225 = Country()
    locations_country_225.GeographicalUnitId = 'Country_BT'
    locations_country_225.GeographicalUnitCategory = 'Country'
    locations_country_225.GeographicalUnitName = 'Bhutan'
    locations_country_225.GeographicalUnitShortName = 'Bhutan'
    locations_country_225.HierarchyLevel = 30
    locations_country_225.IsPartOf = locations_geographicalunit_5
    locations_country_225.geographicalunit_ptr = locations_geographicalunit_234
    locations_country_225.CountryCode = 'BT'
    locations_country_225.ISO3CountryCode = 'BTN'
    locations_country_225.PhonePrefix = '1-441'
    locations_country_225.InternetSuffix = '.bt'
    locations_country_225.ISO3166Country = '64'
    locations_country_225 = importer.save_or_locate(locations_country_225)

    locations_country_226 = Country()
    locations_country_226.GeographicalUnitId = 'Country_BM'
    locations_country_226.GeographicalUnitCategory = 'Country'
    locations_country_226.GeographicalUnitName = 'Bermuda'
    locations_country_226.GeographicalUnitShortName = 'Bermuda'
    locations_country_226.HierarchyLevel = 30
    locations_country_226.IsPartOf = locations_geographicalunit_7
    locations_country_226.geographicalunit_ptr = locations_geographicalunit_235
    locations_country_226.CountryCode = 'BM'
    locations_country_226.ISO3CountryCode = 'BMU'
    locations_country_226.PhonePrefix = '229'
    locations_country_226.InternetSuffix = '.bm'
    locations_country_226.ISO3166Country = '60'
    locations_country_226 = importer.save_or_locate(locations_country_226)

    locations_country_227 = Country()
    locations_country_227.GeographicalUnitId = 'Country_BJ'
    locations_country_227.GeographicalUnitCategory = 'Country'
    locations_country_227.GeographicalUnitName = 'Benin'
    locations_country_227.GeographicalUnitShortName = 'Benin'
    locations_country_227.HierarchyLevel = 30
    locations_country_227.IsPartOf = locations_geographicalunit_3
    locations_country_227.geographicalunit_ptr = locations_geographicalunit_236
    locations_country_227.CountryCode = 'BJ'
    locations_country_227.ISO3CountryCode = 'BEN'
    locations_country_227.PhonePrefix = '501'
    locations_country_227.InternetSuffix = '.bj'
    locations_country_227.ISO3166Country = '204'
    locations_country_227 = importer.save_or_locate(locations_country_227)

    locations_country_228 = Country()
    locations_country_228.GeographicalUnitId = 'Country_BZ'
    locations_country_228.GeographicalUnitCategory = 'Country'
    locations_country_228.GeographicalUnitName = 'Belize'
    locations_country_228.GeographicalUnitShortName = 'Belize'
    locations_country_228.HierarchyLevel = 30
    locations_country_228.IsPartOf = locations_geographicalunit_7
    locations_country_228.geographicalunit_ptr = locations_geographicalunit_237
    locations_country_228.CountryCode = 'BZ'
    locations_country_228.ISO3CountryCode = 'BLZ'
    locations_country_228.PhonePrefix = '32'
    locations_country_228.InternetSuffix = '.bz'
    locations_country_228.ISO3166Country = '84'
    locations_country_228 = importer.save_or_locate(locations_country_228)

    locations_country_229 = Country()
    locations_country_229.GeographicalUnitId = 'Country_BY'
    locations_country_229.GeographicalUnitCategory = 'Country'
    locations_country_229.GeographicalUnitName = 'Belarus'
    locations_country_229.GeographicalUnitShortName = 'Belarus'
    locations_country_229.HierarchyLevel = 30
    locations_country_229.IsPartOf = locations_geographicalunit_2
    locations_country_229.geographicalunit_ptr = locations_geographicalunit_238
    locations_country_229.CountryCode = 'BY'
    locations_country_229.ISO3CountryCode = 'BLR'
    locations_country_229.PhonePrefix = '1-246'
    locations_country_229.InternetSuffix = '.by'
    locations_country_229.ISO3166Country = '112'
    locations_country_229 = importer.save_or_locate(locations_country_229)

    locations_country_230 = Country()
    locations_country_230.GeographicalUnitId = 'Country_BB'
    locations_country_230.GeographicalUnitCategory = 'Country'
    locations_country_230.GeographicalUnitName = 'Barbados'
    locations_country_230.GeographicalUnitShortName = 'Barbados'
    locations_country_230.HierarchyLevel = 30
    locations_country_230.IsPartOf = locations_geographicalunit_7
    locations_country_230.geographicalunit_ptr = locations_geographicalunit_239
    locations_country_230.CountryCode = 'BB'
    locations_country_230.ISO3CountryCode = 'BRB'
    locations_country_230.PhonePrefix = '880'
    locations_country_230.InternetSuffix = '.bb'
    locations_country_230.ISO3166Country = '52'
    locations_country_230 = importer.save_or_locate(locations_country_230)

    locations_country_231 = Country()
    locations_country_231.GeographicalUnitId = 'Country_BD'
    locations_country_231.GeographicalUnitCategory = 'Country'
    locations_country_231.GeographicalUnitName = 'Bangladesh'
    locations_country_231.GeographicalUnitShortName = 'Bangladesh'
    locations_country_231.HierarchyLevel = 30
    locations_country_231.IsPartOf = locations_geographicalunit_5
    locations_country_231.geographicalunit_ptr = locations_geographicalunit_240
    locations_country_231.CountryCode = 'BD'
    locations_country_231.ISO3CountryCode = 'BGD'
    locations_country_231.PhonePrefix = '973'
    locations_country_231.InternetSuffix = '.bd'
    locations_country_231.ISO3166Country = '50'
    locations_country_231 = importer.save_or_locate(locations_country_231)

    locations_country_232 = Country()
    locations_country_232.GeographicalUnitId = 'Country_BH'
    locations_country_232.GeographicalUnitCategory = 'Country'
    locations_country_232.GeographicalUnitName = 'Bahrain'
    locations_country_232.GeographicalUnitShortName = 'Bahrain'
    locations_country_232.HierarchyLevel = 30
    locations_country_232.IsPartOf = locations_geographicalunit_5
    locations_country_232.geographicalunit_ptr = locations_geographicalunit_241
    locations_country_232.CountryCode = 'BH'
    locations_country_232.ISO3CountryCode = 'BHR'
    locations_country_232.PhonePrefix = '1-242'
    locations_country_232.InternetSuffix = '.bh'
    locations_country_232.ISO3166Country = '48'
    locations_country_232 = importer.save_or_locate(locations_country_232)

    locations_country_233 = Country()
    locations_country_233.GeographicalUnitId = 'Country_BS'
    locations_country_233.GeographicalUnitCategory = 'Country'
    locations_country_233.GeographicalUnitName = 'Bahamas (the)'
    locations_country_233.GeographicalUnitShortName = 'Bahamas'
    locations_country_233.HierarchyLevel = 30
    locations_country_233.IsPartOf = locations_geographicalunit_7
    locations_country_233.geographicalunit_ptr = locations_geographicalunit_242
    locations_country_233.CountryCode = 'BS'
    locations_country_233.ISO3CountryCode = 'BHS'
    locations_country_233.PhonePrefix = '994'
    locations_country_233.InternetSuffix = '.bs'
    locations_country_233.ISO3166Country = '44'
    locations_country_233 = importer.save_or_locate(locations_country_233)

    locations_country_234 = Country()
    locations_country_234.GeographicalUnitId = 'Country_AZ'
    locations_country_234.GeographicalUnitCategory = 'Country'
    locations_country_234.GeographicalUnitName = 'Azerbaijan'
    locations_country_234.GeographicalUnitShortName = 'Azerbaijan'
    locations_country_234.HierarchyLevel = 30
    locations_country_234.IsPartOf = locations_geographicalunit_2
    locations_country_234.geographicalunit_ptr = locations_geographicalunit_243
    locations_country_234.CountryCode = 'AZ'
    locations_country_234.ISO3CountryCode = 'AZE'
    locations_country_234.PhonePrefix = '43'
    locations_country_234.InternetSuffix = '.az'
    locations_country_234.ISO3166Country = '31'
    locations_country_234 = importer.save_or_locate(locations_country_234)

    locations_country_235 = Country()
    locations_country_235.GeographicalUnitId = 'Country_AT'
    locations_country_235.GeographicalUnitCategory = 'Country'
    locations_country_235.GeographicalUnitName = 'Austria'
    locations_country_235.GeographicalUnitShortName = 'Austria'
    locations_country_235.HierarchyLevel = 30
    locations_country_235.IsPartOf = locations_geographicalunit_2
    locations_country_235.geographicalunit_ptr = locations_geographicalunit_244
    locations_country_235.CountryCode = 'AT'
    locations_country_235.ISO3CountryCode = 'AUT'
    locations_country_235.PhonePrefix = '61'
    locations_country_235.InternetSuffix = '.at'
    locations_country_235.ISO3166Country = '40'
    locations_country_235 = importer.save_or_locate(locations_country_235)

    locations_country_236 = Country()
    locations_country_236.GeographicalUnitId = 'Country_AU'
    locations_country_236.GeographicalUnitCategory = 'Country'
    locations_country_236.GeographicalUnitName = 'Australia'
    locations_country_236.GeographicalUnitShortName = 'Australia'
    locations_country_236.HierarchyLevel = 30
    locations_country_236.IsPartOf = locations_geographicalunit_6
    locations_country_236.geographicalunit_ptr = locations_geographicalunit_245
    locations_country_236.CountryCode = 'AU'
    locations_country_236.ISO3CountryCode = 'AUS'
    locations_country_236.PhonePrefix = '297'
    locations_country_236.InternetSuffix = '.au'
    locations_country_236.ISO3166Country = '36'
    locations_country_236 = importer.save_or_locate(locations_country_236)

    locations_country_237 = Country()
    locations_country_237.GeographicalUnitId = 'Country_AW'
    locations_country_237.GeographicalUnitCategory = 'Country'
    locations_country_237.GeographicalUnitName = 'Aruba'
    locations_country_237.GeographicalUnitShortName = 'Aruba'
    locations_country_237.HierarchyLevel = 30
    locations_country_237.IsPartOf = locations_geographicalunit_7
    locations_country_237.geographicalunit_ptr = locations_geographicalunit_246
    locations_country_237.CountryCode = 'AW'
    locations_country_237.ISO3CountryCode = 'ABW'
    locations_country_237.PhonePrefix = '374'
    locations_country_237.InternetSuffix = '.aw'
    locations_country_237.ISO3166Country = '533'
    locations_country_237 = importer.save_or_locate(locations_country_237)

    locations_country_238 = Country()
    locations_country_238.GeographicalUnitId = 'Country_AM'
    locations_country_238.GeographicalUnitCategory = 'Country'
    locations_country_238.GeographicalUnitName = 'Armenia'
    locations_country_238.GeographicalUnitShortName = 'Armenia'
    locations_country_238.HierarchyLevel = 30
    locations_country_238.IsPartOf = locations_geographicalunit_2
    locations_country_238.geographicalunit_ptr = locations_geographicalunit_247
    locations_country_238.CountryCode = 'AM'
    locations_country_238.ISO3CountryCode = 'ARM'
    locations_country_238.PhonePrefix = '54'
    locations_country_238.InternetSuffix = '.am'
    locations_country_238.ISO3166Country = '51'
    locations_country_238 = importer.save_or_locate(locations_country_238)

    locations_country_239 = Country()
    locations_country_239.GeographicalUnitId = 'Country_AR'
    locations_country_239.GeographicalUnitCategory = 'Country'
    locations_country_239.GeographicalUnitName = 'Argentina'
    locations_country_239.GeographicalUnitShortName = 'Argentina'
    locations_country_239.HierarchyLevel = 30
    locations_country_239.IsPartOf = locations_geographicalunit_8
    locations_country_239.geographicalunit_ptr = locations_geographicalunit_248
    locations_country_239.CountryCode = 'AR'
    locations_country_239.ISO3CountryCode = 'ARG'
    locations_country_239.PhonePrefix = '1-268'
    locations_country_239.InternetSuffix = '.ar'
    locations_country_239.ISO3166Country = '32'
    locations_country_239 = importer.save_or_locate(locations_country_239)

    locations_country_240 = Country()
    locations_country_240.GeographicalUnitId = 'Country_AG'
    locations_country_240.GeographicalUnitCategory = 'Country'
    locations_country_240.GeographicalUnitName = 'Antigua and Barbuda'
    locations_country_240.GeographicalUnitShortName = 'Antigua and Barbuda'
    locations_country_240.HierarchyLevel = 30
    locations_country_240.IsPartOf = locations_geographicalunit_7
    locations_country_240.geographicalunit_ptr = locations_geographicalunit_249
    locations_country_240.CountryCode = 'AG'
    locations_country_240.ISO3CountryCode = 'ATG'
    locations_country_240.PhonePrefix = '672'
    locations_country_240.InternetSuffix = '.ag'
    locations_country_240.ISO3166Country = '28'
    locations_country_240 = importer.save_or_locate(locations_country_240)

    locations_country_241 = Country()
    locations_country_241.GeographicalUnitId = 'Country_AQ'
    locations_country_241.GeographicalUnitCategory = 'Country'
    locations_country_241.GeographicalUnitName = 'Antarctica'
    locations_country_241.GeographicalUnitShortName = 'Antarctica'
    locations_country_241.HierarchyLevel = 30
    locations_country_241.IsPartOf = locations_geographicalunit_4
    locations_country_241.geographicalunit_ptr = locations_geographicalunit_250
    locations_country_241.CountryCode = 'AQ'
    locations_country_241.ISO3CountryCode = 'ATA'
    locations_country_241.PhonePrefix = '1-264'
    locations_country_241.InternetSuffix = '.aq'
    locations_country_241.ISO3166Country = '10'
    locations_country_241 = importer.save_or_locate(locations_country_241)

    locations_country_242 = Country()
    locations_country_242.GeographicalUnitId = 'Country_AI'
    locations_country_242.GeographicalUnitCategory = 'Country'
    locations_country_242.GeographicalUnitName = 'Anguilla'
    locations_country_242.GeographicalUnitShortName = 'Anguilla'
    locations_country_242.HierarchyLevel = 30
    locations_country_242.IsPartOf = locations_geographicalunit_7
    locations_country_242.geographicalunit_ptr = locations_geographicalunit_251
    locations_country_242.CountryCode = 'AI'
    locations_country_242.ISO3CountryCode = 'AIA'
    locations_country_242.PhonePrefix = '244'
    locations_country_242.InternetSuffix = '.ai'
    locations_country_242.ISO3166Country = '660'
    locations_country_242 = importer.save_or_locate(locations_country_242)

    locations_country_243 = Country()
    locations_country_243.GeographicalUnitId = 'Country_AO'
    locations_country_243.GeographicalUnitCategory = 'Country'
    locations_country_243.GeographicalUnitName = 'Angola'
    locations_country_243.GeographicalUnitShortName = 'Angola'
    locations_country_243.HierarchyLevel = 30
    locations_country_243.IsPartOf = locations_geographicalunit_3
    locations_country_243.geographicalunit_ptr = locations_geographicalunit_252
    locations_country_243.CountryCode = 'AO'
    locations_country_243.ISO3CountryCode = 'AGO'
    locations_country_243.PhonePrefix = '376'
    locations_country_243.InternetSuffix = '.ao'
    locations_country_243.ISO3166Country = '24'
    locations_country_243 = importer.save_or_locate(locations_country_243)

    locations_country_244 = Country()
    locations_country_244.GeographicalUnitId = 'Country_AD'
    locations_country_244.GeographicalUnitCategory = 'Country'
    locations_country_244.GeographicalUnitName = 'Andorra'
    locations_country_244.GeographicalUnitShortName = 'Andorra'
    locations_country_244.HierarchyLevel = 30
    locations_country_244.IsPartOf = locations_geographicalunit_2
    locations_country_244.geographicalunit_ptr = locations_geographicalunit_253
    locations_country_244.CountryCode = 'AD'
    locations_country_244.ISO3CountryCode = 'AND'
    locations_country_244.PhonePrefix = '1-684'
    locations_country_244.InternetSuffix = '.ad'
    locations_country_244.ISO3166Country = '20'
    locations_country_244 = importer.save_or_locate(locations_country_244)

    locations_country_245 = Country()
    locations_country_245.GeographicalUnitId = 'Country_AS'
    locations_country_245.GeographicalUnitCategory = 'Country'
    locations_country_245.GeographicalUnitName = 'American Samoa'
    locations_country_245.GeographicalUnitShortName = 'American Samoa'
    locations_country_245.HierarchyLevel = 30
    locations_country_245.IsPartOf = locations_geographicalunit_6
    locations_country_245.geographicalunit_ptr = locations_geographicalunit_254
    locations_country_245.CountryCode = 'AS'
    locations_country_245.ISO3CountryCode = 'ASM'
    locations_country_245.PhonePrefix = '213'
    locations_country_245.InternetSuffix = '.as'
    locations_country_245.ISO3166Country = '16'
    locations_country_245 = importer.save_or_locate(locations_country_245)

    locations_country_246 = Country()
    locations_country_246.GeographicalUnitId = 'Country_DZ'
    locations_country_246.GeographicalUnitCategory = 'Country'
    locations_country_246.GeographicalUnitName = 'Algeria'
    locations_country_246.GeographicalUnitShortName = 'Algeria'
    locations_country_246.HierarchyLevel = 30
    locations_country_246.IsPartOf = locations_geographicalunit_3
    locations_country_246.geographicalunit_ptr = locations_geographicalunit_255
    locations_country_246.CountryCode = 'DZ'
    locations_country_246.ISO3CountryCode = 'DZA'
    locations_country_246.PhonePrefix = '355'
    locations_country_246.InternetSuffix = '.dz'
    locations_country_246.ISO3166Country = '12'
    locations_country_246 = importer.save_or_locate(locations_country_246)

    locations_country_247 = Country()
    locations_country_247.GeographicalUnitId = 'Country_AL'
    locations_country_247.GeographicalUnitCategory = 'Country'
    locations_country_247.GeographicalUnitName = 'Albania'
    locations_country_247.GeographicalUnitShortName = 'Albania'
    locations_country_247.HierarchyLevel = 30
    locations_country_247.IsPartOf = locations_geographicalunit_2
    locations_country_247.geographicalunit_ptr = locations_geographicalunit_256
    locations_country_247.CountryCode = 'AL'
    locations_country_247.ISO3CountryCode = 'ALB'
    locations_country_247.PhonePrefix = '93'
    locations_country_247.InternetSuffix = '.al'
    locations_country_247.ISO3166Country = '8'
    locations_country_247 = importer.save_or_locate(locations_country_247)

    locations_country_248 = Country()
    locations_country_248.GeographicalUnitId = 'Country_AF'
    locations_country_248.GeographicalUnitCategory = 'Country'
    locations_country_248.GeographicalUnitName = 'Afghanistan'
    locations_country_248.GeographicalUnitShortName = 'Afghanistan'
    locations_country_248.HierarchyLevel = 30
    locations_country_248.IsPartOf = locations_geographicalunit_5
    locations_country_248.geographicalunit_ptr = locations_geographicalunit_257
    locations_country_248.CountryCode = 'AF'
    locations_country_248.ISO3CountryCode = 'AFG'
    locations_country_248.PhonePrefix = '599'
    locations_country_248.InternetSuffix = '.af'
    locations_country_248.ISO3166Country = '4'
    locations_country_248 = importer.save_or_locate(locations_country_248)

    locations_country_249 = Country()
    locations_country_249.GeographicalUnitId = 'Country_AN'
    locations_country_249.GeographicalUnitCategory = 'Country'
    locations_country_249.GeographicalUnitName = 'Antilles Neerlandaises'
    locations_country_249.GeographicalUnitShortName = 'Antilles Neerlandaises'
    locations_country_249.HierarchyLevel = 30
    locations_country_249.IsPartOf = locations_geographicalunit_7
    locations_country_249.geographicalunit_ptr = locations_geographicalunit_258
    locations_country_249.CountryCode = 'AN'
    locations_country_249.ISO3CountryCode = 'ANT'
    locations_country_249.PhonePrefix = None
    locations_country_249.InternetSuffix = '.an'
    locations_country_249.ISO3166Country = '530'
    locations_country_249 = importer.save_or_locate(locations_country_249)

    # Processing model: locations.models.City

    from locations.models import City

    locations_city_1 = City()
    locations_city_1.GeographicalUnitId = 'City_PARIS'
    locations_city_1.GeographicalUnitCategory = 'City'
    locations_city_1.GeographicalUnitName = 'Paris'
    locations_city_1.GeographicalUnitShortName = 'Paris'
    locations_city_1.HierarchyLevel = 40
    locations_city_1.IsPartOf = locations_geographicalunit_1
    locations_city_1.geographicalunit_ptr = locations_geographicalunit_10
    locations_city_1.CityCode = 'PARIS'
    locations_city_1 = importer.save_or_locate(locations_city_1)

    locations_city_2 = City()
    locations_city_2.GeographicalUnitId = 'City_MONTARGIS'
    locations_city_2.GeographicalUnitCategory = 'City'
    locations_city_2.GeographicalUnitName = 'Montargis'
    locations_city_2.GeographicalUnitShortName = 'Montargis'
    locations_city_2.HierarchyLevel = 40
    locations_city_2.IsPartOf = locations_geographicalunit_1
    locations_city_2.geographicalunit_ptr = locations_geographicalunit_11
    locations_city_2.CityCode = 'MONTARGIS'
    locations_city_2 = importer.save_or_locate(locations_city_2)

    # Processing model: locations.models.Address

    from locations.models import Address


    # Processing model: profiles.models.Profile

    from profiles.models import Profile

    profiles_profile_1 = Profile()
    profiles_profile_1.user =  importer.locate_object(User, "id", User, "id", 2, {'id': 2, 'password': 'pbkdf2_sha256$390000$iIccmMGIimyNXeO0Bv79f9$lcHTJxcGN4jPZC5breBTnfJDWiKsBTXwTi3Y4OREgHI=', 'last_login': None, 'is_superuser': False, 'username': 'bob', 'first_name': 'Bob', 'last_name': 'Lucky', 'email': 'g@tchak.com', 'is_staff': False, 'is_active': True, 'date_joined': dateutil.parser.parse("2023-01-24T19:20:54+00:00")} ) 
    profiles_profile_1.RelatedToBusinesspartner = partners_businesspartner_1
    profiles_profile_1.avatar = 'avatar.png'
    profiles_profile_1.updated = dateutil.parser.parse("2023-01-24T22:21:30.087576+00:00")
    profiles_profile_1.created = dateutil.parser.parse("2023-01-24T19:20:54.788363+00:00")
    profiles_profile_1 = importer.save_or_locate(profiles_profile_1)

    # Processing model: boxes.models.BoxReservationRequest

    from boxes.models import BoxReservationRequest


    # Processing model: partners.models.IndividualPerson

    from partners.models import IndividualPerson

    partners_individualperson_1 = IndividualPerson()
    partners_individualperson_1.BusinessPartnerId = 'aaa6782f-4033-4e53-8c62-fe84642558dd'
    partners_individualperson_1.BusinessPartnerclass = 'IndividualPerson'
    partners_individualperson_1.ConsumerStatus = 'Open'
    partners_individualperson_1.businesspartner_ptr = partners_businesspartner_1
    partners_individualperson_1.GivenName = 'Bob'
    partners_individualperson_1.LastName = 'Luck'
    partners_individualperson_1.Title = 'Mr'
    partners_individualperson_1.Consultation = 'Your Highness'
    partners_individualperson_1.Gender = 'M'
    partners_individualperson_1.NameAtBirth = ''
    partners_individualperson_1.DateOfBirth = None
    partners_individualperson_1.PlaceOfBirth = locations_city_1
    partners_individualperson_1.MaritalStatus = 'Single'
    partners_individualperson_1.EducationLevel = ''
    partners_individualperson_1.CountryOfBirth = locations_country_2
    partners_individualperson_1.Nationality = 'FR'
    partners_individualperson_1.SecondNationality = ''
    partners_individualperson_1 = importer.save_or_locate(partners_individualperson_1)

    # Processing model: partners.models.Organization

    from partners.models import Organization

    partners_organization_1 = Organization()
    partners_organization_1.BusinessPartnerId = '5cb0a39b-9460-44a0-9bde-d55bf1d6fa4f'
    partners_organization_1.BusinessPartnerclass = 'Organization'
    partners_organization_1.ConsumerStatus = 'Open'
    partners_organization_1.businesspartner_ptr = partners_businesspartner_2
    partners_organization_1.Name = 'Valentin'
    partners_organization_1.LegalForm = '1L24'
    partners_organization_1.DateOfIncorporation = dateutil.parser.parse("2000-12-06")
    partners_organization_1.CountryOfIncorporation = locations_country_2
    partners_organization_1.Register = '123456'
    partners_organization_1.PlaceOfRegister = ''
    partners_organization_1.RoleInClearing = ''
    partners_organization_1 = importer.save_or_locate(partners_organization_1)

    # Processing model: assets.models.RealEstateProperty

    from assets.models import RealEstateProperty


    # Processing model: assets.models.Box

    from assets.models import Box


    # Processing model: boxes.models.BoxConfirmedReservation

    from boxes.models import BoxConfirmedReservation


    # Processing model: boxes.models.BoxOccupied

    from boxes.models import BoxOccupied


    # Processing model: boxes.models.BoxOccupiedLog

    from boxes.models import BoxOccupiedLog


