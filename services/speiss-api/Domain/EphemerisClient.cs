using Grpc.Net.Client;
using Microsoft.Extensions.Options;
using SpeissApi.Config;
using SpeissApi.Protos;

using static SpeissApi.Protos.Ephemeris;
using static SpeissApi.Protos.SatellitePassesRequest.Types;
using static SpeissApi.Protos.SatellitePassesResponse.Types;

namespace SpeissApi.Domain;

public interface IEphemerisClient
{
    Task<List<SatellitePassesItem>> GetAllSatellitePasses(GetAllSatellitePassesOptions opts);
}

public class EphemerisGrpcClient : IEphemerisClient
{
    private readonly UriConfig _uriConfig;

    public EphemerisGrpcClient(IOptions<UriConfig> uriConfig)
    {
        _uriConfig = uriConfig.Value;
    }
    public async Task<List<SatellitePassesItem>> GetAllSatellitePasses(GetAllSatellitePassesOptions opts)
    {
        using var channel = GrpcChannel.ForAddress(_uriConfig.EphemerisEndpoint);

        var client = new EphemerisClient(channel);

        var request = new SatellitePassesRequest
        {
            StartDate = DateTimeOffset.UtcNow.ToUnixTimeSeconds(),
            EndDate = DateTimeOffset.UtcNow.AddDays(opts.Days).ToUnixTimeSeconds(),
            Location = new Location
            {
                Latitude = opts.Latitude,
                Longitude = opts.Longitude,
                Elevation = opts.Elevation
            },
            Tle = new Tle
            {
                Name = opts.TleName,
                Line1 = opts.TleLine1,
                Line2 = opts.TleLine2
            },
        };

        var response = await client.GetAllSatellitePassesAsync(request);

        return response.Items.ToList();
    }
}

public class GetAllSatellitePassesOptions
{
    public string TleName { get; init; } = String.Empty;
    public string TleLine1 { get; init; } = String.Empty;
    public string TleLine2 { get; init; } =String.Empty;
    public double Latitude { get; init; }
    public double Longitude { get; init; }
    public int Elevation { get; init; }
    public int Days { get; init; }
}