# Resources
Official tutorial - Hello World
https://www.rabbitmq.com/tutorials/tutorial-one-dotnet.html

Official tutorial - Work Queue
https://www.rabbitmq.com/tutorials/tutorial-two-dotnet.html

Official tutorial - Publish/Subscribe
https://www.rabbitmq.com/tutorials/tutorial-three-dotnet.html

RabbitMQ:
https://github.com/jasonwyatt/docker-rabbitmq-demo/blob/master/fig.yml

## Tutum Docker container
```
docker run -d -p 5672:5672 -p 15672:15672 -e RABBITMQ_PASS="mypass" tutum/rabbitmq
```

## rabbitmqctl cli
```
sudo rabbitmqctl list_exchanges
```

## Official Tutorial - Hello World
```
dotnet new console --name Send
mv Send/Program.cs Send/Send.cs
dotnet new console --name Receive
mv Receive/Program.cs Receive/Receive.cs

cd Send
dotnet add package RabbitMQ.Client
dotnet restore
cd ../Receive
dotnet add package RabbitMQ.Client
dotnet restore

d run -d --hostname mytutorrabbit --name mytutorrabbit -p 5673:5672 -p 15673:15672 rabbitmq:3-alpine

cd Receive
dotnet run

# another terminal
cd Send
dotnet run

```

## Official Tutorial - Work Queue
```
dotnet new console --name NewTask
mv NewTask/Program.cs NewTask/NewTask.cs
dotnet new console --name Worker
mv Worker/Program.cs Worker/Worker.cs
cd NewTask
dotnet add package RabbitMQ.Client
dotnet restore
cd ../Worker
dotnet add package RabbitMQ.Client
dotnet restore
```

### Connection code
```csharp
var factory = new ConnectionFactory() {HostName = "localhost", UserName="guest", Password="guest", Port=5673};
```

## Official tutorial - PublisherSubscriber
```
rabbitmqctl list_bindings

d exec <containerid> rabbitmqctl list_bindings
```


