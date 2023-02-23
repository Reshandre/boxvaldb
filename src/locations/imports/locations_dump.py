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
# manage.py dumpscript locations
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

    # Processing model: locations.models.GeographicalUnit

    from locations.models import GeographicalUnit

    locations_geographicalunit_1 = GeographicalUnit()
    locations_geographicalunit_1.GeographicalUnitId = 'Country_FR'
    locations_geographicalunit_1.GeographicalUnitCategory = 'Country'
    locations_geographicalunit_1.GeographicalUnitName = 'Republique Francaise'
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
    locations_geographicalunit_9.GeographicalUnitShortName = 'BEL'
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
    locations_country_1.GeographicalUnitShortName = 'BEL'
    locations_country_1.HierarchyLevel = 30
    locations_country_1.IsPartOf = locations_geographicalunit_2
    locations_country_1.geographicalunit_ptr = locations_geographicalunit_9
    locations_country_1.CountryCode = 'BE'
    locations_country_1.ISO3CountryCode = 'BE'
    locations_country_1.PhonePrefix = '32'
    locations_country_1.InternetSuffix = ''
    locations_country_1 = importer.save_or_locate(locations_country_1)

    locations_country_2 = Country()
    locations_country_2.GeographicalUnitId = 'Country_FR'
    locations_country_2.GeographicalUnitCategory = 'Country'
    locations_country_2.GeographicalUnitName = 'Republique Francaise'
    locations_country_2.GeographicalUnitShortName = 'France'
    locations_country_2.HierarchyLevel = 30
    locations_country_2.IsPartOf = locations_geographicalunit_2
    locations_country_2.geographicalunit_ptr = locations_geographicalunit_1
    locations_country_2.CountryCode = 'FR'
    locations_country_2.ISO3CountryCode = 'FRA'
    locations_country_2.PhonePrefix = '33'
    locations_country_2.InternetSuffix = ''
    locations_country_2 = importer.save_or_locate(locations_country_2)

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


