import os
from domino.flyte.task import DominoJobConfig, DominoJobTask
from flytekit import workflow, task
from flytekit.types.file import FlyteFile, CSVFile
from flytekit.types.directory import FlyteDirectory

api_key=os.environ.get('DOMINO_USER_API_KEY')
owner_name=os.environ.get('DOMINO_USER_NAME')
project_name=os.environ.get('DOMINO_PROJECT_NAME')
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

advs_job_config = DominoJobConfig(
    OwnerName=owner_name,
    ProjectName=project_name,
    ApiKey=api_key,
    Command="prod/advs.sas",
    CommitId=CommitId,
    EnvironmentId="65cd54180df82f018c4fb7cf"
)

advs_job = DominoJobTask(
    "Create ADVS dataset",
    advs_job_config,
    inputs={"ta.sas7bdat": FlyteFile, "adsl.sas7bdat": FlyteFile},
    outputs={"advs": FlyteFile}
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
    "Generate T_AE_REL report",
    t_ae_rel_job_config,
    inputs={"adae.sas7bdat": FlyteFile},
    outputs={"report": FlyteFile}
)

t_vscat_job_config = DominoJobConfig(
    OwnerName=owner_name,
    ProjectName=project_name,
    ApiKey=api_key,
    Command="prod/t_vscat.sas",
    CommitId=CommitId,
    EnvironmentId="65cd54180df82f018c4fb7cf"
)

t_vscat_job = DominoJobTask(
    "Generate T_VSCAT report",
    t_vscat_job_config,
    inputs={"advs.sas7bdat": FlyteFile}
)


# pyflyte run --remote sas-workflow.py sas_workflow --sdtm_tv_file "/mnt/code/data/tv.sas7bdat" --sdtm_ts_file "/mnt/code/data/ts.sas7bdat" --sdtm_ta_file "/mnt/code/data/ta.sas7bdat"
@workflow
def sas_workflow(sdtm_tv_file: FlyteFile, sdtm_ts_file: FlyteFile, sdtm_ta_file: FlyteFile) -> FlyteFile:
    print(sdtm_tv_file)
    adsl_dataset = adsl_job(**{"tv.sas7bdat": sdtm_tv_file})
    adae_dataset = adae_job(**{"ts.sas7bdat": sdtm_ts_file, "adsl.sas7bdat": adsl_dataset})
    advs_dataset = advs_job(**{"ta.sas7bdat": sdtm_ta_file, "adsl.sas7bdat": adsl_dataset})
    t_ae_rel_report = t_ae_rel_job(**{"adae.sas7bdat": adae_dataset})
    t_vscat_job(**{"advs.sas7bdat": advs_dataset})
    return t_ae_rel_report
