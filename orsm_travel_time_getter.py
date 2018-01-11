# -*- coding: utf-8 -*-
import json
import requests
import numpy as np
def query_travel_time(startlat, startlon, endlat, endlon, method):
    """
    Get a travel time back from MapZen's OSRM
    start, end: lon, lat tuples
    method: foot, car, bicycle
    returns travel time, in seconds
    TODO: bounds checking for coords
    """
    allowed = ('car','foot','bicycle')
    if method not in allowed:
        raise Exception(
            "Unknown method. Must be one of %s. Christ." % ', '.join(allowed))
        # http://router.project-osrm.org/route/v1/driving/13.388860,52.517037;13.397634,52.529407
    endpoint = 'http://router.project-osrm.org/route/v1'
    method = '/{m}'.format(m=method)
    # .format(m=method)でmの部分に代入
    # should be properly encoding second loc, but dict keys are unique!
    # reverse lon, lat because ugh
    params = '/{1},{0};{3},{2}'.format(startlon,startlat,endlon,endlat)
    req = requests.get(endpoint + method + params)
    try:
        req.raise_for_status()
    except requests.exceptions.HTTPError:
        return np.nan
    return req
