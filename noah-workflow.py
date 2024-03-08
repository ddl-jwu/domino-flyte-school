import os
from domino.flyte.task import DominoJobConfig, DominoJobTask
from flytekit import workflow, task
from flytekit.types.file import FlyteFile, CSVFile
from flytekit.types.directory import FlyteDirectory

api_key=os.environ.get('DOMINO_USER_API_KEY')
owner_name=os.environ.get('DOMINO_USER_NAME')
project_name=os.environ.get('DOMINO_PROJECT_NAME')
CommitId="a06e6984d022f00671c07b83e5773b9b62849878"

dir_job_config = DominoJobConfig(
    OwnerName=owner_name,
    ProjectName=project_name,
    ApiKey=api_key,
    Command="cp -R test-dir /workflows/outputs",
    CommitId=CommitId,
    EnvironmentId="65cd54180df82f018c4fb7cf"
)


@workflow
def dir_workflow(dir: FlyteDirectory):
    dir_task = DominoJobTask(
        "Create ADAE dataset",
        dir_job_config,
        outputs={"test_dir": FlyteDirectory},
    )

    return dir_task()