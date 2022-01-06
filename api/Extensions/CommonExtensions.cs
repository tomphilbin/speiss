namespace SpeissApi.Extensions;

public static class SpeissApiExtensions
{
    public static DateTime ToUtcDateTime(this long unixTime) => DateTimeOffset.FromUnixTimeSeconds(unixTime).UtcDateTime;
}
