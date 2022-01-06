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

        return new Forecast(
            item.StartTime.ToUtcDateTime(),
            item.StartElevation,
            item.EndTime.ToUtcDateTime(),
            item.EndElevation,
            item.PeakTime.ToUtcDateTime(),
            item.PeakElevation,
            item.Magnitude,
            rating
        );
    }
}

public record Forecast(
    DateTime StartTime,
    double StartElevation,
    DateTime EndTime,
    double EndElevation,
    DateTime PeakTime,
    double PeakElevation,
    double Magnitude,
    double Rating
);
