from utils.flyte import run_domino_job, Input
from flytekit import workflow
from flytekit.types.file import FlyteFile
from flytekit.types.directory import FlyteDirectory

'''
To run this workflowp, execute the following line in the terminal

pyflyte run --remote workflow.py training_workflow
'''
@workflow
def training_workflow(data_path: FlyteFile="/mnt/code/data/data.csv") -> FlyteFile: 

    data_prep_results = run_domino_job(
        name="Prepare data",
        environment="Spark environment",
        hardware_tier="Large-CPU",
        command="python /mnt/code/python/prep-data.py",
        inputs={
            "data_path": Input(type=FlyteFile, value=data_path)
        },
        outputs={
            "processed_data": FlyteFile
        }
    )

    training_results = run_domino_job(
        name="Train model",
        environment="Ray environment",
        hardware_tier="Large-GPU",
        command="python /mnt/code/python/train.py",
        inputs={
            "processed_data": Input(type=FlyteFile, value=data_prep_results['processed_data']),
            "epochs": Input(type=int, value=10),
            "batch_size": Input(type=int, value=32)
        },
        outputs={
            "model": FlyteFile
        }
    )

    return training_results['model']
