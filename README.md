# Street-Group-Task
Data Engineer Task for Street Group

Apache Beam can be used to run ETL pipelines on Google Cloud using a command similar to the one mentioned below :

python data_pipeline.py --project=$PROJECT_ID --region=us-central1 --runner=DataflowRunner --staging_location=gs://$PROJECT_ID/test --temp_location gs://$PROJECT/test --input gs://Some_Cloud_Location/pp-monthly-update-new-version.csv

There are a couple of ways to approach this problem statement.

  1. Convert the .csv file to .json as is and try the grouping on property after loading the data in Google Cloud (possibly in Big Query).
  2. Convert the .csv file to .json and group the data at the .json file level so that the file can be loaded there after.

I have tried to showcase both these approaches in my solution and can explain it further on the call.
