def get_coordinate(record):
    """Return the coordinate string from the (treasure, coordinate) pair."""
    return record[1]


def convert_coordinate(coordinate):
    """Split "2F" into ("2", "F")."""
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Check if Azara's string coordinate matches Rui's tuple coordinate."""
    # Convert Azara's "2F" to ("2", "F") to compare it to Rui's record
    azara_coord = convert_coordinate(azara_record[1])
    rui_coord = rui_record[1]
    
    return azara_coord == rui_coord


def create_record(azara_record, rui_record):
    """Combine records if they match, otherwise return 'not a match'."""
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    """
    Format the combined records into a specific string format.
    Input: (treasure, coord, location, (coord1, coord2), quadrant)
    Output: (treasure, location, (coord1, coord2), quadrant)
    """
    report = ""
    for record in combined_record_group:
        # We exclude record[1] (Azara's string coordinate)
        clean_record = (record[0], record[2], record[3], record[4])
        report += str(clean_record) + "\n"
        
    return report