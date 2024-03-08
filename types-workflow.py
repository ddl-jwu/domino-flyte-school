import os
from domino.flyte.task import DominoJobConfig, DominoJobTask, EnvironmentRevisionSpecification, EnvironmentRevisionType
from flytekit import workflow, task
from flytekit.types.file import FlyteFile, CSVFile
from flytekit.types.directory import FlyteDirectory

api_key=os.environ.get('DOMINO_USER_API_KEY')
owner_name=os.environ.get('DOMINO_USER_NAME')
project_name=os.environ.get('DOMINO_PROJECT_NAME')
CommitId="a06e6984d022f00671c07b83e5773b9b62849878"

job_config = DominoJobConfig(
    OwnerName=owner_name,
    ProjectName=project_name,
    ApiKey=api_key,
    Command="sleep 10",
    CommitId=CommitId,
    EnvironmentId="65cd1bb0cd1d01583b5d8f2d",
    EnvironmentRevisionSpec=EnvironmentRevisionSpecification(
        EnvironmentRevisionType=EnvironmentRevisionType.SomeRevision,
        EnvironmentRevisionId="65dfe2d5428692221d9820a8",
    ),
    HardwareTierId="small-k8s",
    VolumeSizeGiB=10,
    ExternalVolumeMountIds=[]
)

job = DominoJobTask(
    "Dummy job",
    job_config
)

# pyflyte run --remote types-workflow.py types_workflow
@workflow
def types_workflow(
    string_input: str = "Hello",
    int_input: int = 5
): 

    job()

    return 
