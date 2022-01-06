using Grpc.Net.Client;
using Microsoft.Extensions.Options;
using SpeissApi.Config;
using SpeissApi.Protos;

using static SpeissApi.Protos.SatellitePasses;
using static SpeissApi.Protos.SatellitePassesRequest.Types;
using static SpeissApi.Protos.SatellitePassesResponse.Types;

namespace SpeissApi.Domain;

public interface ISatellitePassesClient
{
    Task<List<SatellitePassesItem>> Get(GetAllSatellitePassesOptions opts);
}

public class SatellitePassesGrpcClient : ISatellitePassesClient
{
    private readonly UriConfig _uriConfig;

    public SatellitePassesGrpcClient(IOptions<UriConfig> uriConfig)
    {
        _uriConfig = uriConfig.Value;
    }
    public async Task<List<SatellitePassesItem>> Get(GetAllSatellitePassesOptions opts)
    {
        using var channel = GrpcChannel.ForAddress(_uriConfig.SatellitePassesEndpoint);

        var client = new SatellitePassesClient(channel);

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

        var response = await client.GetAllAsync(request);

        return response.Items.ToList();
    }
}

public record GetAllSatellitePassesOptions(
    string TleName,
    string TleLine1,
    string TleLine2,
    double Latitude,
    double Longitude,
    int Elevation,
    int Days);
