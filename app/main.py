
from .aws_collector import AWSCollector
from .ai_engine import AIEngine
from .analyzer import Analyzer
def main():

    print("Collecting AWS data...")

    collector = AWSCollector()

    aws_data = collector.collect_ec2_data()

    print("Analyzing with AI...")

    ai = AIEngine()

    report = ai.analyze(aws_data)

    analyzer = Analyzer()

    analyzer.summarize(report)


if __name__ == "__main__":
    main()
    