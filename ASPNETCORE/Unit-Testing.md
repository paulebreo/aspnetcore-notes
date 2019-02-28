
## Resources

unit test example: 
https://github.com/julianorinaldi/Cross-Solar-Dotnet

service example - https://code-maze.com/unit-testing-aspnetcore-web-api/#letswritetests
asp.net-hacker rocks - https://asp.net-hacker.rocks/2017/09/27/testing-aspnetcore.html
logging - https://alastaircrabtree.com/using-logging-in-unit-tests-in-net-core
logging unit tests - https://stackoverflow.com/questions/46169169/net-core-2-0-configurelogging-xunit-test
debug unit tests - https://developercommunity.visualstudio.com/content/problem/125430/how-do-i-debug-unit-tests.html
logging - unit tests - https://xunit.github.io/docs/capturing-output

example: Solar App in .net (asp.net - week3)
https://github.com/julianorinaldi/Cross-Solar-Dotnet

* For VS Mac you should install the extension: "xUnit.NET 2 testing framework support"

* When adding a new test project, don't forget to add the Reference to your main project to the "Dependencies" node of your test project.



## Testing strategies

## Testing services

## Test the Get method
```csharp
public class ShoppingCartControllerTest
{
    ShoppingCartController _controller;
    IShoppingCartService _service;
 
    public ShoppingCartControllerTest()
    {
        _service = new ShoppingCartServiceFake();
        _controller = new ShoppingCartController(_service);
    }
 
    [Fact]
    public void Get_WhenCalled_ReturnsOkResult()
    {
        // Act
        var okResult = _controller.Get();
 
        // Assert
        Assert.IsType<OkObjectResult>(okResult.Result);
    }
 
    [Fact]
    public void Get_WhenCalled_ReturnsAllItems()
    {
        // Act
        var okResult = _controller.Get().Result as OkObjectResult;
 
        // Assert
        var items = Assert.IsType<List<ShoppingItem>>(okResult.Value);
        Assert.Equal(3, items.Count);
    }
}
```
## Test the GetById method
```csharp
[Fact]
public void GetById_UnknownGuidPassed_ReturnsNotFoundResult()
{
    // Act
    var notFoundResult = _controller.Get(Guid.NewGuid());
 
    // Assert
    Assert.IsType<NotFoundResult>(notFoundResult.Result);
}
 
[Fact]
public void GetById_ExistingGuidPassed_ReturnsOkResult()
{
    // Arrange
    var testGuid = new Guid("ab2bd817-98cd-4cf3-a80a-53ea0cd9c200");
 
    // Act
    var okResult = _controller.Get(testGuid);
 
    // Assert
    Assert.IsType<OkObjectResult>(okResult.Result);
}
 
[Fact]
public void GetById_ExistingGuidPassed_ReturnsRightItem()
{
    // Arrange
    var testGuid = new Guid("ab2bd817-98cd-4cf3-a80a-53ea0cd9c200");
 
    // Act
    var okResult = _controller.Get(testGuid).Result as OkObjectResult;
 
    // Assert
    Assert.IsType<ShoppingItem>(okResult.Value);
    Assert.Equal(testGuid, (okResult.Value as ShoppingItem).Id);
}
```
## Test the Add method
```csharp
[Fact]
public void Add_InvalidObjectPassed_ReturnsBadRequest()
{
    // Arrange
    var nameMissingItem = new ShoppingItem()
    {
        Manufacturer = "Guinness",
        Price = 12.00M
    };
    _controller.ModelState.AddModelError("Name", "Required");
 
    // Act
    var badResponse = _controller.Post(nameMissingItem);
 
    // Assert
    Assert.IsType<BadRequestObjectResult>(badResponse);
}
 
 
[Fact]
public void Add_ValidObjectPassed_ReturnsCreatedResponse()
{
    // Arrange
    ShoppingItem testItem = new ShoppingItem()
    {
        Name = "Guinness Original 6 Pack",
        Manufacturer = "Guinness",
        Price = 12.00M
    };
 
    // Act
    var createdResponse = _controller.Post(testItem);
 
    // Assert
    Assert.IsType<CreatedAtActionResult>(createdResponse);
}
 
 
[Fact]
public void Add_ValidObjectPassed_ReturnedResponseHasCreatedItem()
{
    // Arrange
    var testItem = new ShoppingItem()
    {
        Name = "Guinness Original 6 Pack",
        Manufacturer = "Guinness",
        Price = 12.00M
    };
 
    // Act
    var createdResponse = _controller.Post(testItem) as CreatedAtActionResult;
    var item = createdResponse.Value as ShoppingItem;
 
    // Assert
    Assert.IsType<ShoppingItem>(item);
    Assert.Equal("Guinness Original 6 Pack", item.Name);
}
```
### Test the Remove method
```csharp
[Fact]
public void Remove_NotExistingGuidPassed_ReturnsNotFoundResponse()
{
    // Arrange
    var notExistingGuid = Guid.NewGuid();
 
    // Act
    var badResponse = _controller.Remove(notExistingGuid);
 
    // Assert
    Assert.IsType<NotFoundResult>(badResponse);
}
 
[Fact]
public void Remove_ExistingGuidPassed_ReturnsOkResult()
{
    // Arrange
    var existingGuid = new Guid("ab2bd817-98cd-4cf3-a80a-53ea0cd9c200");
 
    // Act
    var okResponse = _controller.Remove(existingGuid);
 
    // Assert
    Assert.IsType<OkResult>(okResponse);
}
[Fact]
public void Remove_ExistingGuidPassed_RemovesOneItem()
{
    // Arrange
    var existingGuid = new Guid("ab2bd817-98cd-4cf3-a80a-53ea0cd9c200");
 
    // Act
    var okResponse = _controller.Remove(existingGuid);
 
    // Assert
    Assert.Equal(2, _service.GetAllItems().Count());
}
```

