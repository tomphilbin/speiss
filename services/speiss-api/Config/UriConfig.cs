namespace SpeissApi.Config;

public class UriConfig
{
    public const string Name = "Uri";

    public string TleEndpoint { get; set; } = String.Empty;

    public string EphemerisEndpoint { get; set; } = String.Empty;
}
