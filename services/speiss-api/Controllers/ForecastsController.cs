using System.ComponentModel.DataAnnotations;
using Microsoft.AspNetCore.Mvc;
using SpeissApi.Domain;

namespace SpeissApi.Controllers;

[ApiController]
[Route("[controller]/")]
public class ForecastsController : ControllerBase
{
    private readonly ITleStore _tleStore;
    private readonly IForecastMapper _forecastMapper;
    private readonly IForecastVisibility _forecastVisibility;
    private readonly IEphemerisClient _ephemerisClient;
    private readonly ILogger<ForecastsController> _logger;

    public ForecastsController(
        ITleStore tleStore,
        IForecastMapper forecastMapper,
        IForecastVisibility forecastVisibility,
        IEphemerisClient ephemerisClient,
        ILogger<ForecastsController> logger)
    {
        _tleStore = tleStore;
        _forecastMapper = forecastMapper;
        _forecastVisibility = forecastVisibility;
        _ephemerisClient = ephemerisClient;
        _logger = logger;
    }

    [HttpGet("station/{satelliteId}/{latitude}/{longitude}")]
    [ResponseCache(Duration = 3600)]
    public async Task<IActionResult> GetStations(
        int satelliteId,
        double latitude,
        double longitude,
        [FromQuery, Range(0, 8848)] int elevation = 0,
        [FromQuery, Range(1, 31)] int days = 10,
        [FromQuery, Range(1, 90)] int minDegrees = 10)
    {
        var tle = await _tleStore.GetBySatelliteId(satelliteId);

        if (tle is not null)
        {
            var options = new GetAllSatellitePassesOptions
            {
                TleName = tle.Name,
                TleLine1 = tle.Line1,
                TleLine2 = tle.Line2,
                Latitude = latitude,
                Longitude = longitude,
                Elevation = elevation,
                Days = days
            };

            var passes = await _ephemerisClient.GetAllSatellitePasses(options);

            var forecast = passes
                .Where(pass => pass.PeakElevation >= minDegrees && _forecastVisibility.IsVisible(pass))
                .Select(pass => _forecastMapper.FromSatellitePasses(pass));

            return Ok(forecast);

        }

        return new NotFoundResult();
    }
}
