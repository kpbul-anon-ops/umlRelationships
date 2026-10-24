# Dependency (Uses-a): ReportGenerator uses a Printer only during one method call
class Printer:
    def print_page(self, text: str):
        print(f"Printing: {text}")


class ReportGenerator:
    def __init__(self, content: str):
        self.content = content

    # Depends on a Printer strictly during this call; it is never stored
    def output_report(self, printer_device: Printer):
        printer_device.print_page(self.content)


if __name__ == "__main__":
    # 1. Instantiate the objects independently
    my_printer = Printer()
    quarter_report = ReportGenerator("Q1 Academic Performance: Excellent!")

    # 2. Pass the dependent device in at call time
    quarter_report.output_report(my_printer)
