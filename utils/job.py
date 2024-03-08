import os
from domino.flyte.task import DominoJobConfig, DominoJobTask, EnvironmentRevisionSpecification, EnvironmentRevisionType, GitRef
from flytekit.loggers import logger

api_key=os.environ.get('DOMINO_USER_API_KEY')
owner_name=os.environ.get('DOMINO_USER_NAME')
project_name=os.environ.get('DOMINO_PROJECT_NAME')
CommitId="a06e6984d022f00671c07b83e5773b9b62849878" # DFS artifacts git commit

def define_job(
    name: str, 
    command: str, 
    environmentId: str = "65cd1bb0cd1d01583b5d8f2d", 
    inputs: dict = None,
    outputs: dict = None
) -> DominoJobTask:

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
        name,
        job_config,
        inputs=inputs,
        outputs=outputs
    )

    return job



 