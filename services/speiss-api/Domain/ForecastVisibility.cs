using Microsoft.Extensions.Options;
using SpeissApi.Config;

using static SpeissApi.Protos.SatellitePassesResponse.Types;

namespace SpeissApi.Domain;

public interface IForecastVisibility
{
    double CalculateRating(double maxElevation, double magnitude);
    bool IsVisible(SatellitePassesItem item);
}

public class ForecastVisibility : IForecastVisibility
{
    private const int magnitudeOffset = 2;
    private readonly double _maxDegrees;
    private readonly double _maxMagnitude;

    public ForecastVisibility(IOptions<Constants> constants)
    {
        _maxDegrees = constants.Value.MaxDegrees;
        _maxMagnitude = constants.Value.MaxMagnitude;
    }

    public double CalculateRating(double peakElevation, double magnitude)
    {
        var elevationRating = Math.Round(peakElevation / _maxDegrees, 2);

        var offsetMaxMagnitude = _maxMagnitude + magnitudeOffset;
        var offsetMagnitude = magnitude + magnitudeOffset;
        var magnitudeRating = Math.Round(offsetMaxMagnitude / offsetMagnitude / offsetMaxMagnitude, 2);

        return Math.Round((elevationRating + magnitudeRating) / 2, 2);
    }

    public bool IsVisible(SatellitePassesItem pass) =>
        pass.Magnitude <= _maxMagnitude
        && !pass.SatelliteIsEclipsed
        && !pass.SunIsVisible;

}