``` mermaid
classDiagram
    class SortingAlgorithm {
        <<abstract>>
        +sort(arr: list, key: function) list
    }

    class BubbleSort {
        +sort(arr: list, key: function) list
    }

    class InsertionSort {
        +sort(arr: list, key: function) list
    }

    class QuickSort {
        -steps: list
        -key: function
        +sort(arr: list, key: function) list
        -_partition(arr: list, low: int, high: int) int
        -_quick_sort_recursive(arr: list, low: int, high: int) void
    }

    class DataHandler {
        <<static>>
        +read_data(filename: str) list
        +get_key(sort_type: str) function
    }

    class Visualizer {
        -canvas: FigureCanvasTkAgg
        -ax: Axes
        +visualize_sorting(steps: list, sort_type: str, delay: int) void
        -_convert_values(step: list, sort_type: str) list
        -_add_labels(step: list, values: list, sort_type: str) void
    }

    class SortingApplication {
        -root: Tk
        -filename: str
        -sort_type: str
        -fig: Figure
        -ax: Axes
        -canvas: FigureCanvasTkAgg
        -visualizer: Visualizer
        -algorithms: dict
        +__init__() void
        -_setup_ui() void
        -_choose_file() void
        -_choose_sort_type() void
        -_sort_data(algorithm: str) void
        -_show_result_window(sorted_data: list) void
        +run() void
    }

    SortingAlgorithm <|-- BubbleSort
    SortingAlgorithm <|-- InsertionSort
    SortingAlgorithm <|-- QuickSort
    SortingApplication --> Visualizer
    SortingApplication --> DataHandler
    SortingApplication --> SortingAlgorithm
```
