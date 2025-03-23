#!/usr/bin/python3
"""Unit tests for the invitation generator module."""
import unittest
import os
import shutil
from task_00_intro import generate_invitations, validate_template, validate_attendee


class TestInvitationGenerator(unittest.TestCase):
    """Test cases for the invitation generator module."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""
        
        self.valid_attendees = [
            {
                "name": "Alice",
                "event_title": "Python Conference",
                "event_date": "2023-07-15",
                "event_location": "New York"
            },
            {
                "name": "Bob",
                "event_title": "Data Science Workshop",
                "event_date": "2023-08-20",
                "event_location": "San Francisco"
            }
        ]

        # Create a test directory for output files
        if os.path.exists("invitations"):
            shutil.rmtree("invitations")

    def tearDown(self):
        """Clean up test fixtures after each test method."""
        if os.path.exists("invitations"):
            shutil.rmtree("invitations")

    def test_validate_template(self):
        """Test template validation."""
        # Test valid template
        self.assertTrue(validate_template(self.template))

        # Test invalid template (missing placeholder)
        invalid_template = "Hello {name}, welcome to {event_title}"
        self.assertFalse(validate_template(invalid_template))

        # Test empty template
        self.assertFalse(validate_template(""))

    def test_validate_attendee(self):
        """Test attendee validation."""
        # Test valid attendee
        valid_attendee = self.valid_attendees[0]
        self.assertTrue(validate_attendee(valid_attendee))

        # Test invalid attendee (missing field)
        invalid_attendee = {
            "name": "Charlie",
            "event_title": "AI Summit"
        }
        self.assertFalse(validate_attendee(invalid_attendee))

        # Test invalid attendee (not a dictionary)
        self.assertFalse(validate_attendee(["name", "event"]))

    def test_generate_invitations_valid_input(self):
        """Test invitation generation with valid input."""
        generate_invitations(self.template, self.valid_attendees)

        # Check if output directory exists
        self.assertTrue(os.path.exists("invitations"))

        # Check if correct number of files were generated
        files = os.listdir("invitations")
        self.assertEqual(len(files), len(self.valid_attendees))

        # Check content of generated files
        with open(os.path.join("invitations", "output_1.txt"), "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Alice", content)
            self.assertIn("Python Conference", content)
            self.assertIn("2023-07-15", content)
            self.assertIn("New York", content)

    def test_generate_invitations_with_none_values(self):
        """Test invitation generation with None values in attendee data."""
        attendees_with_none = [
            {
                "name": "Charlie",
                "event_title": None,
                "event_date": "2023-09-01",
                "event_location": "Boston"
            }
        ]
        generate_invitations(self.template, attendees_with_none)

        # Check if N/A is used for None values
        with open(os.path.join("invitations", "output_1.txt"), "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("N/A", content)

    def test_generate_invitations_invalid_inputs(self):
        """Test invitation generation with various invalid inputs."""
        # Test with invalid template type
        generate_invitations(123, self.valid_attendees)
        self.assertFalse(os.path.exists("invitations"))

        # Test with empty template
        generate_invitations("", self.valid_attendees)
        self.assertFalse(os.path.exists("invitations"))

        # Test with invalid attendees type
        generate_invitations(self.template, "not a list")
        self.assertFalse(os.path.exists("invitations"))

        # Test with empty attendees list
        generate_invitations(self.template, [])
        self.assertFalse(os.path.exists("invitations"))


if __name__ == '__main__':
    unittest.main() 