#!/usr/bin/env python3

def generate_invitations(template, attendees):
     if not isinstance(template, str):
        print("Invalid input: template should be a string.")
        return
     if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees should be a list of dictionaries.")
        return
     
     if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
     if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
     
     file_number = 1
     for attendee in attendees:
        text = template

        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")
        if event_date is None:
            event_date = "N/A"
                
        text = text.replace("{name}", str(name))
        text = text.replace("{event_title}", str(event_title))
        text = text.replace("{event_date}", str(event_date))
        text = text.replace("{event_location}", str(event_location))

        filename = f"output_{file_number}.txt"
        try:
            with open(filename, "w") as file:
                file.write(text)
        except Exception as e:
            print(f"Error writing {filename}: {e}")

        file_number += 1
