import numpy as np

def hello():
    return "Hello world"


def generate_locations():

    # Electric Vehicle Points
    ev_pts = pd.read_csv("Unique_EV_Points.csv")
    charge_pts = ev_pts.sample(n=NUM_CHARGERS)[['Longitude', 'Latitude']]
    charge_pts_list = list(charge_pts.itertuples(index=False, name=None))

    # Delivery locations Points
    dl = pd.read_csv("DeliveryLocations.csv")
    todays_locations = dl.sample(n=NUM_CUSTOMERS)
    dl_list = list(todays_locations.itertuples(index=False, name=None))

    # Fedex Ship Centre
    fedex_centre = [(104.0023106, 1.3731437)]

    locations = fedex_centre + dl_list + charge_pts_list
    return charge_pts_list, dl_list, fedex_centre, locations