using Microsoft.AspNetCore.Mvc;
using SpeissApi.Domain;

namespace SpeissApi.Controllers;

[ApiController]
[Route("[controller]/")]
public class StationsController : ControllerBase
{
    private readonly ITleStore _tleStore;
    private readonly ILogger<StationsController> _logger;

    public StationsController(ITleStore tleStore, ILogger<StationsController> logger)
    {
        _tleStore = tleStore;
        _logger = logger;
    }

    [HttpGet]
    [ResponseCache(Duration = 3600)]
    public async Task<IActionResult> GetAll()
    {
        var tles = await _tleStore.GetAll();

        if (tles is not null)
        {
            var response = tles.Select(tle => new Station(tle.NoradNumber, tle.Name));
            return Ok(response);
        }

        return new NotFoundResult();
    }

    [HttpGet("{satelliteId}")]
    [ResponseCache(Duration = 3600)]
    public async Task<IActionResult> GetByStationId(int satelliteId)
    {
        var tle = await _tleStore.GetBySatelliteId(satelliteId);

        return tle is not null
            ? Ok(new Station(tle.NoradNumber, tle.Name))
            : new NotFoundResult();
    }
}

public record Station(uint SatelliteId, string Name);
