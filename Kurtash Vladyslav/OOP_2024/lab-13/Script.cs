using System;
using System.Collections.Generic;

// Single Responsibility Principle (SRP)
public class Payment
{
    public decimal Amount { get; set; }
}

public class PaymentRunner
{
    public void RunPayment(IPaymentMethod paymentMethod, Payment payment)
    {
        paymentMethod.Run(payment);
    }
}

// Open-Closed Principle (OCP)
public interface IPaymentMethod
{
    void Run(Payment payment);
}

public class CreditCardPayment : IPaymentMethod
{
    public void Run(Payment payment)
    {
        Console.WriteLine($"Runing credit card payment of {payment.Amount}.");
    }
}

public class PayPalPayment : IPaymentMethod
{
    public void Run(DiscountedPayment payment)
    {
        Console.WriteLine($"Runing PayPal payment of {payment.Amount} with discount {payment.Discount}.");
    }
}

// Liskov Substitution Principle (LSP)
public class DiscountedPayment : Payment
{
    public decimal Discount { get; set; }
}

// Interface Segregation Principle (ISP)
public interface IRefundable
{
    void Refund(Payment payment);
}

public class RefundableCreditCardPayment : CreditCardPayment, IRefundable
{
    public void Refund(Payment payment)
    {
        Console.WriteLine($"Refunding credit card payment of {payment.Amount}.");
    }
}

// Dependency Inversion Principle (DIP)
public class PaymentService
{
    private readonly IPaymentMethod _paymentMethod;

    public PaymentService(IPaymentMethod paymentMethod)
    {
        _paymentMethod = paymentMethod;
    }

    public void RunPayment(Payment payment)
    {
        _paymentMethod.Run(payment);
    }
}

class Program
{
    static void Main(string[] args)
    {
        var creditCardPayment = new CreditCardPayment();
        var payPalPayment = new PayPalPayment();

        var paymentRunner = new PaymentRunner();
        
        var payment = new Payment { Amount = 100.00m };
        var discountedPayment = new DiscountedPayment { Amount = 80.00m, Discount = 20.00m };

        // SRP, OCP, and LSP
        paymentRunner.RunPayment(creditCardPayment, payment);
        paymentRunner.RunPayment(payPalPayment, discountedPayment);

        // ISP and DIP
        var refundablePayment = new RefundableCreditCardPayment();
        var paymentService = new PaymentService(refundablePayment);

        paymentService.RunPayment(payment);
        ((IRefundable)refundablePayment).Refund(payment);
    }
}
