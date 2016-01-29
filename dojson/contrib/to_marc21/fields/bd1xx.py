# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

from dojson import utils

from ..model import to_marc21


@to_marc21.over('100', '^main_entry_personal_name$')
@utils.filter_values
def reverse_main_entry_personal_name(self, key, value):
    """Reverse - Main Entry-Personal Name."""
    indicator_map1 = {"Family name": "3", "Forename": "0", "Surname": "1"}
    return {
        'a': value.get('personal_name'),
        'c': utils.reverse_force_list(
            value.get('titles_and_words_associated_with_a_name')
        ),
        'b': value.get('numeration'),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': value.get('dates_associated_with_a_name'),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'j': utils.reverse_force_list(
            value.get('attribution_qualifier')
        ),
        'l': value.get('language_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'q': value.get('fuller_form_of_name'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'u': value.get('affiliation'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': value.get('title_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_personal_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('110', '^main_entry_corporate_name$')
@utils.filter_values
def reverse_main_entry_corporate_name(self, key, value):
    """Reverse - Main Entry-Corporate Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    return {
        'a': value.get('corporate_name_or_jurisdiction_name_as_entry_element'),
        'c': value.get('location_of_meeting'),
        'b': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'e': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_meeting_or_treaty_signing')
        ),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'l': value.get('language_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'u': value.get('affiliation'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number_r')
        ),
        't': value.get('title_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_corporate_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('111', '^main_entry_meeting_name$')
@utils.filter_values
def reverse_main_entry_meeting_name(self, key, value):
    """Reverse - Main Entry-Meeting Name."""
    indicator_map1 = {
        "Inverted name": "0",
        "Jurisdiction name": "1",
        "Name in direct order": "2"}
    return {
        'a': value.get('meeting_name_or_jurisdiction_name_as_entry_element'),
        'c': value.get('location_of_meeting'),
        'e': utils.reverse_force_list(
            value.get('subordinate_unit')
        ),
        'd': value.get('date_of_meeting'),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'j': utils.reverse_force_list(
            value.get('relator_term')
        ),
        'l': value.get('language_of_a_work'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_meeting')
        ),
        'q': value.get('name_of_meeting_following_jurisdiction_name_entry_element'),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        'u': value.get('affiliation'),
        '4': utils.reverse_force_list(
            value.get('relator_code')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        't': value.get('title_of_a_work'),
        '$ind1': indicator_map1.get(value.get('type_of_meeting_name_entry_element'), '_'),
        '$ind2': '_',
    }


@to_marc21.over('130', '^main_entry_uniform_title$')
@utils.filter_values
def reverse_main_entry_uniform_title(self, key, value):
    """Reverse - Main Entry-Uniform Title."""
    indicator_map1 = {"Number of nonfiling characters": "8"}
    return {
        'a': value.get('uniform_title'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')
        ),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')
        ),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')
        ),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')
        ),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        't': value.get('title_of_a_work'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('nonfiling_characters'), '_'),
        '$ind2': '_',
    }
