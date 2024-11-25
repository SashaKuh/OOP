using System;
using System.Collections.Generic;

namespace Test
{

public class PaymentRunor
{
    public void RunPayment(string paymentType, decimal amount)
    {
        if (paymentType == "CreditCard")
        {
            Console.WriteLine($"Runing credit card payment of {amount:C}.");
        }
        else if (paymentType == "PayPal")
        {
            Console.WriteLine($"Runing PayPal payment of {amount:C}.");
        }
        else if (paymentType == "BankTransfer")
        {
            Console.WriteLine($"Runing bank transfer payment of {amount:C}.");
        }
        else
        {
            Console.WriteLine("Unsupported payment type.");
        }
    }
}


// 1. Extract Class: Винесення різних типів платежів у класи.
public interface IPaymentHandler
{
    void RunPayment(decimal amount);
}

public class CreditCardPaymentHandler : IPaymentHandler
{
    public void RunPayment(decimal amount)
    {
        Console.WriteLine($"Runing credit card payment of {amount:C}.");
    }
}

public class PayPalPaymentHandler : IPaymentHandler
{
    public void RunPayment(decimal amount)
    {
        Console.WriteLine($"Runing PayPal payment of {amount:C}.");
    }
}

public class BankTransferPaymentHandler : IPaymentHandler
{
    public void RunPayment(decimal amount)
    {
        Console.WriteLine($"Runing bank transfer payment of {amount:C}.");
    }
}

// 2. Replace Conditional with Polymorphism: Використання поліморфізму.
public class PaymentRunor2
{
    private readonly Dictionary<string, IPaymentHandler> _paymentHandlers;

    public PaymentRunor2()
    {
        _paymentHandlers = new Dictionary<string, IPaymentHandler>
        {
            { "CreditCard", new CreditCardPaymentHandler() },
            { "PayPal", new PayPalPaymentHandler() },
            { "BankTransfer", new BankTransferPaymentHandler() }
        };
    }

    public void RunPayment(string paymentType, decimal amount)
    {
        if (_paymentHandlers.ContainsKey(paymentType))
        {
            _paymentHandlers[paymentType].RunPayment(amount);
        }
        else
        {
            Console.WriteLine("Unsupported payment type.");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        var paymentRunor = new PaymentRunor2();

        paymentRunor.RunPayment("CreditCard", 100.00m);
        paymentRunor.RunPayment("PayPal", 200.00m);
        paymentRunor.RunPayment("BankTransfer", 300.00m);
        paymentRunor.RunPayment("Crypto", 500.00m); // Непідтримуваний тип
    }
}
}
