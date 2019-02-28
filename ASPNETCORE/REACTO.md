# Resources
question: cast to generic type
https://stackoverflow.com/questions/1003023/cast-to-generic-type-in-c-sharp

# String

## Examplse
* Remove exclamation : https://repl.it/@paulebreo/c-codewars-remove-n-exclamation-marks

### Useful variables
```
string.Empty
null
```

### Array to List using Linq
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

var lst = new int[] { 1, 2,3};
List<int> numList = lst.ToList();
// or
List<int> numList2 = new List<int>(lst);
```

### String.Split()
```csharp
using System;

var s = "hello";
string[] t = s.Split();
foreach(var c in t) {Console.WriteLine(c);}
```

### string builder
```csharp
public static string Remove(string s, int n)
{
    var builder = new StringBuilder();
    foreach (var c in s)
    {
        if (c == '!' && n > 0)
            n--;
        else
            builder.Append(c); // or AppendLine
    }

    return builder.ToString();
}
```

### string.Join + select linq
```csharp
using System.Linq;

var myArray = new string[] { "hello", "world"};
string myStringOutput = String.Join(",", myArray.Select(p => p.ToString()).ToArray() );
```

### string.Concat + where + linq
```csharp
 public static string Remove(string s, int n)
  {
    return string.Concat(s.Where(c => c == '!' ? n-- <= 0 : true));
  }
```
### join
```csharp
var arr = new int[] {1,2,3};
string.Join("", arr);
```



