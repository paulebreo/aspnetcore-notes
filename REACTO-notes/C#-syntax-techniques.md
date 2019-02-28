
## Stopwatch 
* https://stackoverflow.com/questions/4884050/create-comma-separated-strings-c

## Print a dictionary
```csharp
public static void Print(string s) => Console.WriteLine(s);

var count = new Dictionary<char, int> {
  {'a', 1},
  {'b', 3}
};
var asString = string.Join(";", count);
Print(asString);
```

## print a list
```csharp
var fibNums = new List<int> { 0,1,2,3};
Print(String.Join(",", fibNums));
```

## Enumerable.Range
```csharp
foreach(var index in Enumerable.Range(111, 3))
{
    Console.WriteLine($"Student {index}");
}
```

## List to queue
You would do this if you want to use enqueue and dequeue
```csharp
var L = new List<int> {1,2};
var Q = new Queue<int>(L);
```

## List - pop, shift, unshift
* https://stackoverflow.com/questions/24855908/how-to-dequeue-element-from-a-list

## List - unshift
```csharp
List<T>.Insert(0, item); 
```

## LINQ: Union + Aggregrate + Enumerable.Empty<string>()
An example of using union and aggregate and empty list
https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable.empty?view=netframework-4.7.2
```csharp
string[] names1 = { "Hartono, Tommy" };
string[] names2 = { "Adams, Terry", "Andersen, Henriette Thaulow",
                      "Hedlund, Magnus", "Ito, Shu" };
string[] names3 = { "Solanki, Ajay", "Hoeing, Helge",
                      "Andersen, Henriette Thaulow",
                      "Potra, Cristina", "Iallo, Lucio" };

List<string[]> namesList =
    new List<string[]> { names1, names2, names3 };

// Only include arrays that have four or more elements
IEnumerable<string> allNames =
    namesList.Aggregate(Enumerable.Empty<string>(),
    (current, next) => next.Length > 3 ? current.Union(next) : current);

foreach (string name in allNames)
{
    Console.WriteLine(name);
}

/*
 This code produces the following output:

 Adams, Terry
 Andersen, Henriette Thaulow
 Hedlund, Magnus
 Ito, Shu
 Solanki, Ajay
 Hoeing, Helge
 Potra, Cristina
 Iallo, Lucio
*/
```





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





