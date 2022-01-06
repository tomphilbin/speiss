using SpeissApi.Config;
using SpeissApi.Domain;

var builder = WebApplication.CreateBuilder(args);

builder.Services
    .AddSingleton<ITleStore, CachingTleStore>()
    .AddSingleton<IForecastMapper, ForecastMapper>()
    .AddSingleton<IForecastVisibility, ForecastVisibility>()
    .AddSingleton<ISatellitePassesClient, SatellitePassesGrpcClient>()
    .Configure<UriConfig>(builder.Configuration.GetSection(UriConfig.Name))
    .Configure<Constants>(builder.Configuration.GetSection(Constants.Name))
    .AddMemoryCache()
    .AddControllers();

var app = builder.Build();

app.MapControllers();

app.Run();
