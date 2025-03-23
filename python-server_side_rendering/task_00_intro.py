#!/usr/bin/python3
"""Module for generating personalized invitations from a template."""
import logging


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and list of attendees.

    Args:
        template (str): Template string with placeholders
        attendees (list): List of dictionaries containing attendee information

    Returns:
        None
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Check if template is a string
    if not isinstance(template, str):
        logger.error("Invalid input: template must be a string")
        return

    # Check if template is empty
    if not template.strip():
        logger.error("Template is empty, no output files generated.")
        return

    # Check if attendees is a list
    if not isinstance(attendees, list):
        logger.error("Invalid input: attendees must be a list")
        return

    # Check if attendees list is empty
    if not attendees:
        logger.error("No data provided, no output files generated.")
        return

    # Check if all items in attendees are dictionaries
    if not all(isinstance(item, dict) for item in attendees):
        logger.error("Invalid input: all attendees must be dictionaries")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, 1):
        # Create a copy of the template for this attendee
        invitation = template

        # Replace placeholders with values, using 'N/A' for missing or None values
        for field in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(field)
            value = 'N/A' if value is None else str(value)
            placeholder = '{' + field + '}'
            invitation = invitation.replace(placeholder, value)

        # Write to output file
        try:
            output_filename = f'output_{index}.txt'
            with open(output_filename, 'w') as file:
                file.write(invitation)
            logger.info(f"Generated invitation file: {output_filename}")
        except IOError as e:
            logger.error(f"Error writing to file {output_filename}: {str(e)}") 