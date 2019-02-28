Source: https://www.youtube.com/watch?v=aIkpVzqLuhA&t=688s

`dotnet watch run`

`ConfigureServices`  - declare your middleware
`Configure` - activate and configure your middleware
e.g. 
```csharp
public void ConfigureServices(IServicetCollection services)
{
   service.AddMvc();
}

public void Configure(IApplicationBuilder app, IHostingEnvironment env)
{
   if(env.IsDevelopment())
   {
      app.UseDevelopmentException();
   }
   
   app.UseMvc();
   app.Run(async (context)=>{
      await context.Response.WriteAsynce("Hello world!");
   });
}
```



11:33
```csharp
// Startup.cs

app.Run(async (context)=> {
  await context.Response.WriteAsync("Hello world!");
});
```

12:32 - `BaseController` gives you access to web api vs. `Controller` is used for Razor pages

## Handling HTTP Requests
* The server (kestrel) listens for requests
* The middleware pipeline is invoked for each request
* Use Asp.net Core MVC to route requests to a controller (class) and action (method)
* Responses flows back down the middleware pipeline


## Routing attributes
* In essence: `[HttpGet/Post/Put/Delet("api/orders")]`
* Specificy multiple HTTP verbs with `AcceptVerbsAttribute`
* Use `RouteAttribute` to speciffy no HTTP method at all 
* Controller routes prepend to action routes 
   e.g. 
```csharp
[Route("api/home")]
public class MyController : ControllerBase
{
  // GET /api/home/foo
  [Route("foo")]
  public IActionResult Foo() {
     return Ok(new { data = "foo"});
  }
}
```

namespace: `Microsoft.AspNetCore.Mvc.Core`
`[Route("api/home")]` - example of a controller route attribute
`[HttpGet]` - an example of a RouteAttribute
`[Produces("application/json")]`

Examples:

`[Route("api/orders/{id}")]`

`[Route("api/[controller]")]` -router token that specificies ccontroller/action/area

`[HttpGet("{id?}")]` - optional value

`[HttpGet("{id=latest}")]` - default route value

`[HttpGet("{id:int}")]` - constraints

### Model binding

Examples:

`[FromBody]` - bind the request using formatters
Use the following te restrict model bing to a particular source
`[FromQuery]`
`[FromRoute]`
`[FromForm]`
`[FromHeader]`
Furthermore, we use these anotation to check `ModelState.IsValid`

Example:
```csharp
[HttpPost]
public IActionResult Post([FromBody] Value value)
{
    if (!ModelState.IsValid) 
    {
        // return json of current state of model to help debugging
        return BadRequest(ModelState); 
    }
    
    // Verify that you created the resource and give the link to where the client can get it
    //  param: 
    //   a.the action that the client can use to access the new resource
    //   b.the id of the resource which will be use to created link in response header
    //   c.(optional) the json of the newly created resource
    return CreatedAtAction("Get", new { id = value.id }, value); 
}

public class Value 
{
  [MinimumLength(3)]
  public string Text {get; set;}
}

Json:
{
 "Text": "abc"
}
```


## Action Results
official docs: https://docs.microsoft.com/en-us/aspnet/core/web-api/action-return-types?view=aspnetcore-2.2

### Common Action Results
* Action Results are used to produce the http response
* Return `IActionResult` or `Task<IActionResult>`
* Use helper extension methods on `ControllerBase`

Typically we set the return value for our Actions to `IActionResult`.
We do this because it gives us more flexibility than just some type e.g. `Dictionary<string, string>`.

Here are the common Action Result (as helper methods):
* Ok(object) - 200
* BadRequest(ModelState) - 400 - returns the model state as json to help debugging
* CreatedAtAction(string ActionName, object) - 201 - give link to newly created resource 
* Content(string s) - only works for razor pages (deriving from `Controller`)
* Json(object) - only works with razor pages (deriving from `Controller`) 
   exists in namespace: `Microsoft.AspNetCore.Mvc.ViewFeatures -> Microsoft.AspNetCore.Mvc -> Controller`
* View(object) - only works for razor pages (deriviing from `Controller`)


## Formatting
* There are separate and input and output formatters
* You configure formatters through MVC options
* Input formatter handle request body formatter 
    Don't forget to use `[FromBody]` on your action paramater
* Output formatters handle respons content-negotiation
* Contstraint formats per action configured using [Produces/Consumes]
* New in 2.0 : support for media-type suffixes e.g. application/foo+json

As an example, if you want to add XML formatting you could set options 
or you can use this helper method in  `Startup.cs`:
```csharp
 services.AddMvc()
        .AddXmlDataContractSerializerFormatters()
        .SetCompatibilityVersion(CompatibilityVersion.Version_2_2);
```
No need to change anything with your controller:
```csharp
public IActionResult Get() {
  return Ok(new string[] {"value1", "value2"});
}
```
And in your GET request header
```
key    : value
Accept : application/xml
```
However, you can enforce the output type by annotations like `[Produces/Consumes]`
```csharp
```csharp
[Produces("application/json")]
public IActionResult Get() {
  return Ok(new string[] {"value1", "value2"});
}
```
So even if you change the header to `Accept : application/xml` your action method
will only return JSON formatted data.


## EF Core / Database
* Use EF Core to access a variety of data sources
* Inject DbContext int your web api controllers
* Use visual studio scaffolding to generate web APIs based on your DbContext

To generate controllers based on dbcontext in mac, you need to install:
https://stackoverflow.com/questions/41450148/no-executables-found-matching-command-dotnet-aspnet-codegenerator
https://mattmillican.com/blog/aspnetcore-controller-scaffolding
https://gavilan.blog/2018/04/28/asp-net-core-2-doing-scaffolding-with-dotnet-cli-aspnet-codegenerator/
```bash
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.EntityFrameworkCore.Tools
dotnet add package Microsoft.VisualStudio.Web.CodeGeneration.Design
```

## Debugging
In Visual Studio, you can set a breakpoint on a line in a action method
and then click Play and if you have an error that breakpoint will be where it will pause.

## Namespaces you should be aware of

namespace: `Microsoft.AspNetCore.Mvc.Core -> Microsoft.AspNetCore.Mvc -> ControllerBase`

namespace `Microsoft.AspNetCore.Mvc.ViewFeatures ->  Microsoft.AspNetCore.Mvc -> Controller`

Use when your controller derives from `Controller`
namespace: `Microsoft.AspNetCore.Mvc.Formatters.Json -> JsonResult`




