import os
from flytekit.types.file import FlyteFile
from domino.flyte.task import DominoJobConfig, DominoJobTask, EnvironmentRevisionSpecification, EnvironmentRevisionType, GitRef
from flytekit.loggers import logger

class Input:
    def __init__(self, type: type, value: FlyteFile):
        self.type = type
        self.value = value

def run_domino_job(
    name: str, 
    command: str, 
    environment: str,
    hardware_tier: str, 
    inputs: dict = None,
    outputs: dict = None
) -> DominoJobTask:

    api_key=os.environ.get('DOMINO_USER_API_KEY')
    owner_name=os.environ.get('DOMINO_USER_NAME')
    project_name=os.environ.get('DOMINO_PROJECT_NAME')

     # Hardcoding some stuff right now
    CommitId="a06e6984d022f00671c07b83e5773b9b62849878" # DFS artifacts git commit
    environmentId = "65cd1bb0cd1d01583b5d8f2d" # TODO: Lookup environmentId based on environment name . 
    environmentRevisionId = "65dfe2d5428692221d9820a8" # TODO: Lookup revisionId based on environment revision number. 
    hardwareTierId = "small-k8s" # TODO: Convert hardware tier name to hardware tier ID 

    job_config = DominoJobConfig(
        OwnerName=owner_name,
        ProjectName=project_name,
        ApiKey=api_key,
        Command=command,
        CommitId=CommitId,
        MainRepoGitRef=GitRef(Type="head"),
        EnvironmentId=environmentId,
        EnvironmentRevisionSpec=EnvironmentRevisionSpecification(
            EnvironmentRevisionType=EnvironmentRevisionType.SomeRevision,
            EnvironmentRevisionId=environmentRevisionId,
        ),
        HardwareTierId=hardwareTierId,
        VolumeSizeGiB=10,
        ExternalVolumeMountIds=[]
    )

    input_types = {}
    input_values = {}
    for key, value in inputs.items():
        input_types[key] = value.type
        input_values[key] = value.value

    print(input_types)

    job = DominoJobTask(
        name,
        job_config,
        inputs=input_types,
        outputs=outputs        
    )

    results = job(**input_values)

    return results

