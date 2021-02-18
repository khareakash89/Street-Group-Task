import csv
import json
import argparse
import logging
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class DataIngestion:
    def parse_data():
        csvfile = open('pp-monthly-update-new-version.csv', 'r')
        jsonfile = open('pp-monthly-update-new-version.json', 'w')

        reader = csv.DictReader(csvfile)
        for row in reader:
            json.dump(row, jsonfile, indent=4)
            jsonfile.write('\n')

def run(argv=None):
    parser = argparse.ArgumentParser(description='Convert .csv file to .json file.')

    parser.add_argument('--input',
                        dest='input',
                        help='Input file to read. This can be a local file or '
                             'a file in a Google Storage Bucket.',
                        default='gs://Some_Cloud_Storage/pp-monthly-update-new-version.csv'
                        )

    parser.add_argument('--output',
                        dest='output',
                        help='Output JSON file to write results to.',
                        default='gs://Some_Cloud_Storage/pp-monthly-update-new-version.json')

    known_args, pipeline_args = parser.parse_args(args)

    data_ingestion = DataIngestion()

    p = beam.Pipeline(options=PipelineOptions(pipeline_args))

    (p
     | 'Read from File' >> beam.io.ReadFromText(known_args.input)
     | 'Convert csv to json' >> beam.Map(lambda s: data_ingestion.parse_data())
     | 'Write to file' >> beam.io.Write(known_args.output)
    )

    p.run().wait_until_finish()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()