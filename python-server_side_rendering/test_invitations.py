#!/usr/bin/python3
"""Test file for the invitation generator."""
from task_00_intro import generate_invitations

# Read the template from file
with open('template.txt', 'r') as file:
    template_content = file.read()

# Test data
attendees = [
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
    },
    {
        "name": "Charlie",
        "event_title": "AI Summit",
        "event_date": None,
        "event_location": "Boston"
    }
]

# Generate invitations
generate_invitations(template_content, attendees)

# Test error cases
print("\nTesting error cases:")
print("1. Empty template:")
generate_invitations("", attendees)

print("\n2. Empty attendees list:")
generate_invitations(template_content, [])

print("\n3. Invalid template type:")
generate_invitations(123, attendees)

print("\n4. Invalid attendees type:")
generate_invitations(template_content, "not a list") 