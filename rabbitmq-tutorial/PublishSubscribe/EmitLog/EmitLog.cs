using System;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;
using System.Text;

namespace EmitLog
{
    class Program
    {
        private static string GetMessage(string[] args)
        {
            return ((args.Length > 0) ? string.Join(" ", args) : "Hello world!");
        }

        static void Main(string[] args)
        {
            var factory = new ConnectionFactory() { HostName = "localhost", UserName = "guest", Password = "guest", Port = 5673 };
            using (var connection = factory.CreateConnection())
            using (var channel = connection.CreateModel())
            {
                channel.ExchangeDeclare(exchange: "logs", type: "fanout");
                var message = GetMessage(args);
                var body = Encoding.UTF8.GetBytes(message);

                channel.BasicPublish(exchange: "logs",
                        routingKey: "",
                        basicProperties: null,
                        body: body

                    );
                Console.WriteLine("[x] Sent {0}", message);

            }

            Console.WriteLine("Press [enter] to exit.");
            Console.ReadLine();
        }
    }
}
