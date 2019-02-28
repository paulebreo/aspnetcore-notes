
# Resource
* https://docs.microsoft.com/en-us/aspnet/core/client-side/spa/react?view=aspnetcore-2.2&tabs=netcore-cli
* asp.net core mvc + react + webpack


## React independently
If you don't want CRA (create react app) to restart everytime you rebuild your asp.net
code, you need to run CRA independently.

You do this by changing `Startup.cs`
```csharp
// In ConfigureServices
services.AddSpaStaticFiles(configuration =>
{
    configuration.RootPath = "ClientApp/build";
});

// in Configure
app.UseSpa(spa =>
{
    spa.Options.SourcePath = "ClientApp";

    if (env.IsDevelopment())
    {
        //spa.UseReactDevelopmentServer(npmScript: "start");
        spa.UseProxyToSpaDevelopmentServer("http://localhost:3000");
    }
});

```

Now you can do something like this
```bash

dotnet watch run
cd ClientApp
npm start
```

### CORS
The following code in your `Startup.cs` will open up your API to any
domain. Be careful!!

In the ConfigureServices method:
```csharp
// In ConfigureServices - at the very top (above services.AddMvc())
services.AddCors(options =>
{
    options.AddPolicy("AllowAllPolicy",
        builder => builder.AllowAnyOrigin()
        .AllowAnyMethod()
        .AllowAnyHeader()
        .AllowCredentials());
});
```
In the Configure method:
```csharp
// In Configure
app.UseCors("AllowAllPolicy");
```


## React - package.json
source: week4 - TodoList
```json
{
  "name": "PuppyBook",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "bootstrap": "^4.1.3",
    "jquery": "3.3.1",
    "react": "^16.0.0",
    "react-dom": "^16.0.0",
    "react-router-bootstrap": "^0.24.4",
    "react-router-dom": "^4.2.2",
    "react-scripts": "^1.1.5",
    "reactstrap": "^6.3.0",
    "rimraf": "^2.6.2"
  },
  "devDependencies": {
    "ajv": "^6.0.0",
    "babel-eslint": "^7.2.3",
    "cross-env": "^5.2.0",
    "eslint": "^4.1.1",
    "eslint-config-react-app": "^2.1.0",
    "eslint-plugin-flowtype": "^2.50.3",
    "eslint-plugin-import": "^2.14.0",
    "eslint-plugin-jsx-a11y": "^5.1.1",
    "eslint-plugin-react": "^7.11.1"
  },
  "eslintConfig": {
    "extends": "react-app"
  },
  "scripts": {
    "start": "rimraf ./build && react-scripts start",
    "build": "react-scripts build",
    "test": "cross-env CI=true react-scripts test --env=jsdom",
    "eject": "react-scripts eject",
    "lint": "eslint ./src/"
  }
}

```

