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
    private readonly ISatellitePassesClient _passesClient;
    private readonly ILogger<ForecastsController> _logger;

    public ForecastsController(
        ITleStore tleStore,
        IForecastMapper forecastMapper,
        IForecastVisibility forecastVisibility,
        ISatellitePassesClient passesClient,
        ILogger<ForecastsController> logger)
    {
        _tleStore = tleStore;
        _forecastMapper = forecastMapper;
        _forecastVisibility = forecastVisibility;
        _passesClient = passesClient;
        _logger = logger;
    }

    [HttpGet("station/{satelliteId}/{latitude}/{longitude}")]
    [ResponseCache(Duration = 3600)]
    public async Task<IActionResult> GetStations(
        int satelliteId,
        double latitude,
        double longitude,
        [FromQuery, Range(0, 8848)] int elevation = 0,
        [FromQuery, Range(1, 365)] int days = 7,
        [FromQuery, Range(1, 90)] int minDegrees = 10)
    {
        var tle = await _tleStore.GetBySatelliteId(satelliteId);

        if (tle is not null)
        {
            var options = new GetAllSatellitePassesOptions(tle.Name, tle.Line1, tle.Line2, latitude, longitude, elevation, days);

            var passes = await _passesClient.Get(options);

            var forecast = passes
                .Where(pass => pass.PeakElevation >= minDegrees && _forecastVisibility.IsVisible(pass))
                .Select(pass => _forecastMapper.FromSatellitePasses(pass));

            return Ok(forecast);

        }

        return new NotFoundResult();
    }
}
