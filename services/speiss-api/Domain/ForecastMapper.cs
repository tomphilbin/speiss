using SpeissApi.Extensions;

using static SpeissApi.Protos.SatellitePassesResponse.Types;

namespace SpeissApi.Domain;

public interface IForecastMapper
{
    Forecast FromSatellitePasses(SatellitePassesItem item);
}

public class ForecastMapper : IForecastMapper
{
    private IForecastVisibility _forecastVisibility;

    public ForecastMapper(IForecastVisibility forecastVisibility)
    {
        _forecastVisibility = forecastVisibility;
    }

    public Forecast FromSatellitePasses(SatellitePassesItem item)
    {
        var rating = _forecastVisibility.CalculateRating(item.PeakElevation, item.Magnitude);

        return new Forecast
        {
            StartTime = item.StartTime.ToUtcDateTime(),
            StartElevation = item.StartElevation,
            EndTime = item.EndTime.ToUtcDateTime(),
            EndElevation = item.EndElevation,
            PeakTime = item.PeakTime.ToUtcDateTime(),
            PeakElevation = item.PeakElevation,
            Magnitude = item.Magnitude,
            Rating = rating
        };
    }
}

public class Forecast
{
    public DateTime StartTime { get; init; }
    public double StartElevation { get; init; }
    public DateTime EndTime { get; init; }
    public double EndElevation { get; init; }
    public DateTime PeakTime { get; init; }
    public double PeakElevation { get; init; }
    public double Magnitude { get; init; }
    public double Rating { get; init; }
}