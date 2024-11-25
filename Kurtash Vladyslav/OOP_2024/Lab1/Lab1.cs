using System;

public class FactoryMethodExample
{
    public static void Main(string[] args)
    {
        // Example usage of Factory A
        AnalyticsServiceFactory factoryA = new AnalyticsServiceAFactory("A data 1", "A data 2");
        IService[] servicesA = factoryA.CreateAnalyticServices();
        foreach (var service in servicesA)
        {
            service.Initialize("Initializing Service A");
        }

        // Example usage of Factory B
        AnalyticsServiceFactory factoryB = new AnalyticsServiceBFactory("B data 1", "B data 2", "B data 3");
        IService[] servicesB = factoryB.CreateAnalyticServices();
        foreach (var service in servicesB)
        {
            service.Initialize("Initializing Service B");
        }
    }

    // Abstract factory class
    public abstract class AnalyticsServiceFactory
    {
        public abstract IService[] CreateAnalyticServices();
    }

    // Interface for the product
    public interface IService
    {
        void Initialize(string data);
    }

    // Concrete Factory A
    public class AnalyticsServiceAFactory : AnalyticsServiceFactory
    {
        private string[] _data;

        public AnalyticsServiceAFactory(params string[] data)
        {
            _data = data;
        }

        public override IService[] CreateAnalyticServices()
        {
            IService[] services = new IService[_data.Length];
            for (int i = 0; i < _data.Length; i++)
            {
                services[i] = new AnalyticsServiceA(_data[i]);
            }
            return services;
        }
    }

    // Concrete Factory B
    public class AnalyticsServiceBFactory : AnalyticsServiceFactory
    {
        private string[] _data;

        public AnalyticsServiceBFactory(params string[] data)
        {
            _data = data;
        }

        public override IService[] CreateAnalyticServices()
        {
            IService[] services = new IService[_data.Length];
            for (int i = 0; i < _data.Length; i++)
            {
                services[i] = new AnalyticsServiceB(_data[i]);
            }
            return services;
        }
    }

    // Concrete Product A
    public class AnalyticsServiceA : IService
    {
        private string _data;

        public AnalyticsServiceA(string data)
        {
            _data = data;
        }

        public void Initialize(string data)
        {
            Console.WriteLine($"AnalyticsServiceA initialized with: {_data}. Additional Data: {data}");
        }
    }

    // Concrete Product B
    public class AnalyticsServiceB : IService
    {
        private string _data;

        public AnalyticsServiceB(string data)
        {
            _data = data;
        }

        public void Initialize(string data)
        {
            Console.WriteLine($"AnalyticsServiceB initialized with: {_data}. Additional Data: {data}");
        }
    }
}
