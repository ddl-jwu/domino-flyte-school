from domino.flyte.task import DominoJobConfig, DominoJobTask
from flytekit import workflow, task
from flytekit.types.file import FlyteFile, CSVFile
from flytekit.types.directory import FlyteDirectory

api_key="603d2f07ed65bbb3be5bdf97ef5f10074a555febabd1fd9d1bdf284ab7ec5d27"
owner_name="integration-test"
project_name="john-flyte-testing"
CommitId="a06e6984d022f00671c07b83e5773b9b62849878"

adsl_job_config = DominoJobConfig(
    OwnerName=owner_name,
    ProjectName=project_name,
    ApiKey=api_key,
    Command="prod/adsl.sas",
    CommitId=CommitId,
    EnvironmentId="65cd54180df82f018c4fb7cf"
)

adsl_job = DominoJobTask(
    "Create ADSL dataset",
    adsl_job_config,
    inputs={"tv.sas7bdat": FlyteFile},
    outputs={"adsl": FlyteFile}
)

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
    inputs={"ts.sas7bdat": FlyteFile, "adsl.sas7bdat": FlyteFile},
    outputs={"adae": FlyteFile}
)

t_ae_rel_job_config = DominoJobConfig(
    OwnerName=owner_name,
    ProjectName=project_name,
    ApiKey=api_key,
    Command="prod/t_ae_rel.sas",
    CommitId=CommitId,
    EnvironmentId="65cd54180df82f018c4fb7cf"
)

t_ae_rel_job = DominoJobTask(
    "Generate report",
    t_ae_rel_job_config,
    inputs={"adae.sas7bdat": FlyteFile}
)

# pyflyte run --remote sas-workflow.py sas_workflow
@workflow
def sas_workflow():
    adsl_dataset = adsl_job(**{"tv.sas7bdat": "/mnt/code/data/tv.sas7bdat"})
    adae_dataset = adae_job(**{"ts.sas7bdat": "/mnt/code/data/ts.sas7bdat", "adsl.sas7bdat": adsl_dataset})
    t_ae_rel_job(**{"adae.sas7bdat": adae_dataset})
    return 
