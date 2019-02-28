#### Soource:
https://code-maze.com/unit-testing-aspnetcore-web-api/#letswritetests 


## Controller
```csharp
[Route("api/[controller]")]
[ApiController]
public class ShoppingCartController : ControllerBase
{
    private readonly IShoppingCartService _service;
 
    public ShoppingCartController(IShoppingCartService service)
    {
        _service = service;
    }
 
    // GET api/shoppingcart
    [HttpGet]
    public ActionResult<IEnumerable<ShoppingItem>> Get()
    {
        var items = _service.GetAllItems();
        return Ok(items);
    }
 
    // GET api/shoppingcart/5
    [HttpGet("{id}")]
    public ActionResult<ShoppingItem> Get(Guid id)
    {
        var item = _service.GetById(id);
 
        if (item == null)
        {
            return NotFound();
        }
 
        return Ok(item);
    }
 
    // POST api/shoppingcart
    [HttpPost]
    public ActionResult Post([FromBody] ShoppingItem value)
    {
        if (!ModelState.IsValid)
        {
            return BadRequest(ModelState);
        }
 
        var item = _service.Add(value);
        return CreatedAtAction("Get", new { id = item.Id }, item);
    }
 
    // DELETE api/shoppingcart/5
    [HttpDelete("{id}")]
    public ActionResult Remove(Guid id)
    {
        var existingItem = _service.GetById(id);
 
        if (existingItem == null)
        {
            return NotFound();
        }
 
        _service.Remove(id);
        return Ok();
    }
}
````

## Service
```csharp
public class ShoppingCartService : IShoppingCartService
{
    public ShoppingItem Add(ShoppingItem newItem)
    {
        throw new NotImplementedException();
    }
 
    public IEnumerable<ShoppingItem> GetAllItems()
    {
        throw new NotImplementedException();
    }
 
    public ShoppingItem GetById(Guid id)
    {
        throw new NotImplementedException();
    }
 
    public void Remove(Guid id)
    {
        throw new NotImplementedException();
    }
}
```


