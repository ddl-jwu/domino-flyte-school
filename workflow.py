from domino.flyte.task import DominoJobConfig, DominoJobTask
from flytekit import workflow, task
from flytekit.types.file import FlyteFile, CSVFile
from flytekit.types.directory import FlyteDirectory

api_key="603d2f07ed65bbb3be5bdf97ef5f10074a555febabd1fd9d1bdf284ab7ec5d27"
owner_name="integration-test"
project_name="john-flyte-testing"
CommitId="a06e6984d022f00671c07b83e5773b9b62849878"

prep_data_job_config = DominoJobConfig(
    OwnerName=owner_name,
    ProjectName=project_name,
    ApiKey=api_key,
    Command="python prep-data.py",
    CommitId=CommitId
)

prep_data_job = DominoJobTask(
    "Prepare data",
    prep_data_job_config,
    inputs={"data_path": FlyteFile},
    outputs={"processed_data": FlyteFile}
)

train_job_config = DominoJobConfig(
    OwnerName=owner_name,
    ProjectName=project_name,
    ApiKey=api_key,
    Command="python train.py",
    CommitId=CommitId
)

train_job = DominoJobTask(
    "Train model",
    train_job_config,
    inputs={"processed_data": FlyteFile},
    outputs={"model": FlyteDirectory}
)

# pyflyte run --remote workflow.py training_workflow
@workflow
def training_workflow():
    processed_data = prep_data_job(data_path="./data.csv")
    model = train_job(processed_data=processed_data)
    return 
