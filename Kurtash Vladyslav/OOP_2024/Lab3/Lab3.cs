using System;

public class BridgePatternExample
{
    public static void Main(string[] args)
    {
        // Create different display types
        IDisplayImplementation textDisplay = new TextDisplay();
        IDisplayImplementation graphicalDisplay = new GraphicalDisplay();

        // Create PaymentVisualizer objects with different display implementations
        PaymentVisualizer paymentVisualizerText = new PaymentVisualizer(textDisplay);
        AdvancedPaymentVisualizer paymentVisualizerGraphical = new AdvancedPaymentVisualizer(graphicalDisplay);

        double price = 100.50;

        // Simulate the purchase process
        paymentVisualizerText.ShowPurchaseInProgress();
        paymentVisualizerText.ShowPurchaseSuccess(price);
        paymentVisualizerText.ShowPurchaseFail(price);
        paymentVisualizerText.CancelPurchase();
        
        Console.WriteLine("\n");

        paymentVisualizerGraphical.ShowPurchaseInProgress();
        paymentVisualizerGraphical.ShowPurchaseSuccess(price);
        paymentVisualizerGraphical.ShowPurchaseFail(price);
        paymentVisualizerGraphical.ShowImage("Image1.jpg");
    }

    // Абстракція
    public class PaymentVisualizer
    {
        protected IDisplayImplementation _displayImplementation;

        public PaymentVisualizer(IDisplayImplementation displayImplementation)
        {
            _displayImplementation = displayImplementation;
        }

        public void ShowPurchaseSuccess(double value)
        {
            _displayImplementation.DisplayResult(value, true);
        }

        public void ShowPurchaseFail(double value)
        {
            _displayImplementation.DisplayResult(value, false);
        }

        public void ShowPurchaseInProgress()
        {
            _displayImplementation.DisplayLoading();
        }

        public void CancelPurchase()
        {
            _displayImplementation.Stop();
        }
    }

    // Розширена абстракція для більш складного відображення
    public class AdvancedPaymentVisualizer : PaymentVisualizer
    {
        public AdvancedPaymentVisualizer(IDisplayImplementation displayImplementation) : base(displayImplementation)
        {
        }
        
        public void ShowImage(string imageData)
        {
            _displayImplementation.DisplayServiceImage(imageData);
        }
    }

    // Реалізація моста (спосіб відображення даних)
    public interface IDisplayImplementation
    {
        void DisplayResult(double value, bool success);
        void DisplayLoading();
        void Stop();
        void DisplayServiceImage(string imageData); // Method to display images (added to interface)
    }

    // Конкретна реалізація для текстового відображення
    public class TextDisplay : IDisplayImplementation
    {
        public void DisplayResult(double value, bool success)
        {
            if (success)
            {
                Console.WriteLine($"Payment of {value} was successful! (Text Display)");
            }
            else
            {
                Console.WriteLine($"Payment of {value} failed. (Text Display)");
            }
        }

        public void DisplayLoading()
        {
            Console.WriteLine("Loading payment process... (Text Display)");
        }

        public void Stop()
        {
            Console.WriteLine("Stopping payment process... (Text Display)");
        }

        public void DisplayServiceImage(string imageData)
        {
            Console.WriteLine($"Displaying image: {imageData} (Text Display)");
        }
    }

    // Конкретна реалізація для графічного відображення
    public class GraphicalDisplay : IDisplayImplementation
    {
        public void DisplayResult(double value, bool success)
        {
            if (success)
            {
                Console.WriteLine($"[GRAPHICAL] Payment of {value} was successful!");
            }
            else
            {
                Console.WriteLine($"[GRAPHICAL] Payment of {value} failed.");
            }
        }

        public void DisplayLoading()
        {
            Console.WriteLine("[GRAPHICAL] Loading payment process...");
        }

        public void Stop()
        {
            Console.WriteLine("[GRAPHICAL] Stopping payment process...");
        }

        public void DisplayServiceImage(string imageData)
        {
            Console.WriteLine($"[GRAPHICAL] Displaying image: {imageData}");
        }
    }
}
