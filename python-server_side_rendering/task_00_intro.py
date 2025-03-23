#!/usr/bin/python3
"""Module for generating personalized invitations from a template."""
import logging
import os
from typing import List, Dict, Union


def validate_template(template: str) -> bool:
    """
    Validate the template string.

    Args:
        template (str): Template string to validate

    Returns:
        bool: True if template is valid, False otherwise
    """
    required_placeholders = {'{name}', '{event_title}', '{event_date}', '{event_location}'}
    return all(placeholder in template for placeholder in required_placeholders)


def validate_attendee(attendee: Dict) -> bool:
    """
    Validate an attendee dictionary.

    Args:
        attendee (dict): Attendee dictionary to validate

    Returns:
        bool: True if attendee is valid, False otherwise
    """
    required_fields = {'name', 'event_title', 'event_date', 'event_location'}
    return isinstance(attendee, dict) and all(field in attendee for field in required_fields)


def generate_invitations(template: str, attendees: List[Dict[str, Union[str, None]]]) -> None:
    """
    Generate personalized invitation files from a template and list of attendees.

    Args:
        template (str): Template string with placeholders
        attendees (list): List of dictionaries containing attendee information

    Returns:
        None
    """
    # Configure logging with a more detailed format
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)

    # Input validation
    if not isinstance(template, str):
        logger.error("Invalid input: template must be a string, got %s", type(template))
        return

    if not template.strip():
        logger.error("Template is empty, no output files generated.")
        return

    if not validate_template(template):
        logger.error("Invalid template: missing required placeholders")
        return

    if not isinstance(attendees, list):
        logger.error("Invalid input: attendees must be a list, got %s", type(attendees))
        return

    if not attendees:
        logger.error("No data provided, no output files generated.")
        return

    # Validate all attendees before processing
    if not all(validate_attendee(attendee) for attendee in attendees):
        logger.error("Invalid input: all attendees must be dictionaries with required fields")
        return

    # Create output directory if it doesn't exist
    output_dir = "invitations"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each attendee
    for index, attendee in enumerate(attendees, 1):
        try:
            # Create a copy of the template for this attendee
            invitation = template

            # Replace placeholders with values
            for field in ['name', 'event_title', 'event_date', 'event_location']:
                value = attendee.get(field)
                value = 'N/A' if value is None else str(value)
                placeholder = '{' + field + '}'
                invitation = invitation.replace(placeholder, value)

            # Generate unique filename
            output_filename = os.path.join(output_dir, f'output_{index}.txt')

            # Write to output file
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(invitation)
            logger.info("Generated invitation file: %s", output_filename)

        except IOError as e:
            logger.error("Error writing to file %s: %s", output_filename, str(e))
        except Exception as e:
            logger.error("Unexpected error processing attendee %d: %s", index, str(e))

    logger.info("Invitation generation completed. Total invitations generated: %d", len(attendees)) 