// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler

using System;

public class StrategyPattern
{
    public static void Main(string[] args)
    {
        // Select a payment strategy at runtime
        Console.WriteLine("Choose a payment method: 1. PayPal, 2. Cryptocurrency");
        int choice = int.Parse(Console.ReadLine() ?? "1");
        double price = 100;

        IPaymentStrategy paymentStrategy = choice switch
        {
            1 => new PayPalPayment(),
            2 => new CryptoPayment(),
            _ => throw new InvalidOperationException("Invalid payment method selected!")
        };

        // Use the payment processor with the selected strategy
        Context paymentRunner = new Context(paymentStrategy);
        paymentRunner.RunPayment(price);
    }
    
    // Strategy interface
    public interface IPaymentStrategy
    {
        void Pay(double amount);
    }
    
    // Concrete Strategy: PayPal Payment
    public class PayPalPayment : IPaymentStrategy
    {
        public void Pay(double amount)
        {
            Console.WriteLine($"Paid ${amount} using PayPal.");
        }
    }

    // Concrete Strategy: Cryptocurrency Payment
    public class CryptoPayment : IPaymentStrategy
    {
        public void Pay(double amount)
        {
            Console.WriteLine($"Paid ${amount} using Cryptocurrency.");
        }
    }
    
    public class Context
    {
        private readonly IPaymentStrategy _paymentStrategy;

        public Context(IPaymentStrategy paymentStrategy)
        {
            _paymentStrategy = paymentStrategy;
        }

        public void RunPayment(double amount)
        {
            _paymentStrategy.Pay(amount);
        }
    }
}










