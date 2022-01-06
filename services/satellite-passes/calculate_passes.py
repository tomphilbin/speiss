import math
import ephem

from datetime import datetime, timedelta

AU = ephem.meters_per_au / 1000
STANDARD_MAG = -1.8
TWILIGHT_START_DEG = -6


def get_all(tle, start_date, end_date, location) -> list:
    sun = ephem.Sun()
    observer = ephem.Observer()

    observer.date = datetime.utcfromtimestamp(
        start_date).strftime('%Y/%m/%d %H:%M:%S')
    observer.lat = str(location.latitude)
    observer.lon = str(location.longitude)
    observer.elevation = location.elevation

    satellite = ephem.readtle(tle.name, tle.line1, tle.line2)

    visible_passes = []

    while True:
        try:
            next_pass = observer.next_pass(satellite)
        except:
            break

        pass_end = next_pass[4].datetime()

        if pass_end >= datetime.utcfromtimestamp(end_date):
            break

        pass_start = next_pass[0].datetime()
        peak_elevation_time = next_pass[2].datetime()

        observer.date = pass_start.strftime('%Y/%m/%d %H:%M:%S')

        sun.compute(observer)
        satellite.compute(observer)

        pass_obj = {
            "start_time": round(pass_start.timestamp()),
            "start_elevation": round(next_pass[1], 2),
            "end_time": round(pass_end.timestamp()),
            "end_elevation": round(next_pass[5], 2),
            "peak_time": round(peak_elevation_time.timestamp()),
            "peak_elevation":  round(math.degrees(next_pass[3]), 2),
            "magnitude": calc_magnitude(satellite, sun),
            "sun_is_visible": math.degrees(sun.alt) > TWILIGHT_START_DEG
        }

        observer.date = peak_elevation_time.strftime('%Y/%m/%d %H:%M:%S')

        satellite.compute(observer)

        pass_obj["satellite_is_eclipsed"] = satellite.eclipsed

        visible_passes.append(pass_obj)

        observer.date = pass_end + timedelta(minutes=1)

    return visible_passes


def calc_magnitude(satellite, sun) -> float:
    a = sun.earth_distance * AU - ephem.earth_radius
    b = satellite.range / 1000

    angle_c = ephem.separation(
        (satellite.az, satellite.alt), (sun.az, sun.alt))

    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2) -
                  2 * a * b * math.cos(angle_c))

    phase_angle = math.acos(
        (math.pow(b, 2) + math.pow(c, 2) - math.pow(a, 2)) / (2 * b * c))

    mag = STANDARD_MAG - 15 + 5 * math.log10(satellite.range / 1000) - 2.5 * math.log10(
        math.sin(phase_angle) + ((math.pi - phase_angle) * math.cos(phase_angle)))

    return round(mag, 2)
