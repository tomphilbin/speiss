FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /source

COPY ./SpeissApi.csproj ./api/SpeissApi.csproj
COPY ./protos/* ./services/protos/
RUN dotnet restore ./api

# copy everything else and build app
COPY ./* ./api/
WORKDIR /source/api
RUN dotnet publish -c release -o /app --no-restore

# final stage/image
FROM mcr.microsoft.com/dotnet/aspnet:6.0 as app
WORKDIR /app
COPY --from=build /app ./
ENTRYPOINT ["dotnet", "SpeissApi.dll"]