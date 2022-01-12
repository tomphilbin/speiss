using Microsoft.Extensions.Diagnostics.HealthChecks;
using SpeissApi.Config;
using SpeissApi.Domain;

var builder = WebApplication.CreateBuilder(args);

builder.Services
    .AddSingleton<ITleStore, CachingTleStore>()
    .AddTransient<IForecastMapper, ForecastMapper>()
    .AddTransient<IForecastVisibility, ForecastVisibility>()
    .AddTransient<IEphemerisClient, EphemerisGrpcClient>()
    .Configure<UriConfig>(builder.Configuration.GetSection(UriConfig.Name))
    .Configure<Constants>(builder.Configuration.GetSection(Constants.Name))
    .AddMemoryCache()
    .AddControllers();

builder.Services
    .AddHealthChecks()
    .AddCheck("health", () => HealthCheckResult.Healthy());

var app = builder.Build();

app.UseRouting();

app.UseEndpoints(endpoints =>
{
    endpoints.MapHealthChecks("/");
    endpoints.MapHealthChecks("/ready");
    endpoints.MapControllers();
});

app.Run();