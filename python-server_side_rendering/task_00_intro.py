import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return
    
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    
    index = 1
    for person in attendees:
        content = template

        name = person.get("name") or "N/A"
        event_title = person.get("event_title") or "N/A"
        event_date = person.get("event_date") or "N/A"
        event_location = person.get("event_location") or "N/A"

        content = content.replace("{name}", name)
        content = content.replace("{event_title}", event_title)
        content = content.replace("{event_date}", event_date)
        content = content.replace("{event_location}", event_location)

        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing {filename}: {e}")

        index += 1
