"""
Fake API shared between sites
"""

def get_shows(site_id=None):
    """
    Returns a fake list of stuff based on site id
    """

    if site_id is None:
        return []

    shows = [
        {'name': 'Restaurant Weddings', 'site': 'awesome_new_site'},
        {'name': 'BBQ Master', 'site': 'awesome_new_site'},
        {'name': 'Beverly Hills Tuna', 'site': 'default_site'},
        {'name': 'Beverly Hills Pet Detective', 'site': 'default_site'},
        {'name': 'Wicked Oil', 'site': 'awesome_new_site'},
        {'name': 'CSI Wives', 'site': 'default_site'},
        {'name': 'Whisker Addict', 'site': 'awesome_new_site'},
        {'name': 'Swamp Oil', 'site': 'default_site'},
    ]

    return [i for i in shows if i.get('site') == site_id]