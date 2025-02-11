FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS runtime

# Set the working directory
WORKDIR /app

# Copy the published app from the build stage
COPY . .

# Expose port 80 for HTTP traffic
EXPOSE 80

# Define the entry point for the container
ENTRYPOINT ["dotnet", "Main_menu.Main_menu.dll"]