### Given a service
```csharp
public class ShoppingCartServiceFake: IShoppingCartService
{
    private readonly List<ShoppingItem> _shoppingCart;
 
    public ShoppingCartServiceFake()
    {
        _shoppingCart = new List<ShoppingItem>()
            {
                new ShoppingItem() { Id = new Guid("ab2bd817-98cd-4cf3-a80a-53ea0cd9c200"),
                    Name = "Orange Juice", Manufacturer="Orange Tree", Price = 5.00M },
                new ShoppingItem() { Id = new Guid("815accac-fd5b-478a-a9d6-f171a2f6ae7f"),
                    Name = "Diary Milk", Manufacturer="Cow", Price = 4.00M },
                new ShoppingItem() { Id = new Guid("33704c4a-5b87-464c-bfb6-51971b4d18ad"),
                    Name = "Frozen Pizza", Manufacturer="Uncle Mickey", Price = 12.00M }
            };
    }
 
    public IEnumerable<ShoppingItem> GetAllItems()
    {
        return _shoppingCart;
    }
 
    public ShoppingItem Add(ShoppingItem newItem)
    {
        newItem.Id = Guid.NewGuid();
        _shoppingCart.Add(newItem);
        return newItem;
    }
 
    public ShoppingItem GetById(Guid id)
    {
        return _shoppingCart.Where(a => a.Id == id)
            .FirstOrDefault();
    }
 
    public void Remove(Guid id)
    {
        var existing = _shoppingCart.First(a => a.Id == id);
        _shoppingCart.Remove(existing);
    }
}
```

### Logger for xUnit
Source: https://stackoverflow.com/questions/46169169/net-core-2-0-configurelogging-xunit-test

```csharp
using System;
using Microsoft.Extensions.Logging;
using Xunit.Abstractions;

namespace UnitTestingDemo.Tests
{
    public class XunitLoggerProvider : ILoggerProvider
    {
        private readonly ITestOutputHelper _testOutputHelper;

        public XunitLoggerProvider(ITestOutputHelper testOutputHelper)
        {
            _testOutputHelper = testOutputHelper;
        }

        public ILogger CreateLogger(string categoryName)
            => new XunitLogger(_testOutputHelper, categoryName);

        public void Dispose()
        { }
    }

    public class XunitLogger : ILogger
    {
        private readonly ITestOutputHelper _testOutputHelper;
        private readonly string _categoryName;

        public XunitLogger(ITestOutputHelper testOutputHelper, string categoryName)
        {
            _testOutputHelper = testOutputHelper;
            _categoryName = categoryName;
        }

        public IDisposable BeginScope<TState>(TState state)
            => NoopDisposable.Instance;

        public bool IsEnabled(LogLevel logLevel)
            => true;

        public void Log<TState>(LogLevel logLevel, EventId eventId, TState state, Exception exception, Func<TState, Exception, string> formatter)
        {
            _testOutputHelper.WriteLine($"{_categoryName} [{eventId}] {formatter(state, exception)}");
            if (exception != null)
                _testOutputHelper.WriteLine(exception.ToString());
        }

        private class NoopDisposable : IDisposable
        {
            public static NoopDisposable Instance = new NoopDisposable();
            public void Dispose()
            { }
        }
    }
}

```



























