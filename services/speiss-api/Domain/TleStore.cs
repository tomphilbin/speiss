using Microsoft.Extensions.Caching.Memory;
using Flurl.Http;
using SGPdotNET.TLE;
using SpeissApi.Config;
using Microsoft.Extensions.Options;

namespace SpeissApi.Domain
{
    public interface ITleStore
    {
        Task<Tle?> GetBySatelliteId(int satelliteId);
        Task<IEnumerable<Tle>> GetAll();
    }

    public class CachingTleStore : ITleStore
    {
        private readonly UriConfig _uriConfig;
        private readonly IMemoryCache _cache;
        private const string _cacheKey = "speiss/tle-lines";

        public CachingTleStore(IOptions<UriConfig> uriConfig, IMemoryCache cache)
        {
            _uriConfig = uriConfig.Value;
            _cache = cache;
        }

        public async Task<Tle?> GetBySatelliteId(int id)
        {
            var satellites = await GetAll();

            return satellites?.FirstOrDefault(s => s.NoradNumber == id);
        }

        public async Task<IEnumerable<Tle>> GetAll()
        {
            var tleLines = await FetchTleLines();

            return Tle.ParseElements(tleLines, threeLine: true);
        }

        private Task<string[]> FetchTleLines()
        {
            return _cache.GetOrCreateAsync<string[]>(_cacheKey, async entry =>
            {
                var result = await _uriConfig.TleEndpoint.GetStringAsync();

                entry.AbsoluteExpirationRelativeToNow = result is null
                    ? TimeSpan.FromMinutes(1)
                    : TimeSpan.FromHours(24);

                return result?.Replace("\r\n", "\n").Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries)
                    ?? new string[0];
            });
        }
    }
}