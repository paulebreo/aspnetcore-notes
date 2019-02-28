
## Resources

https://docs.microsoft.com/en-us/ef/core/get-started/aspnetcore/new-db?tabs=netcore-cli

In ConfigureServices
```csharp
// Belowe services.AddMvc();

var connection = @"Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;";
services.AddDbContext<masterContext>
    (options => options.UseSqlServer(connection));
```

In-memory configuration. Put in `ConfigureServices`
```csharp
services.AddDbContext<ValueContext>(options => options.UseInMemoryDatabase("foo"));
```











