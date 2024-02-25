from domino.flyte.task import DominoJobConfig, DominoJobTask
from flytekit import workflow, task
from flytekit.types.file import FlyteFile, CSVFile
from flytekit.types.directory import FlyteDirectory

api_key="603d2f07ed65bbb3be5bdf97ef5f10074a555febabd1fd9d1bdf284ab7ec5d27"
owner_name="integration-test"
project_name="john-flyte-testing"
CommitId="a06e6984d022f00671c07b83e5773b9b62849878"

adae_job_config = DominoJobConfig(
    OwnerName=owner_name,
    ProjectName=project_name,
    ApiKey=api_key,
    Command="prod/adae.sas",
    CommitId=CommitId,
    EnvironmentId="65cd54180df82f018c4fb7cf"
)

adae_job = DominoJobTask(
    "Create ADAE dataset",
    adae_job_config,
    inputs={"data_path": FlyteFile},
    outputs={"adae_data": FlyteDirectory}
)

# pyflyte run --remote sas-workflow.py sas_workflow
@workflow
def sas_workflow():
    adae_data = adae_job(data_path="/mnt/code/data/vs.sas7bdat")
    return 
